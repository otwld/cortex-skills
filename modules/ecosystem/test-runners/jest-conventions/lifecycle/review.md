# Jest Conventions Review

## Overview

Review Jest changes for behavioral coverage, runner correctness, and isolation
risks. Findings should be tied to concrete files, assertions, mocks, or config
entries.

## Workflow

- Runner ownership is proven: the test file is matched by Jest config or a Jest
  script, and imported APIs match the repository's configured style.
- Assertions protect behavior rather than implementation details. A changed
  private call graph should not break a test unless the public outcome changed.
- Mocks replace real boundaries and preserve the dependency contract. Manual
  mocks are discoverable, scoped correctly, and not silently shared across
  unrelated tests.
- Setup and matcher changes have repeated value. Global setup does not create
  hidden application state, mutate shared fixtures, or depend on test order.
- Environment selection is justified. DOM tests do not run under an unsuitable
  environment, and pure logic tests do not pay for browser-like globals without
  a reason.
- Async behavior is awaited through promises, callbacks, timers, or observable
  effects. Timers, system time, mocks, and globals are restored.
- Fixtures are deterministic, readable, and use the recruitment agency job board
  universe when examples are needed.

## Quality Gates

- Over-mocking a collaborator that should be exercised through its public
  contract.
- Assertions that only prove `jest.fn()` was called while missing the user or
  caller-visible result.
- A broad `setupFilesAfterEnv`, transform, alias, or project change that affects
  unrelated tests without validation.
- Snapshot churn that masks an intended contract change.
- Tests that pass only because of file order, shared module cache state, wall
  clock time, or random data.

## Hard Stops

- Do not approve a Jest change that lacks runner evidence for the affected file
  or config path.
- Do not accept a shared setup, matcher, environment, or config change without
  validation covering at least one affected consumer.
- Do not accept tests that rely on leaked timers, mocks, globals, module cache
  state, or external services without reset evidence.

## Phase Output

- Report findings by severity with file references, the violated Jest
  convention, required evidence or fix, and any validation that is still missing.
