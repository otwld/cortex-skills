#!/usr/bin/env python3
"""Validate Cortex routed skill workspace structure, metadata, lifecycle, and generated artifacts."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
REBUILD_PATH = SCRIPT_DIR / 'rebuild-routed-skills.py'
VALID_ACTIVATIONS = {'entry', 'routed', 'explicit'}
VALID_VISIBILITIES = {'public', 'hidden'}
RESOURCE_KEYS = ('references', 'scripts', 'templates', 'assets')
AGENT_SKILL_NAME = 'SKILL.md'
AGENT_METADATA_PATH = Path('agents') / 'openai.yaml'
AGENT_SKILL_NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
AGENT_METADATA_INTERFACE_FIELDS = ('display_name', 'short_description', 'default_prompt')
PROHIBITED_RESOURCE_NAMES = {'legacy-extracted-patterns.md'}
PROHIBITED_METADATA_KEYS = ('relations',)
PROHIBITED_ROUTING_KEYS = ('signals', 'always')
PROHIBITED_LIFECYCLE_TEXT = (
    'BEFORE:',
    'WITH:',
    'AFTER:',
    'using module:',
    'using skill:',
    '# Output Marker',
    'required before modules',
    'evidence-backed with modules',
    'deferred after modules',
)
PROHIBITED_PROSE_PHRASES = (
    'Apply the module-specific rules:',
    'Guidance is grounded in current files or explicit user intent.',
    'Output uses project vocabulary and the recruitment example universe when examples are needed.',
    'Decisions are recorded in the right artifact instead of hidden in transient chat.',
    'Validation or acceptance criteria are named when the module changes behavior or workflow.',
    'Do not create placeholder guidance, examples, metadata, or documentation.',
    'Trigger signal is explicit.',
    'Relevant existing convention or memory was checked.',
    'Module-specific rules were applied.',
    'Remaining decisions, risks, or validation gaps are stated.',
)
PROHIBITED_PROSE_PATTERNS = (
    re.compile(r'^- .+ guidance names the inspected source, request evidence, or declared resource that triggered it\.$'),
    re.compile(r"^- .+ output uses this workspace's terms and the recruitment example universe only when examples are needed\.$"),
    re.compile(r'^- .+ decisions land in metadata, instructions, resources, tests, or docs when they change future behavior\.$'),
    re.compile(r'^- .+ validation names the command, artifact, review proof, or acceptance check that covers its risk\.$'),
    re.compile(r'^- .+ trigger evidence is explicit\.$'),
    re.compile(r'^- .+ source files, project memory, or declared resources were checked\.$'),
    re.compile(r'^- .+ workflow rules were applied at the relevant artifact boundary\.$'),
    re.compile(r'^- .+ docs, metadata, tests, or generated artifacts affected by the change were updated together\.$'),
    re.compile(r'^- .+ risks, rejected paths, and validation gaps are stated\.$'),
)
LIFECYCLE_REQUIRED_MARKERS = (
    '## Overview',
    '## Workflow',
    '## Quality Gates',
    '## Hard Stops',
    '## Phase Output',
)


def load_rebuild_module() -> Any:
    """Load the sibling rebuild script as a module."""
    spec = importlib.util.spec_from_file_location('rebuild_routed_skills', REBUILD_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot load {REBUILD_PATH}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


rebuild = load_rebuild_module()


def rel(root: Path, path: Path) -> str:
    """Return a workspace-relative path."""
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def manifest_value(workspace: Any, key: str, default: dict[str, str]) -> dict[str, str]:
    """Read a manifest mapping through the rebuild helper."""
    return rebuild.merge_defaults(workspace.manifest.get(key), default, key)


def resource_candidates(artifact: Any, workspace: Any, kind: str, value: str) -> list[Path]:
    """Return accepted paths for a resource declaration."""
    if value.startswith('shared/'):
        return [workspace.root / value]
    return [
        artifact.directory / value,
        artifact.directory / kind / value,
        workspace.root / 'shared' / value,
    ]


def is_under_artifact(path: Path, artifact_dirs: set[Path]) -> bool:
    """Return whether a path is inside an artifact directory but is not the artifact root."""
    return any(parent in artifact_dirs for parent in path.parents)


def has_descendant_artifact(path: Path, artifact_dirs: set[Path]) -> bool:
    """Return whether a category folder contains at least one artifact below it."""
    return any(path in artifact.parents for artifact in artifact_dirs)


def has_module_like_contents(path: Path) -> bool:
    """Return whether a non-artifact folder contains files that require artifact metadata."""
    if (path / AGENT_SKILL_NAME).exists() or (path / 'instructions.md').exists():
        return True
    if (path / AGENT_METADATA_PATH).exists() or (path / 'lifecycle').exists():
        return True
    return any((path / folder).exists() for folder in RESOURCE_KEYS)


def validate_modules_tree(root: Path, modules_root: Path, metadata_name: str, errors: list[str]) -> None:
    """Validate nested routed module artifacts and inert category folders."""
    if not modules_root.exists():
        return
    try:
        artifact_dirs = set(rebuild.discover_artifact_directories(modules_root, metadata_name, root))
    except Exception as error:
        errors.append(str(error))
        artifact_dirs = {path.parent for path in modules_root.rglob(metadata_name) if path.is_file()}

    for directory in sorted(path for path in modules_root.rglob('*') if path.is_dir()):
        if directory in artifact_dirs:
            metadata_path = directory / metadata_name
            try:
                metadata = rebuild.load_yaml(metadata_path)
            except Exception as error:
                errors.append(f'{rel(root, metadata_path)}: {error}')
                metadata = {}
            if metadata.get('activation') == 'explicit':
                errors.append(f'{rel(root, directory)}: command skill must live under commands')
            continue

        if is_under_artifact(directory, artifact_dirs):
            continue

        if has_module_like_contents(directory):
            errors.append(f'{rel(root, directory)}: missing {metadata_name}')
        elif not has_descendant_artifact(directory, artifact_dirs):
            errors.append(f'{rel(root, directory)}: category folder has no descendant module artifact')


def validate_resources(workspace: Any, artifact: Any, names: set[str], errors: list[str]) -> None:
    """Validate explicit resource ownership and use declarations."""
    shared_root = workspace.root / manifest_value(workspace, 'paths', rebuild.DEFAULT_PATHS)['shared']
    for target in artifact.uses:
        if target in names:
            continue
        candidates = [shared_root / target, workspace.root / target]
        if not any(candidate.exists() for candidate in candidates):
            errors.append(f'{artifact.name}: uses target does not exist: {target}')

    for kind in RESOURCE_KEYS:
        declared = artifact.resources[kind]
        normalized = set(declared)
        normalized.update(f'{kind}/{value}' for value in declared)
        for value in declared:
            if artifact.status == 'active' and Path(value).name in PROHIBITED_RESOURCE_NAMES:
                errors.append(f'{artifact.name}: legacy-only {kind} resource declared: {value}')
            if not any(candidate.exists() for candidate in resource_candidates(artifact, workspace, kind, value)):
                errors.append(f'{artifact.name}: missing {kind} resource: {value}')
        folder = artifact.directory / kind
        if not folder.exists():
            continue
        for file_path in sorted(path for path in folder.rglob('*') if path.is_file()):
            relative_to_artifact = file_path.relative_to(artifact.directory).as_posix()
            relative_to_kind = file_path.relative_to(folder).as_posix()
            if relative_to_artifact not in normalized and relative_to_kind not in normalized:
                errors.append(f'{artifact.name}: orphaned {kind} resource: {relative_to_artifact}')


def validate_generated(workspace: Any, errors: list[str]) -> None:
    """Validate generated artifacts are fresh."""
    for path, expected in rebuild.render_artifacts(workspace).items():
        if not path.exists():
            errors.append(f'{rel(workspace.root, path)}: missing generated artifact')
            continue
        actual = path.read_text(encoding='utf-8')
        if actual != expected:
            errors.append(f'{rel(workspace.root, path)}: stale generated artifact')


def validate_agent_skill_frontmatter(root: Path, skill_path: Path, expected_name: str, errors: list[str]) -> None:
    """Validate a public agent skill frontmatter block."""
    if not skill_path.exists():
        errors.append(f'{rel(root, skill_path.parent)}: missing {AGENT_SKILL_NAME}')
        return
    text = skill_path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        errors.append(f'{rel(root, skill_path)}: missing YAML frontmatter')
        return
    try:
        closing_index = text.index('\n---', 4)
    except ValueError:
        errors.append(f'{rel(root, skill_path)}: invalid YAML frontmatter')
        return
    try:
        data = rebuild.simple_yaml_load(text[4:closing_index])
    except Exception as error:
        errors.append(f'{rel(root, skill_path)}: invalid YAML frontmatter: {error}')
        return
    name = data.get('name')
    description = data.get('description')
    if not isinstance(name, str) or not name:
        errors.append(f'{rel(root, skill_path)}: missing name in frontmatter')
    elif not AGENT_SKILL_NAME_RE.fullmatch(name):
        errors.append(f'{rel(root, skill_path)}: invalid skill name {name!r}')
    elif name != expected_name:
        errors.append(f'{rel(root, skill_path)}: name {name!r} does not match metadata {expected_name!r}')
    if not isinstance(description, str) or not description:
        errors.append(f'{rel(root, skill_path)}: missing description in frontmatter')


def validate_agent_skill_folder(root: Path, skill_dir: Path, expected_name: str, errors: list[str]) -> None:
    """Validate a public agent skill folder and direct-invocation UI metadata."""
    validate_agent_skill_frontmatter(root, skill_dir / AGENT_SKILL_NAME, expected_name, errors)

    agent_metadata = skill_dir / AGENT_METADATA_PATH
    if not agent_metadata.exists():
        errors.append(f'{rel(root, skill_dir)}: missing {AGENT_METADATA_PATH.as_posix()}')
        return
    try:
        metadata = rebuild.load_yaml(agent_metadata)
        interface = rebuild.as_mapping(metadata.get('interface'), 'agents.openai.yaml.interface')
        policy = rebuild.as_mapping(metadata.get('policy'), 'agents.openai.yaml.policy')
    except Exception as error:
        errors.append(f'{rel(root, agent_metadata)}: {error}')
    else:
        for field in AGENT_METADATA_INTERFACE_FIELDS:
            value = interface.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f'{rel(root, agent_metadata)}: interface.{field} must be a non-empty string')
        if policy.get('allow_implicit_invocation') is not False:
            errors.append(f'{rel(root, agent_metadata)}: policy.allow_implicit_invocation must be false')


def validate_agent_entry(root: Path, entry_dir: Path, expected_name: str, errors: list[str]) -> None:
    """Validate the public entry is also an invokable agent skill."""
    validate_agent_skill_folder(root, entry_dir, expected_name, errors)

    legacy_agent_metadata = entry_dir / 'openai.yaml'
    if legacy_agent_metadata.exists():
        errors.append(f'{rel(root, legacy_agent_metadata)}: use agents/openai.yaml instead')

    entry_instructions = entry_dir / 'instructions.md'
    if entry_instructions.exists():
        errors.append(f'{rel(root, entry_instructions)}: entry instructions belong in {AGENT_SKILL_NAME}')


def load_metadata(root: Path, artifact: Any, errors: list[str]) -> dict[str, Any]:
    """Load artifact metadata for validation-only checks."""
    metadata_path = artifact.directory / 'skill.yaml'
    try:
        return rebuild.load_yaml(metadata_path)
    except Exception as error:
        errors.append(f'{rel(root, metadata_path)}: {error}')
        return {}


def validate_lifecycle_file(root: Path, artifact: Any, phase: str, raw_path: str, errors: list[str]) -> None:
    """Validate one lifecycle phase file."""
    if phase not in artifact.lifecycle:
        return
    relative = Path(raw_path)
    if relative.is_absolute() or '..' in relative.parts:
        errors.append(f'{artifact.name}: lifecycle {phase} path must stay inside the module: {raw_path}')
        return
    if not relative.parts or relative.parts[0] != 'lifecycle':
        errors.append(f'{artifact.name}: lifecycle {phase} path must be under lifecycle/: {raw_path}')
    path = artifact.directory / relative
    try:
        path.relative_to(artifact.directory)
    except ValueError:
        errors.append(f'{artifact.name}: lifecycle {phase} path must stay inside the module: {raw_path}')
        return
    if not path.exists():
        errors.append(f'{artifact.name}: missing lifecycle file: {raw_path}')
        return
    text = path.read_text(encoding='utf-8')
    for marker in LIFECYCLE_REQUIRED_MARKERS:
        if marker not in text:
            errors.append(f'{rel(root, path)}: missing required lifecycle section: {marker}')
    for phrase in PROHIBITED_LIFECYCLE_TEXT:
        if phrase in text:
            errors.append(f'{rel(root, path)}: prohibited lifecycle routing/output text remains: {phrase}')
    for phrase in PROHIBITED_PROSE_PHRASES:
        if phrase in text:
            errors.append(f'{rel(root, path)}: template prose remains: {phrase}')
    for line_number, line in enumerate(text.splitlines(), 1):
        if any(pattern.fullmatch(line) for pattern in PROHIBITED_PROSE_PATTERNS):
            errors.append(f'{rel(root, path)}:{line_number}: title-swapped boilerplate remains')


def validate_lifecycle(workspace: Any, artifact: Any, metadata: dict[str, Any], errors: list[str]) -> None:
    """Validate routed module lifecycle declarations and files."""
    if artifact.activation == 'explicit' and metadata.get('lifecycle'):
        errors.append(f'{artifact.name}: command skills must not declare lifecycle files')
    if artifact.activation != 'routed':
        return

    instructions_path = artifact.directory / 'instructions.md'
    if instructions_path.exists():
        errors.append(f'{rel(workspace.root, instructions_path)}: routed module runtime belongs in lifecycle files')

    for phase in artifact.lifecycle:
        if phase not in workspace.phases:
            errors.append(f'{artifact.name}: unknown lifecycle phase: {phase}')
    for phase, path in artifact.lifecycle.items():
        validate_lifecycle_file(workspace.root, artifact, phase, path, errors)

    lifecycle_dir = artifact.directory / 'lifecycle'
    declared = {value for value in artifact.lifecycle.values()}
    if lifecycle_dir.exists():
        for file_path in sorted(path for path in lifecycle_dir.rglob('*.md') if path.is_file()):
            relative = file_path.relative_to(artifact.directory).as_posix()
            if relative not in declared:
                errors.append(f'{artifact.name}: undeclared lifecycle file: {relative}')

    if artifact.status == 'active' and not artifact.lifecycle:
        errors.append(f'{artifact.name}: active routed module has no lifecycle files')


def normalized_text(value: str) -> str:
    """Normalize text for weak routing-quality checks."""
    return re.sub(r'[^a-z0-9]+', ' ', value.lower()).strip()


def validate_facets(workspace: Any, artifact: Any, metadata: dict[str, Any], errors: list[str]) -> None:
    """Validate structured routing facets for routed modules."""
    routing = rebuild.as_mapping(metadata.get('routing'), f'{artifact.name}.routing')
    for key in PROHIBITED_ROUTING_KEYS:
        if key in routing:
            errors.append(f'{artifact.name}: prohibited routing key remains: {key}')

    facets_raw = rebuild.as_mapping(routing.get('facets'), f'{artifact.name}.routing.facets')
    for key in facets_raw:
        if key not in workspace.facet_keys:
            errors.append(f'{artifact.name}: unknown routing facet key: {key}')
    if artifact.activation != 'routed' or artifact.status != 'active':
        return

    values = [value for facet_values in artifact.facets.values() for value in facet_values]
    if not values:
        errors.append(f'{artifact.name}: active routed module has no routing facets')
    normalized_name = normalized_text(artifact.name)
    for key, facet_values in artifact.facets.items():
        for value in facet_values:
            normalized_value = normalized_text(value)
            if not normalized_value:
                errors.append(f'{artifact.name}: empty routing facet value in {key}')
            if normalized_value == normalized_name:
                errors.append(f'{artifact.name}: routing facet only restates module name: {value}')
            if 'evidence for ' in value.lower():
                errors.append(f'{artifact.name}: routing facet uses mechanical evidence wording: {value}')


def runtime_dir(workspace: Any) -> str:
    """Return the entry-local runtime directory name."""
    return f'.{workspace.entry.name}'


def validate_runtime_config(workspace: Any, names: dict[str, Any], errors: list[str]) -> None:
    """Validate operator-local entry config if it exists."""
    config_path = workspace.root / runtime_dir(workspace) / 'config.json'
    if not config_path.exists():
        return
    try:
        data = json.loads(config_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as error:
        errors.append(f'{rel(workspace.root, config_path)}: invalid JSON: {error}')
        return
    if not isinstance(data, dict):
        errors.append(f'{rel(workspace.root, config_path)}: expected JSON object')
        return
    phases = data.get('phases')
    if not isinstance(phases, dict):
        errors.append(f'{rel(workspace.root, config_path)}: phases must be an object')
        return
    for phase, config in phases.items():
        if phase not in workspace.phases:
            errors.append(f'{rel(workspace.root, config_path)}: unknown phase in config: {phase}')
            continue
        if not isinstance(config, dict):
            errors.append(f'{rel(workspace.root, config_path)}: phases.{phase} must be an object')
            continue
        always = config.get('always', [])
        if not isinstance(always, list):
            errors.append(f'{rel(workspace.root, config_path)}: phases.{phase}.always must be a list')
            continue
        for target in always:
            if not isinstance(target, str):
                errors.append(f'{rel(workspace.root, config_path)}: phases.{phase}.always must contain strings')
                continue
            artifact = names.get(target)
            if artifact is None:
                errors.append(f'{rel(workspace.root, config_path)}: phases.{phase}.always target does not exist: {target}')
            elif artifact.activation != 'routed' or artifact.visibility != 'hidden' or artifact.status != 'active':
                errors.append(f'{rel(workspace.root, config_path)}: phases.{phase}.always target must be an active hidden routed module: {target}')


def validate_gitignore(workspace: Any, errors: list[str]) -> None:
    """Validate local runtime state is ignored by git."""
    root = workspace.root
    runtime = f'{runtime_dir(workspace)}/'
    gitignore = root / '.gitignore'
    if not gitignore.exists():
        errors.append(f'.gitignore: missing file required to ignore {runtime}')
        return
    lines = {line.strip() for line in gitignore.read_text(encoding='utf-8').splitlines()}
    if runtime not in lines:
        errors.append(f'.gitignore: missing {runtime}')


def validate_workspace(raw_manifest: str | None) -> list[str]:
    """Return Cortex routed workspace validation errors."""
    errors: list[str] = []
    try:
        manifest_path = rebuild.find_manifest(raw_manifest)
        manifest = rebuild.load_yaml(manifest_path)
    except Exception as error:
        return [str(error)]

    root = manifest_path.parent
    try:
        paths = rebuild.merge_defaults(manifest.get('paths'), rebuild.DEFAULT_PATHS, 'paths')
        artifacts = rebuild.merge_defaults(manifest.get('artifacts'), rebuild.DEFAULT_ARTIFACTS, 'artifacts')
        facet_keys = rebuild.facet_keys_from_manifest(manifest)
        phases = rebuild.phases_from_manifest(manifest)
    except Exception as error:
        return [str(error)]
    if not facet_keys:
        errors.append('routing.facets.keys: expected at least one facet key')
    if not phases:
        errors.append('lifecycle.phases: expected at least one phase')

    entry_config = rebuild.as_mapping(manifest.get('entry'), 'entry')
    entry_path_value = entry_config.get('path')
    if not isinstance(entry_path_value, str) or not entry_path_value:
        return ['entry.path: expected string']

    entry_root = root / paths['entry']
    entry_dir = root / entry_path_value
    metadata_name = artifacts['metadata']

    entry_dirs: list[Path] = []
    if entry_root.exists():
        for child in sorted(entry_root.iterdir()):
            metadata_path = child / metadata_name
            if child.is_dir() and metadata_path.exists():
                try:
                    metadata = rebuild.load_yaml(metadata_path)
                except Exception as error:
                    errors.append(f'{rel(root, metadata_path)}: {error}')
                    continue
                if metadata.get('activation') == 'entry':
                    entry_dirs.append(child)
    if len(entry_dirs) != 1:
        errors.append(f'expected exactly one entry skill, found {len(entry_dirs)}')
    elif entry_dirs[0] != entry_dir:
        errors.append(f'entry.path points to {entry_path_value}, but entry skill is {rel(root, entry_dirs[0])}')

    if not (entry_dir / metadata_name).exists():
        errors.append(f'{rel(root, entry_dir)}: missing {metadata_name}')

    modules_root = root / paths['modules']
    validate_modules_tree(root, modules_root, metadata_name, errors)

    commands_root = root / paths['commands']
    if commands_root.exists():
        for child in sorted(commands_root.iterdir()):
            if not child.is_dir():
                continue
            if not (child / metadata_name).exists():
                errors.append(f'{rel(root, child)}: missing {metadata_name}')
            if (child / 'instructions.md').exists():
                errors.append(f'{rel(root, child / "instructions.md")}: command behavior belongs in {AGENT_SKILL_NAME}')

    try:
        workspace = rebuild.load_workspace(str(manifest_path))
    except Exception as error:
        errors.append(str(error))
        return sorted(set(errors))

    names: dict[str, Any] = {}
    for artifact in workspace.artifacts:
        if artifact.name in names:
            errors.append(f'duplicate artifact name: {artifact.name}')
        names[artifact.name] = artifact

    known_names = set(names)
    for artifact in workspace.artifacts:
        metadata = load_metadata(workspace.root, artifact, errors)
        for key in PROHIBITED_METADATA_KEYS:
            if key in metadata:
                errors.append(f'{artifact.name}: prohibited metadata key remains: {key}')
        if artifact.activation not in VALID_ACTIVATIONS:
            errors.append(f'{artifact.name}: invalid activation {artifact.activation!r}')
        if artifact.visibility not in VALID_VISIBILITIES:
            errors.append(f'{artifact.name}: invalid visibility {artifact.visibility!r}')
        if artifact.activation == 'entry' and artifact.visibility != 'public':
            errors.append(f'{artifact.name}: entry skill must be public')
        if artifact.activation == 'routed' and artifact.visibility != 'hidden':
            errors.append(f'{artifact.name}: routed module must be hidden')
        if artifact.activation == 'explicit' and artifact.visibility != 'public':
            errors.append(f'{artifact.name}: command skill must be public')
        validate_resources(workspace, artifact, known_names, errors)
        validate_facets(workspace, artifact, metadata, errors)
        validate_lifecycle(workspace, artifact, metadata, errors)
        if artifact.activation == 'explicit':
            validate_agent_skill_folder(workspace.root, artifact.directory, artifact.name, errors)

    if workspace.entry.activation != 'entry':
        errors.append(f'{workspace.entry.name}: entry skill must use activation entry')
    if workspace.entry.visibility != 'public':
        errors.append(f'{workspace.entry.name}: entry skill must be public')
    validate_agent_entry(workspace.root, workspace.entry.directory, workspace.entry.name, errors)

    validate_runtime_config(workspace, names, errors)
    validate_gitignore(workspace, errors)
    validate_generated(workspace, errors)
    return sorted(set(errors))


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', nargs='?', help='Path to routed-skills.yaml or its directory.')
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run Cortex routed workspace validation."""
    args = parse_args(argv)
    errors = validate_workspace(args.manifest)
    if errors:
        for error in errors:
            print(f'error: {error}', file=sys.stderr)
        return 1
    print('validation ok')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
