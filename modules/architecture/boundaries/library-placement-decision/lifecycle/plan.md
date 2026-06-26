# Library Placement Decision Plan

## Overview

Plan code placement by owner responsibility, consumer scope, and dependency
direction rather than folder convenience.

## Workflow

1. Name the behavior or contract in one sentence.
2. Identify the smallest current owner that can own that behavior for all known
   consumers.
3. Choose one placement outcome: keep local, move to an existing owner, create an
   owned library, or split mixed responsibilities.
4. Define the public surface that consumers may import.
5. Name the tests, docs, exports, and boundary checks affected by the move.

## Quality Gates

- The selected location has a named domain, integration, feature, UI, adapter,
  utility, or test-support owner.
- The plan rejects locations that would invert dependency direction or expose
  private implementation details.
- Validation includes import searches or boundary checks for affected consumers.

## Hard Stops

- Do not create a new library when an existing owner already fits.
- Do not move feature-specific UI, orchestration, or fixtures into a shared
  surface because they look reusable.
- Do not leave mixed responsibilities in one package; split them or keep them
  local.

## Phase Output

- Return the selected location, rejected locations, ownership rationale, files to
  move or keep local, exports to add or remove, and validation required.
