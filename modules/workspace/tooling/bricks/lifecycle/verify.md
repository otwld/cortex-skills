# Bricks Verify

## Overview

Prove the Bricks workflow left consumer and source state understandable,
recoverable, and assigned to the correct owner.

## Workflow

1. Use `bricks status`, `bricks diff`, `bricks doctor`, merge continuation
  status, or contribution status according to the command family used.
2. Inspect Git status in the consumer workspace for expected installed-copy
  changes and unrelated user work.
3. For install or merge work, run the consumer repo's relevant format, lint, test,
  typecheck, or Nx target when available.
4. For contribution work, inspect and validate the dedicated source worktree, then
  use contribution status to confirm the session state.
5. Record any command that was skipped because the repo lacks dependencies,
  current docs are missing, or the user asked for guidance only.

## Quality Gates

- Consumer-owned files, source cache, and contribution worktree changes are not
  mixed together in the final explanation.
- Bricks provenance was preserved through commands rather than manual file copy.
- Dirty worktrees are intentional and explained.
- Release or publish steps were not added unless the Bricks consumer workflow
  explicitly required them.

## Hard Stops

- Do not report a merge or contribution complete while conflict markers,
  unstaged source worktree changes, or failed required validation remain
  unresolved.
- Do not recommend push or commit when verification only covered the consumer
  workspace and not the contribution worktree.
- Do not hide skipped validation; name the missing command, dependency, or
  evidence.

## Phase Output

Return verification commands, observed state, unresolved diffs or conflicts,
skipped checks, and the remaining user decision if the workflow cannot be
completed safely.
