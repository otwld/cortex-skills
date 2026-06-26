# RxJS Conventions Review

## Overview

Review RxJS changes for hidden subscriptions, mismatched operators, leaked
mutation paths, missing teardown, and untested time-dependent behavior.

## Workflow

1. Trace each changed stream from source to subscriber. Include subjects,
   multicasting, manual subscriptions, and framework-managed subscriptions.
2. Check flattening operators against the requirement for cancellation,
   concurrency, ordering, and ignored work.
3. Inspect side effects and terminal subscriptions for ownership, idempotence,
   cleanup, and error handling.
4. Check subject exposure. Consumers should usually receive an observable view
   rather than direct mutation methods.
5. Inspect multicasting or caching operators for lifetime behavior, duplicate
   subscription prevention, and stale-value risk.
6. Verify error handlers do not accidentally terminate shared streams, retry
   forever, or hide user-visible failures.
7. Review tests for marble coverage, fake timers, cleanup assertions, or focused
   integration behavior that proves the changed stream semantics.

## Quality Gates

- Findings cite the operator chain, subscription, subject, or stream boundary
  that creates the risk.
- Operator feedback states the observed behavior mismatch, not only a preferred
  operator name.
- Teardown findings identify the owner that should release the subscription.
- Test gaps describe the missing timing, cancellation, ordering, or error case.

## Hard Stops

- Do not approve nested subscriptions that change cancellation or error
  behavior silently.
- Do not approve unowned subjects, global event buses, or exposed mutation paths
  without an explicit API reason.
- Do not approve a long-lived stream or subscription when disposal cannot be
  located.
- Do not approve an operator change that alters ordering or cancellation without
  test evidence or a stated migration.

## Phase Output

Return findings ordered by stream risk, operator or ownership corrections
required, validation evidence reviewed, and unresolved timing or lifecycle gaps.
