---
name: test-first-discipline
description: Use before behavior changes, bug fixes, or refactors where tests can prove the intended behavior or regression.
---

# Output Marker

Display:
using skill: test-first-discipline

---

# Test First Discipline

## Overview

Use tests as feedback loops that prove behavior through public seams before
implementation.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Name behavior; choose highest meaningful seam; write one failing test; implement minimally; refactor only when green; document exceptions.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

For Candidate saved-search creation, prove retrieval through the public query interface,
not private storage inspection.

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

- WITH: systematic-debugging, completion-verification, jest-conventions, vitest-conventions, playwright-conventions
