---
name: public-api-design
description: Use when adding or changing exports, shared contracts, DTOs, reusable abstractions, entry points, package boundaries, or import paths.
---

# Output Marker

Display:
using skill: public-api-design

---

# Public API Design

## Overview

Treat reusable package exports as contracts. Keep public surfaces explicit,
stable, minimal, typed, and intentionally documented by names and structure.

## Export Rules

Prefer:

- Explicit exports of supported symbols.
- Narrow entry points with clear ownership.
- Type-only exports for type-only symbols.
- Stable import paths that do not expose internals.

Avoid:

- Broad barrels that accidentally export implementation details.
- Deep imports as the primary usage path.
- Re-exporting third-party APIs unless that is a deliberate wrapper contract.
- Public types that expose private or framework-specific internals.

## Contract Rules

- DTOs and shared contracts must have clear domain ownership.
- Avoid optional fields that hide separate contract variants.
- Prefer discriminated unions over ad-hoc flags when states differ.
- Shared contracts must not depend on UI or application-only concerns.
- Breaking changes need an explicit migration path.

## Hard Stops

Stop and propose a corrected surface when:

- Internal types leak into exports.
- Consumers need deep imports to use supported behavior.
- A shared contract mixes application-specific fields into reusable API.
- A public API is weakly typed to avoid fixing the model.

## Usage Checklist

- Supported import paths are clear.
- Exports are minimal and intentional.
- Public types are stable and do not leak internals.
- Breaking-change impact is identified.
- Migration notes exist when compatibility changes.

## Cross-References

- BEFORE: library-placement-decision
- WITH: naming-consistency, typescript-api-conventions, code-documentation
