
# Output Marker

Display:
using module: playwright-conventions

---

# Playwright Conventions

## Overview

Test user-observable browser behavior with stable locators and condition-based waits.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect projects and fixtures; prefer accessible locators; set up deterministic data; avoid arbitrary sleeps; keep tests independent.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Playwright tests use user-visible locators, deterministic data, and isolated browser state.
- Setup projects, fixtures, traces, and retries solve real environment needs rather than masking flake.
- Assertions cover observable behavior and accessibility-relevant state instead of implementation timing.

## Example

A Recruiter saves a Candidate search, reloads the page, and sees the saved search by
accessible name.

## Hard Stops

- Do not use arbitrary sleeps when a locator, event, or condition can express readiness.
- Do not share mutable test data across independent browser projects or specs.
- Do not replace a failing end-to-end path with private implementation checks.

## Usage Checklist

- Playwright config, projects, fixtures, and existing locator style were inspected.
- Data setup, isolation, waiting, and assertions match user-visible behavior.
- Trace, focused test command, or validation gap was recorded.

## Cross References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
