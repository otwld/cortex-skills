# Contributing

Cortex is a routed skill workspace. Keep changes inspectable, validated, and
free of hidden coupling.

## Routing Contract

- Use `skill.yaml` as the source of truth for metadata, facets, lifecycle
  declarations, resources, and ownership.
- Use lifecycle files for routed module runtime behavior.
- Do not add routed module `instructions.md`.
- Do not add module relations such as `before`, `with`, `after`, `excludes`, or
  `replaces`.
- Do not add output marker blocks.

## Module Rules

Active routed modules must:

- use `activation: routed` and `visibility: hidden`;
- declare structured routing facets;
- declare at least one lifecycle file;
- keep lifecycle guidance phase-specific;
- avoid naming peer modules or routing other atoms;
- declare owned resources under `resources`.

Draft modules may keep incomplete facets while their routing evidence is still
being designed.

## Command Rules

Command skills live under `commands/`, use `activation: explicit`, and are
public. They own `SKILL.md`, `agents/openai.yaml`, and `skill.yaml`. Commands do
not declare lifecycle files.

`$cortex` may invoke command atoms when orchestration requires it.

## Validation

Run before opening a pull request:

```bash
python3 scripts/rebuild-routed-skills.py routed-skills.yaml
python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

When rebuild or validation behavior changes, also run:

```bash
python3 scripts/test-validate-routed-skills.py
```

## Generated Files

Do not hand-edit files under `generated/`. Rebuild them from metadata.

## Examples

Examples, fixtures, and snippets should use the recruitment agency universe:
Candidate, JobOffer, Application, Recruiter, Company, Interview, Contract, and
SkillTag.
