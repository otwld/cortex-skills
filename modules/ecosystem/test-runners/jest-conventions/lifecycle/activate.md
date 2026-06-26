# Jest Conventions Activate

## Overview

Confirm that the work is actually on a Jest-run surface, then capture the
runner facts that constrain implementation and review. Activation should end
with enough evidence to choose the test seam, environment, mock boundary, and
validation command.

## Workflow

### Evidence To Inspect

- `package.json` scripts, dependency declarations, and any workspace runner that
  invokes `jest`.
- `jest.config.*`, package-level Jest config, project entries, `testMatch`,
  `testRegex`, transforms, `moduleNameMapper`, and selected `testEnvironment`.
- Existing setup files, `setupFilesAfterEnv`, custom matchers, environment
  classes, fixture helpers, and `__mocks__` directories.
- Nearby tests that prove the local naming, import, assertion, async, timer, and
  mock style.
- The code under test's public entry point, externally observable behavior, and
  real integration boundaries such as file systems, clocks, network clients,
  queues, databases, or framework adapters.

### Decisions

- Treat a file as Jest-owned only when config, scripts, imports, globals, or
  path inclusion prove it runs under Jest.
- Choose the highest meaningful public seam available: exported function,
  service method, adapter contract, command behavior, or rendered output. Do not
  start from private helpers unless that is the published contract.
- Select the environment from the behavior under test. Pure logic belongs in a
  Node-like environment; DOM behavior needs the configured DOM environment.
- Mock true boundaries and costly nondeterminism. Prefer real collaborators
  inside the same behavioral unit.
- Change global setup, custom matchers, or environment files only when repeated
  tests need the behavior and the change is safe for the whole configured Jest
  project.

## Quality Gates

- Activation names concrete Jest config, script, import, global API, or file
  matching evidence.
- The selected public seam and mock boundary are tied to observable behavior, not
  private implementation convenience.
- Any setup, matcher, environment, or config concern is scoped to repeated runner
  value rather than a single test.
- The phase output includes a focused validation path or an explicit reason one
  cannot be selected yet.

## Hard Stops

- No repository evidence proves that the affected test or config is run by
  Jest.
- The requested mock would freeze private implementation structure instead of
  replacing an external dependency.
- A global setup, matcher, environment, or config change exists only to support a
  single local test case.
- The test requires nondeterministic wall-clock time, random data, real network
  access, or shared mutable state without an explicit control plan.

## Phase Output

- Report the Jest config or script evidence, affected test files, selected
  environment, public seam, intended mock boundaries, and the likely focused
  validation command.
