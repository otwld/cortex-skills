# Playwright Conventions Activate

## Overview

Confirm that the task belongs to a Playwright browser-test surface and capture
the evidence needed to choose locators, data setup, browser projects, waiting
conditions, and validation scope.

## Workflow

### Evidence To Inspect

- `playwright.config.*`, package scripts, project names, `testDir`, `use`
  options, `webServer`, retries, trace, screenshot, video, and reporter config.
- Existing setup projects, storage state files, authentication helpers,
  fixtures, page objects, and browser project dependencies.
- Nearby tests for locator strategy, assertion style, fixture boundaries, data
  setup, teardown, and project selection.
- The user-observable workflow being protected, including the page route,
  accessible names, form labels, visible status text, persisted browser state,
  and expected network or navigation effects.
- CI constraints such as browser installation, base URL, seeded data, service
  startup, and report artifact collection.

### Decisions

- Treat a test as Playwright-owned only when config, scripts, imports, or file
  matching show it runs through Playwright Test.
- Prefer locators based on user-facing contracts: role, label, text, placeholder,
  alt text, title, or an intentional test id. Use CSS or XPath only when that is
  the maintained contract for the surface.
- Define readiness as an observable condition: URL, locator state, network
  completion exposed through UI, navigation, dialog, download, or async
  assertion. Avoid timer sleeps as readiness proof.
- Scope data and browser state to the smallest reliable unit: test, worker,
  setup project, or browser project. Shared state requires explicit isolation
  and cleanup evidence.
- Select only the browser projects affected by the behavior unless config or
  compatibility changes require a wider matrix.

## Quality Gates

- Activation names concrete Playwright config, script, import, or file matching
  evidence.
- The selected workflow has a user-observable browser outcome and an accessible
  or intentional locator contract.
- Data setup, storage state, browser project scope, and readiness condition are
  explicit enough to review.
- The phase output includes a focused browser-project validation path or an
  explicit reason one cannot be selected yet.

## Hard Stops

- No repository evidence proves the affected spec or config runs under
  Playwright Test.
- The proposed test cannot identify a user-observable browser outcome.
- The workflow depends on mutable shared data, reused authentication state, or
  external services without a reset or isolation plan.
- The only readiness mechanism is a fixed wait, arbitrary timeout increase, or
  blind retry.

## Phase Output

- Report the Playwright config or script evidence, affected specs, browser
  projects, locator contract, data isolation plan, readiness condition, and
  likely focused validation command.
