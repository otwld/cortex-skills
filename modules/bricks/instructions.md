
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

- Bricks guidance names the inspected source, request evidence, or declared resource that triggered it.
- Bricks output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Bricks decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Bricks validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

If a Candidate UI brick has local consumer edits, inspect Bricks diff before merging an
upstream update.

## Hard Stops

- Do not use Bricks without direct routing evidence or a required relation.
- Do not expand Bricks beyond its stated responsibility.
- Do not add placeholder Bricks guidance, examples, metadata, resources, or validation.
- Do not claim Bricks is satisfied without evidence for its checklist.

## Usage Checklist

- Bricks trigger evidence is explicit.
- Bricks source files, project memory, or declared resources were checked.
- Bricks workflow rules were applied at the relevant artifact boundary.
- Bricks docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Bricks risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: workspace-state-guard, nx-conventions, completion-verification
