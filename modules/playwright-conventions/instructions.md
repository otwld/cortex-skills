
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

- Playwright Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- Playwright Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Playwright Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Playwright Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

A Recruiter saves a Candidate search, reloads the page, and sees the saved search by
accessible name.

## Hard Stops

- Do not use Playwright Conventions without direct routing evidence or a required relation.
- Do not expand Playwright Conventions beyond its stated responsibility.
- Do not add placeholder Playwright Conventions guidance, examples, metadata, resources, or validation.
- Do not claim Playwright Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- Playwright Conventions trigger evidence is explicit.
- Playwright Conventions source files, project memory, or declared resources were checked.
- Playwright Conventions workflow rules were applied at the relevant artifact boundary.
- Playwright Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Playwright Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
