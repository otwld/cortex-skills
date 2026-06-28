# Minimize Cognitive Load Verify

## Overview

Verify that the final touched code is obvious, predictable, cohesive, explicit,
and reviewable without hiding necessary complexity.

## Workflow

1. Re-read the touched behavior as a future maintainer: identify intent, inputs,
   outputs, dependencies, state changes, side effects, and failure paths.
2. Confirm control flow is shallow enough to follow and that any branching,
   recursion, callback, async sequence, or lifecycle hook has a clear reason.
3. Confirm data flow stays local or explicitly connected, without needless
   helper, service, utility, manager, factory, or abstraction hops.
4. Confirm new files, exports, interfaces, parameters, options, and extension
   points are necessary for the current behavior.
5. Confirm the diff is reviewable: functional changes are not buried under
   unrelated formatting, moves, renames, or broad cleanup.

## Quality Gates

- A maintainer can explain the changed behavior without chasing unrelated files.
- Remaining complexity is justified by correctness, an external contract,
  framework requirement, or measured performance.
- Validation commands appropriate to the touched code have been run or a reason
  for skipping them is recorded.

## Hard Stops

- Do not mark verification complete when the implementation hides data flow or
  side effects behind unnecessary indirection.
- Do not accept speculative public surface or extension points.
- Do not claim reviewability when unrelated churn obscures the behavior.

## Phase Output

- Return verification result, reader-path summary, retained complexity,
  validation commands run, skipped checks, and unresolved cognitive-load risks.
