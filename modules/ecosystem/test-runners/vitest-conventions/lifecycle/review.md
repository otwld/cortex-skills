# Vitest Conventions Review

## Overview

Review Vitest changes for Vite alignment, behavioral coverage, correct
environment choice, safe mocking, and isolation. Findings should identify exact
tests, config entries, setup files, or `vi.*` calls.

## Workflow

- Runner ownership is proven through Vitest config, script, imports, globals, or
  file inclusion.
- Vite integration is preserved. Aliases, plugins, transforms, mode behavior,
  and `import.meta.env` assumptions still match how the code runs in tests.
- Environment selection matches the behavior. DOM APIs, browser APIs, and pure
  Node logic are not blurred together for convenience.
- Assertions prove public behavior rather than private call graphs. Spies and
  mocks are used only where indirect calls are part of the contract or boundary.
- Module mocks account for hoisting, static imports, direct `vi` imports, setup
  file caching, and dynamic import order.
- Fake timers, system time, env stubs, global stubs, spies, and module mocks are
  restored or reset by config.
- Setup files have repeated value and do not create hidden per-test data,
  expensive worker work, or shared mutable state.
- Isolation, pool, sequence, and workspace changes are justified by behavior and
  not used to hide test order dependence.

## Quality Gates

- A mock that cannot affect the code path because the module was already cached
  or statically imported.
- A separate config that drops Vite aliases or plugins needed by tests.
- DOM tests that pass only because globals are incidentally available, not
  because the environment is configured.
- A fake timer, stubbed env value, or global mutation that leaks into later
  tests.
- A test whose pass/fail result changes based on file order, worker reuse, or
  disabled isolation.

## Hard Stops

- Do not approve a Vitest change that lacks runner evidence for the affected file
  or config path.
- Do not accept a mock whose import order, hoisting behavior, or setup-file cache
  interaction is unknown.
- Do not accept shared setup, globals, timers, env, isolation, or Vite config
  changes without validation covering an affected consumer.

## Phase Output

- Report findings by severity with file references, the violated Vitest
  convention, required evidence or fix, and validation still needed.
