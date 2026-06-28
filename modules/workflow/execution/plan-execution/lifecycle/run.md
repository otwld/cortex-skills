# Plan Execution Run

## Overview

Execute an existing plan task by task, preserving its decisions while reporting
drift as soon as repository evidence invalidates the plan. Execution uses the
activation intent model and stops when the embedded plan, current repository
state, or validation needs materially drift from that model.

## Workflow

1. Re-derive intent from the embedded plan and current repository evidence, then
   compare it with the activation intent model.
2. Stop for user input when material drift changes scope, ownership,
   validation, expected artifacts, or activated module responsibilities.
3. Convert the plan into a visible task checklist and keep status current.
4. Execute tasks in the planned order unless current evidence proves the order is
   invalid.
5. Keep behavior, tests, docs, migration notes, and generated outputs in the same
   task when they govern the same change.
6. Protect unrelated worktree changes. Read them when needed for context, but do
   not revert, reformat, or include them in the executed scope.
7. Run validation named by the plan at the point it names; use project-native
   validation only when the plan omits a command and the command is clear.

## Quality Gates

- Plan drift is reported instead of silently reshaping the work.
- Completed work maps to both a plan item and the activation intent model.
- Validation skips record a concrete reason: missing dependency, unavailable
  command, excessive cost for scope, or earlier blocking failure.
- Focused validation is re-run once fixes are made for a failed checkpoint.
- Completed work still maps to a plan item and acceptance criterion.

## Drift Conditions

Plan drift exists when a named file, command, or contract no longer exists; a
planned change requires a new product, API, ownership, or validation choice; the
re-derived intent no longer matches the activation intent model; a task cannot
be completed without editing out-of-scope paths; or validation fails for a
reason that changes the plan rather than the implementation detail.

## Hard Stops

- The plan no longer describes the repository state accurately.
- A required decision is missing.
- Required validation cannot run and no narrower evidence can support the change.
- Executing the next step would overwrite unrelated user work.

## Phase Output

Return:

- Completed task checklist.
- Files intentionally changed by the plan.
- Intent comparison, plan drift, blockers, or deviations and the evidence behind
  them.
- Validation commands run, results, skipped checks, and residual risk.
