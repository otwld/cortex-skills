# Plan Execution Activate

## Overview

Confirm that the user has provided a decision-complete plan that can be executed
against the repository as it exists now. Re-derive intent from the embedded
plan and current repository state before execution, then compare it with the
entry intent model.

## Workflow

1. Read the entry intent model and note explicit intents, inferred intents,
   affected surfaces, validation needs, activated modules, and missing coverage.
2. Read the written plan, task list, goal record, issue body, or PRD section the
   user wants executed.
3. Derive the plan's current intent from embedded plan content and repository
   evidence.
4. Check current git status for overlapping user work and generated artifacts.
5. Identify files, interfaces, tests, docs, and commands named or implied by the
   plan.
6. Extract acceptance criteria, validation commands, migration notes, and
   compatibility constraints.
7. Compare plan assumptions and derived intent against current repository state
   and the entry intent model.

## Quality Gates

- The plan states what changes, in what order, and how completion is checked.
- Product behavior, API shape, ownership, migration strategy, and validation are
  already decided or explicitly out of scope.
- The re-derived plan intent materially matches the entry intent model.
- The current repository still matches the assumptions the plan depends on.
- Existing uncommitted changes can be separated from the planned edits.

## Hard Stops

- The plan asks for implementation but still contains open choices an implementer
  would need to make.
- The plan is stale because relevant files, commands, or ownership boundaries no
  longer match.
- Re-derived intent expands scope, changes ownership, or changes validation
  needs relative to the activation intent model.
- Required validation is absent and cannot be inferred from project-native
  commands.
- Unrelated dirty-tree changes overlap the planned paths.

## Phase Output

Return:

- Executable task inventory in the plan's order.
- Re-derived intent summary, comparison against the entry intent model, and any
  material drift.
- Files, commands, docs, generated outputs, and tests expected per task.
- Dirty-tree conflicts or stale assumptions.
- Named validation checkpoints and any blockers requiring user input.
