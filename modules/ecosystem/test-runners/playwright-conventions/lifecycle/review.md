# Playwright Conventions Review

## Overview

Review Playwright changes for browser-observable coverage, locator durability,
data isolation, and diagnostic validation. Findings should identify the exact
spec, locator, fixture, config option, or assertion at risk.

## Workflow

- Runner ownership is proven through Playwright config, script, imports, or file
  inclusion.
- The test protects a user-visible workflow and asserts the final observable
  state, not only an internal request, class name, or implementation timing.
- Locators prioritize accessible or intentional user-facing contracts. CSS,
  XPath, index-based selection, and brittle text fragments require a documented
  reason.
- Actions and assertions use Playwright waiting semantics. Fixed waits,
  unconditional timeout increases, and manual polling are justified only when no
  observable condition exists.
- Data setup is deterministic and isolated. Fixtures and setup projects clean up
  their own state or create uniquely owned state.
- Browser project, device, locale, permission, storage state, trace, screenshot,
  video, and retry changes are scoped to the behavior they support.
- Failures will leave useful evidence in CI: trace, report, screenshot, video,
  console/network output, or a clear assertion mismatch.

## Quality Gates

- A locator tied to DOM hierarchy, generated class names, or ordering when a
  role, label, text, or test id contract exists.
- A test that passes only when another spec ran first or reused mutable browser
  state.
- A retry, timeout, or trace change presented as a flake fix without removing
  the underlying race.
- Assertions that check only that an action was attempted, not that the browser
  reached the expected state.
- Project matrix changes that skip a browser or device where the feature is
  expected to work.

## Hard Stops

- Do not approve a Playwright change that cannot identify the browser project or
  config path it affects.
- Do not accept fixed waits, timeout inflation, or retry-only fixes as a flake
  resolution.
- Do not accept shared mutable data or storage state without isolation and
  cleanup evidence.

## Phase Output

- Report findings by severity with file references, the violated Playwright
  convention, required evidence or fix, and validation still needed.
