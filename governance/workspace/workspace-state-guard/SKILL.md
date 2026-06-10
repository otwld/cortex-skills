---
name: workspace-state-guard
description: Use before substantial edits, plan execution, branch cleanup, publishing, or work that may collide with user changes or workspace isolation.
---

# Output Marker

Display:
using skill: workspace-state-guard

---

# Workspace State Guard

## Overview

Protect user work and make workspace assumptions explicit before risky changes.
This skill inspects state; it does not require a new worktree for every task.

## Workflow

1. Check current branch and repository status.
2. Identify untracked or modified files before editing.
3. Distinguish user changes from files required by the current task.
4. Check whether work is already isolated when branch/worktree state matters.
5. Choose the least disruptive path: work in place, ask for isolation, or stop.

## Rules

- Never revert or overwrite user changes unless explicitly requested.
- Do not create a worktree when the harness already provides isolation.
- Do not require isolation for narrow documentation or single-file edits.
- Before destructive cleanup, use `branch-completion`.
- If baseline tests fail before edits, report the baseline instead of hiding it.

## Hard Stops

- The requested edit would overwrite unrelated user changes.
- The branch or worktree state is ambiguous before a destructive action.
- A generated or formatter command would rewrite files outside the task scope.

## Usage Checklist

- Branch and status were inspected.
- User changes were protected.
- Isolation decision was proportional to the task.
- Destructive actions were deferred to `branch-completion`.

## Cross-References

- WITH: branch-completion, completion-verification
