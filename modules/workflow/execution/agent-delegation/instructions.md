
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

- Delegated work is independent enough that no worker needs mutable local state from another worker.
- Each delegation brief names scope, allowed evidence sources, expected output, and integration criteria.
- Returned findings are inspected before they change the main recommendation or implementation.

## Example

One agent reviews validator tests while another inspects catalog consistency, but both
do not edit the same file.

## Hard Stops

- Do not delegate work that depends on an unresolved design decision in the main thread.
- Do not ask parallel workers to edit the same files or rely on each other's uncommitted output.
- Do not integrate delegated conclusions without checking the cited evidence yourself.

## Usage Checklist

- Independence and sequencing constraints were checked before delegation.
- Each worker received a bounded brief with evidence and output requirements.
- Delegated results were reconciled against the primary task before use.

## Cross References

- WITH: plan-execution, review-gate, systematic-debugging, completion-verification
