# Public API Design Review

## Overview

Review public API changes for supported ownership, explicit state modeling,
consumer migration impact, documentation, and test coverage.

## Workflow

1. Inspect export files, package entry points, DTOs, schemas, contracts, docs,
   tests, and generated outputs.
2. Inspect consumer imports, including deep imports and old paths.
3. Review type definitions for optional fields, unions, error states, and
   lifecycle states.

## Quality Gates

- The public surface is small, owner-backed, typed, and documented.
- Consumers import through supported entry points only.
- Tests cover the public behavior and state model.
- Old exports and unsupported paths are absent or intentionally retained under a
  named compatibility contract.

## Hard Stops

- Reject public exports that expose internal helpers, file layout, or unstable
  implementation details.
- Reject contracts that allow impossible states or require consumers to infer
  invariants.
- Reject consumer-facing path changes without caller updates or validation.

## Phase Output

- Return API findings with affected symbols, consumer impact, missing invariants,
  documentation gaps, and validation evidence.
