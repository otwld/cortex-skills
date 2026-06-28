# Implementation Plan Plan

## Overview

Write a plan that is executable from the current repository state. Each task must
name its objective, affected surface, expected change, validation evidence, and
handoff condition. The plan begins from the activation intent model so module
responsibilities, inferred requirements, validation needs, and excluded scope are
settled before task sequencing.

## Workflow

1. Copy or summarize the activation intent model: explicit and inferred intent,
   operation type, affected surfaces, expected artifacts, risk profile,
   validation needs, excluded scope, activated modules, and missing coverage.
2. State goal and non-goals.
3. Summarize current-state evidence and affected surfaces.
4. Name which module responsibilities govern the plan and where coverage is
   missing or intentionally out of scope.
5. Order tasks or vertical slices.
6. Name interface, data, migration, compatibility, docs, and generated-output
   impact.
7. Build a validation matrix listing command, scope, and when it should run.
8. Record risks, assumptions, rollback notes, and follow-up notes.

## Quality Gates

- A task changes one coherent behavior or contract; it is not merely "update
  backend" or "add UI" when a vertical slice is possible.
- Derived intent, affected surfaces, validation needs, and module
  responsibilities appear before task sequencing.
- Tests, docs, generated outputs, and migration work stay in the same task as the
  behavior they govern.
- A task does not ask the implementer to choose product behavior, API names,
  ownership, or validation strategy.
- Validation is concrete: command name, expected evidence, or explicit reason no
  command applies.

## Hard Stops

- Any task contains "decide", "figure out", or "choose" for a requirement that
  should already be settled.
- Compatibility or migration risk is hidden inside a generic refactor task.
- Public API, user-facing behavior, docs, or generated outputs are affected but
  absent from the plan.
- The plan cannot be checked by another engineer without returning to the user
  for core decisions.

## Phase Output

Return:

- Decision-complete implementation plan.
- Derived intent summary, affected surfaces, validation needs, activated module
  responsibilities, and missing coverage.
- Validation matrix and docs/generated-output checklist.
- Explicit assumptions and non-goals.
- Residual risks and user decisions, if any remain.
