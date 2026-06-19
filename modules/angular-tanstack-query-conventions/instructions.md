
# Output Marker

Display:
using module: angular-tanstack-query-conventions

---

# Angular TanStack Query Conventions

## Overview

Treat query integration as a cache identity and data-contract concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Keys include every variable that changes data; skippable inputs are explicit; mutations name cache impact; pagination belongs in keys.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Query keys include every variable that changes the server result or cache partition.
- Skippable inputs, pagination, mutation side effects, and invalidation rules are explicit.
- Observable and Angular boundaries keep query state consumption predictable for components.

## Example

Candidate search includes companyId, jobOfferId, filters, and page in the key because
each changes results.

## Hard Stops

- Do not reuse a query key across different inputs or authorization-sensitive result sets.
- Do not hide disabled-query behavior inside nullable values without a clear skip condition.
- Do not mutate cache state without naming the affected queries and UI states.

## Usage Checklist

- Query key shape was checked against all data-changing inputs.
- Skip, pagination, mutation, and cache invalidation behavior were specified.
- Component consumption and public API effects were reviewed together.

## Cross References

- BEFORE: angular-conventions
- WITH: rxjs-conventions, typescript-api-conventions, public-api-design, code-documentation
- AFTER: skill-evolution
