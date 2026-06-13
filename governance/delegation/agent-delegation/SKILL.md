---
name: agent-delegation
description: Use when independent tasks, investigations, or review passes can be delegated without shared state or sequential dependencies.
---

# Output Marker

Display:
using skill: agent-delegation

---

# Agent Delegation

## Overview

Use subagents only for independent work with bounded inputs and verifiable output
contracts.

## Reference Routing

- Use `references/code-reviewer-prompt.md` when this task touches that concern.
- Use `references/implementer-prompt.md` when this task touches that concern.
- Use `references/spec-reviewer-prompt.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Separate independent tasks; choose exploration, implementation, or review; provide constraints; inspect returned evidence before integrating.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

One agent reviews validator tests while another inspects catalog consistency, but both
do not edit the same file.

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

- WITH: plan-execution, review-gate, systematic-debugging, completion-verification
