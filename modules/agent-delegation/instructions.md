
# Output Marker

Display:
using module: agent-delegation

---

# Agent Delegation

## Overview

Use subagents only for independent work with bounded inputs and verifiable output
contracts.

## Reference Routing

- Use `references/code-reviewer-prompt.md` when this task touches that concern.
- Use `references/implementer-prompt.md` when this task touches that concern.
- Use `references/spec-reviewer-prompt.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Separate independent tasks; choose exploration, implementation, or review; provide constraints; inspect returned evidence before integrating.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Agent Delegation guidance names the inspected source, request evidence, or declared resource that triggered it.
- Agent Delegation output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Agent Delegation decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Agent Delegation validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

One agent reviews validator tests while another inspects catalog consistency, but both
do not edit the same file.

## Hard Stops

- Do not use Agent Delegation without direct routing evidence or a required relation.
- Do not expand Agent Delegation beyond its stated responsibility.
- Do not add placeholder Agent Delegation guidance, examples, metadata, resources, or validation.
- Do not claim Agent Delegation is satisfied without evidence for its checklist.

## Usage Checklist

- Agent Delegation trigger evidence is explicit.
- Agent Delegation source files, project memory, or declared resources were checked.
- Agent Delegation workflow rules were applied at the relevant artifact boundary.
- Agent Delegation docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Agent Delegation risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: plan-execution, review-gate, systematic-debugging, completion-verification
