
# Output Marker

Display:
using module: bricks

---

# Bricks

## Overview

Operate Bricks installed-source workflows without confusing consumer edits, source
worktrees, and release flows.

## Reference Routing

- Use `references/product-model.md` when this task touches that concern.
- Use `references/cli-workflows.md` when this task touches that concern.
- Use `references/contribution-workflow.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect Bricks status; identify workflow branch; use Bricks commands instead of manual copies; protect consumer edits; run doctor or diff checks.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Bricks workflow state is read from the consumer workspace before source or installed-copy decisions.
- Consumer edits, source worktree changes, and contribution steps stay assigned to the correct side.
- Bricks doctor, diff, status, merge, or contribution checks back the final recommendation.

## Example

If a Candidate UI brick has local consumer edits, inspect Bricks diff before merging an
upstream update.

## Hard Stops

- Do not manually copy installed brick files when a Bricks command owns the workflow.
- Do not treat Nx release, npm publish, or source-repo maintainer work as Bricks consumer work without direct evidence.
- Do not overwrite consumer edits while updating an installed brick or source worktree.

## Usage Checklist

- Installed brick state, source worktree, and consumer changes were classified.
- The selected Bricks workflow command was named before edits or guidance.
- Doctor, status, diff, merge, or contribution validation was run or blocked explicitly.

## Cross References

- WITH: workspace-state-guard, nx-conventions, completion-verification
