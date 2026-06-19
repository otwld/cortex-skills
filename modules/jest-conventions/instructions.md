
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

- Jest Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- Jest Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Jest Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Jest Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Test that a Candidate retrieves submitted Applications through a public service instead
of asserting a repository call.

## Hard Stops

- Do not use Jest Conventions without direct routing evidence or a required relation.
- Do not expand Jest Conventions beyond its stated responsibility.
- Do not add placeholder Jest Conventions guidance, examples, metadata, resources, or validation.
- Do not claim Jest Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- Jest Conventions trigger evidence is explicit.
- Jest Conventions source files, project memory, or declared resources were checked.
- Jest Conventions workflow rules were applied at the relevant artifact boundary.
- Jest Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Jest Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
