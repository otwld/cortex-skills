#!/usr/bin/env python3
"""Validate local skill structure, metadata, graph edges, and extracted residue."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "references" / "skill-graph.md"
SELF = Path(__file__).resolve()

EDGE_LABELS = ("BEFORE", "WITH", "AFTER")
SKIP_SCAN_PARTS = {
    ".git",
    ".agents",
    ".codex",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    "__pycache__",
    "node_modules",
}

FORBIDDEN_ACTIVE_TERMS = [
    "Cortex",
    "@cortex",
    ".agents",
    "PLAN",
    "GOVERNANCE",
    "codebase-vacuum",
    "nx_workspace",
    "nx_project_details",
    "nx-generate",
    "/home/ntrehout",
    "\ue200cite",
    "Deep Architecture",
    "apps/documentation",
    "createStorybookNodeSourceLoaderPlugin",
    "createFakerGenetics",
    "createMswSearchGetHandler",
    "AbstractRepository",
    "MatchRule",
    "buildMatchStage",
    "buildPipeline",
    "buildFacet",
    "buildPaginatedFacet",
    "buildRelationLookup",
    "buildRelationsLookup",
    "toObjectId",
    "toObjectIds",
    "Skippable",
    "runSkippableQuery",
    "createQueryKey",
    "strictMutationOptions",
    "coerceQueryOptions",
    "coerceQueryInfiniteOptions",
    "selectPaginatedResponse",
    "PaginationInfo",
    "formServiceProvide",
    "source-loader:",
]

CASCADE_SCENARIOS = [
    (
        "angular-material-nx-storybook",
        [
            "architecture-drift-detector",
            "nx-conventions",
            "nx-module-boundaries",
            "library-placement-decision",
            "angular-material-conventions",
            "storybook-angular-conventions",
            "public-api-design",
            "code-documentation",
            "example-universe-enforcer",
        ],
        12,
    ),
    (
        "nestjs-mongoose-extraction",
        [
            "architecture-drift-detector",
            "extraction-decision",
            "nestjs-mongoose-conventions",
            "public-api-design",
            "code-documentation",
            "example-universe-enforcer",
        ],
        10,
    ),
    (
        "angular-tanstack-query-wrapper",
        [
            "angular-tanstack-query-conventions",
            "typescript-api-conventions",
            "code-documentation",
            "example-universe-enforcer",
        ],
        7,
    ),
    (
        "vite-bundle-review",
        ["vite-conventions", "bundle-performance", "public-api-design"],
        6,
    ),
    (
        "playwright-e2e-test",
        ["playwright-conventions", "typescript-code-style", "example-universe-enforcer"],
        5,
    ),
    ("diary-handoff", ["diary"], 2),
    ("skill-doctrine-gap", ["skill-evolution"], 2),
    (
        "vue-rxjs-public-props",
        [
            "vue-conventions",
            "rxjs-conventions",
            "typescript-api-conventions",
            "code-documentation",
            "example-universe-enforcer",
        ],
        7,
    ),
    (
        "jest-public-utility",
        [
            "jest-conventions",
            "typescript-code-style",
            "typescript-api-conventions",
            "example-universe-enforcer",
        ],
        6,
    ),
]

FORBIDDEN_EXAMPLE_IDENTIFIERS = [
    "Americano",
    "Coffee",
    "CoffeeMaker",
    "Grinder",
    "Latte",
    "ReportRow",
    "RequestContext",
    "Scheduler",
    "Widget",
    "currentUser",
    "getCurrentUser",
    "loadUser",
]

EXPECTED_SKILL_DIRS = {
    "architecture-drift-detector": Path("architecture/drift-detector"),
    "bundle-performance": Path("architecture/bundle-performance"),
    "extraction-decision": Path("architecture/extraction-decision"),
    "library-placement-decision": Path("architecture/library-placement-decision"),
    "naming-consistency": Path("architecture/naming-consistency"),
    "nx-module-boundaries": Path("architecture/nx-module-boundaries"),
    "public-api-design": Path("architecture/public-api-design"),
    "code-documentation": Path("documentation/code"),
    "angular-conventions": Path("frameworks/angular/core"),
    "angular-material-conventions": Path("frameworks/angular/material"),
    "angular-tanstack-query-conventions": Path("frameworks/angular/tanstack-query"),
    "nestjs-conventions": Path("frameworks/nestjs/core"),
    "nestjs-mongoose-conventions": Path("frameworks/nestjs/mongoose"),
    "nx-conventions": Path("frameworks/nx"),
    "rxjs-conventions": Path("frameworks/rxjs"),
    "storybook-angular-conventions": Path("frameworks/angular/storybook"),
    "storybook-conventions": Path("frameworks/storybook"),
    "vite-conventions": Path("frameworks/vite"),
    "vue-conventions": Path("frameworks/vue"),
    "diary": Path("maintenance/diary"),
    "example-universe-enforcer": Path("maintenance/example-universe-enforcer"),
    "skill-evolution": Path("maintenance/skill-evolution"),
    "jest-conventions": Path("testing/jest"),
    "playwright-conventions": Path("testing/playwright"),
    "vitest-conventions": Path("testing/vitest"),
    "typescript-api-conventions": Path("typescript/api"),
    "typescript-code-style": Path("typescript/code-style"),
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def should_skip_path(path: Path) -> bool:
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return False
    return any(part in SKIP_SCAN_PARTS for part in relative.parts)


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        errors.append(f"{rel(path)}: missing YAML frontmatter")
        return {}

    end = text.find("\n---", 4)
    if end == -1:
        errors.append(f"{rel(path)}: unterminated YAML frontmatter")
        return {}

    frontmatter = text[4:end].strip().splitlines()
    values: dict[str, str] = {}
    for line in frontmatter:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def parse_openai_metadata(path: Path, errors: list[str]) -> dict[str, str]:
    if not path.exists():
        errors.append(f"{rel(path)}: missing agents/openai.yaml")
        return {}

    values: dict[str, str] = {}
    for line in read_text(path).splitlines():
        match = re.match(r"\s+(display_name|short_description|default_prompt):\s*(.+?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return values


def parse_list(value: str) -> list[str]:
    value = value.strip()
    if not value or value == "None":
        return []
    return [part.strip().strip("`") for part in value.split(",") if part.strip()]


def parse_cross_references(path: Path, errors: list[str]) -> dict[str, list[str]]:
    text = read_text(path)
    lines = text.splitlines()
    section_start = None
    for index, line in enumerate(lines):
        if line.strip() == "## Cross-References":
            section_start = index + 1
            break

    if section_start is None:
        errors.append(f"{rel(path)}: missing Cross-References section")
        return {label: [] for label in EDGE_LABELS}

    section: list[str] = []
    for line in lines[section_start:]:
        if line.startswith("## "):
            break
        section.append(line)

    bullets = [line.strip() for line in section if line.strip().startswith("- ")]
    if not bullets:
        errors.append(f"{rel(path)}: Cross-References must include - None or labeled edges")
        return {label: [] for label in EDGE_LABELS}

    edges = {label: [] for label in EDGE_LABELS}
    saw_none = False
    for bullet in bullets:
        value = bullet[2:].strip()
        if value == "None":
            saw_none = True
            continue

        match = re.match(r"^(BEFORE|WITH|AFTER):\s*(.+)$", value)
        if not match:
            errors.append(
                f"{rel(path)}: invalid Cross-References bullet {bullet!r}; "
                "use BEFORE, WITH, AFTER, or None"
            )
            continue
        label, targets = match.groups()
        edges[label].extend(parse_list(targets))

    if saw_none and any(edges[label] for label in EDGE_LABELS):
        errors.append(f"{rel(path)}: Cross-References cannot mix None with edges")

    return edges


def parse_graph(errors: list[str]) -> dict[str, dict[str, list[str]]]:
    if not GRAPH_PATH.exists():
        errors.append(f"{rel(GRAPH_PATH)}: missing central skill graph")
        return {}

    graph: dict[str, dict[str, list[str]]] = {}
    for line_number, line in enumerate(read_text(GRAPH_PATH).splitlines(), start=1):
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            errors.append(f"{rel(GRAPH_PATH)}:{line_number}: expected 4 table columns")
            continue
        skill = cells[0].strip("`")
        graph[skill] = {
            "BEFORE": parse_list(cells[1]),
            "WITH": parse_list(cells[2]),
            "AFTER": parse_list(cells[3]),
        }

    if not graph:
        errors.append(f"{rel(GRAPH_PATH)}: graph table is empty")
    return graph


def check_resource_references(path: Path, errors: list[str]) -> None:
    text = read_text(path)
    for match in re.finditer(r"`((?:references|scripts|assets)/[^`]+)`", text):
        raw = match.group(1)
        target = raw.split()[0]
        if not (path.parent / target).exists():
            errors.append(f"{rel(path)}: referenced resource does not exist: {target}")

    for match in re.finditer(r"\]\(((?:references|scripts|assets)/[^)]+)\)", text):
        target = match.group(1).split()[0]
        if not (path.parent / target).exists():
            errors.append(f"{rel(path)}: linked resource does not exist: {target}")


def check_legacy_heading(path: Path, errors: list[str]) -> None:
    if "legacy" not in rel(path).lower():
        return

    for line in read_text(path).splitlines():
        if line.startswith("#"):
            if "Legacy" not in line:
                errors.append(f"{rel(path)}: first markdown heading must include Legacy")
            return
    errors.append(f"{rel(path)}: legacy file must include a markdown heading")


def check_forbidden_active_terms(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if should_skip_path(path):
            continue
        if path.name == ".gitignore":
            continue
        if path.resolve() == SELF:
            continue
        if "legacy" in rel(path).lower():
            continue

        try:
            text = read_text(path)
        except UnicodeDecodeError:
            continue

        text = text.replace("Cortex Skills", "")
        for term in FORBIDDEN_ACTIVE_TERMS:
            if term in text:
                errors.append(f"{rel(path)}: forbidden active source-project residue: {term}")


def check_empty_directories(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if should_skip_path(path):
            continue
        if path.is_dir() and not any(path.iterdir()):
            errors.append(f"{rel(path)}: empty directory")


def cascade_order(
    graph: dict[str, dict[str, list[str]]],
    initial: list[str],
) -> tuple[list[str], list[str]]:
    order: list[str] = []
    seen: set[str] = set()
    visiting: list[str] = []
    cycles: list[str] = []

    def add(name: str) -> None:
        if name not in graph:
            return
        if name in visiting:
            cycles.append(" -> ".join(visiting[visiting.index(name):] + [name]))
            return
        if name in seen:
            return

        visiting.append(name)
        for target in graph[name]["BEFORE"]:
            add(target)
        visiting.pop()

        seen.add(name)
        order.append(name)

    for name in initial:
        add(name)

    return order, cycles


def check_cascade(
    graph: dict[str, dict[str, list[str]]],
    errors: list[str],
    show: bool,
) -> None:
    if not graph:
        return

    for name in graph:
        _, cycles = cascade_order(graph, [name])
        for cycle in cycles:
            errors.append(f"{rel(GRAPH_PATH)}: BEFORE cycle: {cycle}")

    for scenario, initial, max_loaded in CASCADE_SCENARIOS:
        order, cycles = cascade_order(graph, initial)
        for cycle in cycles:
            errors.append(f"cascade {scenario}: BEFORE cycle: {cycle}")
        if len(order) > max_loaded:
            errors.append(
                f"cascade {scenario}: loaded {len(order)} skills, "
                f"expected at most {max_loaded}: {', '.join(order)}"
            )
        if show:
            print(f"cascade {scenario}: {len(order)} skill(s): {', '.join(order)}")


def iter_code_blocks(text: str) -> Iterable[tuple[int, str]]:
    in_block = False
    start_line = 0
    block: list[str] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("```"):
            if in_block:
                yield start_line, "\n".join(block)
                block = []
                in_block = False
            else:
                in_block = True
                start_line = line_number
            continue

        if in_block:
            block.append(line)


def check_example_universe(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if should_skip_path(path):
            continue
        if "legacy" in rel(path).lower():
            continue

        text = read_text(path)
        for start_line, block in iter_code_blocks(text):
            for identifier in FORBIDDEN_EXAMPLE_IDENTIFIERS:
                if re.search(rf"\b{re.escape(identifier)}\b", block):
                    errors.append(
                        f"{rel(path)}:{start_line}: example code uses non-recruitment identifier {identifier}"
                    )


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cascade",
        action="store_true",
        help="Print representative non-transitive cascade simulations.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors: list[str] = []

    skill_paths = sorted(path for path in ROOT.rglob("SKILL.md") if not should_skip_path(path))
    if not skill_paths:
        errors.append("no skills found")

    graph = parse_graph(errors)
    names: dict[str, Path] = {}
    metadata_count = 0

    for skill_path in skill_paths:
        skill_dir = skill_path.parent
        values = parse_frontmatter(skill_path, errors)
        name = values.get("name", "")
        description = values.get("description", "")

        if not name:
            errors.append(f"{rel(skill_path)}: missing frontmatter name")
        elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{rel(skill_path)}: invalid skill name {name!r}")
        elif name not in EXPECTED_SKILL_DIRS:
            errors.append(f"{rel(skill_path)}: no expected directory registered for skill {name!r}")
        elif skill_dir.relative_to(ROOT) != EXPECTED_SKILL_DIRS[name]:
            errors.append(f"{rel(skill_path)}: expected directory {EXPECTED_SKILL_DIRS[name]}")
        elif name in names:
            errors.append(f"{rel(skill_path)}: duplicate skill name also in {rel(names[name])}")
        else:
            names[name] = skill_path

        if not description:
            errors.append(f"{rel(skill_path)}: missing frontmatter description")

        text = read_text(skill_path)
        if "# Output Marker" not in text:
            errors.append(f"{rel(skill_path)}: missing Output Marker")
        if name and f"using skill: {name}" not in text:
            errors.append(f"{rel(skill_path)}: Output Marker must use frontmatter name")

        metadata_path = skill_dir / "agents" / "openai.yaml"
        metadata = parse_openai_metadata(metadata_path, errors)
        if metadata:
            metadata_count += 1
        display_name = metadata.get("display_name", "")
        short_description = metadata.get("short_description", "")
        default_prompt = metadata.get("default_prompt", "")
        if metadata_path.exists():
            if "(otwld)" not in display_name:
                errors.append(f"{rel(metadata_path)}: display_name must include (otwld)")
            if not short_description:
                errors.append(f"{rel(metadata_path)}: missing short_description")
            if not default_prompt:
                errors.append(f"{rel(metadata_path)}: missing default_prompt")
            elif name and not default_prompt.startswith(f"Use ${name} "):
                errors.append(f"{rel(metadata_path)}: default_prompt must start with Use ${name} ")

        edges = parse_cross_references(skill_path, errors)
        if name and graph:
            if name not in graph:
                errors.append(f"{rel(GRAPH_PATH)}: missing graph row for {name}")
            elif edges != graph[name]:
                errors.append(f"{rel(skill_path)}: Cross-References do not match {rel(GRAPH_PATH)}")

        check_resource_references(skill_path, errors)

    for name, edges in graph.items():
        if name not in names:
            errors.append(f"{rel(GRAPH_PATH)}: graph row references missing skill {name}")
        for label, targets in edges.items():
            for target in targets:
                if target not in names:
                    errors.append(f"{rel(GRAPH_PATH)}: {name} {label} references missing skill {target}")

    for path in ROOT.rglob("*.md"):
        if not should_skip_path(path):
            check_legacy_heading(path, errors)

    check_cascade(graph, errors, args.cascade)
    check_example_universe(errors)
    check_forbidden_active_terms(errors)
    check_empty_directories(errors)

    if errors:
        for error in sorted(set(errors)):
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"validation ok: skills={len(skill_paths)} metadata={metadata_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
