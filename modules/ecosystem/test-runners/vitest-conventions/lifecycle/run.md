# Vitest Conventions Run

## Overview

Implement Vitest tests and runner changes that stay aligned with Vite, exercise
public behavior, and leave no mock, timer, env, or global state behind.

## Workflow

- Put Vitest options under the `test` config. When a separate `vitest.config.*`
  is needed, preserve required Vite aliases, plugins, mode behavior, and
  transforms through the repository's established merge pattern.
- Match the repository's API style. If globals are disabled, import `test`,
  `expect`, `vi`, and hooks from `vitest`; if globals are enabled, ensure
  TypeScript types and cleanup behavior match the config.
- Use the environment that matches the code. Do not run DOM-dependent behavior in
  a pure Node environment, and do not add DOM environments to pure logic tests
  without a concrete need.
- Prefer real modules and public contracts. Use `vi.fn`, `vi.spyOn`, `vi.mock`,
  or `vi.doMock` for external boundaries, clocks, env variables, globals, and
  adapters that would make the test nondeterministic or slow.
- Keep `vi.mock` in test files or deliberate test support files. Account for
  hoisting, direct `vi` imports, static imports, and the fact that modules loaded
  by setup files may already be cached.
- Use `vi.doMock` only when non-hoisted dynamic-import behavior is required and
  the import order is explicit in the test.
- Restore `vi.useFakeTimers`, `vi.setSystemTime`, `vi.stubEnv`,
  `vi.stubGlobal`, spies, and module mocks in cleanup hooks or enabled reset
  config.
- Keep setup files small. Use them for repeated matcher registration, test
  library cleanup, and deterministic environment setup, not for per-test data.
- For recruitment-domain examples, express behavior through public concepts such
  as JobOffer ranking, Candidate filters, Application status, or Recruiter
  workflows.

## Quality Gates

- Adding or changing `setupFiles` must include evidence that the code can safely
  run in every matching test file and process.
- Changing `globals`, `environment`, `isolate`, pools, or workspace projects must
  identify the affected files and the cleanup or type changes required.
- Changes involving `import.meta.env` must reset values or enable the
  repository-supported unstub/reset behavior.
- Changes involving fake timers or system time must restore real timers and
  avoid leaking the mocked date into other tests.

## Hard Stops

- Do not copy another runner's globals, setup behavior, or mocking assumptions
  into Vitest without config evidence.
- Do not mock modules that should be exercised through their public contract.
- Do not disable isolation or force single-worker behavior as a substitute for
  cleaning shared state.
- Do not leave watch-only behavior, focused tests, or skipped tests behind.

## Phase Output

- Summarize changed tests/config, Vite integration points, selected environment,
  public behavior covered, mock/timer/env/global cleanup, and focused validation
  command.
