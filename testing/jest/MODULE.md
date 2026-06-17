---
name: jest-conventions
description: Internal Cortex module applied when creating, modifying, or reviewing Jest configuration, Jest tests, setup files, custom matchers, test environments, or Jest mocks.
---

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
3. Apply the module-specific rules: Inspect config; choose public seam; use deterministic fixtures; mock true boundaries; keep setup small; add matchers only for clarity.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

Test that a Candidate retrieves submitted Applications through a public service instead
of asserting a repository call.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this module's checklist.

## Usage Checklist

- Trigger signal is explicit.
- Relevant existing convention or memory was checked.
- Module-specific rules were applied.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining decisions, risks, or validation gaps are stated.

## Cross-References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
