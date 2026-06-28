# Single Source Of Truth Run

## Overview

Implement source-of-truth decisions by removing drift-prone copies and wiring
consumers to the chosen owner.

## Workflow

1. Replace copied constants, defaults, field lists, validation rules, policy
   checks, calculations, and schema fragments with imports, shared schema use,
   selectors, generated outputs, adapters, or owner-owned functions.
2. Collapse competing writable state so only the owner mutates the value; keep
   local UI state limited to presentation state or explicit draft state.
3. Turn stored derivations into computed values unless persistence, indexing,
   caching, or integration requirements justify a projection.
4. Update generated inputs, docs snippets, fixtures, examples, tests, and
   mapping layers so they follow the owner instead of restating business rules.
5. Document accepted exceptions near the synchronization, regeneration,
   invalidation, or migration mechanism, not as broad rationale.

## Quality Gates

- Touched consumers read, import, derive, generate, or project from the owner.
- No new copied validator, constant, config value, state value, or business rule
  is introduced without a bounded exception.
- The smallest change that removes the competing truth is preferred over a
  broad unrelated refactor.

## Hard Stops

- Do not introduce a convenience duplicate merely to reduce import distance.
- Do not let generated files or fixtures become hand-maintained policy owners.
- Do not remove compatibility duplication that is still required by a bounded
  migration without preserving the declared migration path.

## Phase Output

- Return changed owners and consumers, removed copies, accepted exceptions,
  documentation or fixture updates, and verification commands or checks.
