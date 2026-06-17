# Contributing

Pull requests are welcome for new modules, module refinements, public skill
metadata fixes, validation improvements, and documentation updates.

## Contribution Rules

- Keep active instructions project-agnostic and reusable across TypeScript
  ecosystem projects.
- Preserve narrow scope. Prefer small focused modules over broad doctrine
  documents.
- Put agent workflow gates and operating policy modules under `governance/`.
- Keep the public brand separate from old extracted project assumptions.
- Put retained historical details only in `references/legacy-*.md` files whose
  first heading includes `Legacy`.
- Keep all illustrative examples inside the recruitment job-board universe.
- Update `agents/openai.yaml` only when the public `cortex` skill trigger or
  public name changes.
- Update `references/module-graph.md` whenever `Cross-References` changes.
- Update `SKILL_CATALOG.md` whenever a skill or module is added, removed, moved, or
  renamed.

## Artifact Structure

The public skill must keep this exact shape:

```text
governance/core/cortex/
|-- SKILL.md
`-- agents/
    `-- openai.yaml
```

Internal modules must include:

```text
taxonomy[/group]/folder-slug/
`-- MODULE.md
```

Use concise folder slugs and keep the canonical module name in `MODULE.md`
frontmatter. For example, `frameworks/angular/core` can contain the
`angular-conventions` module, while `frameworks/angular/material` can contain
the Angular Material module. Governance modules may use grouping paths such as
`governance/core/cortex` and `governance/review/review-gate`.

Optional runtime support files belong in:

- `references/` for detailed guidance loaded only when needed.
- `scripts/` for deterministic checks or repeated operations.
- `assets/` for reusable templates or output resources.

## Validation

Run the validator before opening a pull request:

```bash
python3 scripts/validate-skills.py
```

For graph changes, also inspect the cascade simulation:

```bash
python3 scripts/validate-skills.py --cascade
```

For validator or routing-contract changes, run the fixture regression suite:

```bash
python3 scripts/test-validate-skills.py
```

The validator checks public skill structure, module structure, OpenAI
`interface:` metadata, catalog entries and taxonomy headings, cross-references,
referenced files, legacy-file headings, active source-project residue, example
policy, empty directories, and representative cascade size.
Ordinary module additions should not require validator source-code changes.

## Pull Request Checklist

- The changed artifact remains focused on one task, domain, or workflow.
- The public `SKILL.md` or internal `MODULE.md` has valid frontmatter, an output
  marker, and a `Cross-References` section.
- Only the public `agents/openai.yaml` exists, contains `(otwld)` in
  `interface.display_name`, and sets `policy.allow_implicit_invocation: false`.
- New examples use `JobOffer`, `Candidate`, `Application`, `Recruiter`,
  `Company`, `Interview`, `Contract`, or `SkillTag` where examples need domain
  entities.
- Any new script is deterministic and documented from the artifact that uses it.
- `python3 scripts/validate-skills.py` passes.
- `python3 scripts/test-validate-skills.py` passes when validator behavior
  changes.

## Release Notes

User-visible changes should update `CHANGELOG.md`. Keep entries concise and
grouped by release.
