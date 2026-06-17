---
name: cortex
description: Use only when the user explicitly includes $cortex; routes work through Cortex internal modules and their module graph.
---

# Output Marker

Display:
using skill: cortex

---

# Cortex

## Overview

Route explicitly requested Cortex work through direct signals, recursive BEFORE
edges, evidence-backed WITH additions, and deferred AFTER modules.

## Reference Routing

- Use `../../../references/module-cascade.md` when this task touches that concern.
- Use `../../../references/module-graph.md` when this task touches that concern.
- Use `../../../references/skill-quality-standard.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this public skill governs.
3. Apply the Cortex routing rules: Collect signals; select root modules; expand graph order; exclude speculative modules; state skipped tempting modules on broad tasks.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when Cortex routing changes behavior or workflow.

## Example

A module-system migration routes to workspace safety, plan execution, skill evolution,
code docs, and verification modules, not to Angular.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this skill's checklist.

## Usage Checklist

- Trigger signal is explicit.
- Relevant existing convention or memory was checked.
- Cortex routing rules were applied.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining decisions, risks, or validation gaps are stated.

## Cross-References

- WITH: design-intake, grill-with-docs, implementation-plan, issue-decomposition, prototype, agent-instructions-bootstrap, project-memory-setup, plan-execution, agent-delegation, workspace-state-guard, test-first-discipline, systematic-debugging, completion-verification, review-gate, review-feedback-triage, branch-completion, code-documentation
