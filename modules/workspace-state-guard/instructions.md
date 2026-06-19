
# Output Marker

Display:
using module: workspace-state-guard

---

# Workspace State Guard

## Overview

Protect user work and control generated-write scope before risky changes.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect status; classify dirty files; leave unrelated work alone; avoid destructive commands; report baseline failures plainly.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Dirty tree, ignored files, generated outputs, and user-owned changes are classified before edits or cleanup.
- Commands avoid destructive git operations unless the user explicitly requested that exact action.
- Baseline failures are separated from failures introduced by the current work.

## Example

If validation scripts are already modified and the task is validator migration, replace
them as task-relevant and leave unrelated README edits alone.

## Hard Stops

- Do not revert, reset, overwrite, or clean files you did not create without explicit user permission.
- Do not hide unrelated dirty files by staging or formatting them with task changes.
- Do not report validation failures as new if the baseline already failed before edits.

## Usage Checklist

- Git status and relevant generated or ignored paths were inspected.
- User-owned changes were preserved and unrelated files left alone.
- Baseline failures, current-work failures, and cleanup decisions were reported separately.

## Cross References

- WITH: branch-completion, completion-verification
