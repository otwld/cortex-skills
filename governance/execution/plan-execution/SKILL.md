---
name: plan-execution
description: Use when executing a written implementation plan task-by-task with validation checkpoints and no remaining design decisions.
---

# Output Marker

Display:
using skill: plan-execution

---

# Plan Execution

## Overview

Execute a decision-complete plan in order. Preserve momentum, but stop when the
plan is wrong, ambiguous, or no longer matches the repository.

## Workflow

1. Read the plan once and check it against current repository state.
2. Run `workspace-state-guard` before substantial edits.
3. Execute tasks in order unless the plan explicitly allows parallel work.
4. Apply `test-first-discipline` for behavior changes and bug fixes.
5. Apply `code-documentation` during any code generation, edit, move, split, or
   refactor.
6. Run the validation named for each task.
7. Use `review-gate` at major checkpoints and before publishing.
8. Use `completion-verification` before claiming completion.

## Stop Conditions

- The plan conflicts with current code.
- A task has missing inputs or requires a design decision.
- Validation fails for reasons not understood.
- The task grows beyond the plan's stated scope.

## Hard Stops

- Do not silently reinterpret the plan.
- Do not skip validations because later tasks may cover them.
- Do not continue after a blocker that changes scope or architecture.

## Usage Checklist

- Plan was reviewed against current files.
- Tasks were executed in order or with explicit independence.
- Each task-level validation result is known.
- Blockers and plan drift were surfaced instead of guessed through.

## Cross-References

- BEFORE: workspace-state-guard
- WITH: agent-delegation, test-first-discipline, code-documentation, review-gate, completion-verification
- AFTER: branch-completion
