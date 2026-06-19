#!/usr/bin/env python3
"""Fixture tests for routed skill workspace validation and rebuild scripts."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
AUDIT = SCRIPT_DIR / 'audit-routed-history.py'
REBUILD = SCRIPT_DIR / 'rebuild-routed-skills.py'
VALIDATE = SCRIPT_DIR / 'validate-routed-skills.py'
SETUP_TEMPLATE_ROOT = SCRIPT_DIR.parent / 'commands' / 'setup-routed-skill-workspace' / 'assets' / 'templates'


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run a script command in a fixture workspace."""
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def write(path: Path, text: str) -> None:
    """Write fixture text, creating parents first."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def render_setup_template(relative_path: str, values: dict[str, str]) -> str:
    """Render a bundled setup template for validator fixture coverage."""
    text = (SETUP_TEMPLATE_ROOT / relative_path).read_text(encoding='utf-8')
    for key, value in values.items():
        text = text.replace(f'{{{{{key}}}}}', value)
    if '{{' in text or '}}' in text:
        raise AssertionError(f'unresolved template placeholder in {relative_path}')
    return text


def manifest(root_name: str, *, max_depth: int = 3, always: str = '') -> str:
    """Return fixture manifest text."""
    routing_block = f'''
routing:
  always:
    - {always}
''' if always else ''
    return f'''name: ascend
root: {root_name}

paths:
  entry: entry
  modules: modules
  commands: commands
  shared: shared
  generated: generated
  proposals: proposals

artifacts:
  metadata: skill.yaml
  instructions: instructions.md

entry:
  required: true
  path: entry/ascend

{routing_block}
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


def command_skill(name: str = 'setup-ci') -> str:
    """Return fixture public command skill instructions."""
    return f'''---
name: {name}
description: Use only when the user explicitly includes ${name}; runs a direct command workflow.
---

# Output Marker

Display:
using skill: {name}

---

# {name}

Run only when directly invoked as `${name}`.
'''


def setup_template_values() -> dict[str, str]:
    """Return placeholder values for setup-template fixtures."""
    return {
        'workspace_name': 'ascend',
        'root': '.skills',
        'entry_slug': 'ascend',
        'entry_name': 'ascend',
        'entry_invocation': '$ascend',
        'entry_display_name': 'Ascend',
        'entry_short_description': 'Route workspace modules.',
    }


def module_setup_template_values(name: str) -> dict[str, str]:
    """Return module placeholder values for setup-template fixtures."""
    return {
        'module_name': name,
        'module_description': f'Guidance for {name}.',
        'module_purpose': f'Validate generated guidance for {name}.',
    }


def create_workspace_from_setup_templates(temp_dir: Path) -> Path:
    """Create an empty routed workspace using bundled setup templates."""
    root = temp_dir / '.skills'
    values = setup_template_values()
    write(root / 'routed-skills.yaml', render_setup_template('routed-skills.yaml', values))
    write(root / 'entry' / 'ascend' / 'SKILL.md', render_setup_template('entry/SKILL.md.template', values))
    write(root / 'entry' / 'ascend' / 'agents' / 'openai.yaml', render_setup_template('entry/agents/openai.yaml.template', values))
    write(root / 'entry' / 'ascend' / 'skill.yaml', render_setup_template('entry/skill.yaml', values))
    for folder in ('modules', 'commands', 'shared', 'generated', 'scripts', 'proposals'):
        (root / folder).mkdir(parents=True, exist_ok=True)
    result = run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], temp_dir)
    if result.returncode != 0:
        raise AssertionError(f'setup-template rebuild failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
    return root


def module_from_setup_template(name: str, *, status: str = 'draft', strong: str = '') -> str:
    """Return rendered module metadata from the bundled setup template."""
    text = render_setup_template('module/skill.yaml', module_setup_template_values(name))
    text = text.replace('status: draft', f'status: {status}')
    if strong:
        text = text.replace('strong: []', f'strong:\n      - {strong}')
    return text


def module_instructions_from_setup_template(name: str) -> str:
    """Return rendered module instructions from the bundled setup template."""
    return render_setup_template('module/instructions.md', module_setup_template_values(name))


def setup_templates_empty_workspace_validates() -> None:
    """Validate an empty workspace created from bundled setup templates."""
    with tempfile.TemporaryDirectory(prefix='routed-skills-') as raw:
        temp_dir = Path(raw)
        root = create_workspace_from_setup_templates(temp_dir)
        result = run([sys.executable, str(VALIDATE), str(root / 'routed-skills.yaml')], temp_dir)
        if result.returncode != 0:
            raise AssertionError(f'setup-template empty workspace should validate\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
        print('ok: setup templates empty workspace validates')


def setup_templates_active_modules_validate() -> None:
    """Validate several active modules created from bundled setup templates."""
    with tempfile.TemporaryDirectory(prefix='routed-skills-') as raw:
        temp_dir = Path(raw)
        root = create_workspace_from_setup_templates(temp_dir)
        modules = {
            'module-creation': 'user asks to create a module',
            'quality-standard': 'user asks for quality gates',
            'final-check': 'user asks for final check',
        }
        for name, signal in modules.items():
            write(root / 'modules' / name / 'skill.yaml', module_from_setup_template(name, status='active', strong=signal))
            write(root / 'modules' / name / 'instructions.md', module_instructions_from_setup_template(name))
        run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], temp_dir)
        result = run([sys.executable, str(VALIDATE), str(root / 'routed-skills.yaml')], temp_dir)
        if result.returncode != 0:
            raise AssertionError(f'setup-template active modules should validate\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
        print('ok: setup templates active modules validate')


def setup_template_active_empty_signals_fail() -> None:
    """Validate active setup-template modules still need routing signals."""
    with tempfile.TemporaryDirectory(prefix='routed-skills-') as raw:
        temp_dir = Path(raw)
        root = create_workspace_from_setup_templates(temp_dir)
        write(root / 'modules' / 'module-creation' / 'skill.yaml', module_from_setup_template('module-creation', status='active'))
        write(root / 'modules' / 'module-creation' / 'instructions.md', module_instructions_from_setup_template('module-creation'))
        run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], temp_dir)
        result = run([sys.executable, str(VALIDATE), str(root / 'routed-skills.yaml')], temp_dir)
        output = f'{result.stdout}\n{result.stderr}'
        if result.returncode == 0:
            raise AssertionError(f'setup-template active empty-signal module should fail\n{output}')
        if 'active routed module has no routing signals' not in output:
            raise AssertionError(f'setup-template active empty-signal failure missing diagnostic\n{output}')
        print('ok: setup template active empty signals fail')


def module_metadata(
    name: str,
    *,
    activation: str = 'routed',
    visibility: str = 'hidden',
    status: str = 'active',
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
status: {status}

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

# {title}

## Overview

Validate fixture guidance for {name}.

## Workflow

1. Inspect the request.
2. Apply focused {name} guidance.

## Quality Gates

- Evidence is direct.

## Hard Stops

- Do not broaden scope.

## Usage Checklist

- Evidence checked.

## Cross References

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
    for folder in ('commands', 'shared', 'generated', 'scripts', 'proposals'):
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
    """Add a valid command skill."""
    write(root / 'commands' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'commands' / 'setup-ci' / 'SKILL.md', command_skill())
    write(root / 'commands' / 'setup-ci' / 'agents' / 'openai.yaml', agent_metadata())
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


def missing_agent_display_name(root: Path) -> None:
    """Remove required public skill UI metadata."""
    write(
        root / 'entry' / 'ascend' / 'agents' / 'openai.yaml',
        agent_metadata().replace('  display_name: "Ascend"\n', ''),
    )


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
    """Use a routed module display marker for a command skill."""
    write(root / 'commands' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'commands' / 'setup-ci' / 'SKILL.md', command_skill().replace('using skill: setup-ci', 'using module: setup-ci'))
    write(root / 'commands' / 'setup-ci' / 'agents' / 'openai.yaml', agent_metadata())
    run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], root.parent)


def explicit_under_modules(root: Path) -> None:
    """Add a legacy command skill under the routed modules folder."""
    write(root / 'modules' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'modules' / 'setup-ci' / 'instructions.md', instructions('Set up CI when directly invoked.', name='setup-ci', marker='skill'))


def missing_command_skill(root: Path) -> None:
    """Add a command skill without its public SKILL.md."""
    write(root / 'commands' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'commands' / 'setup-ci' / 'agents' / 'openai.yaml', agent_metadata())


def missing_command_agent_metadata(root: Path) -> None:
    """Add a command skill without UI metadata."""
    write(root / 'commands' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'commands' / 'setup-ci' / 'SKILL.md', command_skill())


def allow_implicit_command(root: Path) -> None:
    """Allow implicit invocation for a direct command skill."""
    write(root / 'commands' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'commands' / 'setup-ci' / 'SKILL.md', command_skill())
    write(root / 'commands' / 'setup-ci' / 'agents' / 'openai.yaml', agent_metadata(True))


def legacy_command_instructions(root: Path) -> None:
    """Add legacy instructions beside a command SKILL.md."""
    add_explicit_command(root)
    write(root / 'commands' / 'setup-ci' / 'instructions.md', instructions('Legacy command instructions.', name='setup-ci', marker='skill'))


def stale_generated(root: Path) -> None:
    """Modify a generated artifact by hand."""
    (root / 'generated' / 'module-graph.md').write_text('# Manual edit\n', encoding='utf-8')


def enable_always_loaded_module(root: Path) -> None:
    """Configure an active routed module as always loaded."""
    write(root / 'routed-skills.yaml', manifest('.skills', always='quality-standard'))
    run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], root.parent)


def generated_always_loaded_module_is_rendered() -> None:
    """Validate generated cascade output includes always-loaded modules."""
    with tempfile.TemporaryDirectory(prefix='routed-skills-') as raw:
        temp_dir = Path(raw)
        root = create_workspace(temp_dir)
        enable_always_loaded_module(root)
        cascade = (root / 'generated' / 'module-cascade.md').read_text(encoding='utf-8')
        if '## Always Loaded Modules' not in cascade or '| `quality-standard` |' not in cascade:
            raise AssertionError('always-loaded module missing from generated cascade')
        if 'intent-understanding gate' not in cascade:
            raise AssertionError('intent-first routing phase missing from generated cascade')
        result = run([sys.executable, str(VALIDATE), str(root / 'routed-skills.yaml')], temp_dir)
        if result.returncode != 0:
            raise AssertionError(f'always-loaded generated output should validate\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
        print('ok: always-loaded generated output is rendered')


def always_loaded_missing_target(root: Path) -> None:
    """Point routing.always at a missing module."""
    write(root / 'routed-skills.yaml', manifest('.skills', always='missing-module'))


def always_loaded_command_target(root: Path) -> None:
    """Point routing.always at a command skill."""
    write(root / 'commands' / 'setup-ci' / 'skill.yaml', module_metadata('setup-ci', activation='explicit', visibility='public'))
    write(root / 'commands' / 'setup-ci' / 'SKILL.md', command_skill())
    write(root / 'commands' / 'setup-ci' / 'agents' / 'openai.yaml', agent_metadata())
    write(root / 'routed-skills.yaml', manifest('.skills', always='setup-ci'))


def always_loaded_inactive_target(root: Path) -> None:
    """Point routing.always at an inactive routed module."""
    write(root / 'modules' / 'quality-standard' / 'skill.yaml', module_metadata('quality-standard', status='draft'))
    write(root / 'routed-skills.yaml', manifest('.skills', always='quality-standard'))


def always_loaded_scalar_target(root: Path) -> None:
    """Configure routing.always as a scalar instead of a list."""
    write(root / 'routed-skills.yaml', manifest('.skills').replace('\ngenerated:', '\nrouting:\n  always: quality-standard\n\ngenerated:'))


def duplicate_signal(root: Path) -> None:
    """Duplicate a strong signal across unrelated modules."""
    signal = 'user asks for the same routing signal'
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', strong=signal))
    write(root / 'modules' / 'quality-standard' / 'skill.yaml', module_metadata('quality-standard', strong=signal))


def active_empty_signals(root: Path) -> None:
    """Make an active routed module unreachable through routing evidence."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation'))


def mechanical_strong_signal(root: Path) -> None:
    """Use a generated-looking strong signal instead of direct routing evidence."""
    signal = 'Module creation evidence for module-creation: user asks to create a module'
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', strong=signal))


def restated_strong_signal(root: Path) -> None:
    """Use a module name as the whole strong signal."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', strong='module-creation'))


def restated_weak_signal(root: Path) -> None:
    """Use a module name as the whole weak signal."""
    metadata = module_metadata('module-creation', strong='user asks to create a module')
    write(root / 'modules' / 'module-creation' / 'skill.yaml', metadata.replace('    weak: []', '    weak:\n      - module-creation'))


def duplicate_signal_category(root: Path) -> None:
    """Reuse the same strong-signal category across unrelated modules."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', strong='Shared category: user asks to create a module'))
    write(root / 'modules' / 'quality-standard' / 'skill.yaml', module_metadata('quality-standard', strong='Shared category: user asks for quality gates'))


def broad_lifecycle_strong_signal(root: Path) -> None:
    """Use broad lifecycle wording as direct routing evidence."""
    signal = 'Completion evidence: final response or success claim exists'
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', strong=signal))


def legacy_declared_resource(root: Path) -> None:
    """Declare a legacy-only resource as active guidance."""
    write(root / 'modules' / 'module-creation' / 'references' / 'legacy-extracted-patterns.md', '# Legacy\n')
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', strong='user asks to create a module', resource='legacy-extracted-patterns.md'))


def template_instruction_prose(root: Path) -> None:
    """Reintroduce template prose into active module instructions."""
    text = (root / 'modules' / 'module-creation' / 'instructions.md').read_text(encoding='utf-8')
    text = text.replace('2. Apply focused module-creation guidance.', '2. Apply the module-specific rules: create modules.')
    write(root / 'modules' / 'module-creation' / 'instructions.md', text)


def title_swapped_boilerplate(root: Path) -> None:
    """Reintroduce title-swapped checklist prose."""
    text = (root / 'modules' / 'module-creation' / 'instructions.md').read_text(encoding='utf-8')
    text = text.replace('- Evidence is direct.', '- Module Creation guidance names the inspected source, request evidence, or declared resource that triggered it.')
    write(root / 'modules' / 'module-creation' / 'instructions.md', text)


def duplicated_instruction_bullets(root: Path) -> None:
    """Add a third active module that repeats existing instruction bullets."""
    write(root / 'modules' / 'final-check' / 'skill.yaml', module_metadata('final-check', strong='user asks for final check'))
    write(root / 'modules' / 'final-check' / 'instructions.md', instructions('Final Check', name='final-check'))


def missing_required_instruction_section(root: Path) -> None:
    """Remove a required active module instruction section."""
    text = (root / 'modules' / 'module-creation' / 'instructions.md').read_text(encoding='utf-8')
    text = text.replace('## Quality Gates', '## Gates')
    write(root / 'modules' / 'module-creation' / 'instructions.md', text)


def missing_resource(root: Path) -> None:
    """Declare a missing resource."""
    write(root / 'modules' / 'module-creation' / 'skill.yaml', module_metadata('module-creation', resource='missing.md'))


def orphan_resource(root: Path) -> None:
    """Create an unlisted module resource."""
    write(root / 'modules' / 'module-creation' / 'references' / 'extra.md', '# Extra\n')


def audit_history_reports_under_signaled_terms() -> None:
    """Validate the routing history audit reports missing signal language."""
    with tempfile.TemporaryDirectory(prefix='routed-skills-') as raw:
        temp_dir = Path(raw)
        root = create_workspace(temp_dir)
        write(
            root / 'modules' / 'implementation-plan' / 'skill.yaml',
            module_metadata('implementation-plan', strong='Multi-step work: cross-boundary change'),
        )
        write(root / 'modules' / 'implementation-plan' / 'instructions.md', instructions('Implementation Plan', name='implementation-plan'))
        run([sys.executable, str(REBUILD), str(root / 'routed-skills.yaml')], temp_dir)
        history = temp_dir / 'history.jsonl'
        history.write_text(
            json.dumps({
                'session_id': 'fixture-session',
                'ts': 1781890000,
                'text': '$cortex draft a plan with phases',
            }) + '\n',
            encoding='utf-8',
        )
        result = run(
            [
                sys.executable,
                str(AUDIT),
                '--workspace',
                str(root / 'routed-skills.yaml'),
                '--history',
                str(history),
                '--logs',
                str(temp_dir / 'missing.sqlite'),
                '--recent',
                '10',
            ],
            temp_dir,
        )
        if result.returncode != 0:
            raise AssertionError(f'audit history should run\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
        if 'implementation-plan' not in result.stdout or 'draft a plan' not in result.stdout:
            raise AssertionError(f'audit history missing under-signaled module\nstdout:\n{result.stdout}')
        print('ok: audit history reports under-signaled terms')


def main() -> int:
    """Run routed workspace validator fixtures."""
    expect_success('valid workspace in .skills')
    expect_success('valid workspace in skills', root_name='skills')
    expect_success('valid workspace at repository root', root_name='.')
    expect_success('command skill validates', add_explicit_command)
    expect_success('always-loaded module validates', enable_always_loaded_module)
    generated_always_loaded_module_is_rendered()
    setup_templates_empty_workspace_validates()
    setup_templates_active_modules_validate()
    setup_template_active_empty_signals_fail()
    expect_failure('missing entry fails', remove_entry, 'expected exactly one entry skill')
    expect_failure('multiple entries fail', add_second_entry, 'expected exactly one entry skill')
    expect_failure('missing entry SKILL.md fails', remove_entry_skill, 'missing SKILL.md')
    expect_failure('missing entry agents metadata fails', remove_entry_agent_metadata, 'missing agents/openai.yaml')
    expect_failure('entry SKILL.md name mismatch fails', mismatch_entry_skill_name, 'does not match metadata')
    expect_failure('entry output marker mismatch fails', wrong_entry_output_marker, 'missing output marker: using skill: ascend')
    expect_failure('entry implicit invocation fails', allow_implicit_entry, 'allow_implicit_invocation must be false')
    expect_failure('entry missing display name fails', missing_agent_display_name, 'interface.display_name must be a non-empty string')
    expect_failure('legacy entry instructions fail', add_legacy_entry_instructions, 'entry instructions belong in SKILL.md')
    expect_failure('legacy entry openai metadata fails', add_legacy_entry_metadata, 'use agents/openai.yaml instead')
    expect_failure('missing metadata fails', add_missing_metadata_module, 'missing skill.yaml')
    expect_failure('missing instructions fails', add_missing_instructions_module, 'missing instructions.md')
    expect_failure('missing module output marker fails', missing_module_output_marker, 'missing output marker: using module: module-creation')
    expect_failure('legacy command skill under modules fails', explicit_under_modules, 'command skill must live under commands')
    expect_failure('missing command SKILL.md fails', missing_command_skill, 'missing SKILL.md')
    expect_failure('missing command agents metadata fails', missing_command_agent_metadata, 'missing agents/openai.yaml')
    expect_failure('command implicit invocation fails', allow_implicit_command, 'allow_implicit_invocation must be false')
    expect_failure('legacy command instructions fail', legacy_command_instructions, 'command behavior belongs in SKILL.md')
    expect_failure('explicit output marker mismatch fails', wrong_explicit_output_marker, 'missing output marker: using skill: setup-ci')
    expect_failure('broken relation fails', add_broken_relation, 'before target does not exist: missing-module', rebuild_after=True)
    expect_failure('before cycle fails', add_cycle, 'before cycle', rebuild_after=True)
    expect_failure('before depth cap fails', add_depth_violation, 'exceeds cap 1', rebuild_after=True)
    expect_failure('always-loaded missing target fails', always_loaded_missing_target, 'routing.always target does not exist: missing-module', rebuild_after=True)
    expect_failure('always-loaded command target fails', always_loaded_command_target, 'routing.always target must be a routed module: setup-ci', rebuild_after=True)
    expect_failure('always-loaded inactive target fails', always_loaded_inactive_target, 'routing.always target must be active: quality-standard', rebuild_after=True)
    expect_failure('always-loaded scalar target fails', always_loaded_scalar_target, 'routing.always: expected list')
    expect_failure('stale generated artifact fails', stale_generated, 'stale generated artifact')
    expect_failure('duplicate strong signal fails', duplicate_signal, 'duplicate strong signal', rebuild_after=True)
    expect_failure('active empty signals fail', active_empty_signals, 'active routed module has no routing signals', rebuild_after=True)
    expect_failure('mechanical strong signal fails', mechanical_strong_signal, 'strong signal uses mechanical evidence prefix', rebuild_after=True)
    expect_failure('restated strong signal fails', restated_strong_signal, 'strong signal only restates module name', rebuild_after=True)
    expect_failure('restated weak signal fails', restated_weak_signal, 'weak signal only restates module name', rebuild_after=True)
    expect_failure('duplicate strong signal category fails', duplicate_signal_category, 'duplicate strong signal category', rebuild_after=True)
    expect_failure('broad lifecycle strong signal fails', broad_lifecycle_strong_signal, 'strong signal uses broad lifecycle wording', rebuild_after=True)
    expect_failure('legacy declared resource fails', legacy_declared_resource, 'legacy-only references resource declared', rebuild_after=True)
    expect_failure('template instruction prose fails', template_instruction_prose, 'template prose remains')
    expect_failure('title-swapped instruction prose fails', title_swapped_boilerplate, 'title-swapped boilerplate remains')
    expect_failure('duplicated instruction bullets fail', duplicated_instruction_bullets, 'duplicated instruction bullet', rebuild_after=True)
    expect_failure('missing required instruction section fails', missing_required_instruction_section, 'missing required instruction section')
    expect_failure('missing resource fails', missing_resource, 'missing references resource', rebuild_after=True)
    expect_failure('orphan resource fails', orphan_resource, 'orphaned references resource')
    audit_history_reports_under_signaled_terms()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
