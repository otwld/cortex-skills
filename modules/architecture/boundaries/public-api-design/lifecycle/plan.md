# Public API Design Plan

## Overview

Plan public API changes so exported symbols are small, owner-backed, typed,
documented, and reachable only through supported entry points.

## Workflow

1. Name the owner and supported consumers.
2. Decide the minimum public symbols required by those consumers.
3. Encode valid states, invariants, and error cases in the type or schema.
4. Define the import path and reject unsupported internal paths.
5. Plan updates to callers, tests, docs, generated outputs, and examples.

## Quality Gates

- Public exports represent behavior or contracts the owner is prepared to
  support.
- DTOs and schemas preserve invariants at construction or parsing boundaries.
- Documentation is planned for new exports and changed invariants.
- Validation includes type-checking or compiling affected consumers.

## Hard Stops

- Do not use broad barrels that expose implementation structure.
- Do not add a public symbol without a current consumer or supported contract.
- Do not plan API changes without searching for old import paths and deep
  imports.

## Phase Output

- Return the owner, exported symbols, import paths, invariants, consumer updates,
  docs updates, and validation plan.
