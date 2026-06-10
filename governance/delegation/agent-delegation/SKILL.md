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

Delegate only when work is genuinely independent and the environment supports
it. If subagents are unavailable, use the same scoping rules for local
self-review or sequential investigation.

## Delegation Rules

- Split by independent problem domain, not by convenience.
- Provide complete task-local context; do not rely on conversation history.
- Give each delegate a narrow goal, constraints, expected output, and validation.
- Keep dependent or shared-state edits sequential.
- Review returned work before integrating or reporting it.

## Reference Templates

Load only the template needed for the current delegation:

- `references/implementer-prompt.md` for isolated implementation tasks.
- `references/spec-reviewer-prompt.md` for requirement compliance review.
- `references/code-reviewer-prompt.md` for implementation quality review.

## Fallback

When no delegation tool exists, perform the same roles sequentially in the main
session: implement, then inspect for requirement fit, then inspect for quality.

## Hard Stops

- Tasks touch the same files or mutable state without coordination.
- The delegate would need hidden context not supplied in the prompt.
- Returned work is accepted without reading the diff or running validation.

## Usage Checklist

- Independence was established.
- Prompt context was complete and bounded.
- Returned work was reviewed before integration.
- Fallback path was used if subagents were unavailable.

## Cross-References

- WITH: plan-execution, review-gate, systematic-debugging, completion-verification
