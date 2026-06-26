# RxJS Conventions Run

## Overview

Implement RxJS code so stream ownership, cancellation, ordering, multicasting,
teardown, and errors are visible in the operator chain and tests.

## Workflow

1. Describe the stream in terms of source type, emission timing, hot or cold
   behavior, subscriber count, owner lifetime, and expected completion.
2. Prefer composition through `pipe` over nested subscriptions. Keep side
   effects isolated in `tap` or terminal subscription handlers where they are
   owned and testable.
3. Choose flattening operators by observable semantics:
   `switchMap` for stale-work cancellation, `mergeMap` for allowed
   concurrency, `concatMap` for ordered queueing, and `exhaustMap` for ignoring
   new work while current work is active.
4. Use subjects only when the current scope owns production of values. Expose
   read-only observable surfaces to consumers unless mutation is the explicit
   public contract.
5. Treat multicasting and caching as lifetime choices. Document whether cached
   values reset on completion, error, ref-count loss, or owner disposal when
   that behavior matters to callers.
6. Put error handling at the level that matches the recovery model. Avoid
   swallowing failures with empty streams unless the resulting user-visible
   state is intentional and tested.
7. Ensure manual subscriptions have a disposal owner. Prefer framework-managed
   subscription helpers where the project already uses them.
8. Add or update tests that prove cancellation, ordering, duplicate emission
   prevention, teardown, and error behavior for the changed stream.

## Quality Gates

- Operator choice is justified by explicit concurrency, cancellation, ordering,
  or backpressure behavior.
- Subjects and multicasted streams have a named owner and constrained mutation
  surface.
- Manual subscriptions terminate through a visible lifecycle path.
- Error handling preserves the intended stream lifetime and user-visible state.
- Tests exercise time-dependent behavior instead of only checking one emitted
  value.

## Hard Stops

- Do not nest `subscribe()` calls when an operator chain can express the flow.
- Do not add a subject as a shared event bus without a single owner and disposal
  story.
- Do not expose a subject's `next`, `error`, or `complete` methods to consumers
  unless mutation is intentionally part of the API.
- Do not leave a long-lived subscription without teardown.
- Do not use `catchError(() => EMPTY)` or equivalent silence without explaining
  and validating the resulting state.

## Phase Output

Return the stream design, operator choices and reasons, ownership and teardown
decisions, subject or multicasting constraints, tests added or updated, and any
remaining timing risks.
