#!/usr/bin/env python3
"""Fixture tests for Cortex routed skill workspace validation and rebuild scripts."""

from __future__ import annotations

import json
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


def manifest(root_name: str) -> str:
    """Return fixture manifest text."""
    return f'''name: ascend
root: {root_name}

paths:
  entry: entry
  modules: modules
  commands: commands
  shared: shared
  generated: generated

artifacts:
  metadata: skill.yaml

entry:
  required: true
  path: entry/ascend

routing:
  facets:
    keys:
      - intents
      - surfaces
      - risks
      - artifacts
      - repo
      - request

lifecycle:
  phases:
    - activate
    - plan
    - run
    - review
    - verify
    - finalize

generated:
  catalog: generated/SKILL_CATALOG.md
  graph: generated/module-graph.md
  cascade: generated/module-cascade.md
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
description: Use only when the user explicitly includes ${name}; routes work through hidden lifecycle atoms.
---

# {name}

Route explicit ${name} requests through hidden lifecycle atoms.
'''


def agent_metadata(allow_implicit: bool = False) -> str:
    """Return fixture UI metadata."""
    implicit = 'true' if allow_implicit else 'false'
    return f'''interface:
  display_name: "Ascend"
  short_description: "Route workspace atoms"
  default_prompt: "Use $ascend to route work through lifecycle atoms."
policy:
  allow_implicit_invocation: {implicit}
'''


def command_skill(name: str = 'setup-ci') -> str:
    """Return fixture public command skill instructions."""
    return f'''---
name: {name}
description: Use only when the user explicitly includes ${name}; runs a direct command workflow.
---

# {name}

Run the command workflow.
'''


def module_metadata(
    name: str,
    *,
    activation: str = 'routed',
    visibility: str = 'hidden',
    status: str = 'active',
    facet_key: str = 'intents',
    facet_value: str = 'create module',
    lifecycle: str = 'activate: lifecycle/activate.md',
) -> str:
    """Return fixture module metadata."""
    lifecycle_block = f'\n  {lifecycle.lstrip()}' if lifecycle else ' {}'
    return f'''name: {name}
description: Guidance for {name}.
activation: {activation}
visibility: {visibility}
status: {status}

routing:
  priority: 5
  facets:
    {facet_key}:
      - {facet_value}
    surfaces: []
    risks: []
    artifacts: []
    repo: []
    request: []

lifecycle:{lifecycle_block}

uses: []

resources:
  references: []
  scripts: []
  templates: []
  assets: []
'''


def module_metadata_with_facets(name: str, *, status: str = 'active', facets: bool = True, lifecycle: str = 'activate: lifecycle/activate.md') -> str:
    """Return fixture module metadata with optional empty facets."""
    facet_value = 'create module' if facets else ''
    if facets:
        return module_metadata(name, status=status, lifecycle=lifecycle, facet_value=facet_value)
    lifecycle_block = f'\n  {lifecycle.lstrip()}' if lifecycle else ' {}'
    return f'''name: {name}
description: Guidance for {name}.
activation: routed
visibility: hidden
status: {status}

routing:
  priority: 5
  facets:
    intents: []
    surfaces: []
    risks: []
    artifacts: []
    repo: []
    request: []

lifecycle:{lifecycle_block}

uses: []

resources:
  references: []
  scripts: []
  templates: []
  assets: []
'''


def all_lifecycle_metadata(name: str, *, status: str = 'draft') -> str:
    """Return fixture metadata declaring every lifecycle phase."""
    return module_metadata_with_facets(
        name,
        status=status,
        facets=False,
        lifecycle='\n  activate: lifecycle/activate.md\n  plan: lifecycle/plan.md\n  run: lifecycle/run.md\n  review: lifecycle/review.md\n  verify: lifecycle/verify.md\n  finalize: lifecycle/finalize.md',
    )


def lifecycle_text(title: str = 'Create Module') -> str:
    """Return valid lifecycle file text."""
    return f'''# {title} Activate

## Overview

Validate fixture lifecycle guidance.

## Workflow

1. Match direct request or repository evidence.

## Quality Gates

- Facet evidence is explicit.

## Hard Stops

- Do not route peer modules.

## Phase Output

- Return matched evidence and phase constraints.
'''


def create_workspace(temp_dir: Path, root_name: str = '.skills') -> Path:
    """Create and rebuild a valid fixture workspace."""
    root = temp_dir if root_name == '.' else temp_dir / root_name
    write(root / 'routed-skills.yaml', manifest(root_name))
    write(root / '.gitignore', '.ascend/\n')
    write(root / 'entry' / 'ascend' / 'skill.yaml', entry_metadata())
    write(root / 'entry' / 'ascend' / 'SKILL.md', entry_skill())
    write(root / 'entry' / 'ascend' / 'agents' / 'openai.yaml', agent_metadata())
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation'))
    write(root / 'modules' / 'module-creation' / 'lifecycle' / 'activate.md', lifecycle_text())
    for folder in ('commands', 'shared', 'generated', 'scripts'):
        (root / folder).mkdir(parents=True, exist_ok=True)
    result = run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], temp_dir)
    if result.returncode != 0:
        raise AssertionError(f'rebuild failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
    return root


def expect_success(name: str, mutate=None, root_name: str = '.skills') -> None:
    """Run a fixture expected to validate."""
    with tempfile.TemporaryDirectory(prefix='cortex-skills-') as raw:
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
    with tempfile.TemporaryDirectory(prefix='cortex-skills-') as raw:
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
    """Add a valid command skill."""
    write(root / 'commands' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public', lifecycle=''))
    write(root / 'commands' / 'setup-ci' / 'SKILL.md', command_skill())
    write(root / 'commands' / 'setup-ci' / 'agents' / 'openai.yaml', agent_metadata())
    run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], root.parent)


def add_second_entry(root: Path) -> None:
    """Add a second entry skill."""
    write(root / 'entry' / 'second' / 'skill.yaml', entry_metadata('second'))
    write(root / 'entry' / 'second' / 'SKILL.md', entry_skill('second'))
    write(root / 'entry' / 'second' / 'agents' / 'openai.yaml', agent_metadata())


def add_legacy_module_instructions(root: Path) -> None:
    """Add legacy routed module instructions."""
    write(root / 'modules' / 'module-creation' / 'instructions.md', '# Legacy\n')


def add_relations(root: Path) -> None:
    """Reintroduce relation metadata."""
    path = root / 'modules' / 'module-creation' / 'skill.yaml'
    path.write_text(path.read_text(encoding='utf-8') + '\nrelations:\n  before: []\n', encoding='utf-8')


def add_signals(root: Path) -> None:
    """Reintroduce old signal metadata."""
    path = root / 'modules' / 'module-creation' / 'skill.yaml'
    text = path.read_text(encoding='utf-8').replace('  facets:', '  signals:\n    strong: []\n    medium: []\n    weak: []\n  facets:')
    path.write_text(text, encoding='utf-8')


def remove_lifecycle(root: Path) -> None:
    """Remove active module lifecycle declarations."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', lifecycle=''))


def missing_lifecycle_file(root: Path) -> None:
    """Delete a declared lifecycle file."""
    (root / 'modules' / 'module-creation' / 'lifecycle' / 'activate.md').unlink()


def undeclared_lifecycle_file(root: Path) -> None:
    """Add an undeclared lifecycle file."""
    write(root / 'modules' / 'module-creation' / 'lifecycle' / 'plan.md', lifecycle_text('Create Module Plan'))


def unknown_lifecycle_phase(root: Path) -> None:
    """Declare an unknown lifecycle phase."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', lifecycle='invent: lifecycle/activate.md'))


def unknown_facet_key(root: Path) -> None:
    """Use a facet key not declared by the manifest."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', facet_key='unknown'))


def missing_gitignore(root: Path) -> None:
    """Remove the run-trace ignore policy."""
    (root / '.gitignore').write_text('', encoding='utf-8')


def invalid_entry_config(root: Path) -> None:
    """Write an invalid entry-local operator config."""
    write(root / '.ascend' / 'config.json', json.dumps({'phases': {'activate': {'always': ['missing-module']}}}))


def write_valid_entry_config(root: Path) -> None:
    """Write a valid entry-local operator config."""
    write(root / '.ascend' / 'config.json', json.dumps({'phases': {'activate': {'always': ['module-creation']}}}))


def valid_entry_config(root: Path) -> None:
    """Write a valid entry-local operator config."""
    write_valid_entry_config(root)


def stale_generated(root: Path) -> None:
    """Modify a generated artifact by hand."""
    (root / 'generated' / 'module-graph.md').write_text('# Manual edit\n', encoding='utf-8')


def lifecycle_output_marker(root: Path) -> None:
    """Reintroduce prohibited lifecycle output marker text."""
    path = root / 'modules' / 'module-creation' / 'lifecycle' / 'activate.md'
    path.write_text('# Output Marker\n\nDisplay:\nusing module: module-creation\n\n---\n' + path.read_text(encoding='utf-8'), encoding='utf-8')


def draft_all_phase_module(root: Path) -> None:
    """Replace the fixture module with a draft all-phase scaffold."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', all_lifecycle_metadata('module-creation'))
    for phase in ('activate', 'plan', 'run', 'review', 'verify', 'finalize'):
        write(root / 'modules' / 'module-creation' / 'lifecycle' / f'{phase}.md', lifecycle_text(f'Module Creation {phase.title()}'))
    run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], root.parent)


def active_module_without_facets(root: Path) -> None:
    """Remove all active module facets."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata_with_facets('module-creation', facets=False))


def command_with_lifecycle(root: Path) -> None:
    """Add a command that incorrectly declares lifecycle files."""
    add_explicit_command(root)
    path = root / 'commands' / 'setup-ci' / 'skill.yaml'
    path.write_text(path.read_text(encoding='utf-8') + '\nlifecycle:\n  activate: lifecycle/activate.md\n', encoding='utf-8')


def main() -> int:
    """Run Cortex routed workspace validator fixtures."""
    expect_success('valid workspace in .skills')
    expect_success('valid workspace in skills', root_name='skills')
    expect_success('valid workspace at repository root', root_name='.')
    expect_success('command skill validates', add_explicit_command)
    expect_success('valid entry config validates', valid_entry_config)
    expect_success('draft all-phase module validates', draft_all_phase_module)
    expect_failure('multiple entries fail', add_second_entry, 'expected exactly one entry skill')
    expect_failure('legacy module instructions fail', add_legacy_module_instructions, 'routed module runtime belongs in lifecycle files')
    expect_failure('relations fail', add_relations, 'prohibited metadata key remains: relations')
    expect_failure('old signals fail', add_signals, 'prohibited routing key remains: signals')
    expect_failure('active module without lifecycle fails', remove_lifecycle, 'active routed module has no lifecycle files', rebuild_after=True)
    expect_failure('missing lifecycle file fails', missing_lifecycle_file, 'missing lifecycle file')
    expect_failure('undeclared lifecycle file fails', undeclared_lifecycle_file, 'undeclared lifecycle file')
    expect_failure('unknown lifecycle phase fails', unknown_lifecycle_phase, 'unknown lifecycle phase', rebuild_after=True)
    expect_failure('unknown facet key fails', unknown_facet_key, 'unknown routing facet key')
    expect_failure('active module without facets fails', active_module_without_facets, 'active routed module has no routing facets', rebuild_after=True)
    expect_failure('missing runtime ignore fails', missing_gitignore, 'missing .ascend/')
    expect_failure('invalid entry config fails', invalid_entry_config, 'always target does not exist')
    expect_failure('command lifecycle fails', command_with_lifecycle, 'command skills must not declare lifecycle files')
    expect_failure('stale generated fails', stale_generated, 'stale generated artifact')
    expect_failure('lifecycle output marker fails', lifecycle_output_marker, 'prohibited lifecycle routing/output text remains')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
