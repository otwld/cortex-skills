# Plan Execution Activate

## Overview

Confirm that the user has provided a decision-complete plan that can be executed
against the repository as it exists now.

## Workflow

1. Read the written plan, task list, goal record, issue body, or PRD section the
   user wants executed.
2. Check current git status for overlapping user work and generated artifacts.
3. Identify files, interfaces, tests, docs, and commands named or implied by the
   plan.
4. Extract acceptance criteria, validation commands, migration notes, and
   compatibility constraints.
5. Compare plan assumptions against current repository state.

## Quality Gates

- The plan states what changes, in what order, and how completion is checked.
- Product behavior, API shape, ownership, migration strategy, and validation are
  already decided or explicitly out of scope.
- The current repository still matches the assumptions the plan depends on.
- Existing uncommitted changes can be separated from the planned edits.

## Hard Stops

- The plan asks for implementation but still contains open choices an implementer
  would need to make.
- The plan is stale because relevant files, commands, or ownership boundaries no
  longer match.
- Required validation is absent and cannot be inferred from project-native
  commands.
- Unrelated dirty-tree changes overlap the planned paths.

## Phase Output

Return:

- Executable task inventory in the plan's order.
- Files, commands, docs, generated outputs, and tests expected per task.
- Dirty-tree conflicts or stale assumptions.
- Named validation checkpoints and any blockers requiring user input.
