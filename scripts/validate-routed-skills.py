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
AGENT_SKILL_NAME = 'SKILL.md'
AGENT_METADATA_PATH = Path('agents') / 'openai.yaml'
AGENT_SKILL_NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


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


def resource_candidates(artifact: Any, workspace: Any, kind: str, value: str) -> list[Path]:
    """Return accepted paths for a resource declaration."""
    if value.startswith('shared/'):
        return [workspace.root / value]
    return [
        artifact.directory / value,
        artifact.directory / kind / value,
        workspace.root / 'shared' / value,
    ]


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
    skill_path = entry_dir / AGENT_SKILL_NAME
    frontmatter = load_agent_skill_frontmatter(root, skill_path, errors)
    name = frontmatter.get('name')
    description = frontmatter.get('description')
    if not isinstance(name, str) or not name:
        errors.append(f'{rel(root, skill_path)}: missing name in frontmatter')
    elif not AGENT_SKILL_NAME_RE.fullmatch(name):
        errors.append(f'{rel(root, skill_path)}: invalid skill name {name!r}')
    elif name != expected_name:
        errors.append(f'{rel(root, skill_path)}: name {name!r} does not match entry metadata {expected_name!r}')
    if not isinstance(description, str) or not description:
        errors.append(f'{rel(root, skill_path)}: missing description in frontmatter')

    agent_metadata = entry_dir / AGENT_METADATA_PATH
    if not agent_metadata.exists():
        errors.append(f'{rel(root, entry_dir)}: missing {AGENT_METADATA_PATH.as_posix()}')
    else:
        try:
            metadata = rebuild.load_yaml(agent_metadata)
            policy = rebuild.as_mapping(metadata.get('policy'), 'agents.openai.yaml.policy')
        except Exception as error:
            errors.append(f'{rel(root, agent_metadata)}: {error}')
        else:
            if policy.get('allow_implicit_invocation') is not False:
                errors.append(f'{rel(root, agent_metadata)}: policy.allow_implicit_invocation must be false')

    legacy_agent_metadata = entry_dir / 'openai.yaml'
    if legacy_agent_metadata.exists():
        errors.append(f'{rel(root, legacy_agent_metadata)}: use agents/openai.yaml instead')

    entry_instructions = entry_dir / instructions_name
    if entry_instructions.exists():
        errors.append(f'{rel(root, entry_instructions)}: entry instructions belong in {AGENT_SKILL_NAME}')


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
    if modules_root.exists():
        for child in sorted(modules_root.iterdir()):
            if not child.is_dir():
                continue
            if not (child / metadata_name).exists():
                errors.append(f'{rel(root, child)}: missing {metadata_name}')
            if not (child / instructions_name).exists():
                errors.append(f'{rel(root, child)}: missing {instructions_name}')

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
            errors.append(f'{artifact.name}: explicit command must be public')
        if artifact.activation != 'entry' and not (artifact.directory / instructions_name).exists():
            errors.append(f'{artifact.name}: missing {instructions_name}')

    if workspace.entry.activation != 'entry':
        errors.append(f'{workspace.entry.name}: entry skill must use activation entry')
    if workspace.entry.visibility != 'public':
        errors.append(f'{workspace.entry.name}: entry skill must be public')
    validate_agent_entry(workspace.root, workspace.entry.directory, workspace.entry.name, instructions_name, errors)

    name_set = set(names)
    for artifact in workspace.modules:
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
    for name in before_map:
        before_chain(name, before_map, [], errors, max_depth)

    active_routed = [
        artifact for artifact in workspace.modules
        if artifact.activation == 'routed' and artifact.status == 'active'
    ]
    signals: dict[str, list[Any]] = {}
    for artifact in active_routed:
        for signal in artifact.signals['strong']:
            signals.setdefault(signal.strip().lower(), []).append(artifact)
    for signal, artifacts_with_signal in signals.items():
        if len(artifacts_with_signal) < 2:
            continue
        unrelated = [
            artifact.name for artifact in artifacts_with_signal
            if any(not connected(artifact, other) for other in artifacts_with_signal if other is not artifact)
        ]
        if unrelated:
            errors.append(f'duplicate strong signal across unrelated modules: {signal}')

    shared_root = workspace.root / paths['shared']
    used_shared = {
        value.removeprefix('shared/')
        for artifact in workspace.modules
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
