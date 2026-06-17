#!/usr/bin/env python3
"""Run fixture-based regression tests for scripts/validate-skills.py."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = Path('scripts/validate-skills.py')

TAXONOMY_PROBER_MODULE = '''---
name: taxonomy-prober
description: Internal Cortex module applied when checking that module discovery validates through generic taxonomy rules.
---

# Output Marker

Display:
using module: taxonomy-prober

---

# Taxonomy Prober

## Overview

Validate that modules can be discovered from filesystem state, graph, and catalog
instead of a validator source-code registry.

## Workflow

1. Add a module directory under a valid taxonomy.
2. Add graph and catalog entries.
3. Run the validator.

## Quality Gates

- Discovery is derived from workspace files.

## Example

Example: A maintenance taxonomy fixture proves discovery without editing the validator.

## Hard Stops

- The validator requires a source-code registry edit for an otherwise valid module.

## Usage Checklist

- The module has frontmatter, graph, and catalog entries.

## Cross-References

- None
'''

TAXONOMY_PROBER_SKILL = TAXONOMY_PROBER_MODULE.replace(
    'using module: taxonomy-prober',
    'using skill: taxonomy-prober',
)

TAXONOMY_PROBER_METADATA = '''interface:
  display_name: "(otwld) Taxonomy Prober"
  short_description: "Check generic module discovery"
  default_prompt: "Use $taxonomy-prober when checking generic module discovery."
'''


def run_validator(workspace: Path, *args: str) -> subprocess.CompletedProcess[str]:
    """Run the validator in a fixture workspace and capture output."""
    return subprocess.run([sys.executable, str(VALIDATOR), *args], cwd=workspace, text=True, capture_output=True, check=False)


def replace_required(path: Path, old: str, new: str) -> None:
    """Replace fixture text and fail if the anchor moved."""
    text = path.read_text(encoding='utf-8')
    if old not in text:
        raise AssertionError(f'{path}: missing fixture anchor {old!r}')
    path.write_text(text.replace(old, new), encoding='utf-8')


def find_catalog_row(catalog_path: Path, name: str) -> str:
    """Return a catalog row by public skill or module name."""
    prefix = f'| `{name}` | '
    for line in catalog_path.read_text(encoding='utf-8').splitlines():
        if line.startswith(prefix):
            return f'{line}\n'
    raise AssertionError(f'{catalog_path}: missing catalog row for {name!r}')


def increment_catalog_module_count(catalog_path: Path) -> None:
    """Increment the catalog summary count for one fixture module."""
    text = catalog_path.read_text(encoding='utf-8')
    match = re.search(r'Cortex Skills contains (\d+) public skill and (\d+) internal modules', text)
    if match is None:
        raise AssertionError(f'{catalog_path}: missing skill/module count summary')
    updated = text[:match.start(2)] + str(int(match.group(2)) + 1) + text[match.end(2):]
    catalog_path.write_text(updated, encoding='utf-8')


def add_taxonomy_prober(workspace: Path, taxonomy: str = 'maintenance') -> None:
    """Add a fully wired fixture module under the selected taxonomy."""
    module_dir = workspace / taxonomy / 'taxonomy-prober'
    module_dir.mkdir(parents=True)
    (module_dir / 'MODULE.md').write_text(TAXONOMY_PROBER_MODULE, encoding='utf-8')
    graph_path = workspace / 'references' / 'module-graph.md'
    skill_evolution_row = '| `skill-evolution` | None | None | None |\n'
    replace_required(graph_path, skill_evolution_row, skill_evolution_row + '| `taxonomy-prober` | None | None | None |\n')
    catalog_path = workspace / 'SKILL_CATALOG.md'
    increment_catalog_module_count(catalog_path)
    row = find_catalog_row(catalog_path, 'skill-evolution')
    replace_required(catalog_path, row, row + '| `taxonomy-prober` | Checking generic module discovery through taxonomy, graph, and catalog rules. | `maintenance/taxonomy-prober/` |\n')


def add_direct_skill(workspace: Path) -> None:
    """Add a second public skill where only internal modules are allowed."""
    skill_dir = workspace / 'maintenance' / 'taxonomy-prober'
    skill_dir.mkdir(parents=True)
    (skill_dir / 'SKILL.md').write_text(TAXONOMY_PROBER_SKILL, encoding='utf-8')


def add_module_metadata(workspace: Path) -> None:
    """Add OpenAI metadata to an internal module."""
    agents_dir = workspace / 'maintenance' / 'skill-evolution' / 'agents'
    agents_dir.mkdir()
    (agents_dir / 'openai.yaml').write_text(TAXONOMY_PROBER_METADATA, encoding='utf-8')


def move_catalog_row_to_wrong_section(workspace: Path) -> None:
    """Move a valid catalog row under the wrong taxonomy heading."""
    catalog_path = workspace / 'SKILL_CATALOG.md'
    code_documentation_row = find_catalog_row(catalog_path, 'code-documentation')
    public_api_row = find_catalog_row(catalog_path, 'public-api-design')
    replace_required(catalog_path, code_documentation_row, '')
    replace_required(catalog_path, public_api_row, public_api_row + code_documentation_row)


def break_workspace_relative_reference(workspace: Path) -> None:
    """Point the public Cortex skill at a missing workspace reference."""
    path = workspace / 'governance' / 'core' / 'cortex' / 'SKILL.md'
    replace_required(path, '`../../../references/module-graph.md`', '`../../../references/missing-module-graph.md`')


def rename_openai_interface_block(workspace: Path) -> None:
    """Move public skill metadata fields out of the interface block."""
    path = workspace / 'governance' / 'core' / 'cortex' / 'agents' / 'openai.yaml'
    replace_required(path, 'interface:\n', 'metadata:\n')


def remove_quality_section(workspace: Path) -> None:
    """Remove a required quality section from one module."""
    path = workspace / 'maintenance' / 'skill-evolution' / 'MODULE.md'
    replace_required(path, '## Hard Stops\n\n', '')


def remove_workspace_reference(workspace: Path) -> None:
    """Delete a required workspace reference."""
    (workspace / 'references' / 'agent-briefs.md').unlink()


def fixture_workspace() -> tempfile.TemporaryDirectory[str]:
    """Copy the current repository into a temporary validation workspace."""
    temp_dir = tempfile.TemporaryDirectory(prefix='cortex-validator-')
    shutil.copytree(ROOT, Path(temp_dir.name) / 'skills', ignore=shutil.ignore_patterns('.git', '.idea', '.vscode', '__pycache__', 'node_modules'))
    return temp_dir


def expect_success(name: str, mutate: Callable[[Path], None]) -> None:
    """Run a fixture that should validate successfully."""
    with fixture_workspace() as temp_dir:
        workspace = Path(temp_dir) / 'skills'
        mutate(workspace)
        result = run_validator(workspace)
        if result.returncode != 0:
            raise AssertionError(f'{name}: expected success, got {result.returncode}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
        print(f'ok: {name}')


def expect_failure(name: str, mutate: Callable[[Path], None], expected_error: str) -> None:
    """Run a fixture that should fail with a specific diagnostic."""
    with fixture_workspace() as temp_dir:
        workspace = Path(temp_dir) / 'skills'
        mutate(workspace)
        result = run_validator(workspace)
        output = f'{result.stdout}\n{result.stderr}'
        if result.returncode == 0:
            raise AssertionError(f'{name}: expected failure, got success\n{output}')
        if expected_error not in output:
            raise AssertionError(f'{name}: missing expected diagnostic {expected_error!r}\n{output}')
        print(f'ok: {name}')


def main() -> int:
    """Run validator regression fixtures."""
    expect_success('current repository validates', lambda _workspace: None)
    expect_success('fully wired new module needs no validator registry', add_taxonomy_prober)
    expect_failure('unknown taxonomy is rejected', lambda workspace: add_taxonomy_prober(workspace, taxonomy='misc'), "unknown module taxonomy 'misc'")
    expect_failure('non-cortex public skill is rejected', add_direct_skill, 'only governance/core/cortex/SKILL.md may be a public SKILL.md')
    expect_failure('internal module metadata is rejected', add_module_metadata, 'internal module must not define agents/openai.yaml')
    expect_failure('catalog section must match taxonomy', move_catalog_row_to_wrong_section, "catalog section for 'code-documentation' is 'Architecture', expected 'Documentation'")
    expect_failure('workspace-relative support references must exist', break_workspace_relative_reference, 'referenced resource does not exist: ../../../references/missing-module-graph.md')
    expect_failure('OpenAI metadata must use interface block', rename_openai_interface_block, 'missing interface block')
    expect_failure('module quality sections are required', remove_quality_section, 'missing required quality section ## Hard Stops')
    expect_failure('workspace references are required', remove_workspace_reference, 'references/agent-briefs.md: missing required workspace reference')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
