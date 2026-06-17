#!/usr/bin/env python3
"""Validate Cortex public skill, internal modules, routing, and quality contracts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / 'references' / 'module-graph.md'
CASCADE_PATH = ROOT / 'references' / 'module-cascade.md'
CATALOG_PATH = ROOT / 'SKILL_CATALOG.md'
SELF = Path(__file__).resolve()
PUBLIC_SKILL_NAME = 'cortex'
PUBLIC_SKILL_PATH = ROOT / 'governance' / 'core' / 'cortex' / 'SKILL.md'
PUBLIC_METADATA_PATH = PUBLIC_SKILL_PATH.parent / 'agents' / 'openai.yaml'
EDGE_LABELS = ('BEFORE', 'WITH', 'AFTER')
TAXONOMY_HEADINGS = {
    'architecture': 'Architecture',
    'documentation': 'Documentation',
    'frameworks': 'Frameworks',
    'governance': 'Governance',
    'maintenance': 'Maintenance',
    'testing': 'Testing',
    'tools': 'Tools',
    'typescript': 'TypeScript',
}
REQUIRED_WORKSPACE_REFERENCES = [
    'references/skill-quality-standard.md',
    'references/project-memory.md',
    'references/domain-glossary.md',
    'references/adr-format.md',
    'references/out-of-scope-decisions.md',
    'references/issue-tracker-setup.md',
    'references/vertical-slices.md',
    'references/agent-briefs.md',
    'references/architecture-deepening.md',
    'references/prototype-guidance.md',
]
REQUIRED_ARTIFACT_SECTIONS = [
    '# Output Marker',
    '## Overview',
    '## Workflow',
    '## Quality Gates',
    '## Example',
    '## Hard Stops',
    '## Usage Checklist',
    '## Cross-References',
]
SKIP_PARTS = {'.git', '.agents', '.codex', '.hg', '.svn', '.idea', '.vscode', '__pycache__', 'node_modules'}
FORBIDDEN_ACTIVE_TERMS = [
    '@cortex', '.agents', 'GOVERNANCE', 'codebase-vacuum', 'nx_workspace', 'nx_project_details',
    'nx-generate', '/home/ntrehout', '\ue200cite', 'Deep Architecture', 'apps/documentation',
    'createStorybookNodeSourceLoaderPlugin', 'createFakerGenetics', 'createMswSearchGetHandler',
    'AbstractRepository', 'MatchRule', 'buildMatchStage', 'buildPipeline', 'buildFacet',
    'buildPaginatedFacet', 'buildRelationLookup', 'buildRelationsLookup', 'toObjectId',
    'toObjectIds', 'Skippable', 'runSkippableQuery', 'createQueryKey', 'strictMutationOptions',
    'coerceQueryOptions', 'coerceQueryInfiniteOptions', 'selectPaginatedResponse', 'PaginationInfo',
    'formServiceProvide', 'source-loader:',
]
FORBIDDEN_EXAMPLE_IDENTIFIERS = [
    'Americano', 'Coffee', 'CoffeeMaker', 'Grinder', 'Latte', 'ReportRow', 'RequestContext',
    'Scheduler', 'Widget', 'currentUser', 'getCurrentUser', 'loadUser', 'Product', 'Item',
]
MAX_BEFORE_CASCADE = 5


def rel(path: Path) -> str:
    """Return a repository-relative path."""
    return str(path.relative_to(ROOT))


def read_text(path: Path) -> str:
    """Read a UTF-8 file."""
    return path.read_text(encoding='utf-8')


def skip(path: Path) -> bool:
    """Return whether path should be ignored by recursive scans."""
    try:
        parts = path.relative_to(ROOT).parts
    except ValueError:
        return False
    return any(part in SKIP_PARTS for part in parts)


def valid_slug(value: str) -> bool:
    """Return whether a value is a lowercase kebab-case slug."""
    return re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', value) is not None


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    """Parse the minimal YAML frontmatter used by Cortex artifacts."""
    text = read_text(path)
    if not text.startswith('---\n'):
        errors.append(f'{rel(path)}: missing YAML frontmatter')
        return {}
    end = text.find('\n---', 4)
    if end == -1:
        errors.append(f'{rel(path)}: unterminated YAML frontmatter')
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].strip().splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def parse_openai_metadata(path: Path, errors: list[str]) -> dict[str, str]:
    """Parse required public skill metadata fields from agents/openai.yaml."""
    if not path.exists():
        errors.append(f'{rel(path)}: missing agents/openai.yaml')
        return {}
    values: dict[str, str] = {}
    in_interface = False
    in_policy = False
    saw_interface = False
    for line in read_text(path).splitlines():
        if line == 'interface:':
            in_interface = True
            in_policy = False
            saw_interface = True
            continue
        if line == 'policy:':
            in_interface = False
            in_policy = True
            continue
        if line and not line.startswith((' ', '\t')):
            in_interface = False
            in_policy = False
        if in_interface:
            match = re.match(r'\s+(display_name|short_description|default_prompt):\s*(.+?)\s*$', line)
            if match:
                values[match.group(1)] = match.group(2).strip().strip('"').strip("'")
        if in_policy:
            match = re.match(r'\s+(allow_implicit_invocation):\s*(.+?)\s*$', line)
            if match:
                values[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    if not saw_interface:
        errors.append(f'{rel(path)}: missing interface block')
    return values


def parse_list(value: str) -> list[str]:
    """Parse a graph or cross-reference list cell."""
    value = value.strip()
    if not value or value == 'None':
        return []
    return [part.strip().strip('`') for part in value.split(',') if part.strip()]


def parse_graph(errors: list[str]) -> dict[str, dict[str, list[str]]]:
    """Parse references/module-graph.md."""
    if not GRAPH_PATH.exists():
        errors.append(f'{rel(GRAPH_PATH)}: missing central module graph')
        return {}
    graph: dict[str, dict[str, list[str]]] = {}
    for line_number, line in enumerate(read_text(GRAPH_PATH).splitlines(), start=1):
        if not line.startswith('| `'):
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells) != 4:
            errors.append(f'{rel(GRAPH_PATH)}:{line_number}: expected 4 table columns')
            continue
        graph[cells[0].strip('`')] = {
            'BEFORE': parse_list(cells[1]),
            'WITH': parse_list(cells[2]),
            'AFTER': parse_list(cells[3]),
        }
    if not graph:
        errors.append(f'{rel(GRAPH_PATH)}: graph table is empty')
    return graph


def parse_cross_references(path: Path, errors: list[str]) -> dict[str, list[str]]:
    """Parse a Cross-References section from a public skill or internal module."""
    lines = read_text(path).splitlines()
    try:
        start = lines.index('## Cross-References') + 1
    except ValueError:
        errors.append(f'{rel(path)}: missing Cross-References section')
        return {label: [] for label in EDGE_LABELS}
    section: list[str] = []
    for line in lines[start:]:
        if line.startswith('## '):
            break
        section.append(line)
    bullets = [line.strip() for line in section if line.strip().startswith('- ')]
    if not bullets:
        errors.append(f'{rel(path)}: Cross-References must include - None or labeled edges')
        return {label: [] for label in EDGE_LABELS}
    edges = {label: [] for label in EDGE_LABELS}
    saw_none = False
    for bullet in bullets:
        value = bullet[2:].strip()
        if value == 'None':
            saw_none = True
            continue
        match = re.match(r'^(BEFORE|WITH|AFTER):\s*(.+)$', value)
        if not match:
            errors.append(f'{rel(path)}: invalid Cross-References bullet {bullet!r}')
            continue
        label, targets = match.groups()
        edges[label].extend(parse_list(targets))
    if saw_none and any(edges[label] for label in EDGE_LABELS):
        errors.append(f'{rel(path)}: Cross-References cannot mix None with edges')
    return edges


def check_artifact_location(path: Path, errors: list[str], label: str) -> bool:
    """Validate taxonomy/group/slug directory shape for a skill or module."""
    parts = path.parent.relative_to(ROOT).parts
    if len(parts) not in (2, 3):
        errors.append(f'{rel(path)}: {label} directory must match taxonomy/folder-slug or taxonomy/group/folder-slug')
        return False
    taxonomy = parts[0]
    if taxonomy not in TAXONOMY_HEADINGS:
        errors.append(f'{rel(path)}: unknown {label} taxonomy {taxonomy!r}')
        return False
    bad = [part for part in parts if not valid_slug(part)]
    if bad:
        errors.append(f'{rel(path)}: directory parts must be lowercase slugs: {", ".join(bad)}')
        return False
    return True


def check_artifact_quality(path: Path, errors: list[str]) -> None:
    """Validate required active Cortex quality sections."""
    text = read_text(path)
    for section in REQUIRED_ARTIFACT_SECTIONS:
        if section not in text:
            errors.append(f'{rel(path)}: missing required quality section {section}')
    if re.search(r'\b(TBD|TODO)\b', text):
        errors.append(f'{rel(path)}: contains placeholder TODO/TBD text')


def check_resource_references(path: Path, errors: list[str]) -> None:
    """Validate referenced local and workspace support files exist."""
    text = read_text(path)
    pattern = r'(?:\.\./)*(?:references|scripts)/[^`)]+\.\w+'
    for match in re.finditer(rf'`({pattern})`', text):
        target = match.group(1).split()[0]
        if not (path.parent / target).exists():
            errors.append(f'{rel(path)}: referenced resource does not exist: {target}')
    for match in re.finditer(rf'\]\(({pattern})\)', text):
        target = match.group(1).split()[0]
        if not (path.parent / target).exists():
            errors.append(f'{rel(path)}: linked resource does not exist: {target}')


def check_required_workspace_references(errors: list[str]) -> None:
    """Ensure the workspace-level reference layer exists."""
    for reference in REQUIRED_WORKSPACE_REFERENCES:
        path = ROOT / reference
        if not path.exists():
            errors.append(f'{reference}: missing required workspace reference')
        elif len(read_text(path).strip().splitlines()) < 3:
            errors.append(f'{reference}: reference is too thin to be useful')


def check_legacy_heading(path: Path, errors: list[str]) -> None:
    """Ensure legacy reference files identify themselves as legacy."""
    if 'legacy' not in rel(path).lower():
        return
    for line in read_text(path).splitlines():
        if line.startswith('#'):
            if 'Legacy' not in line:
                errors.append(f'{rel(path)}: first markdown heading must include Legacy')
            return
    errors.append(f'{rel(path)}: legacy file must include a markdown heading')


def check_forbidden_active_terms(errors: list[str]) -> None:
    """Reject source-project residue in active instruction files."""
    for path in ROOT.rglob('*'):
        if not path.is_file() or skip(path) or path.name == '.gitignore' or path.resolve() == SELF:
            continue
        if 'legacy' in rel(path).lower():
            continue
        try:
            text = read_text(path).replace('Cortex Skills', '')
        except UnicodeDecodeError:
            continue
        for term in FORBIDDEN_ACTIVE_TERMS:
            if term in text:
                errors.append(f'{rel(path)}: forbidden active source-project residue: {term}')


def check_empty_directories(errors: list[str]) -> None:
    """Reject empty directories in the workspace."""
    for path in ROOT.rglob('*'):
        if not skip(path) and path.is_dir() and not any(path.iterdir()):
            errors.append(f'{rel(path)}: empty directory')


def check_cascade_reference(names: dict[str, Path], errors: list[str]) -> None:
    """Validate the signal-routing reference."""
    if not CASCADE_PATH.exists():
        errors.append(f'{rel(CASCADE_PATH)}: missing cascade routing reference')
        return
    text = read_text(CASCADE_PATH)
    for heading in ('## Cascade Algorithm', '## Signal Rules', '## Guardrails'):
        if heading not in text:
            errors.append(f'{rel(CASCADE_PATH)}: missing {heading}')
    rows = [line for line in text.splitlines() if line.startswith('| ') and not line.startswith('| Signal ') and not line.startswith('| ---')]
    if len(rows) < 12:
        errors.append(f'{rel(CASCADE_PATH)}: expected at least 12 signal rule rows')
    allowed = {'BEFORE', 'WITH', 'AFTER'}
    for match in re.finditer(r'`([a-zA-Z0-9_.-]+)`', text):
        token = match.group(1)
        if token in allowed or '.' in token:
            continue
        if re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', token) and token not in names:
            errors.append(f'{rel(CASCADE_PATH)}: unknown module reference {token!r}')


def check_catalog(names: dict[str, Path], public_count: int, module_count: int, errors: list[str]) -> None:
    """Validate SKILL_CATALOG.md counts, paths, and taxonomy sections."""
    if not CATALOG_PATH.exists():
        errors.append(f'{rel(CATALOG_PATH)}: missing skill catalog')
        return
    text = read_text(CATALOG_PATH)
    count_match = re.search(r'Cortex Skills contains (\d+) public skill and (\d+) internal modules', text)
    if not count_match:
        errors.append(f'{rel(CATALOG_PATH)}: missing skill/module count summary')
    else:
        if int(count_match.group(1)) != public_count:
            errors.append(f'{rel(CATALOG_PATH)}: public skill count says {count_match.group(1)}, expected {public_count}')
        if int(count_match.group(2)) != module_count:
            errors.append(f'{rel(CATALOG_PATH)}: module count says {count_match.group(2)}, expected {module_count}')
    rows: dict[str, tuple[int, str, str]] = {}
    heading = ''
    for line_number, line in enumerate(text.splitlines(), start=1):
        heading_match = re.match(r'^## (.+)$', line)
        if heading_match:
            heading = heading_match.group(1)
            continue
        match = re.match(r'\| `([^`]+)` \| .* \| `([^`]+)` \|$', line)
        if not match:
            continue
        name, catalog_path = match.groups()
        if name in rows:
            errors.append(f'{rel(CATALOG_PATH)}:{line_number}: duplicate catalog row for {name!r}')
        rows[name] = (line_number, catalog_path, heading)
    for name, (line_number, _, _) in rows.items():
        if name not in names:
            errors.append(f'{rel(CATALOG_PATH)}:{line_number}: unknown catalog entry {name!r}')
    for name, artifact_path in names.items():
        expected_path = f'{rel(artifact_path.parent)}/'
        if name not in rows:
            errors.append(f'{rel(CATALOG_PATH)}: missing catalog row for {name!r}')
            continue
        line_number, catalog_path, row_heading = rows[name]
        if catalog_path != expected_path:
            errors.append(f'{rel(CATALOG_PATH)}:{line_number}: catalog path for {name!r} is {catalog_path!r}, expected {expected_path!r}')
        expected_heading = TAXONOMY_HEADINGS[artifact_path.parent.relative_to(ROOT).parts[0]]
        if row_heading != expected_heading:
            errors.append(f'{rel(CATALOG_PATH)}:{line_number}: catalog section for {name!r} is {row_heading!r}, expected {expected_heading!r}')


def cascade_order(graph: dict[str, dict[str, list[str]]], initial: list[str]) -> tuple[list[str], list[str]]:
    """Return recursive BEFORE order and cycle diagnostics."""
    order: list[str] = []
    seen: set[str] = set()
    visiting: list[str] = []
    cycles: list[str] = []

    def add(name: str) -> None:
        if name not in graph:
            return
        if name in visiting:
            cycles.append(' -> '.join(visiting[visiting.index(name):] + [name]))
            return
        if name in seen:
            return
        visiting.append(name)
        for target in graph[name]['BEFORE']:
            add(target)
        visiting.pop()
        seen.add(name)
        order.append(name)

    for name in initial:
        add(name)
    return order, cycles


def check_cascade(graph: dict[str, dict[str, list[str]]], errors: list[str], show: bool) -> None:
    """Validate graph expansion is bounded and acyclic."""
    if graph.get(PUBLIC_SKILL_NAME, {}).get('BEFORE'):
        errors.append(f'{rel(GRAPH_PATH)}: {PUBLIC_SKILL_NAME} must not define hard BEFORE cascades')
    for name in graph:
        order, cycles = cascade_order(graph, [name])
        for cycle in cycles:
            errors.append(f'{rel(GRAPH_PATH)}: BEFORE cycle: {cycle}')
        if len(order) > MAX_BEFORE_CASCADE:
            errors.append(f'cascade {name}: BEFORE cascade loads {len(order)} entries, expected at most {MAX_BEFORE_CASCADE}: {", ".join(order)}')
        if show:
            print(f'cascade {name}: {len(order)} entry(s): {", ".join(order)}')


def iter_code_blocks(text: str) -> Iterable[tuple[int, str]]:
    """Yield fenced code blocks with starting line numbers."""
    in_block = False
    start_line = 0
    block: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith('```'):
            if in_block:
                yield start_line, '\n'.join(block)
                block = []
                in_block = False
            else:
                in_block = True
                start_line = line_number
            continue
        if in_block:
            block.append(line)


def check_example_universe(errors: list[str]) -> None:
    """Reject known non-recruitment examples in code blocks."""
    for path in ROOT.rglob('*.md'):
        if skip(path) or 'legacy' in rel(path).lower():
            continue
        for start_line, block in iter_code_blocks(read_text(path)):
            for identifier in FORBIDDEN_EXAMPLE_IDENTIFIERS:
                if re.search(rf'\b{re.escape(identifier)}\b', block):
                    errors.append(f'{rel(path)}:{start_line}: example code uses non-recruitment identifier {identifier}')


def check_public_skill_paths(public_skill_paths: list[Path], errors: list[str]) -> None:
    """Validate that Cortex exposes exactly one public SKILL.md surface."""
    if PUBLIC_SKILL_PATH not in public_skill_paths:
        errors.append(f'{rel(PUBLIC_SKILL_PATH)}: missing public Cortex SKILL.md')
    for path in public_skill_paths:
        if path != PUBLIC_SKILL_PATH:
            errors.append(f'{rel(path)}: only {rel(PUBLIC_SKILL_PATH)} may be a public SKILL.md')


def check_metadata_paths(module_paths: list[Path], errors: list[str]) -> None:
    """Ensure OpenAI metadata exists only for the public Cortex skill."""
    module_parents = {path.parent for path in module_paths}
    for metadata_path in sorted(path for path in ROOT.rglob('agents/openai.yaml') if not skip(path)):
        if metadata_path == PUBLIC_METADATA_PATH:
            continue
        if metadata_path.parent.parent in module_parents:
            errors.append(f'{rel(metadata_path.parent.parent / "MODULE.md")}: internal module must not define agents/openai.yaml')
        else:
            errors.append(f'{rel(metadata_path)}: only {rel(PUBLIC_METADATA_PATH)} may define OpenAI skill metadata')


def validate_artifact(path: Path, errors: list[str], names: dict[str, Path], label: str, marker_kind: str) -> str:
    """Validate shared frontmatter, marker, quality, and resource rules."""
    values = parse_frontmatter(path, errors)
    name = values.get('name', '')
    description = values.get('description', '')
    if not name:
        errors.append(f'{rel(path)}: missing frontmatter name')
    elif not valid_slug(name):
        errors.append(f'{rel(path)}: invalid {label} name {name!r}')
    elif name in names:
        errors.append(f'{rel(path)}: duplicate {label} name also in {rel(names[name])}')
    elif check_artifact_location(path, errors, label):
        names[name] = path
    if not description:
        errors.append(f'{rel(path)}: missing frontmatter description')
    if name and f'using {marker_kind}: {name}' not in read_text(path):
        errors.append(f'{rel(path)}: Output Marker must use frontmatter name')
    check_artifact_quality(path, errors)
    check_resource_references(path, errors)
    return name


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cascade', action='store_true', help='Print graph-derived BEFORE cascade closures.')
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run all workspace validations."""
    args = parse_args(argv)
    errors: list[str] = []
    graph = parse_graph(errors)
    names: dict[str, Path] = {}
    public_skill_paths = sorted(path for path in ROOT.rglob('SKILL.md') if not skip(path))
    module_paths = sorted(path for path in ROOT.rglob('MODULE.md') if not skip(path))
    check_public_skill_paths(public_skill_paths, errors)
    check_metadata_paths(module_paths, errors)

    if PUBLIC_SKILL_PATH.exists():
        name = validate_artifact(PUBLIC_SKILL_PATH, errors, names, 'public skill', 'skill')
        if name and name != PUBLIC_SKILL_NAME:
            errors.append(f'{rel(PUBLIC_SKILL_PATH)}: public skill name must be {PUBLIC_SKILL_NAME!r}')
        metadata = parse_openai_metadata(PUBLIC_METADATA_PATH, errors)
        display_name = metadata.get('display_name', '')
        short_description = metadata.get('short_description', '')
        default_prompt = metadata.get('default_prompt', '')
        if PUBLIC_METADATA_PATH.exists():
            if '(otwld)' not in display_name:
                errors.append(f'{rel(PUBLIC_METADATA_PATH)}: display_name must include (otwld)')
            if not short_description:
                errors.append(f'{rel(PUBLIC_METADATA_PATH)}: missing short_description')
            if not default_prompt:
                errors.append(f'{rel(PUBLIC_METADATA_PATH)}: missing default_prompt')
            elif not default_prompt.startswith(f'Use ${PUBLIC_SKILL_NAME} '):
                errors.append(f'{rel(PUBLIC_METADATA_PATH)}: default_prompt must start with Use ${PUBLIC_SKILL_NAME} ')
            if metadata.get('allow_implicit_invocation') != 'false':
                errors.append(f'{rel(PUBLIC_METADATA_PATH)}: policy.allow_implicit_invocation must be false')

    if not module_paths:
        errors.append('no modules found')
    for module_path in module_paths:
        validate_artifact(module_path, errors, names, 'module', 'module')

    for artifact_name, artifact_path in names.items():
        edges = parse_cross_references(artifact_path, errors)
        if graph:
            if artifact_name not in graph:
                errors.append(f'{rel(GRAPH_PATH)}: missing graph row for {artifact_name}')
            elif edges != graph[artifact_name]:
                errors.append(f'{rel(artifact_path)}: Cross-References do not match {rel(GRAPH_PATH)}')
    for name, edges in graph.items():
        if name not in names:
            errors.append(f'{rel(GRAPH_PATH)}: graph row references missing module {name}')
        for label, targets in edges.items():
            for target in targets:
                if target not in names:
                    errors.append(f'{rel(GRAPH_PATH)}: {name} {label} references missing module {target}')

    check_required_workspace_references(errors)
    check_cascade_reference(names, errors)
    check_catalog(names, len(public_skill_paths), len(module_paths), errors)
    for path in ROOT.rglob('*.md'):
        if not skip(path):
            check_legacy_heading(path, errors)
    check_cascade(graph, errors, args.cascade)
    check_example_universe(errors)
    check_forbidden_active_terms(errors)
    check_empty_directories(errors)
    if errors:
        for error in sorted(set(errors)):
            print(f'error: {error}', file=sys.stderr)
        return 1
    print(f'validation ok: skills={len(public_skill_paths)} modules={len(module_paths)} metadata=1')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
