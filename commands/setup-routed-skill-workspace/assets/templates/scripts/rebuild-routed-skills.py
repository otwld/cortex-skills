#!/usr/bin/env python3
"""Regenerate Cortex routed skill catalog, lifecycle graph, and cascade artifacts."""

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
}
DEFAULT_ARTIFACTS = {
    'metadata': 'skill.yaml',
}
DEFAULT_GENERATED = {
    'catalog': 'generated/SKILL_CATALOG.md',
    'graph': 'generated/module-graph.md',
    'cascade': 'generated/module-cascade.md',
}
DEFAULT_FACET_KEYS = ('intents', 'surfaces', 'risks', 'artifacts', 'repo', 'request')
DEFAULT_PHASES = ('activate', 'plan', 'run', 'review', 'verify', 'finalize')
RESOURCE_KEYS = ('references', 'scripts', 'templates', 'assets')


class RoutedSkillError(Exception):
    """Raised when a Cortex routed skill workspace cannot be loaded or rebuilt."""


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
    facets: dict[str, list[str]]
    lifecycle: dict[str, str]
    uses: list[str]
    resources: dict[str, list[str]]


@dataclass(frozen=True)
class Workspace:
    """Loaded Cortex routed skill workspace model."""

    manifest_path: Path
    root: Path
    manifest: dict[str, Any]
    entry: Artifact
    modules: list[Artifact]
    commands: list[Artifact]
    metadata_name: str
    facet_keys: list[str]
    phases: list[str]

    @property
    def artifacts(self) -> list[Artifact]:
        """Return all loaded artifacts in deterministic order."""
        return [self.entry, *self.modules, *self.commands]


def parse_scalar(value: str) -> Any:
    """Parse the constrained YAML scalar shape used by Cortex metadata."""
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
    """Load the small YAML subset used by Cortex workspace metadata."""
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
    """Merge a manifest mapping with string defaults and reject unknown keys."""
    raw = as_mapping(value, label)
    merged = dict(defaults)
    for key, item in raw.items():
        if key not in defaults:
            raise RoutedSkillError(f'{label}.{key}: unknown key')
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


def facet_keys_from_manifest(manifest: dict[str, Any]) -> list[str]:
    """Return manifest-declared facet keys or Cortex defaults."""
    routing = as_mapping(manifest.get('routing'), 'routing')
    facets = as_mapping(routing.get('facets'), 'routing.facets')
    keys = as_list(facets.get('keys'), 'routing.facets.keys')
    return keys or list(DEFAULT_FACET_KEYS)


def phases_from_manifest(manifest: dict[str, Any]) -> list[str]:
    """Return manifest-declared lifecycle phases or Cortex defaults."""
    lifecycle = as_mapping(manifest.get('lifecycle'), 'lifecycle')
    phases = as_list(lifecycle.get('phases'), 'lifecycle.phases')
    return phases or list(DEFAULT_PHASES)


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
    facets_raw = as_mapping(routing.get('facets'), f'{name}.routing.facets')
    resources_raw = as_mapping(metadata.get('resources'), f'{name}.resources')
    lifecycle_raw = as_mapping(metadata.get('lifecycle'), f'{name}.lifecycle')
    priority = routing.get('priority', 0)
    if not isinstance(priority, int):
        raise RoutedSkillError(f'{name}.routing.priority: expected integer')

    lifecycle: dict[str, str] = {}
    for phase, path in lifecycle_raw.items():
        if not isinstance(path, str):
            raise RoutedSkillError(f'{name}.lifecycle.{phase}: expected string')
        lifecycle[str(phase)] = path

    return Artifact(
        name=name,
        description=description,
        activation=activation,
        visibility=visibility,
        status=status,
        directory=directory,
        relative_path=workspace_relative(root, directory),
        priority=priority,
        facets={key: as_list(value, f'{name}.routing.facets.{key}') for key, value in facets_raw.items()},
        lifecycle=lifecycle,
        uses=as_list(metadata.get('uses'), f'{name}.uses'),
        resources={key: as_list(resources_raw.get(key), f'{name}.resources.{key}') for key in RESOURCE_KEYS},
    )


def discover_artifact_directories(search_root: Path, metadata_name: str, root: Path) -> list[Path]:
    """Return artifact directories under a root while rejecting nested artifacts."""
    if not search_root.exists():
        return []

    directories = sorted({path.parent for path in search_root.rglob(metadata_name) if path.is_file()})
    directory_set = set(directories)
    for directory in directories:
        for ancestor in directory.parents:
            if ancestor == search_root.parent:
                break
            if ancestor in directory_set:
                raise RoutedSkillError(
                    f'{workspace_relative(root, directory)}: artifact cannot be nested inside '
                    f'{workspace_relative(root, ancestor)}'
                )
    return directories


def load_workspace(raw_manifest: str | None = None) -> Workspace:
    """Load a Cortex routed skill workspace from its manifest."""
    manifest_path = find_manifest(raw_manifest)
    manifest = load_yaml(manifest_path)
    root = manifest_path.parent
    paths = merge_defaults(manifest.get('paths'), DEFAULT_PATHS, 'paths')
    artifacts = merge_defaults(manifest.get('artifacts'), DEFAULT_ARTIFACTS, 'artifacts')
    facet_keys = facet_keys_from_manifest(manifest)
    phases = phases_from_manifest(manifest)
    entry_config = as_mapping(manifest.get('entry'), 'entry')
    entry_path = entry_config.get('path')
    if not isinstance(entry_path, str) or not entry_path:
        raise RoutedSkillError('entry.path: expected string')

    entry = load_artifact(root / entry_path, artifacts['metadata'], root)
    modules_root = root / paths['modules']
    modules: list[Artifact] = []
    for directory in discover_artifact_directories(modules_root, artifacts['metadata'], root):
        artifact = load_artifact(directory, artifacts['metadata'], root)
        if artifact.activation == 'explicit':
            raise RoutedSkillError(f'{artifact.relative_path}: command skill must live under {paths["commands"]}')
        modules.append(artifact)
    modules.sort(key=lambda item: item.name)

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
        metadata_name=artifacts['metadata'],
        facet_keys=facet_keys,
        phases=phases,
    )


def text_cell(value: str) -> str:
    """Escape generated table text."""
    return value.replace('|', '\\|').replace('\n', ' ')


def list_text(values: list[str]) -> str:
    """Render list text for a generated table cell."""
    return '<br>'.join(text_cell(value) for value in values) if values else 'None'


def lifecycle_text(artifact: Artifact) -> str:
    """Render lifecycle phase names for a generated table cell."""
    return ', '.join(f'`{phase}`' for phase in artifact.lifecycle) if artifact.lifecycle else 'None'


def facets_text(artifact: Artifact, facet_keys: list[str]) -> str:
    """Render compact facet text for a generated table cell."""
    entries: list[str] = []
    for key in facet_keys:
        values = artifact.facets.get(key, [])
        if values:
            entries.append(f'`{key}`: {", ".join(text_cell(value) for value in values)}')
    return '<br>'.join(entries) if entries else 'None'


def runtime_dir(workspace: Workspace) -> str:
    """Return the entry-local runtime directory name."""
    return f'.{workspace.entry.name}'


def entry_invocation(workspace: Workspace) -> str:
    """Return the public entry invocation token."""
    return f'${workspace.entry.name}'


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
        '| Module | Description | Priority | Lifecycle | Status | Path |',
        '| --- | --- | --- | --- | --- | --- |',
    ]
    if routed:
        for artifact in routed:
            lines.append(
                f'| `{artifact.name}` | {text_cell(artifact.description)} | {artifact.priority} | '
                f'{lifecycle_text(artifact)} | `{artifact.status}` | `{artifact.relative_path}/` |'
            )
    else:
        lines.append('| None | None | None | None | None | None |')
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
        '## Routing Facets',
        '',
        '| Module | Priority | Facets | Lifecycle |',
        '| --- | --- | --- | --- |',
    ])
    if routed:
        for artifact in routed:
            lines.append(
                f'| `{artifact.name}` | {artifact.priority} | {facets_text(artifact, workspace.facet_keys)} | '
                f'{lifecycle_text(artifact)} |'
            )
    else:
        lines.append('| None | None | None | None |')
    return '\n'.join(lines) + '\n'


def render_graph(workspace: Workspace) -> str:
    """Render a generated bipartite module-to-facet and module-to-phase graph."""
    routed = [artifact for artifact in workspace.modules if artifact.activation == 'routed']
    lines = [
        '# Module Graph',
        '',
        'Generated from routed module facets and lifecycle declarations. Do not edit by hand.',
        '',
        'This graph is bipartite: modules link to facet values and lifecycle phases. It contains no module-to-module dependency edges.',
        '',
        '## Module To Facets',
        '',
        '| Module | Facet Key | Values |',
        '| --- | --- | --- |',
    ]
    has_facets = False
    for artifact in routed:
        for key in workspace.facet_keys:
            values = artifact.facets.get(key, [])
            if not values:
                continue
            has_facets = True
            lines.append(f'| `{artifact.name}` | `{key}` | {list_text(values)} |')
    if not has_facets:
        lines.append('| None | None | None |')

    lines.extend([
        '',
        '## Module To Lifecycle Phases',
        '',
        '| Module | Phase | File |',
        '| --- | --- | --- |',
    ])
    has_lifecycle = False
    for artifact in routed:
        for phase in workspace.phases:
            path = artifact.lifecycle.get(phase)
            if not path:
                continue
            has_lifecycle = True
            lines.append(f'| `{artifact.name}` | `{phase}` | `{path}` |')
    if not has_lifecycle:
        lines.append('| None | None | None |')
    return '\n'.join(lines) + '\n'


def render_cascade(workspace: Workspace) -> str:
    """Render the generated routing cascade."""
    routed = [artifact for artifact in workspace.modules if artifact.activation == 'routed']
    commands = [artifact for artifact in workspace.commands if artifact.activation == 'explicit']
    runtime = runtime_dir(workspace)
    lines = [
        '# Module Cascade',
        '',
        'Generated from routed module metadata. Do not edit by hand.',
        '',
        '## Routing Rules',
        '',
        f'1. Start a run trace under `{runtime}/runs/{{date-slug}}/`.',
        f'2. Read `{runtime}/config.json`; if missing, invoke the config command atom and scaffold an empty phase config.',
        '3. Run lifecycle phases in order: ' + ', '.join(f'`{phase}`' for phase in workspace.phases) + '.',
        '4. For each phase, combine phase-specific config `always` modules with modules matched by structured facets.',
        '5. Collect request and repository evidence before selecting modules.',
        '6. Prefer higher-priority modules when facet evidence is otherwise equivalent.',
        '7. A phase subagent may own the whole phase and returns visible phase output plus hidden trace data.',
        '8. Hidden phase trace carries selected modules, matched facets, lifecycle files used, and next-phase inputs.',
        '9. Command skills are public atoms; `$cortex` may invoke them when orchestration requires it.',
        '10. Routed modules never declare peer module dependencies or exclusions.',
        '',
        '## Lifecycle Phases',
        '',
        '| Phase |',
        '| --- |',
        *[f'| `{phase}` |' for phase in workspace.phases],
        '',
        '## Facet Keys',
        '',
        '| Facet Key |',
        '| --- |',
        *[f'| `{key}` |' for key in workspace.facet_keys],
        '',
        '## Routed Modules',
        '',
        '| Module | Priority | Facets | Lifecycle |',
        '| --- | --- | --- | --- |',
    ]
    if routed:
        for artifact in sorted(routed, key=lambda item: (-item.priority, item.name)):
            lines.append(
                f'| `{artifact.name}` | {artifact.priority} | {facets_text(artifact, workspace.facet_keys)} | '
                f'{lifecycle_text(artifact)} |'
            )
    else:
        lines.append('| None | None | None | None |')
    lines.extend([
        '',
        '## Command Skills',
        '',
        f'Command skills are public atoms. They are not selected by facet routing, but `{entry_invocation(workspace)}` may invoke them for orchestration such as config bootstrap.',
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
