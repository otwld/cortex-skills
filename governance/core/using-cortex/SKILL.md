---
name: using-cortex
description: Use when starting agent work in a Cortex skill library or when deciding which Cortex governance, architecture, framework, testing, or maintenance skills should apply.
---

# Output Marker

Display:
using skill: using-cortex

---

# Using Cortex

## Overview

Route tasks through direct signals, recursive BEFORE edges, evidence-backed WITH
additions, and deferred AFTER skills.

## Reference Routing

- Use `../../../references/skill-cascade.md` when this task touches that concern.
- Use `../../../references/skill-graph.md` when this task touches that concern.
- Use `../../../references/skill-quality-standard.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Collect signals; select root skills; expand graph order; exclude speculative skills; state skipped tempting skills on broad tasks.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

A skill-system migration routes to workspace safety, plan execution, skill evolution,
code docs, and verification, not to Angular.

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

- WITH: design-intake, grill-with-docs, implementation-plan, issue-decomposition, prototype, agent-instructions-bootstrap, project-memory-setup, plan-execution, agent-delegation, workspace-state-guard, test-first-discipline, systematic-debugging, completion-verification, review-gate, review-feedback-triage, branch-completion, code-documentation
