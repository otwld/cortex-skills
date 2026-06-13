---
name: vitest-conventions
description: Use when creating, modifying, or reviewing Vitest configuration, Vitest tests, setup files, environments, mocks, or Vite-integrated test behavior.
---

# Output Marker

Display:
using skill: vitest-conventions

---

# Vitest Conventions

## Overview

Keep Vitest aligned with Vite while testing behavior through stable seams.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Inspect config; choose correct environment; prefer real modules; mock boundaries; control timers deliberately; keep setup minimal.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

A pure JobOffer ranking function runs in node; a Candidate filter component using DOM
APIs uses the configured DOM environment.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this skill's checklist.

## Usage Checklist

- Trigger signal is explicit.
- Relevant existing convention or memory was checked.
- Skill-specific rules were applied.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining decisions, risks, or validation gaps are stated.

## Cross-References

- WITH: vite-conventions, typescript-code-style, code-documentation
- AFTER: skill-evolution
