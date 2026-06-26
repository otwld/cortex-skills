# Implementation Plan Plan

## Overview

Write a plan that is executable from the current repository state. Each task must
name its objective, affected surface, expected change, validation evidence, and
handoff condition.

## Workflow

1. State goal and non-goals.
2. Summarize current-state evidence and affected surfaces.
3. Order tasks or vertical slices.
4. Name interface, data, migration, compatibility, docs, and generated-output
   impact.
5. Build a validation matrix listing command, scope, and when it should run.
6. Record risks, assumptions, rollback notes, and follow-up notes.

## Quality Gates

- A task changes one coherent behavior or contract; it is not merely "update
  backend" or "add UI" when a vertical slice is possible.
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
- Validation matrix and docs/generated-output checklist.
- Explicit assumptions and non-goals.
- Residual risks and user decisions, if any remain.
