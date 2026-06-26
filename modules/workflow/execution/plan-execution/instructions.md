
# Output Marker

Display:
using module: plan-execution

---

# Plan Execution

## Overview

Execute the agreed plan against current repository state without silently replanning it.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Derive requirements; check workspace state; execute tasks in order; apply test-first and docs gates; run named validation; surface plan drift.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Execution follows a decision-complete plan without opening new design choices silently.
- Workspace state, tests, docs, generated artifacts, and review checkpoints are handled at the planned step.
- Plan drift is reported immediately with the requirement or file that caused it.

## Example

If the plan says rewrite all modules and validator tests, do not stop after adding
references.

## Hard Stops

- Do not execute a plan that leaves API, ownership, or validation decisions unresolved.
- Do not skip planned validation because an earlier step appeared low risk.
- Do not absorb unrelated dirty-tree changes into plan execution.

## Usage Checklist

- Plan requirements and workspace state were rechecked before edits.
- Tasks were completed in order with tests, docs, and generated outputs kept together.
- Plan drift, blockers, and validation evidence were reported as they appeared.

## Cross References

- BEFORE: workspace-state-guard
- WITH: agent-delegation, test-first-discipline, code-documentation, review-gate, completion-verification
- AFTER: branch-completion
