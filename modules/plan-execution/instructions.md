
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

- Plan Execution guidance names the inspected source, request evidence, or declared resource that triggered it.
- Plan Execution output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Plan Execution decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Plan Execution validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

If the plan says rewrite all modules and validator tests, do not stop after adding
references.

## Hard Stops

- Do not use Plan Execution without direct routing evidence or a required relation.
- Do not expand Plan Execution beyond its stated responsibility.
- Do not add placeholder Plan Execution guidance, examples, metadata, resources, or validation.
- Do not claim Plan Execution is satisfied without evidence for its checklist.

## Usage Checklist

- Plan Execution trigger evidence is explicit.
- Plan Execution source files, project memory, or declared resources were checked.
- Plan Execution workflow rules were applied at the relevant artifact boundary.
- Plan Execution docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Plan Execution risks, rejected paths, and validation gaps are stated.

## Cross References

- BEFORE: workspace-state-guard
- WITH: agent-delegation, test-first-discipline, code-documentation, review-gate, completion-verification
- AFTER: branch-completion
