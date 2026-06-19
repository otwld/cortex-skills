
# Output Marker

Display:
using module: design-intake

---

# Design Intake

## Overview

Clarify intent before implementation, after exploring facts the repository can answer.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Separate facts from preferences; ask only decision-changing questions; recommend defaults; record non-goals and success criteria.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Design Intake guidance names the inspected source, request evidence, or declared resource that triggered it.
- Design Intake output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Design Intake decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Design Intake validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

For a Candidate dashboard, inspect existing pages first and ask audience only if the
repo cannot reveal it.

## Hard Stops

- Do not use Design Intake without direct routing evidence or a required relation.
- Do not expand Design Intake beyond its stated responsibility.
- Do not add placeholder Design Intake guidance, examples, metadata, resources, or validation.
- Do not claim Design Intake is satisfied without evidence for its checklist.

## Usage Checklist

- Design Intake trigger evidence is explicit.
- Design Intake source files, project memory, or declared resources were checked.
- Design Intake workflow rules were applied at the relevant artifact boundary.
- Design Intake docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Design Intake risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: grill-with-docs, prototype, architecture-drift-detector, library-placement-decision, public-api-design
- AFTER: implementation-plan
