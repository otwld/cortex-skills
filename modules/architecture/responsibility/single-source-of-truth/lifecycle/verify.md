# Single Source Of Truth Verify

## Overview

Verify that touched information now has one authoritative owner and that all
remaining duplication is bounded, generated, synchronized, or intentionally
read-only.

## Workflow

1. Re-scan touched files and related consumers for copied constants, defaults,
   field lists, schemas, validators, permissions, calculations, and business
   rules.
2. Confirm mutable state has one owner and that consumers read, subscribe,
   derive, or dispatch through that owner.
3. Confirm generated artifacts, docs, examples, and fixtures were updated from
   or aligned with the authoritative source.
4. Confirm allowed caches, projections, snapshots, migration bridges, and
   compatibility layers have clear regeneration, invalidation, synchronization,
   or removal behavior.
5. Run the relevant project validation for the touched surfaces and include any
   residual drift risk in the final phase output.

## Quality Gates

- Every touched fact or rule has a named owner.
- Every consumer either references the owner or has a justified exception.
- No stale generated or documentation artifact contradicts the owner.

## Hard Stops

- Do not mark verification complete if a touched rule still has two writable
  owners.
- Do not accept manually synchronized duplication without a concrete check,
  generation command, invalidation path, or bounded removal plan.
- Do not skip generated artifact freshness when metadata or generated sources
  changed.

## Phase Output

- Return verification result, owner and consumer summary, remaining exceptions,
  validation commands run, and unresolved drift risks.
