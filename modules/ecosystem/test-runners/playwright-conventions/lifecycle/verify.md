# Playwright Conventions Verify

## Overview

Define the evidence required to treat Playwright work as verified. Browser tests
need both command results and enough artifact context to diagnose failures.

## Workflow

- Use the repository's package manager and existing Playwright script first. If
  no script exists, use the local Playwright Test binary through the package
  manager.
- For spec-only changes, run the affected spec with the relevant browser project,
  for example the repository equivalent of
  `playwright test <spec> --project=<project>`.
- For locator, fixture, setup project, authentication, storage state, or data
  isolation changes, run the affected spec and at least one neighboring workflow
  that shares the fixture or state.
- For config, project matrix, `webServer`, reporter, trace, retry, screenshot, or
  video changes, list or run the affected projects so the changed configuration
  path is exercised.
- Preserve trace, report, screenshot, video, console, or network evidence for
  failures when the repository can produce it.
- Record skipped validation explicitly when browsers, services, seed data,
  credentials, or CI-only infrastructure are unavailable.

## Quality Gates

- Command, working directory, package manager, browser project, base URL, and any
  selected config file.
- Affected specs and whether they passed, failed, were skipped, or could not run.
- For failures, the first actionable cause: locator mismatch, assertion timeout,
  navigation failure, service startup failure, data collision, browser install
  issue, or product regression.
- Artifact location for any trace, report, screenshot, or video used to diagnose
  the result.

## Hard Stops

- Do not call Playwright work verified from static review alone when the affected
  browser workflow can run.
- Do not accept a retry pass without understanding the failing attempt.
- Do not mark config or project changes verified by running a different browser
  project than the one affected.

## Phase Output

- Return the exact validation commands, browser projects, results, diagnostic
  artifacts, residual gaps, and follow-up needed for failures outside the edited
  Playwright surface.
