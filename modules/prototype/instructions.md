
# Output Marker

Display:
using module: prototype

---

# Prototype

## Overview

Build disposable code that answers one design question and is deleted or absorbed
afterward.

## Reference Routing

- Use `shared/prototype-guidance.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. State the question; choose logic or UI branch; isolate throwaway shell; use in-memory state; provide one command; capture the answer.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Prototype guidance names the inspected source, request evidence, or declared resource that triggered it.
- Prototype output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Prototype decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Prototype validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

An Interview scheduling state-machine prototype tests reschedule and cancellation cases
before the real module design.

## Hard Stops

- Do not use Prototype without direct routing evidence or a required relation.
- Do not expand Prototype beyond its stated responsibility.
- Do not add placeholder Prototype guidance, examples, metadata, resources, or validation.
- Do not claim Prototype is satisfied without evidence for its checklist.

## Usage Checklist

- Prototype trigger evidence is explicit.
- Prototype source files, project memory, or declared resources were checked.
- Prototype workflow rules were applied at the relevant artifact boundary.
- Prototype docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Prototype risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: design-intake, test-first-discipline, code-documentation
- AFTER: issue-decomposition
