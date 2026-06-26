# Vitest Conventions Activate

## Overview

Confirm that the task belongs to a Vitest surface and capture the Vite, runner,
environment, mock, timer, and isolation facts that constrain the work.

## Workflow

### Evidence To Inspect

- `vitest.config.*`, `vite.config.*`, package scripts, workspace projects,
  aliases, test include/exclude patterns, and selected config file.
- `test` config for environment, globals, setup files, global setup, isolation,
  pools, sequence, coverage, browser mode, and project-specific overrides.
- Existing tests that import from `vitest`, use `vi.*`, rely on globals, or guard
  code with `import.meta.vitest`.
- Setup files and global setup files, especially imports that may be cached
  before a test tries to mock a module.
- Code under test and whether it depends on Node APIs, DOM APIs, Vite transforms,
  Vite aliases, `import.meta.env`, timers, globals, or browser behavior.

### Decisions

- Treat a file as Vitest-owned only when config, scripts, imports, globals, or
  path inclusion prove it runs under Vitest.
- Choose the environment from the behavior under test: Node for pure logic,
  configured DOM environment for component or browser-adjacent behavior, and a
  browser project only when actual browser execution is required.
- Decide whether the test should import APIs explicitly or rely on configured
  globals. Follow the repository's current Vitest style.
- Prefer real modules inside the behavioral unit. Mock external boundaries,
  nondeterministic clocks, env variables, globals, and expensive adapters.
- Plan cleanup for fake timers, stubbed env, stubbed globals, spies, module
  mocks, and mutated Vite state.

## Quality Gates

- Activation names concrete Vitest config, Vite config, script, import, global
  API, or file matching evidence.
- Environment, API style, Vite integration, and mock boundaries are selected
  from inspected repository behavior.
- Timer, env, global, module cache, and isolation risks have a cleanup or reset
  plan.
- The phase output includes a focused validation path or an explicit reason one
  cannot be selected yet.

## Hard Stops

- No repository evidence proves the affected test or config runs under Vitest.
- The intended mock targets a module that is already imported through setup-file
  caching or static imports in a way the test cannot control.
- The test depends on disabled isolation, shared worker state, wall-clock time,
  random data, or mutated `import.meta.env` without reset evidence.
- A separate Vitest config is introduced without accounting for Vite config,
  aliases, plugins, and transforms that the tests still need.

## Phase Output

- Report Vitest/Vite config evidence, affected tests, selected environment,
  API style, mock boundaries, timer/global cleanup plan, and likely focused
  validation command.
