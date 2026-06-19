
# Output Marker

Display:
using module: extraction-decision

---

# Extraction Decision

## Overview

Decide whether duplication is stable enough to extract, and whether extraction improves
ownership, leverage, and locality.

## Reference Routing

- Use `shared/architecture-deepening.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inventory consumers; separate stable behavior from coincidental shape; choose owner before API; preserve dependency direction.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Extraction candidates are based on stable shared behavior, not coincidental shape or two similar files.
- Ownership, dependency direction, and public API surface are decided before moving code.
- The extraction reduces duplication or responsibility spread without creating a shallow utility module.

## Example

Three Application status mappers with identical business rules may become one domain
mapper; similar Candidate cards may remain local if behavior differs.

## Hard Stops

- Do not extract just because code is repeated once or names look similar.
- Do not create shared/common/helper modules before identifying an owner and consumers.
- Do not invert dependency direction to make extraction convenient.

## Usage Checklist

- Consumers, duplicated behavior, and variation points were inventoried.
- Owner, API, and dependency direction were chosen before extraction.
- Extraction recommendation names code to move, keep local, or delete.

## Cross References

- BEFORE: library-placement-decision, nx-module-boundaries
- WITH: public-api-design, naming-consistency, bundle-performance, code-documentation
- AFTER: skill-evolution
