
# Output Marker

Display:
using module: code-documentation

---

# Code Documentation

## Overview

Make documentation impact part of planned code-touching work rather than a cleanup pass.

## Reference Routing

- Use `shared/skill-quality-standard.md` when this task touches that concern.
- Use `shared/recruitment-universe.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. For work that creates, edits, moves, deletes, splits, refactors, or materially reviews code, identify the documentation impact before implementation or review conclusions.
4. Document touched public or reusable surfaces; move docs with code; update Storybook or MDX where that is the docs surface; avoid placeholder comments.
5. Prefer durable artifacts, public seams, and validation evidence over local convenience.
6. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Touched public, exported, reusable, or user-facing surfaces have current JSDoc, TSDoc, Storybook, MDX, or usage notes.
- Documentation describes behavior, invariants, and consumer expectations instead of restating implementation lines.
- Examples and fixtures use the recruitment universe unless the user explicitly provides another domain.

## Example

A reusable CandidateCard documents required data, empty states, and selection behavior
instead of commenting each template line.

## Hard Stops

- Do not treat documentation as a final optional cleanup after code has changed.
- Do not add placeholder comments, generic examples, or stale docs to satisfy a checkbox.
- Do not move or split code without moving or updating its owning documentation surface.
- Do not treat conceptual code discussion with no planned code touch as documentation work.

## Usage Checklist

- Every touched public or reusable surface was checked for documentation impact.
- Docs, stories, examples, and fixtures were updated alongside the behavior they explain.
- Documentation validation or the remaining documentation gap was named.

## Cross References

- WITH: example-universe-enforcer, storybook-conventions
- AFTER: skill-evolution
