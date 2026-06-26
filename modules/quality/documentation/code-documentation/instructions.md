
# Output Marker

Display:
using module: code-documentation

---

# Code Documentation

## Overview

Make documentation coverage part of every code-touching task and treat public
documentation as part of the contract, not as cleanup.

## Reference Routing

- Use `references/coverage-and-comments.md` whenever code is created, edited,
  moved, deleted, split, refactored, or materially reviewed.
- Use `shared/skill-quality-standard.md` when this task touches that concern.
- Use `shared/recruitment-universe.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Before implementation or review conclusions, load `references/coverage-and-comments.md` and list the touched public, exported, reusable, user-facing, and dense-logic documentation surfaces.
4. Update the nearest owning JSDoc, TSDoc, README, Storybook, MDX, generated-doc, fixture, example, or usage-note surface in the same change as the behavior.
5. Add concise `//` block-level comments inside dense functions when phases, invariants, ordering, lifecycle, error recovery, caching, concurrency, or performance choices are not obvious.
6. Move or delete stale documentation with moved, split, renamed, or deleted code so obsolete contracts stop being reachable.
7. Prefer durable artifacts, public seams, and validation evidence over local convenience.
8. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Touched public, exported, reusable, framework-bound, or user-facing surfaces have current JSDoc, TSDoc, Storybook, MDX, generated docs, examples, fixtures, or usage notes.
- Documentation describes responsibility, supported states, invariants, constraints, lifecycle, failure modes, side effects, and consumer expectations instead of restating implementation lines.
- Dense functions have phase or invariant comments where extraction would not be clearer.
- Stale docs, examples, stories, fixtures, and comments are updated or removed with the code they describe.
- Examples and fixtures use the recruitment universe unless the user explicitly provides another domain.

## Example

A reusable CandidateCard documents required data, empty states, and selection behavior
instead of commenting each template line. A long Application ranking function uses
short line comments to mark normalization, eligibility filtering, scoring, and
tie-break phases when those phases must stay together.

## Hard Stops

- Do not treat documentation as a final optional cleanup after code has changed.
- Do not accept undocumented touched public surfaces without naming the remaining gap and blocker.
- Do not add placeholder comments, syntax narration, generic examples, or stale docs to satisfy a checkbox.
- Do not leave dense logic without phase comments when a maintainer must infer non-obvious intent from control flow.
- Do not move or split code without moving or updating its owning documentation surface.
- Do not treat conceptual code discussion with no planned code touch as documentation work.

## Usage Checklist

- `references/coverage-and-comments.md` was used for code-touching work or material review.
- Every touched public, exported, reusable, framework-bound, or user-facing surface was checked for documentation impact.
- Docs, stories, examples, and fixtures were updated alongside the behavior they explain.
- Dense functions were checked for phase, invariant, and reasoning comments.
- Documentation validation or each remaining documentation gap was named.

## Cross References

- Reference: `references/coverage-and-comments.md`
- WITH: example-universe-enforcer, storybook-conventions
- AFTER: skill-evolution
