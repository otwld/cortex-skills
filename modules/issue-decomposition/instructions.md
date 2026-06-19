
# Output Marker

Display:
using module: issue-decomposition

---

# Issue Decomposition

## Overview

Convert broad work into independently verifiable vertical slices and durable agent
briefs.

## Reference Routing

- Use `shared/vertical-slices.md` when this task touches that concern.
- Use `shared/agent-briefs.md` when this task touches that concern.
- Use `shared/issue-tracker-setup.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Read source context; break end-to-end slices; classify AFK or human-in-loop; write behavioral briefs; publish only through configured tracker rules.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Issue Decomposition guidance names the inspected source, request evidence, or declared resource that triggered it.
- Issue Decomposition output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Issue Decomposition decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Issue Decomposition validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Candidate saved searches decomposes into persistence, query API, saved-search UI, and
delete behavior slices.

## Hard Stops

- Do not use Issue Decomposition without direct routing evidence or a required relation.
- Do not expand Issue Decomposition beyond its stated responsibility.
- Do not add placeholder Issue Decomposition guidance, examples, metadata, resources, or validation.
- Do not claim Issue Decomposition is satisfied without evidence for its checklist.

## Usage Checklist

- Issue Decomposition trigger evidence is explicit.
- Issue Decomposition source files, project memory, or declared resources were checked.
- Issue Decomposition workflow rules were applied at the relevant artifact boundary.
- Issue Decomposition docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Issue Decomposition risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: implementation-plan, grill-with-docs
- AFTER: plan-execution
