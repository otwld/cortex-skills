#!/usr/bin/env python3
"""Regenerate routed skill workspace catalog, graph, and cascade artifacts."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_PATHS = {
    'entry': 'entry',
    'modules': 'modules',
    'commands': 'commands',
    'shared': 'shared',
    'generated': 'generated',
    'proposals': 'proposals',
}
DEFAULT_ARTIFACTS = {
    'metadata': 'skill.yaml',
    'instructions': 'instructions.md',
}
DEFAULT_GENERATED = {
    'catalog': 'generated/SKILL_CATALOG.md',
    'graph': 'generated/module-graph.md',
    'cascade': 'generated/module-cascade.md',
}
RELATION_KEYS = ('before', 'with', 'after', 'excludes', 'replaces')
SIGNAL_KEYS = ('strong', 'medium', 'weak')


class RoutedSkillError(Exception):
    """Raised when a routed skill workspace cannot be loaded or rebuilt."""


@dataclass(frozen=True)
class Artifact:
    """Loaded entry, routed module, or command skill metadata."""

    name: str
    description: str
    activation: str
    visibility: str
    status: str
    directory: Path
    relative_path: str
    priority: int
    signals: dict[str, list[str]]
    relations: dict[str, list[str]]
    uses: list[str]
    resources: dict[str, list[str]]


@dataclass(frozen=True)
class Workspace:
    """Loaded routed skill workspace model with separated module and command collections."""

    manifest_path: Path
    root: Path
    manifest: dict[str, Any]
    entry: Artifact
    modules: list[Artifact]
    commands: list[Artifact]
    always: list[str]
    metadata_name: str
    instructions_name: str

    @property
    def artifacts(self) -> list[Artifact]:
        """Return all loaded artifacts in deterministic order."""
        return [self.entry, *self.modules, *self.commands]


def parse_scalar(value: str) -> Any:
    """Parse the constrained YAML scalar shape used by templates."""
    value = value.strip()
    if value == '':
        return ''
    if value == '[]':
        return []
    if value == '{}':
        return {}
    if value in ('true', 'false'):
        return value == 'true'
    if value in ('null', 'None'):
        return None
    if value.startswith(("'", '"')) and value.endswith(("'", '"')):
        return value[1:-1]
    if value.startswith('[') and value.endswith(']'):
        body = value[1:-1].strip()
        if not body:
            return []
        return [parse_scalar(part.strip()) for part in body.split(',')]
    try:
        return int(value)
    except ValueError:
        return value


def simple_yaml_load(text: str) -> dict[str, Any]:
    """Load the small YAML subset used by routed workspace metadata."""
    logical_lines: list[tuple[int, str]] = []
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith('#'):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(' '))
        logical_lines.append((indent, raw_line.strip()))

    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]

    for index, (indent, stripped) in enumerate(logical_lines):
        while indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if stripped.startswith('- '):
            if not isinstance(parent, list):
                raise RoutedSkillError('YAML list item found outside a list')
            parent.append(parse_scalar(stripped[2:].strip()))
            continue
        if ':' not in stripped:
            raise RoutedSkillError(f'invalid YAML line: {stripped}')
        key, raw_value = stripped.split(':', 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if not isinstance(parent, dict):
            raise RoutedSkillError(f'YAML mapping key {key!r} found outside a mapping')
        if raw_value:
            parent[key] = parse_scalar(raw_value)
            continue
        child: Any = {}
        for next_indent, next_text in logical_lines[index + 1:]:
            if next_indent <= indent:
                break
            child = [] if next_text.startswith('- ') else {}
            break
        parent[key] = child
        stack.append((indent, child))

    return root


def load_yaml(path: Path) -> dict[str, Any]:
    """Load YAML using PyYAML when available, otherwise the constrained parser."""
    try:
        import yaml  # type: ignore
    except ImportError:
        data = simple_yaml_load(path.read_text(encoding='utf-8'))
    else:
        data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    if not isinstance(data, dict):
        raise RoutedSkillError(f'{path}: expected a YAML mapping')
    return data


def find_manifest(raw_path: str | None) -> Path:
    """Find the routed workspace manifest."""
    if raw_path:
        candidate = Path(raw_path)
        if candidate.is_dir():
            candidate = candidate / 'routed-skills.yaml'
        if not candidate.exists():
            raise RoutedSkillError(f'manifest not found: {candidate}')
        return candidate.resolve()
    for candidate in (Path('routed-skills.yaml'), Path('.skills/routed-skills.yaml'), Path('skills/routed-skills.yaml')):
        if candidate.exists():
            return candidate.resolve()
    raise RoutedSkillError('manifest not found; pass routed-skills.yaml explicitly')


def as_mapping(value: Any, label: str) -> dict[str, Any]:
    """Return a mapping or fail with a clear label."""
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise RoutedSkillError(f'{label}: expected mapping')
    return value


def as_list(value: Any, label: str) -> list[str]:
    """Return a string list or fail with a clear label."""
    if value is None:
        return []
    if not isinstance(value, list):
        raise RoutedSkillError(f'{label}: expected list')
    result: list[str] = []
    for entry in value:
        if not isinstance(entry, str):
            raise RoutedSkillError(f'{label}: expected list of strings')
        result.append(entry)
    return result


def merge_defaults(value: Any, defaults: dict[str, str], label: str) -> dict[str, str]:
    """Merge a manifest mapping with string defaults."""
    raw = as_mapping(value, label)
    merged = dict(defaults)
    for key, item in raw.items():
        if not isinstance(item, str):
            raise RoutedSkillError(f'{label}.{key}: expected string')
        merged[key] = item
    return merged


def workspace_relative(root: Path, path: Path) -> str:
    """Return a stable workspace-relative path."""
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def load_artifact(directory: Path, metadata_name: str, root: Path) -> Artifact:
    """Load one artifact directory."""
    metadata_path = directory / metadata_name
    if not metadata_path.exists():
        raise RoutedSkillError(f'{workspace_relative(root, directory)}: missing {metadata_name}')
    metadata = load_yaml(metadata_path)
    name = metadata.get('name')
    if not isinstance(name, str) or not name:
        raise RoutedSkillError(f'{workspace_relative(root, metadata_path)}: missing name')
    description = metadata.get('description')
    if not isinstance(description, str) or not description:
        raise RoutedSkillError(f'{workspace_relative(root, metadata_path)}: missing description')
    activation = metadata.get('activation', '')
    visibility = metadata.get('visibility', '')
    status = metadata.get('status', 'active')
    if not isinstance(activation, str) or not isinstance(visibility, str) or not isinstance(status, str):
        raise RoutedSkillError(f'{workspace_relative(root, metadata_path)}: activation, visibility, and status must be strings')

    routing = as_mapping(metadata.get('routing'), f'{name}.routing')
    signals_raw = as_mapping(routing.get('signals'), f'{name}.routing.signals')
    relations_raw = as_mapping(metadata.get('relations'), f'{name}.relations')
    resources_raw = as_mapping(metadata.get('resources'), f'{name}.resources')
    priority = routing.get('priority', 0)
    if not isinstance(priority, int):
        raise RoutedSkillError(f'{name}.routing.priority: expected integer')

    return Artifact(
        name=name,
        description=description,
        activation=activation,
        visibility=visibility,
        status=status,
        directory=directory,
        relative_path=workspace_relative(root, directory),
        priority=priority,
        signals={key: as_list(signals_raw.get(key), f'{name}.signals.{key}') for key in SIGNAL_KEYS},
        relations={key: as_list(relations_raw.get(key), f'{name}.relations.{key}') for key in RELATION_KEYS},
        uses=as_list(metadata.get('uses'), f'{name}.uses'),
        resources={key: as_list(resources_raw.get(key), f'{name}.resources.{key}') for key in ('references', 'scripts', 'templates', 'assets')},
    )


def load_workspace(raw_manifest: str | None = None) -> Workspace:
    """Load a routed skill workspace from its manifest."""
    manifest_path = find_manifest(raw_manifest)
    manifest = load_yaml(manifest_path)
    root = manifest_path.parent
    paths = merge_defaults(manifest.get('paths'), DEFAULT_PATHS, 'paths')
    artifacts = merge_defaults(manifest.get('artifacts'), DEFAULT_ARTIFACTS, 'artifacts')
    routing = as_mapping(manifest.get('routing'), 'routing')
    always = as_list(routing.get('always'), 'routing.always')
    entry_config = as_mapping(manifest.get('entry'), 'entry')
    entry_path = entry_config.get('path')
    if not isinstance(entry_path, str) or not entry_path:
        raise RoutedSkillError('entry.path: expected string')

    entry = load_artifact(root / entry_path, artifacts['metadata'], root)
    modules_root = root / paths['modules']
    modules: list[Artifact] = []
    if modules_root.exists():
        for child in sorted(modules_root.iterdir()):
            if child.is_dir() and (child / artifacts['metadata']).exists():
                artifact = load_artifact(child, artifacts['metadata'], root)
                if artifact.activation == 'explicit':
                    raise RoutedSkillError(f'{artifact.relative_path}: command skill must live under {paths["commands"]}')
                modules.append(artifact)

    commands_root = root / paths['commands']
    commands: list[Artifact] = []
    if commands_root.exists():
        for child in sorted(commands_root.iterdir()):
            if child.is_dir() and (child / artifacts['metadata']).exists():
                artifact = load_artifact(child, artifacts['metadata'], root)
                if artifact.activation != 'explicit':
                    raise RoutedSkillError(f'{artifact.relative_path}: command skill must use activation explicit')
                commands.append(artifact)

    return Workspace(
        manifest_path=manifest_path,
        root=root,
        manifest=manifest,
        entry=entry,
        modules=modules,
        commands=commands,
        always=always,
        metadata_name=artifacts['metadata'],
        instructions_name=artifacts['instructions'],
    )


def cell(values: list[str]) -> str:
    """Render a generated table cell."""
    return ', '.join(f'`{value}`' for value in values) if values else 'None'


def text_cell(value: str) -> str:
    """Escape generated table text."""
    return value.replace('|', '\\|').replace('\n', ' ')


def list_text(values: list[str]) -> str:
    """Render signal text for a generated table cell."""
    return '<br>'.join(text_cell(value) for value in values) if values else 'None'


def rows_for_values(values: list[str]) -> list[str]:
    """Render a one-column generated table body."""
    if not values:
        return ['| None |']
    return [f'| `{value}` |' for value in values]


def generated_paths(workspace: Workspace) -> dict[str, Path]:
    """Return generated artifact paths from the manifest."""
    generated = merge_defaults(workspace.manifest.get('generated'), DEFAULT_GENERATED, 'generated')
    return {
        'catalog': workspace.root / generated['catalog'],
        'graph': workspace.root / generated['graph'],
        'cascade': workspace.root / generated['cascade'],
    }


def render_catalog(workspace: Workspace) -> str:
    """Render the generated skill catalog."""
    routed = [artifact for artifact in workspace.modules if artifact.activation == 'routed']
    commands = [artifact for artifact in workspace.commands if artifact.activation == 'explicit']
    lines = [
        '# Skill Catalog',
        '',
        'Generated from `routed-skills.yaml` and `skill.yaml` metadata. Do not edit by hand.',
        '',
        f'Workspace: `{workspace.manifest.get("name", workspace.entry.name)}`',
        '',
        '## Entry Skill',
        '',
        '| Name | Description | Activation | Visibility | Status | Path |',
        '| --- | --- | --- | --- | --- | --- |',
        f'| `{workspace.entry.name}` | {text_cell(workspace.entry.description)} | `{workspace.entry.activation}` | `{workspace.entry.visibility}` | `{workspace.entry.status}` | `{workspace.entry.relative_path}/` |',
        '',
        '## Routed Modules',
        '',
        '| Module | Description | Priority | Status | Path |',
        '| --- | --- | --- | --- | --- |',
    ]
    if routed:
        for artifact in routed:
            lines.append(f'| `{artifact.name}` | {text_cell(artifact.description)} | {artifact.priority} | `{artifact.status}` | `{artifact.relative_path}/` |')
    else:
        lines.append('| None | None | None | None | None |')
    lines.extend([
        '',
        '## Command Skills',
        '',
        '| Command | Description | Status | Path |',
        '| --- | --- | --- | --- |',
    ])
    if commands:
        for artifact in commands:
            lines.append(f'| `{artifact.name}` | {text_cell(artifact.description)} | `{artifact.status}` | `{artifact.relative_path}/` |')
    else:
        lines.append('| None | None | None | None |')
    lines.extend([
        '',
        '## Routing Signals',
        '',
        '| Module | Priority | Strong | Medium | Weak |',
        '| --- | --- | --- | --- | --- |',
    ])
    if routed:
        for artifact in routed:
            lines.append(
                f'| `{artifact.name}` | {artifact.priority} | {list_text(artifact.signals["strong"])} | '
                f'{list_text(artifact.signals["medium"])} | {list_text(artifact.signals["weak"])} |'
            )
    else:
        lines.append('| None | None | None | None | None |')
    return '\n'.join(lines) + '\n'


def render_graph(workspace: Workspace) -> str:
    """Render the generated relation graph."""
    lines = [
        '# Module Graph',
        '',
        'Generated from routed module and command skill relation metadata. Do not edit by hand.',
        '',
        '| Artifact | Activation | Before | With | After | Excludes | Replaces |',
        '| --- | --- | --- | --- | --- | --- | --- |',
    ]
    relation_artifacts = [*workspace.modules, *workspace.commands]
    if relation_artifacts:
        for artifact in relation_artifacts:
            relations = artifact.relations
            lines.append(
                f'| `{artifact.name}` | `{artifact.activation}` | {cell(relations["before"])} | '
                f'{cell(relations["with"])} | {cell(relations["after"])} | '
                f'{cell(relations["excludes"])} | {cell(relations["replaces"])} |'
            )
    else:
        lines.append('| None | None | None | None | None | None | None |')
    return '\n'.join(lines) + '\n'


def render_cascade(workspace: Workspace) -> str:
    """Render the generated routing cascade."""
    routed = [artifact for artifact in workspace.modules if artifact.activation == 'routed']
    commands = [artifact for artifact in workspace.commands if artifact.activation == 'explicit']
    lines = [
        '# Module Cascade',
        '',
        'Generated from routed module metadata. Do not edit by hand.',
        '',
        '## Routing Rules',
        '',
        '1. Load modules listed in `routing.always` for every routed request.',
        '2. Run the entry skill intent-understanding gate before challenge, planning, implementation, or review modules.',
        '3. Collect direct evidence from the user request and relevant files.',
        '4. Prefer strong signals over medium signals.',
        '5. Prefer medium signals over weak signals.',
        '6. Break ties using priority.',
        '7. Classify selected, candidate, deferred, and skipped modules when routing is broad or ambiguous.',
        '8. Ask operator questions only for candidate modules where the answer changes routing or execution.',
        '9. Load `before` modules recursively up to the manifest depth cap.',
        '10. Load `with` modules only when they also have direct evidence.',
        '11. Suggest `after` modules only when the later phase becomes relevant.',
        '12. Reject combinations declared in `excludes`.',
        '13. Prefer modules declared as replacements through `replaces`.',
        '',
        '## Always Loaded Modules',
        '',
        'These modules load for every routed request before evidence-selected modules.',
        '',
        '| Module |',
        '| --- |',
        *rows_for_values(workspace.always),
        '',
        '## Routed Modules',
        '',
        '| Module | Priority | Strong Signals | Medium Signals | Weak Signals | Before | With | After | Excludes | Replaces |',
        '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    if routed:
        for artifact in sorted(routed, key=lambda item: (-item.priority, item.name)):
            relations = artifact.relations
            lines.append(
                f'| `{artifact.name}` | {artifact.priority} | {list_text(artifact.signals["strong"])} | '
                f'{list_text(artifact.signals["medium"])} | {list_text(artifact.signals["weak"])} | '
                f'{cell(relations["before"])} | {cell(relations["with"])} | '
                f'{cell(relations["after"])} | {cell(relations["excludes"])} | {cell(relations["replaces"])} |'
            )
    else:
        lines.append('| None | None | None | None | None | None | None | None | None | None |')
    lines.extend([
        '',
        '## Command Skills',
        '',
        'Command skills are public direct-invocation skills and are excluded from routed cascade selection.',
        '',
        '| Command | Path |',
        '| --- | --- |',
    ])
    if commands:
        for artifact in commands:
            lines.append(f'| `{artifact.name}` | `{artifact.relative_path}/` |')
    else:
        lines.append('| None | None |')
    return '\n'.join(lines) + '\n'


def render_artifacts(workspace: Workspace) -> dict[Path, str]:
    """Render all generated artifact contents."""
    paths = generated_paths(workspace)
    return {
        paths['catalog']: render_catalog(workspace),
        paths['graph']: render_graph(workspace),
        paths['cascade']: render_cascade(workspace),
    }


def rebuild(workspace: Workspace, check: bool) -> list[str]:
    """Write or check generated artifacts."""
    stale: list[str] = []
    for path, expected in render_artifacts(workspace).items():
        if check:
            actual = path.read_text(encoding='utf-8') if path.exists() else ''
            if actual != expected:
                stale.append(workspace_relative(workspace.root, path))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expected, encoding='utf-8')
    return stale


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', nargs='?', help='Path to routed-skills.yaml or its directory.')
    parser.add_argument('--check', action='store_true', help='Fail if generated artifacts are stale.')
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the rebuild command."""
    args = parse_args(argv)
    try:
        workspace = load_workspace(args.manifest)
        stale = rebuild(workspace, args.check)
    except RoutedSkillError as error:
        print(f'error: {error}', file=sys.stderr)
        return 1
    if stale:
        for path in stale:
            print(f'error: stale generated artifact: {path}', file=sys.stderr)
        return 1
    action = 'checked' if args.check else 'rebuilt'
    print(f'{action}: {workspace_relative(workspace.root, workspace.manifest_path)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
