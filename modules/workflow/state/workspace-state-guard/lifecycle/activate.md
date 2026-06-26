# Workspace State Guard Activate

## Overview

Protect user-owned workspace state when a task may edit files, stage files,
delete files, run formatters, regenerate artifacts, clean up branches, or publish
repository state.

## Workflow

### Inspect

- Inspect current branch and repository status, including staged, unstaged,
  untracked, and ignored files when ignored files affect the requested action.
- Inspect scoped diffs for files that may overlap the requested work.
- Identify generated outputs and disposable artifacts separately from source
  files.
- Capture baseline command failures when a validation or build check is already
  failing prior to the current work.

### Classify

- `task-owned`: files the current request clearly requires changing.
- `user-owned`: pre-existing changes that are unrelated or ambiguous.
- `generated`: reproducible outputs that should be regenerated, not hand-edited,
  unless the repository treats them as source.
- `disposable`: temporary files created by the current agent that may be removed
  once scope is confirmed.
- `blocked`: files whose ownership cannot be determined from available evidence.

## Quality Gates

- Dirty-tree classification is based on current status and scoped diffs.
- User-owned and blocked files are excluded from broad writes or cleanup.
- Baseline failures are recorded separately from current-work failures.

## Hard Stops

- Do not revert, reset, overwrite, clean, remove, or reformat files that are
  user-owned or blocked unless the user explicitly asks for that exact action.
- Do not stage broad paths when unrelated dirty files exist.
- Do not hide unrelated changes by formatting or regenerating them alongside
  task-owned files.
- Do not present baseline failures as introduced by the current work.

## Phase Output

- Current branch and dirty-tree summary.
- File ownership classification and any blocked ownership questions.
- Destructive or broad commands that are forbidden for this task.
- Baseline failures that must be kept separate from current-work failures.
