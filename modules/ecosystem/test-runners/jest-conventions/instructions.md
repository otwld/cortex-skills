
# Output Marker

Display:
using module: jest-conventions

---

# Jest Conventions

## Overview

Use Jest to prove behavior through stable seams with minimal boundary mocks.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect config; choose public seam; use deterministic fixtures; mock true boundaries; keep setup small; add matchers only for clarity.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Jest tests exercise the highest meaningful public seam with deterministic fixtures and assertions.
- Mocks replace real boundaries, not internal implementation details that should be tested directly.
- Config, setup files, custom matchers, and environments stay small and justified by repeated need.

## Example

Test that a Candidate retrieves submitted Applications through a public service instead
of asserting a repository call.

## Hard Stops

- Do not add Jest mocks that freeze private implementation structure.
- Do not put one-test convenience into global setup or custom matchers.
- Do not mix Jest assumptions into Vitest or Playwright files without direct evidence.

## Usage Checklist

- Jest config, setup, environment, and existing test style were inspected.
- Public seam, fixture determinism, and boundary mocks were chosen deliberately.
- Focused Jest command or validation gap was recorded.

## Cross References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
