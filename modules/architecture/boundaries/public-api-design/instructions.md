
# Output Marker

Display:
using module: public-api-design

---

# Public API Design

## Overview

Keep public surfaces explicit, small, stable, typed, and documented as contracts.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Choose owner first; export supported symbols only; encode states with strong types; document invariants and migration impact.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- The owning package or module is chosen before exports, DTOs, contracts, or import paths are added.
- Public symbols encode supported states and invariants with explicit types and documentation.
- Migration impact is named when changing exports, entry points, or shared contracts.

## Example

ApplicationReviewResult with accepted and rejected variants is clearer than optional
rejectionReason on every result.

## Hard Stops

- Do not export implementation details because another file currently wants them.
- Do not use optional-field state bags where a discriminated contract would describe valid states.
- Do not change public import paths without naming consumers and migration validation.

## Usage Checklist

- Owner, consumers, exports, and entry points were inspected before API design.
- States, invariants, naming, and documentation are explicit in the public surface.
- Consumer updates, migration notes, and validation were included or ruled out.

## Cross References

- BEFORE: library-placement-decision
- WITH: naming-consistency, typescript-api-conventions, code-documentation
