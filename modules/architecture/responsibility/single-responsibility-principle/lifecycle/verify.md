# Single Responsibility Principle Verify

## Overview

Verify that final touched code units have one clear reason to change or an
explicit deferred boundary risk.

## Workflow

1. Re-read the final touched files, functions, methods, classes, components,
   hooks, services, controllers, commands, providers, schemas, and modules.
2. Confirm each touched unit has one responsibility sentence or a documented
   reason it remains cohesive.
3. Confirm any split removed independent change drivers without creating
   pass-through wrappers or caller-coordinated internals.
4. Confirm remaining mixed concerns share one use case, actor, lifecycle, or
   owner.
5. Record validation commands, tests, static inspection, or blockers that cover
   the SRP risk.

## Quality Gates

- Verification names the touched units checked and their responsibility outcome.
- No known independent change driver remains mixed without a blocker or follow-up
  owner.
- Validation evidence matches the behavior or boundary affected by the change.

## Hard Stops

- Do not claim SRP verification from tests alone when the responsibility boundary
  was not inspected.
- Do not leave a split half-applied with old mixed callers still wired.
- Do not hide unresolved reusable abstraction, package placement, or public API
  decisions inside an SRP pass.

## Phase Output

- Return verified units, keep/split outcomes, validation evidence, unresolved
  SRP risks, and any required follow-up owner.

