# Skill Evolution Run

## Overview

Apply the planned skill change while keeping artifact scope narrow and the
router-owned lifecycle model explicit.

## Workflow

1. Write routing facets as structured evidence: user intent, touched surfaces,
  artifacts, repository paths, and concrete risks. Do not copy old keyword lists
  into metadata.
2. Put runtime behavior in lifecycle phase files. Each phase should state what to
  inspect, what decision to make, failure conditions, and expected phase output.
3. Preserve useful old doctrine only when it describes durable behavior. Rewrite
  it for independent artifacts and explicit resource declarations.
4. Delete lifecycle files that add no distinct phase value, then remove their
  entries from `skill.yaml`.
5. Keep declared resources discoverable from `skill.yaml`; move stable detail to
  references only when lifecycle text would become bulky or repetitive.

## Quality Gates

- Use concrete nouns from the owned artifact: file paths, metadata fields,
  command families, review evidence, or validation commands.
- Prefer hard stops over broad advice when a wrong action could create duplicate
  ownership, stale metadata, or hidden coupling.
- Keep examples in the recruitment agency job board universe unless the user
  explicitly requires another domain.
- Avoid copied checklist language. A reviewer should be able to tell which
  artifact the phase belongs to even if the heading is removed.

## Hard Stops

- Do not add `instructions.md`, `MODULE.md`, compatibility shims, or hidden
  inheritance paths.
- Do not hand-edit generated catalogs or routing views.
- Do not change behavior in prose while leaving metadata, resource declarations,
  or validation expectations stale.

## Phase Output

Return the files changed, lifecycle phases kept or deleted, resource declaration
changes, and validation checkpoints that remain for review.
