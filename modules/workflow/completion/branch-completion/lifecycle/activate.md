# Branch Completion Activate

## Overview

Prepare a user-directed branch finish action from the real repository state.
This phase defines the requested action, its file scope, and the evidence needed
to make that action reviewable.

## Workflow

### Inspect

- Read the latest user request and identify the exact action: commit, push, pull
  request, merge, release, publish, discard, cleanup, or handoff only.
- Inspect the current branch, upstream tracking, staged changes, unstaged
  changes, untracked files, and unpushed commits.
- Inspect the scoped diff for files that appear unrelated to the requested
  branch action.
- Locate fresh validation or review evidence that supports the branch readiness
  claim. Treat missing evidence as a named gap, not as implied success.

### Decide

- Decide which changed files belong to the branch action and which must remain
  untouched.
- Decide whether the user has explicitly authorized the requested irreversible
  step. Commit, push, merge, publish, release, discard, and cleanup are separate
  permissions.
- Decide whether validation is current enough for the action. If validation is
  stale, blocked, or absent, state the risk and ask only when the action cannot
  proceed responsibly.

## Quality Gates

- The requested branch action is explicit and separate from adjacent actions.
- The in-scope file list is derived from current repository status and diff
  evidence.
- Validation or review evidence is named as current, stale, blocked, or absent.

## Hard Stops

- Do not commit, push, merge, publish, release, discard, or clean up branch work
  unless the user explicitly requested that exact action.
- Do not stage, format, rewrite, or remove unrelated dirty files while preparing
  branch completion.
- Do not describe the branch as ready when validation is missing, stale, or
  contradicted by the current diff.

## Phase Output

- Requested branch action and whether authorization is explicit.
- Current branch and dirty-tree summary, including staged, unstaged, untracked,
  and unpushed work.
- Files in scope, files intentionally left alone, and any ambiguous files.
- Validation or review evidence needed prior to the branch action.
