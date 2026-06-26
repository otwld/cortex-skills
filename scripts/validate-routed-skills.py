#!/usr/bin/env python3
"""Validate routed skill workspace structure, metadata, routing, and generated artifacts."""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
REBUILD_PATH = SCRIPT_DIR / 'rebuild-routed-skills.py'
VALID_ACTIVATIONS = {'entry', 'routed', 'explicit'}
VALID_VISIBILITIES = {'public', 'hidden'}
RELATION_KEYS = ('before', 'with', 'after', 'excludes', 'replaces')
RESOURCE_KEYS = ('references', 'scripts', 'templates', 'assets')
DEFAULT_MODULE_PATH_MIN_DEPTH = 1
DEFAULT_MODULE_PATH_MAX_DEPTH = 4
AGENT_SKILL_NAME = 'SKILL.md'
AGENT_METADATA_PATH = Path('agents') / 'openai.yaml'
AGENT_SKILL_NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
INSTRUCTION_REQUIRED_MARKERS = (
    '# Output Marker',
    '## Overview',
    '## Workflow',
    '## Quality Gates',
    '## Hard Stops',
    '## Usage Checklist',
    '## Cross References',
)
PROHIBITED_RESOURCE_NAMES = {'legacy-extracted-patterns.md'}
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
NON_CONTENT_BULLET_SECTIONS = {'Reference Routing', 'Cross References'}
DUPLICATED_BULLET_LIMIT = 2
AGENT_METADATA_INTERFACE_FIELDS = ('display_name', 'short_description', 'default_prompt')
BROAD_STRONG_SIGNAL_TERMS = ('final response',)


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


def relation_targets(artifact: Any) -> set[str]:
    """Return all relation targets for one artifact."""
    targets: set[str] = set()
    for key in RELATION_KEYS:
        targets.update(artifact.relations[key])
    return targets


def before_chain(name: str, before_map: dict[str, list[str]], stack: list[str], errors: list[str], limit: int) -> int:
    """Return maximum before depth while recording cycles and depth violations."""
    if name in stack:
        errors.append(f'before cycle: {" -> ".join(stack[stack.index(name):] + [name])}')
        return 0
    children = before_map.get(name, [])
    if not children:
        return 0
    max_depth = 0
    for child in children:
        depth = 1 + before_chain(child, before_map, [*stack, name], errors, limit)
        max_depth = max(max_depth, depth)
    if max_depth > limit:
        errors.append(f'{name}: before depth {max_depth} exceeds cap {limit}')
    return max_depth


def connected(left: Any, right: Any) -> bool:
    """Return whether two artifacts are directly related."""
    return right.name in relation_targets(left) or left.name in relation_targets(right)


def normalized_signal_text(value: str) -> str:
    """Normalize a signal or artifact name for routing-quality comparisons."""
    return re.sub(r'[^a-z0-9]+', ' ', value.lower()).strip()


def signal_category(value: str) -> str | None:
    """Return a strong-signal category prefix when the signal declares one."""
    if ':' not in value:
        return None
    category = normalized_signal_text(value.split(':', 1)[0])
    return category or None


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


def has_module_like_contents(path: Path, instructions_name: str) -> bool:
    """Return whether a non-artifact folder contains files that require artifact metadata."""
    if (path / instructions_name).exists() or (path / AGENT_SKILL_NAME).exists():
        return True
    if (path / AGENT_METADATA_PATH).exists():
        return True
    return any((path / folder).exists() for folder in RESOURCE_KEYS)


def validate_modules_tree(root: Path, modules_root: Path, metadata_name: str, instructions_name: str, errors: list[str]) -> None:
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
            if not (directory / instructions_name).exists():
                errors.append(f'{rel(root, directory)}: missing {instructions_name}')
            continue

        if is_under_artifact(directory, artifact_dirs):
            continue

        if has_module_like_contents(directory, instructions_name):
            errors.append(f'{rel(root, directory)}: missing {metadata_name}')
        elif not has_descendant_artifact(directory, artifact_dirs):
            errors.append(f'{rel(root, directory)}: category folder has no descendant module artifact')


def validation_integer(value: Any, label: str, default: int, errors: list[str]) -> int:
    """Return an integer validation setting or record an error and use a default."""
    if value is None:
        return default
    if not isinstance(value, int):
        errors.append(f'{label}: expected integer')
        return default
    return value


def validate_module_path_depths(workspace: Any, validation: dict[str, Any], errors: list[str]) -> None:
    """Validate module artifact path depth relative to the modules root."""
    min_depth = validation_integer(
        validation.get('module_path_min_depth'),
        'validation.module_path_min_depth',
        DEFAULT_MODULE_PATH_MIN_DEPTH,
        errors,
    )
    max_depth = validation_integer(
        validation.get('module_path_max_depth'),
        'validation.module_path_max_depth',
        DEFAULT_MODULE_PATH_MAX_DEPTH,
        errors,
    )
    if min_depth > max_depth:
        errors.append('validation.module_path_min_depth must be less than or equal to validation.module_path_max_depth')
        return

    modules_root = workspace.root / manifest_value(workspace, 'paths', rebuild.DEFAULT_PATHS)['modules']
    for artifact in workspace.modules:
        try:
            depth = len(artifact.directory.relative_to(modules_root).parts)
        except ValueError:
            continue
        if depth < min_depth:
            errors.append(f'{artifact.relative_path}: module path depth {depth} is below minimum {min_depth}')
        if depth > max_depth:
            errors.append(f'{artifact.relative_path}: module path depth {depth} exceeds maximum {max_depth}')


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


def validate_always_loaded_modules(workspace: Any, names: dict[str, Any], errors: list[str]) -> None:
    """Validate manifest-level always-loaded routed modules."""
    for target in workspace.always:
        artifact = names.get(target)
        if artifact is None:
            errors.append(f'routing.always target does not exist: {target}')
            continue
        if artifact.activation != 'routed':
            errors.append(f'routing.always target must be a routed module: {target}')
        if artifact.visibility != 'hidden':
            errors.append(f'routing.always target must be hidden: {target}')
        if artifact.status != 'active':
            errors.append(f'routing.always target must be active: {target}')


def validate_active_routed_module_content(
    workspace: Any,
    active_routed: list[Any],
    instructions_name: str,
    errors: list[str],
) -> None:
    """Validate active module reachability and instruction prose quality."""
    duplicated_bullets: dict[str, list[str]] = {}
    for artifact in active_routed:
        if not any(artifact.signals[key] for key in rebuild.SIGNAL_KEYS):
            errors.append(f'{artifact.name}: active routed module has no routing signals')
        for signal in artifact.signals['strong']:
            normalized_signal = normalized_signal_text(signal)
            normalized_name = normalized_signal_text(artifact.name)
            if re.search(rf'\bevidence for {re.escape(artifact.name)}:', signal, re.IGNORECASE):
                errors.append(f'{artifact.name}: strong signal uses mechanical evidence prefix: {signal}')
            if normalized_signal == normalized_name:
                errors.append(f'{artifact.name}: strong signal only restates module name: {signal}')
            for term in BROAD_STRONG_SIGNAL_TERMS:
                if term in signal.lower():
                    errors.append(f'{artifact.name}: strong signal uses broad lifecycle wording: {signal}')
        for signal in artifact.signals['weak']:
            if normalized_signal_text(signal) == normalized_signal_text(artifact.name):
                errors.append(f'{artifact.name}: weak signal only restates module name: {signal}')

        instruction_path = artifact.directory / instructions_name
        if not instruction_path.exists():
            continue
        text = instruction_path.read_text(encoding='utf-8')
        for marker in INSTRUCTION_REQUIRED_MARKERS:
            if marker not in text:
                errors.append(f'{rel(workspace.root, instruction_path)}: missing required instruction section: {marker}')
        for phrase in PROHIBITED_PROSE_PHRASES:
            if phrase in text:
                errors.append(f'{rel(workspace.root, instruction_path)}: template prose remains: {phrase}')
        for line_number, line in enumerate(text.splitlines(), 1):
            if any(pattern.fullmatch(line) for pattern in PROHIBITED_PROSE_PATTERNS):
                errors.append(f'{rel(workspace.root, instruction_path)}:{line_number}: title-swapped boilerplate remains')

        section = ''
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.startswith('## '):
                section = line[3:].strip()
            if not line.startswith('- ') or section in NON_CONTENT_BULLET_SECTIONS:
                continue
            duplicated_bullets.setdefault(line, []).append(f'{rel(workspace.root, instruction_path)}:{line_number}')

    for bullet, locations in duplicated_bullets.items():
        if len(locations) > DUPLICATED_BULLET_LIMIT:
            errors.append(f'duplicated instruction bullet across active modules: {bullet}')


def load_agent_skill_frontmatter(root: Path, skill_path: Path, errors: list[str]) -> dict[str, Any]:
    """Load the constrained YAML frontmatter from an agent SKILL.md."""
    if not skill_path.exists():
        errors.append(f'{rel(root, skill_path.parent)}: missing {AGENT_SKILL_NAME}')
        return {}
    text = skill_path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        errors.append(f'{rel(root, skill_path)}: missing YAML frontmatter')
        return {}
    try:
        closing_index = text.index('\n---', 4)
    except ValueError:
        errors.append(f'{rel(root, skill_path)}: invalid YAML frontmatter')
        return {}
    try:
        data = rebuild.simple_yaml_load(text[4:closing_index])
    except Exception as error:
        errors.append(f'{rel(root, skill_path)}: invalid YAML frontmatter: {error}')
        return {}
    if not isinstance(data, dict):
        errors.append(f'{rel(root, skill_path)}: frontmatter must be a mapping')
        return {}
    return data


def validate_agent_entry(root: Path, entry_dir: Path, expected_name: str, instructions_name: str, errors: list[str]) -> None:
    """Validate the public entry is also an invokable agent skill."""
    validate_agent_skill_folder(root, entry_dir, expected_name, errors)

    legacy_agent_metadata = entry_dir / 'openai.yaml'
    if legacy_agent_metadata.exists():
        errors.append(f'{rel(root, legacy_agent_metadata)}: use agents/openai.yaml instead')

    entry_instructions = entry_dir / instructions_name
    if entry_instructions.exists():
        errors.append(f'{rel(root, entry_instructions)}: entry instructions belong in {AGENT_SKILL_NAME}')


def validate_agent_skill_folder(root: Path, skill_dir: Path, expected_name: str, errors: list[str]) -> None:
    """Validate a public agent skill folder and direct-invocation policy."""
    skill_path = skill_dir / AGENT_SKILL_NAME
    frontmatter = load_agent_skill_frontmatter(root, skill_path, errors)
    validate_output_marker(root, skill_path, f'using skill: {expected_name}', errors)
    name = frontmatter.get('name')
    description = frontmatter.get('description')
    if not isinstance(name, str) or not name:
        errors.append(f'{rel(root, skill_path)}: missing name in frontmatter')
    elif not AGENT_SKILL_NAME_RE.fullmatch(name):
        errors.append(f'{rel(root, skill_path)}: invalid skill name {name!r}')
    elif name != expected_name:
        errors.append(f'{rel(root, skill_path)}: name {name!r} does not match metadata {expected_name!r}')
    if not isinstance(description, str) or not description:
        errors.append(f'{rel(root, skill_path)}: missing description in frontmatter')

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


def validate_output_marker(root: Path, path: Path, expected_line: str, errors: list[str]) -> None:
    """Validate an instruction artifact declares its client display marker."""
    if not path.exists():
        return
    text = path.read_text(encoding='utf-8')
    if '# Output Marker' not in text or 'Display:' not in text or expected_line not in text:
        errors.append(f'{rel(root, path)}: missing output marker: {expected_line}')


def validate_workspace(raw_manifest: str | None) -> list[str]:
    """Return routed workspace validation errors."""
    errors: list[str] = []
    try:
        manifest_path = rebuild.find_manifest(raw_manifest)
        manifest = rebuild.load_yaml(manifest_path)
    except Exception as error:
        return [str(error)]

    root = manifest_path.parent
    paths = rebuild.merge_defaults(manifest.get('paths'), rebuild.DEFAULT_PATHS, 'paths')
    artifacts = rebuild.merge_defaults(manifest.get('artifacts'), rebuild.DEFAULT_ARTIFACTS, 'artifacts')
    entry_config = rebuild.as_mapping(manifest.get('entry'), 'entry')
    entry_path_value = entry_config.get('path')
    if not isinstance(entry_path_value, str) or not entry_path_value:
        return ['entry.path: expected string']

    entry_root = root / paths['entry']
    entry_dir = root / entry_path_value
    metadata_name = artifacts['metadata']
    instructions_name = artifacts['instructions']

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
    validate_modules_tree(root, modules_root, metadata_name, instructions_name, errors)

    commands_root = root / paths['commands']
    if commands_root.exists():
        for child in sorted(commands_root.iterdir()):
            if not child.is_dir():
                continue
            if not (child / metadata_name).exists():
                errors.append(f'{rel(root, child)}: missing {metadata_name}')
            if (child / instructions_name).exists():
                errors.append(f'{rel(root, child / instructions_name)}: command behavior belongs in {AGENT_SKILL_NAME}')

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
        if artifact.activation == 'routed' and not (artifact.directory / instructions_name).exists():
            errors.append(f'{artifact.name}: missing {instructions_name}')
        if artifact.activation == 'routed':
            validate_output_marker(
                workspace.root,
                artifact.directory / instructions_name,
                f'using module: {artifact.name}',
                errors,
            )
        if artifact.activation == 'explicit':
            validate_agent_skill_folder(workspace.root, artifact.directory, artifact.name, errors)

    if workspace.entry.activation != 'entry':
        errors.append(f'{workspace.entry.name}: entry skill must use activation entry')
    if workspace.entry.visibility != 'public':
        errors.append(f'{workspace.entry.name}: entry skill must be public')
    validate_agent_entry(workspace.root, workspace.entry.directory, workspace.entry.name, instructions_name, errors)
    validate_always_loaded_modules(workspace, names, errors)

    name_set = set(names)
    for artifact in [*workspace.modules, *workspace.commands]:
        for key in RELATION_KEYS:
            for target in artifact.relations[key]:
                if target not in name_set:
                    errors.append(f'{artifact.name}: {key} target does not exist: {target}')
        validate_resources(workspace, artifact, name_set, errors)

    before_map = {
        artifact.name: artifact.relations['before']
        for artifact in workspace.modules
        if artifact.activation == 'routed'
    }
    validation = rebuild.as_mapping(workspace.manifest.get('validation'), 'validation')
    max_depth = validation.get('max_before_depth', 3)
    if not isinstance(max_depth, int):
        errors.append('validation.max_before_depth: expected integer')
        max_depth = 3
    validate_module_path_depths(workspace, validation, errors)
    for name in before_map:
        before_chain(name, before_map, [], errors, max_depth)

    active_routed = [
        artifact for artifact in workspace.modules
        if artifact.activation == 'routed' and artifact.status == 'active'
    ]
    validate_active_routed_module_content(workspace, active_routed, instructions_name, errors)
    signals: dict[str, list[Any]] = {}
    signal_categories: dict[str, list[Any]] = {}
    for artifact in active_routed:
        for signal in artifact.signals['strong']:
            signals.setdefault(signal.strip().lower(), []).append(artifact)
            category = signal_category(signal)
            if category is not None:
                signal_categories.setdefault(category, []).append(artifact)
    for signal, artifacts_with_signal in signals.items():
        if len(artifacts_with_signal) < 2:
            continue
        unrelated = [
            artifact.name for artifact in artifacts_with_signal
            if any(not connected(artifact, other) for other in artifacts_with_signal if other is not artifact)
        ]
        if unrelated:
            errors.append(f'duplicate strong signal across unrelated modules: {signal}')
    for category, artifacts_with_category in signal_categories.items():
        if len(artifacts_with_category) < 2:
            continue
        unrelated = [
            artifact.name for artifact in artifacts_with_category
            if any(not connected(artifact, other) for other in artifacts_with_category if other is not artifact)
        ]
        if unrelated:
            errors.append(f'duplicate strong signal category across unrelated modules: {category}')

    shared_root = workspace.root / paths['shared']
    used_shared = {
        value.removeprefix('shared/')
        for artifact in [*workspace.modules, *workspace.commands]
        for value in [*artifact.uses, *sum((artifact.resources[key] for key in RESOURCE_KEYS), [])]
        if value.startswith('shared/')
    }
    if shared_root.exists():
        for child in sorted(shared_root.iterdir()):
            if child.name not in used_shared and not any(value.startswith(f'{child.name}/') for value in used_shared):
                errors.append(f'{rel(workspace.root, child)}: orphaned shared resource')

    validate_generated(workspace, errors)
    return sorted(set(errors))


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', nargs='?', help='Path to routed-skills.yaml or its directory.')
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run routed workspace validation."""
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
