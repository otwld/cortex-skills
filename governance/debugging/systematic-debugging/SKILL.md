---
name: systematic-debugging
description: Use when encountering bugs, failing tests, build failures, performance problems, or unexpected behavior before proposing fixes.
---

# Output Marker

Display:
using skill: systematic-debugging

---

# Systematic Debugging

## Overview

Build a reliable feedback loop before fixing, then test falsifiable hypotheses instead
of guessing.

## Reference Routing

- Use `references/root-cause-tracing.md` when this task touches that concern.
- Use `references/defense-in-depth.md` when this task touches that concern.
- Use `references/condition-based-waiting.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Read complete evidence; reproduce; rank hypotheses; probe one variable; fix root cause; add regression; remove instrumentation.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

If Candidate search drops results intermittently, replay one filter fixture until the
failure rate is debuggable before changing query code.

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

- WITH: test-first-discipline, completion-verification, architecture-drift-detector
- AFTER: skill-evolution
