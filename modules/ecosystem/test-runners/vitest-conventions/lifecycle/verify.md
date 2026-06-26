# Vitest Conventions Verify

## Overview

Define the evidence required to treat Vitest work as verified. Focus on the
affected test files first, then widen for config, setup, environment, mock,
timer, globals, isolation, or Vite integration changes.

## Workflow

- Use the repository's package manager and existing Vitest script first. If no
  script exists, use the local Vitest binary through the package manager.
- For test-only changes, run the affected files in non-watch mode, such as the
  repository equivalent of `vitest run <file>`.
- For config or Vite integration changes, run a command that uses the selected
  config file and exercises aliases, plugins, transforms, and environment
  options touched by the change.
- For setup files, globals, fake timers, env stubs, global stubs, module mocks,
  or isolation changes, run the affected file plus at least one neighboring file
  that shares the setup or worker context.
- For workspace or project changes, run the affected project selection rather
  than a default command that may skip the changed project.
- Record skipped validation explicitly when dependencies, generated artifacts,
  browser providers, services, or credentials are unavailable.

## Quality Gates

- Command, working directory, package manager, config file, project/workspace
  selection, and environment.
- Affected test files and whether they passed, failed, were skipped, or could
  not run.
- For failures, the first actionable cause: environment mismatch, unresolved
  Vite alias or transform, mock hoisting/import-order issue, setup-file cache
  issue, leaked timer/env/global/module state, or product behavior mismatch.
- Any widened command needed because shared Vitest config, setup, or isolation
  changed.

## Hard Stops

- Do not call Vitest work verified from static review alone when runnable tests
  exist.
- Do not accept a pass that only occurs under watch mode, disabled isolation, or
  a single worker unless that is the configured production test path.
- Do not ignore a neighboring failure introduced by shared setup, env, globals,
  or module-cache changes.

## Phase Output

- Return the exact validation commands, results, residual gaps, and follow-up
  needed for failures outside the edited Vitest surface.
