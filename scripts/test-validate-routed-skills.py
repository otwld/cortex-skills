#!/usr/bin/env python3
"""Fixture tests for routed skill workspace validation and rebuild scripts."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REBUILD = SCRIPT_DIR / 'rebuild-routed-skills.py'
VALIDATE = SCRIPT_DIR / 'validate-routed-skills.py'


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run a script command in a fixture workspace."""
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def write(path: Path, text: str) -> None:
    """Write fixture text, creating parents first."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def manifest(root_name: str, *, max_depth: int = 3) -> str:
    """Return fixture manifest text."""
    return f'''name: ascend
root: {root_name}

paths:
  entry: entry
  modules: modules
  shared: shared
  generated: generated
  proposals: proposals

artifacts:
  metadata: skill.yaml
  instructions: instructions.md

entry:
  required: true
  path: entry/ascend

generated:
  catalog: generated/SKILL_CATALOG.md
  graph: generated/module-graph.md
  cascade: generated/module-cascade.md

validation:
  max_before_depth: {max_depth}
'''


def entry_metadata(name: str = 'ascend') -> str:
    """Return fixture entry metadata."""
    return f'''name: {name}
description: Public entry skill for Ascend.
activation: entry
visibility: public
status: active
'''


def entry_skill(name: str = 'ascend') -> str:
    """Return fixture public agent skill entry instructions."""
    return f'''---
name: {name}
description: Use only when the user explicitly includes ${name}; routes work through hidden modules.
---

# Output Marker

Display:
using skill: {name}

---

# {name}

Route explicit ${name} requests through hidden routed modules.
'''


def agent_metadata(allow_implicit: bool = False) -> str:
    """Return fixture UI metadata."""
    implicit = 'true' if allow_implicit else 'false'
    return f'''interface:
  display_name: "Ascend"
  short_description: "Route workspace modules"
  default_prompt: "Use $ascend to route work through hidden modules."
policy:
  allow_implicit_invocation: {implicit}
'''


def module_metadata(
    name: str,
    *,
    activation: str = 'routed',
    visibility: str = 'hidden',
    strong: str = '',
    before: str = '',
    uses: str = '',
    resource: str = '',
) -> str:
    """Return fixture module metadata."""
    strong_value = f'\n      - {strong}' if strong else ' []'
    before_value = f'\n    - {before}' if before else ' []'
    uses_value = f'\n  - {uses}' if uses else ' []'
    resource_value = f'\n    - {resource}' if resource else ' []'
    return f'''name: {name}
description: Guidance for {name}.
activation: {activation}
visibility: {visibility}
status: active

routing:
  priority: 5
  signals:
    strong:{strong_value}
    medium: []
    weak: []

relations:
  before:{before_value}
  with: []
  after: []
  excludes: []
  replaces: []

uses:{uses_value}

resources:
  references:{resource_value}
  scripts: []
  templates: []
  assets: []
'''


def instructions(title: str, *, name: str = 'module-creation', marker: str = 'module') -> str:
    """Return fixture instructions."""
    return f'''# Output Marker

Display:
using {marker}: {name}

---

# Purpose

{title}

# When To Use

Use when routed evidence matches.

# Workflow

1. Inspect the request.
2. Apply the module guidance.

# Gates

- Evidence is direct.

# Hard Stops

- Do not broaden scope.

# Output Format

Report the result.

# Checklist

- Evidence checked.

# Cross References

- None
'''


def create_workspace(temp_dir: Path, root_name: str = '.skills', *, max_depth: int = 3) -> Path:
    """Create and rebuild a valid fixture workspace."""
    root = temp_dir if root_name == '.' else temp_dir / root_name
    write(root / 'routed-skills.yaml', manifest(root_name, max_depth=max_depth))
    write(root / 'entry' / 'ascend' / 'skill.yaml', entry_metadata())
    write(root / 'entry' / 'ascend' / 'SKILL.md', entry_skill())
    write(root / 'entry' / 'ascend' / 'agents' / 'openai.yaml', agent_metadata())
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', strong='user asks to create a module'))
    write(root / 'modules' / 'module-creation' / 'instructions.md', instructions('Create modules.', name='module-creation'))
    write(root / 'modules' / 'quality-standard' / 'skill.yaml', module_metadata('quality-standard', strong='user asks for quality gates'))
    write(root / 'modules' / 'quality-standard' / 'instructions.md', instructions('Apply quality standards.', name='quality-standard'))
    for folder in ('shared', 'generated', 'scripts', 'proposals'):
        (root / folder).mkdir(parents=True, exist_ok=True)
    result = run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], temp_dir)
    if result.returncode != 0:
        raise AssertionError(f'rebuild failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
    return root


def expect_success(name: str, mutate=None, root_name: str = '.skills') -> None:
    """Run a fixture expected to validate."""
    with tempfile.TemporaryDirectory(prefix='routed-skills-') as raw:
        temp_dir = Path(raw)
        root = create_workspace(temp_dir, root_name)
        if mutate:
            mutate(root)
        result = run([sys.executable, str(VALIDATE), str(root / 'routed-skills.yaml')], temp_dir)
        if result.returncode != 0:
            raise AssertionError(f'{name}: expected success\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
        print(f'ok: {name}')


def expect_failure(name: str, mutate, expected: str, *, rebuild_after: bool = False) -> None:
    """Run a fixture expected to fail with a diagnostic."""
    with tempfile.TemporaryDirectory(prefix='routed-skills-') as raw:
        temp_dir = Path(raw)
        root = create_workspace(temp_dir)
        mutate(root)
        if rebuild_after:
            run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], temp_dir)
        result = run([sys.executable, str(VALIDATE), str(root / 'routed-skills.yaml')], temp_dir)
        output = f'{result.stdout}\n{result.stderr}'
        if result.returncode == 0:
            raise AssertionError(f'{name}: expected failure\n{output}')
        if expected not in output:
            raise AssertionError(f'{name}: missing {expected!r}\n{output}')
        print(f'ok: {name}')


def add_explicit_command(root: Path) -> None:
    """Add a valid explicit command module."""
    write(root / 'modules' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'modules' / 'setup-ci' / 'instructions.md', instructions('Set up CI when directly invoked.', name='setup-ci', marker='skill'))
    run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], root.parent)


def remove_entry(root: Path) -> None:
    """Remove the mandatory entry skill."""
    shutil.rmtree(root / 'entry' / 'ascend')


def add_second_entry(root: Path) -> None:
    """Add a second entry skill."""
    write(root / 'entry' / 'second' / 'skill.yaml', entry_metadata('second'))
    write(root / 'entry' / 'second' / 'SKILL.md', entry_skill('second'))
    write(root / 'entry' / 'second' / 'agents' / 'openai.yaml', agent_metadata())


def remove_entry_skill(root: Path) -> None:
    """Remove the public agent skill entry file."""
    (root / 'entry' / 'ascend' / 'SKILL.md').unlink()


def remove_entry_agent_metadata(root: Path) -> None:
    """Remove public entry UI metadata."""
    (root / 'entry' / 'ascend' / 'agents' / 'openai.yaml').unlink()


def mismatch_entry_skill_name(root: Path) -> None:
    """Make SKILL.md frontmatter disagree with routed entry metadata."""
    write(root / 'entry' / 'ascend' / 'SKILL.md', entry_skill('not-ascend'))


def allow_implicit_entry(root: Path) -> None:
    """Allow implicit invocation in public entry UI metadata."""
    write(root / 'entry' / 'ascend' / 'agents' / 'openai.yaml', agent_metadata(True))


def add_legacy_entry_instructions(root: Path) -> None:
    """Add a legacy entry instructions file."""
    write(root / 'entry' / 'ascend' / 'instructions.md', instructions('Legacy duplicate.', name='ascend', marker='skill'))


def add_legacy_entry_metadata(root: Path) -> None:
    """Add a legacy root openai.yaml metadata file."""
    write(root / 'entry' / 'ascend' / 'openai.yaml', agent_metadata())


def add_missing_metadata_module(root: Path) -> None:
    """Add a module without metadata."""
    write(root / 'modules' / 'missing-metadata' / 'instructions.md', instructions('Missing metadata fixture.', name='missing-metadata'))


def add_missing_instructions_module(root: Path) -> None:
    """Add a module without instructions."""
    write(root / 'modules' / 'missing-instructions' / 'skill.yaml', module_metadata('missing-instructions'))


def add_broken_relation(root: Path) -> None:
    """Point a relation at a missing module."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', before='missing-module'))


def add_cycle(root: Path) -> None:
    """Create a circular before relation."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', before='quality-standard'))
    write(root / 'modules' / 'quality-standard' / 'skill.yaml', module_metadata('quality-standard', before='module-creation'))


def add_depth_violation(root: Path) -> None:
    """Create a before chain deeper than the cap."""
    write(root / 'routed-skills.yaml', manifest('.skills', max_depth=1))
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', before='quality-standard'))
    write(root / 'modules' / 'quality-standard' / 'skill.yaml', module_metadata('quality-standard', before='final-check'))
    write(root / 'modules' / 'final-check' / 'skill.yaml', module_metadata('final-check'))
    write(root / 'modules' / 'final-check' / 'instructions.md', instructions('Final check.', name='final-check'))


def wrong_entry_output_marker(root: Path) -> None:
    """Make the entry display marker disagree with entry metadata."""
    write(root / 'entry' / 'ascend' / 'SKILL.md', entry_skill().replace('using skill: ascend', 'using skill: wrong'))


def missing_module_output_marker(root: Path) -> None:
    """Remove the module display marker from a routed module."""
    write(root / 'modules' / 'module-creation' / 'instructions.md', instructions('Create modules.', name='module-creation').replace('using module: module-creation', ''))


def wrong_explicit_output_marker(root: Path) -> None:
    """Use a routed module display marker for an explicit command."""
    write(root / 'modules' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'modules' / 'setup-ci' / 'instructions.md', instructions('Set up CI when directly invoked.', name='setup-ci', marker='module'))
    run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], root.parent)


def stale_generated(root: Path) -> None:
    """Modify a generated artifact by hand."""
    (root / 'generated' / 'module-graph.md').write_text('# Manual edit\n', encoding='utf-8')


def duplicate_signal(root: Path) -> None:
    """Duplicate a strong signal across unrelated modules."""
    signal = 'user asks for the same routing signal'
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', strong=signal))
    write(root / 'modules' / 'quality-standard' / 'skill.yaml', module_metadata('quality-standard', strong=signal))


def missing_resource(root: Path) -> None:
    """Declare a missing resource."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', resource='missing.md'))


def orphan_resource(root: Path) -> None:
    """Create an unlisted module resource."""
    write(root / 'modules' / 'module-creation' / 'references' / 'extra.md', '# Extra\n')


def main() -> int:
    """Run routed workspace validator fixtures."""
    expect_success('valid workspace in .skills')
    expect_success('valid workspace in skills', root_name='skills')
    expect_success('valid workspace at repository root', root_name='.')
    expect_success('explicit command validates', add_explicit_command)
    expect_failure('missing entry fails', remove_entry, 'expected exactly one entry skill')
    expect_failure('multiple entries fail', add_second_entry, 'expected exactly one entry skill')
    expect_failure('missing entry SKILL.md fails', remove_entry_skill, 'missing SKILL.md')
    expect_failure('missing entry agents metadata fails', remove_entry_agent_metadata, 'missing agents/openai.yaml')
    expect_failure('entry SKILL.md name mismatch fails', mismatch_entry_skill_name, 'does not match entry metadata')
    expect_failure('entry output marker mismatch fails', wrong_entry_output_marker, 'missing output marker: using skill: ascend')
    expect_failure('entry implicit invocation fails', allow_implicit_entry, 'allow_implicit_invocation must be false')
    expect_failure('legacy entry instructions fail', add_legacy_entry_instructions, 'entry instructions belong in SKILL.md')
    expect_failure('legacy entry openai metadata fails', add_legacy_entry_metadata, 'use agents/openai.yaml instead')
    expect_failure('missing metadata fails', add_missing_metadata_module, 'missing skill.yaml')
    expect_failure('missing instructions fails', add_missing_instructions_module, 'missing instructions.md')
    expect_failure('missing module output marker fails', missing_module_output_marker, 'missing output marker: using module: module-creation')
    expect_failure('explicit output marker mismatch fails', wrong_explicit_output_marker, 'missing output marker: using skill: setup-ci')
    expect_failure('broken relation fails', add_broken_relation, 'before target does not exist: missing-module', rebuild_after=True)
    expect_failure('before cycle fails', add_cycle, 'before cycle', rebuild_after=True)
    expect_failure('before depth cap fails', add_depth_violation, 'exceeds cap 1', rebuild_after=True)
    expect_failure('stale generated artifact fails', stale_generated, 'stale generated artifact')
    expect_failure('duplicate strong signal fails', duplicate_signal, 'duplicate strong signal', rebuild_after=True)
    expect_failure('missing resource fails', missing_resource, 'missing references resource', rebuild_after=True)
    expect_failure('orphan resource fails', orphan_resource, 'orphaned references resource')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
