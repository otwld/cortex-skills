# Single Responsibility Principle Plan

## Overview

Plan code changes so each touched unit keeps one coherent responsibility and
splits happen only when responsibilities differ.

## Workflow

1. For each touched unit, write the responsibility it should own in one sentence.
2. Decide one outcome: keep cohesive, split local responsibilities, defer with a
   named blocker, or hand off extraction, placement, public API, or deepening
   decisions to the relevant module.
3. When splitting, name the new unit responsibilities, call boundary, ownership,
   tests, docs, and caller updates.
4. When keeping code together, state why the steps serve one use case, actor, or
   lifecycle.
5. Keep validation focused on behavior through the owning unit rather than tests
   of arbitrary private fragments.

## Quality Gates

- The plan names independent reasons to change before proposing a split.
- Each planned unit has a responsibility name stronger than helper, util,
  manager, handler, or processor.
- Splits reduce responsibility mixing without creating pass-through wrappers or
  caller-coordinated internals.
- Validation covers the behavior that motivated the boundary decision.

## Hard Stops

- Do not split merely to reduce line count or increase file count.
- Do not plan a shared abstraction without current consumers and a named owner.
- Do not leave UI, validation, persistence, networking, and business policy
  coupled when they have independent change drivers.

## Phase Output

- Return keep/split/defer decisions, intended responsibilities, affected callers,
  tests, docs, overlap handoffs, and validation evidence required.

