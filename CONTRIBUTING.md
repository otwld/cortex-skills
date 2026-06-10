# Contributing

Pull requests are welcome for new skills, skill refinements, metadata fixes,
validation improvements, and documentation updates.

## Contribution Rules

- Keep active skill instructions project-agnostic and reusable across TypeScript
  ecosystem projects.
- Preserve narrow skill scope. Prefer small focused skills over broad doctrine
  documents.
- Put agent workflow gates and operating policy skills under `governance/`.
- Keep the public brand separate from old extracted project assumptions.
- Put retained historical details only in `references/legacy-*.md` files whose
  first heading includes `Legacy`.
- Keep all illustrative examples inside the recruitment job-board universe.
- Update `agents/openai.yaml` whenever a skill trigger or public name changes.
- Update `references/skill-graph.md` whenever `Cross-References` changes.

## Skill Structure

Every skill must include:

```text
taxonomy[/group]/folder-slug/
|-- SKILL.md
`-- agents/
    `-- openai.yaml
```

Use concise folder slugs and keep the canonical skill name in `SKILL.md`
frontmatter. For example, `frameworks/angular/core` can contain the
`angular-conventions` skill, while `frameworks/angular/material` can contain
the Angular Material skill. Governance skills may use grouping paths such as
`governance/core/using-cortex` and `governance/review/review-gate`.

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

The validator checks structure, metadata, cross-references, referenced files,
legacy-file headings, active source-project residue, example policy, empty
directories, and representative cascade size.

## Pull Request Checklist

- The changed skill remains focused on one task, domain, or workflow.
- `SKILL.md` has valid frontmatter, an output marker, and a `Cross-References`
  section.
- `agents/openai.yaml` contains `(otwld)` in `interface.display_name`.
- New examples use `JobOffer`, `Candidate`, `Application`, `Recruiter`,
  `Company`, `Interview`, `Contract`, or `SkillTag` where examples need domain
  entities.
- Any new script is deterministic and documented from the skill that uses it.
- `python3 scripts/validate-skills.py` passes.

## Release Notes

User-visible changes should update `CHANGELOG.md`. Keep entries concise and
grouped by release.
