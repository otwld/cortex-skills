
# Output Marker

Display:
using module: branch-completion

---

# Branch Completion

## Overview

Turn local work into a durable handoff or published change without sweeping unrelated
files into release steps.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect status; verify; review if major; summarize scope; commit scoped changes only when requested; push or PR only with user direction.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Branch completion starts from the actual dirty tree and only includes changes in scope.
- Verification, review, commit, push, PR, release, or cleanup steps follow explicit user direction.
- Remaining risk is reported before any publish or irreversible branch action.

## Example

Commit module bodies, references, catalog, graph, and validator tests together while
leaving unrelated README edits uncommitted.

## Hard Stops

- Do not commit, push, merge, publish, or discard changes without explicit user direction.
- Do not include unrelated dirty files in branch-completion output or commits.
- Do not claim a branch is ready without fresh verification or a clearly named validation gap.

## Usage Checklist

- Git status and scoped diff were inspected before completion steps.
- Validation and review evidence were collected or the blocker was named.
- User-directed branch action and remaining risks were stated plainly.

## Cross References

- BEFORE: workspace-state-guard, completion-verification
- WITH: review-gate
