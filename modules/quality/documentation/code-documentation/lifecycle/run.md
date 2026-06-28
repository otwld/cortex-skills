# Code Documentation Run

## Overview

Keep documentation and comments synchronized while code is being changed.

## Workflow

1. For each touched file, list the public, exported, reusable, user-facing,
   structural, behavioral, or dense private surfaces affected by the change.
2. Update the nearest owning JSDoc, TSDoc, README, MDX, Storybook, generated doc,
   fixture, payload sample, or usage note in the same change as the behavior.
3. Document touched interfaces, type members, properties, schema fields, DTO
   fields, config fields, component contracts, public methods, and public or
   reusable functions at the member or nearest owning surface.
4. Document touched named functions and methods with more than five body lines
   even when private; use the nearest owning surface only when the language
   cannot attach documentation directly.
5. Move or remove stale documentation when code is moved, split, renamed, or
   deleted.
6. Add short flow comments in long or dense functions where they preserve
   non-obvious phases, invariants, ordering, lifecycle timing, caching,
   concurrency, retries, pagination, transactions, error recovery, side effects,
   or failure semantics.
7. When no documentation edit is needed, record the specific reason: private
   short self-evident change, docs already current, or no consumer-visible
   behavior.

## Quality Gates

- Touched public and reusable surfaces answer what the surface owns, how callers
  use it, relevant constraints, side effects, and failure modes.
- Touched interfaces, type members, properties, fields, component contracts,
  schemas, DTOs, config options, functions, and methods meet the documentation
  standard in `references/coverage-and-comments.md`.
- Dense and long logic comments explain phases, flow, or invariants instead of
  restating syntax.
- Examples, fixtures, stories, and payload samples still describe the behavior
  being implemented.
- Deleted or renamed code has no reachable stale docs that describe the old path.

## Hard Stops

- Do not add placeholder comments or line-by-line narration to satisfy coverage.
- Do not leave a touched public surface undocumented without an explicit blocker.
- Do not leave a touched named function or method over five body lines
  undocumented.
- Do not move, split, or rename code while leaving its owning documentation behind.

## Phase Output

- Return the documentation surfaces changed, comments added or rejected, stale
  docs removed, and any remaining documentation gap with its blocker.
