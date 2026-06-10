---
name: branch-completion
description: Use when implementation is complete and the user asks to merge, push, open a pull request, publish, discard, clean up, or finish branch work.
---

# Output Marker

Display:
using skill: branch-completion

---

# Branch Completion

## Overview

Finish branch work by verifying state, presenting clear options, and protecting
work from accidental loss.

## Workflow

1. Run `completion-verification` for the relevant project checks.
2. Inspect branch, upstream, remote, and worktree state.
3. Summarize what is ready and what risk remains.
4. Present the appropriate finish options: merge, push or PR, keep branch,
   cleanup, or discard.
5. Execute only the selected option.
6. Confirm before destructive cleanup or discard.

## Rules

- Do not force-push unless explicitly requested.
- Do not delete branches or worktrees without confirmation.
- Do not clean up a worktree owned by the harness or another tool.
- Keep PR workspaces available for follow-up unless the user asks to remove them.
- Use repository-specific PR tooling when available; otherwise report the Git
  state and next command.

## Hard Stops

- Verification fails before publish or merge.
- The base branch or upstream is ambiguous.
- Discard or cleanup would remove commits or files without explicit
  confirmation.

## Usage Checklist

- Verification result is fresh.
- Branch and remote state are known.
- Finish option is explicit.
- Destructive actions were confirmed.

## Cross-References

- BEFORE: workspace-state-guard, completion-verification
- WITH: review-gate
