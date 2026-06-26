# Jest Conventions Verify

## Overview

Define the evidence required to treat Jest work as verified. Prefer focused
commands that exercise the affected config path, then widen only when config,
setup, environment, or shared matcher behavior changed.

## Workflow

- Use the repository's package manager and existing script first. If no script
  exists, use the local Jest binary through the package manager.
- For test-only changes, run the affected files or project slice, such as
  `jest --runTestsByPath <file>` or the repository's equivalent script args.
- For config, setup, environment, transform, matcher, or manual mock changes,
  run at least one focused affected test and enough neighboring tests to prove
  the shared runner behavior did not regress.
- For project-level config changes, inspect the resolved config or list the
  matched files when the repository provides a reliable command for that.
- Record skipped validation explicitly when dependencies, generated artifacts,
  browsers, services, or credentials are unavailable.

## Quality Gates

- Command, working directory, package manager, and relevant config or project
  selection.
- Affected test files and whether they passed, failed, were skipped, or could
  not run.
- For failures, the first actionable failure cause: assertion mismatch,
  environment mismatch, unresolved transform/alias, leaked timer/mock/global, or
  missing external service.
- Any widened command needed because shared Jest setup or config changed.

## Hard Stops

- Do not call Jest work verified from static review alone when runnable tests
  exist.
- Do not treat snapshot updates as validation unless a behavioral assertion or
  review explains the intended output change.
- Do not hide failing neighboring tests introduced by shared setup or config
  changes.

## Phase Output

- Return the exact validation commands, results, residual gaps, and any follow-up
  needed for failures outside the edited Jest surface.
