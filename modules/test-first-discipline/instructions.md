
# Output Marker

Display:
using module: test-first-discipline

---

# Test First Discipline

## Overview

Use tests as feedback loops that prove behavior through public seams before
implementation.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Name behavior; choose highest meaningful seam; write one failing test; implement minimally; refactor only when green; document exceptions.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Test First Discipline guidance names the inspected source, request evidence, or declared resource that triggered it.
- Test First Discipline output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Test First Discipline decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Test First Discipline validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

For Candidate saved-search creation, prove retrieval through the public query interface,
not private storage inspection.

## Hard Stops

- Do not use Test First Discipline without direct routing evidence or a required relation.
- Do not expand Test First Discipline beyond its stated responsibility.
- Do not add placeholder Test First Discipline guidance, examples, metadata, resources, or validation.
- Do not claim Test First Discipline is satisfied without evidence for its checklist.

## Usage Checklist

- Test First Discipline trigger evidence is explicit.
- Test First Discipline source files, project memory, or declared resources were checked.
- Test First Discipline workflow rules were applied at the relevant artifact boundary.
- Test First Discipline docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Test First Discipline risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: systematic-debugging, completion-verification, jest-conventions, vitest-conventions, playwright-conventions
