# Branch Completion Verify

## Overview

Prove that the planned branch action matches the intended scope and that any
readiness claim is backed by current evidence.

## Workflow

### Required Checks

- Re-read repository status following any edits, staging, commit, cleanup, or
  generated output step.
- Compare the staged set or proposed commit set to the in-scope file list from
  activation.
- Inspect a scoped diff or summary that is specific enough to catch accidental
  unrelated changes.
- Run the project validation that is relevant to the completed work, or record
  the concrete blocker and residual risk.
- For remote-facing actions, inspect branch tracking, unpushed commits, and the
  target branch or pull request metadata available locally.

### Failure Modes

- A commit includes unrelated local edits because staging used a broad path.
- A push or pull request is created from stale local state.
- A release or publish step is attempted from a branch that has unverified
  changes or unknown divergence.
- A cleanup action removes user-owned work because untracked or ignored files
  were not classified.

## Quality Gates

- Staged or publish-bound files match the in-scope file list.
- Latest status and diff evidence are inspected during this phase.
- Remote-facing actions account for branch tracking and unpushed commits.

## Hard Stops

- Stop when scoped status cannot distinguish owned task changes from unrelated
  work.
- Stop when validation needed for the branch action cannot run and the user has
  not accepted the named risk.
- Stop when local and remote branch state conflict in a way that changes the
  requested action.

## Phase Output

- Verification commands or inspections performed, including latest status
  evidence.
- Validation result, blocked check, or explicit reason validation was not run.
- Confirmation that staged or publish-bound files match scope, or a precise gap
  that prevents the action.
