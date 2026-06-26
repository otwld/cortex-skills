# Branch Completion Finalize

## Overview

Report the branch action in durable terms: what happened, what evidence supports
it, what remains local, and what risk the next agent or maintainer inherits.

## Workflow

### Report

- Name the exact branch action completed or the reason it was not completed.
- List durable artifacts created or updated: commit SHA, pushed branch, pull
  request URL, release identifier, tag, cleanup result, or handoff note.
- Summarize changed files by scope, not by every line of diff.
- Include latest validation evidence and any skipped or blocked checks.
- State remaining local changes, untracked files, or follow-up work plainly.

## Quality Gates

- Final branch status is based on the latest inspected repository state.
- Durable artifact identifiers are included when branch actions created them.
- Remaining local changes and validation gaps are visible in the handoff.

## Hard Stops

- Do not present a commit, push, pull request, merge, release, publish, discard,
  or cleanup as completed unless that action actually succeeded.
- Do not hide unrelated dirty files in a successful branch-completion summary.
- Do not omit validation gaps when the final branch state depends on them.

## Phase Output

- Completed branch action and durable artifact identifiers.
- Scope summary for included files and excluded local changes.
- Validation evidence, unresolved risks, and next action if the branch is not
  fully complete.
