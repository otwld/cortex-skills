# Code Documentation Run

## Overview

Keep documentation and comments synchronized while code is being changed.

## Workflow

1. For each touched file, list the public, exported, reusable, user-facing, or
   dense private surfaces affected by the change.
2. Update the nearest owning JSDoc, TSDoc, README, MDX, Storybook, generated doc,
   fixture, payload sample, or usage note in the same change as the behavior.
3. Move or remove stale documentation when code is moved, split, renamed, or
   deleted.
4. Add short block-level comments only where they preserve non-obvious intent,
   invariants, ordering, lifecycle timing, caching, concurrency, retries,
   pagination, error recovery, or failure semantics.
5. When no documentation edit is needed, record the specific reason: private
   self-evident change, docs already current, or no consumer-visible behavior.

## Quality Gates

- Touched public and reusable surfaces answer what the surface owns, how callers
  use it, relevant constraints, side effects, and failure modes.
- Dense logic comments explain phases or invariants instead of restating syntax.
- Examples, fixtures, stories, and payload samples still describe the behavior
  being implemented.
- Deleted or renamed code has no reachable stale docs that describe the old path.

## Hard Stops

- Do not add placeholder comments or line-by-line narration to satisfy coverage.
- Do not leave a touched public surface undocumented without an explicit blocker.
- Do not move, split, or rename code while leaving its owning documentation behind.

## Phase Output

- Return the documentation surfaces changed, comments added or rejected, stale
  docs removed, and any remaining documentation gap with its blocker.
