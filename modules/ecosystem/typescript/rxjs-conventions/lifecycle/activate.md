# RxJS Conventions Activate

## Overview

Use this phase when the task creates, modifies, or reviews observable stream
behavior. The trigger is time-dependent RxJS behavior, not ordinary async code
that happens to live in TypeScript.

## Workflow

1. Inspect the request, diff, and imports for `rxjs`, `rxjs/operators`,
   `Observable`, `Subject`, `BehaviorSubject`, `ReplaySubject`, `Subscription`,
   `pipe`, `subscribe`, and flattening or multicasting operators.
2. Identify the stream boundary: source, owner, subscribers, lifetime, exposed
   API, and framework disposal mechanism.
3. Name the behavior under design or review: ordering, cancellation,
   concurrency, retry, error propagation, completion, caching, sharing, or
   teardown.
4. Check whether the change exposes mutation paths such as subjects or manual
   subscriptions to consumers.
5. Identify validation that can observe stream behavior: marble tests, fake
   timers, focused unit tests, integration tests, or cleanup assertions.

## Quality Gates

- Activation names the observable source, owner, and subscriber context.
- The phase identifies the specific time or lifecycle behavior that could fail.
- Manual subscriptions, subjects, and multicasting are treated as ownership
  decisions, not incidental implementation details.
- Expected validation is observable in tests or a stated review gap.

## Hard Stops

- Do not activate for a promise or callback change unless it is converted to or
  consumed by an RxJS stream.
- Do not treat every `$`-suffixed variable as RxJS without confirming the type
  or import context.
- Do not assume a subscription is short-lived without locating its disposal
  owner.
- Do not expand the task into general framework state management unless the
  observable boundary is being changed.

## Phase Output

Return the activation decision, stream boundary, time or lifecycle behavior at
risk, subject or subscription ownership facts, and validation evidence required.
