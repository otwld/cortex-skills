# Playwright Conventions Run

## Overview

Implement Playwright tests and configuration that exercise user-observable
browser behavior through stable locators, deterministic data, and condition-based
assertions.

## Workflow

- Start each spec from the user workflow: navigation, interaction, persisted
  state, visible result, download, dialog, or route transition. Keep private
  implementation checks out of the browser test.
- Use locator APIs that reflect how a user or accessibility tree identifies the
  element. Chain and filter locators to narrow scope instead of reaching into
  DOM structure.
- Use Playwright's auto-waiting actions and async locator assertions for
  readiness. Replace fixed sleeps with an assertion on visible state, URL, event,
  request outcome, or disabled/enabled state.
- Create or reset data through fixtures, setup projects, API helpers, or
  repository-provided test utilities. The test should not depend on data created
  by another independent spec.
- Encapsulate repeated setup and teardown in fixtures when multiple tests need
  the behavior. Keep one-off setup in the spec so the workflow remains readable.
- Use storage state deliberately. Name the actor, scope it to the browser
  project or worker that owns it, and avoid mutating a shared authenticated
  session across tests.
- For authenticated suites, prefer a setup project that writes storage state and
  make dependent browser projects consume that file explicitly.
- Keep configuration concerns in the right place: runner options at top level,
  browser context options in `use`, and project-specific overrides in the
  matching project entry.
- Use retries, trace, screenshots, and video as diagnostic evidence. Do not use
  them to make an unstable test acceptable without fixing the cause.
- For recruitment-domain examples, assert user-visible behavior such as a
  Recruiter saving a Candidate search or seeing a submitted Application status.

## Quality Gates

- The spec asserts a final browser-observable state through Playwright
  assertions, not only an attempted action.
- Locators use user-facing or intentional contracts and avoid brittle DOM
  structure unless no better contract exists.
- Test data, storage state, downloads, and generated records are isolated to the
  smallest reliable scope.
- Config changes exercise the intended browser project and preserve CI evidence
  such as traces or reports for failures.

## Hard Stops

- Do not replace a browser workflow with direct component, service, or database
  assertions when the task is to protect end-to-end behavior.
- Do not add broad timeouts, unconditional waits, or retry-only fixes for flake.
- Do not share mutable accounts, records, storage state, or downloaded files
  across independent specs without isolation.
- Do not leave `test.only`, debug pauses, headed-only assumptions, or local URLs
  that bypass repository config.

## Phase Output

- Summarize changed specs/config, user workflow covered, locator strategy,
  readiness conditions, data isolation, browser projects affected, and validation
  command.
