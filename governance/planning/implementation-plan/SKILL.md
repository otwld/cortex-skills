---
name: implementation-plan
description: Use when requirements are known and the work is multi-step, cross-boundary, migration-related, high-risk, or needs a written execution path before edits.
---

# Output Marker

Display:
using skill: implementation-plan

---

# Implementation Plan

## Overview

Turn stable requirements into an execution plan that another engineer or agent
can follow without making design decisions. Plans should be specific enough to
prevent drift and compact enough to stay useful.

## Workflow

1. Confirm requirements, non-goals, and success criteria.
2. Map the main files or modules and each responsibility.
3. Break the work into independently verifiable tasks.
4. Include JSDoc/TSDoc updates for any planned code generation, edit, move,
   split, or refactor.
5. Name expected validation commands and acceptance checks.
6. Identify needed governance and domain skills for execution.
7. Save a plan only when useful or requested.

Default artifact path is `docs/cortex/plans/` when the target repository has no
existing plan convention.

## Plan Rules

- No placeholders such as `TBD`, `TODO`, or vague "handle edge cases" steps.
- Include exact commands when validation is known.
- Include code snippets only where they remove ambiguity.
- Prefer behavior-level task descriptions over file-by-file churn.
- Do not require intermediate commits unless the user workflow does.

## Hard Stops

- A requirement cannot be mapped to a task.
- A task requires a decision not captured in the plan.
- Validation is unspecified for a risky behavior change.

## Usage Checklist

- Requirements and non-goals are stable.
- Tasks are ordered and independently checkable.
- Validation commands or acceptance checks are named.
- Execution can start without new design decisions.

## Cross-References

- WITH: design-intake, workspace-state-guard, test-first-discipline, architecture-drift-detector, library-placement-decision, public-api-design, code-documentation
- AFTER: plan-execution
