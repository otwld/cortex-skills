# Contributing

Pull requests are welcome for routed modules, explicit command artifacts,
metadata refinements, validation improvements, generated artifact handling, and
documentation updates.

## Contribution Rules

- Keep active instructions project-agnostic and reusable across TypeScript
  ecosystem projects.
- Preserve narrow scope. Prefer small focused artifacts over broad doctrine
  documents.
- Use `skill.yaml` as the source of truth for routing, relations, resources,
  activation, visibility, and generated catalog data.
- Keep selected-module behavior in `instructions.md`.
- Keep the public `$cortex` entry as the only public agent `SKILL.md`.
- Do not add `MODULE.md`, taxonomy folders, compatibility shims, implicit
  inheritance, or hidden resource sharing.
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

Routed modules and explicit commands use:

```text
modules/artifact-name/
|-- instructions.md
`-- skill.yaml
```

Optional runtime support files belong under the owning module:

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

The validator checks entry shape, metadata, activation and visibility rules,
relations, resources, duplicate strong signals, generated freshness, explicit
command exclusion, and the public entry's agent-skill shape.

## Pull Request Checklist

- The changed artifact remains focused on one task, domain, or workflow.
- Metadata and instructions are updated together.
- Routed modules use `activation: routed` and `visibility: hidden`.
- Explicit command artifacts use `activation: explicit`, `visibility: public`,
  and say they run only when directly invoked.
- New or moved resources are declared.
- Generated artifacts were rebuilt or verified fresh.
- New examples use `JobOffer`, `Candidate`, `Application`, `Recruiter`,
  `Company`, `Interview`, `Contract`, or `SkillTag` where examples need domain
  entities.
- `python3 scripts/validate-routed-skills.py routed-skills.yaml` passes.
- `python3 scripts/test-validate-routed-skills.py` passes when validator
  behavior changes.

## Release Notes

User-visible changes should update `CHANGELOG.md`. Keep entries concise and
grouped by release.
