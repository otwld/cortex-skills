# Single Source Of Truth Plan

## Overview

Plan code changes so each touched fact has one durable owner and all other
surfaces consume, derive, generate, cache, or project from that owner.

## Workflow

1. For each touched fact or rule, choose the authoritative owner before editing:
   domain model, schema, validator, configuration source, state store, database,
   generated input, public contract, or documented source file.
2. Convert copied consumers into imports, references, selector calls,
   derivations, generator inputs, schema reuse, adapter mappings, or explicit
   read-only projections.
3. For caches, denormalized projections, generated artifacts, snapshots,
   compatibility layers, or migration bridges, define the owner, regeneration or
   invalidation path, drift detection, and removal condition when applicable.
4. Keep documentation, examples, fixtures, and generated files aligned with the
   authoritative code or schema instead of making them second policy owners.
5. Coordinate with neighboring modules when the plan also changes
   responsibility boundaries, reusable abstractions, public APIs, inheritance
   structure, transitional states, or documentation policy.

## Quality Gates

- The plan names one owner for every touched fact or rule.
- Each copied consumer has a concrete conversion path or a justified exception.
- Accepted duplication has a sync, regeneration, invalidation, or expiration
  rule.

## Hard Stops

- Do not plan two writable owners for the same fact unless the work is an
  explicit bounded migration or compatibility bridge.
- Do not make a shared constant or helper the owner when a stronger domain,
  schema, configuration, or persistence source already exists.
- Do not hide business rules inside UI, tests, fixtures, or documentation when a
  runtime owner should enforce them.

## Phase Output

- Return authoritative owner decisions, consumer conversion paths, justified
  exceptions, sync or removal rules, overlap handoffs, and verification targets.
