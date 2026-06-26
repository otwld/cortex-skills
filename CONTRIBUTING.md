# Contributing

Pull requests are welcome for routed modules, command skills,
metadata refinements, validation improvements, generated artifact handling, and
documentation updates.

## Contribution Rules

- Keep active instructions project-agnostic and reusable across TypeScript
  ecosystem projects.
- Preserve narrow scope. Prefer small focused artifacts over broad doctrine
  documents.
- Write strong routing signals as direct request or repository evidence. Do not
  use generated phrases such as `evidence for <module>` or signals that only
  restate the module name.
- Use `skill.yaml` as the source of truth for routing, relations, resources,
  activation, visibility, and generated catalog data.
- Keep selected-module behavior in `instructions.md`.
- Keep the public `$cortex` entry as the only public routed entry skill.
- Do not add `MODULE.md`, compatibility shims, implicit inheritance, or hidden
  resource sharing.
- Category folders under `modules/` are allowed only as readability containers;
  they do not create routing behavior, inheritance, or implicit resources.
- Keep all illustrative examples inside the recruitment job-board universe.
- Do not hand-edit files under `generated/`.

## Artifact Structure

The public entry skill must keep this shape:

```text
entry/cortex/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
`-- skill.yaml
```

Routed modules use:

```text
modules/category/path/artifact-name/
|-- instructions.md
`-- skill.yaml
```

Generic routed workspaces may keep flat `modules/artifact-name/` paths. This
repository uses nested category paths for readability while keeping category
folders inert.

Command skills use:

```text
commands/command-name/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
`-- skill.yaml
```

Optional runtime support files belong under the owning artifact:

- `references/` for detailed guidance loaded only when needed.
- `scripts/` for deterministic checks or repeated operations.
- `templates/` for reusable text or scaffold inputs.
- `assets/` for reusable output resources.

Cross-cutting support files belong under `shared/` and must be declared by each
consumer in `skill.yaml`.

## Validation

Run the validator before opening a pull request:

```bash
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

Check generated freshness:

```bash
python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml
```

For validator or rebuild changes, run the fixture regression suite:

```bash
python3 scripts/test-validate-routed-skills.py
```

The validator checks entry shape, command skill shape, nested module categories,
metadata, activation and visibility rules, relations, resources, active module
reachability, instruction prose quality, title-swapped boilerplate, public
`agents/openai.yaml` display metadata, duplicate strong signals, generated
freshness, and routed cascade exclusion for command skills.

## Pull Request Checklist

- The changed artifact remains focused on one task, domain, or workflow.
- Metadata and instructions are updated together.
- Routed modules use `activation: routed` and `visibility: hidden`.
- Command skills live under `commands/`, use `activation: explicit` and
  `visibility: public`, and say they run only when directly invoked.
- New or moved resources are declared.
- Active routed modules have routing signals and no legacy-only declared
  resources.
- Instruction changes avoid copied template prose, title-swapped quality gates,
  and repeated low-value checklist bullets.
- Public entry and command skills keep complete `agents/openai.yaml` interface
  metadata and `policy.allow_implicit_invocation: false`.
- Generated artifacts were rebuilt or verified fresh.
- New examples use `JobOffer`, `Candidate`, `Application`, `Recruiter`,
  `Company`, `Interview`, `Contract`, or `SkillTag` where examples need domain
  entities.
- `python3 scripts/validate-routed-skills.py routed-skills.yaml` passes.
- `python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml`
  passes.
- `python3 scripts/test-validate-routed-skills.py` passes when validator
  behavior changes.

## Release Notes

User-visible changes should update `CHANGELOG.md`. Keep entries concise and
grouped by release.
