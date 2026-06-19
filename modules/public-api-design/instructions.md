
# Output Marker

Display:
using module: public-api-design

---

# Public API Design

## Overview

Keep public surfaces explicit, small, stable, typed, and documented as contracts.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Choose owner first; export supported symbols only; encode states with strong types; document invariants and migration impact.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Public API Design guidance names the inspected source, request evidence, or declared resource that triggered it.
- Public API Design output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Public API Design decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Public API Design validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

ApplicationReviewResult with accepted and rejected variants is clearer than optional
rejectionReason on every result.

## Hard Stops

- Do not use Public API Design without direct routing evidence or a required relation.
- Do not expand Public API Design beyond its stated responsibility.
- Do not add placeholder Public API Design guidance, examples, metadata, resources, or validation.
- Do not claim Public API Design is satisfied without evidence for its checklist.

## Usage Checklist

- Public API Design trigger evidence is explicit.
- Public API Design source files, project memory, or declared resources were checked.
- Public API Design workflow rules were applied at the relevant artifact boundary.
- Public API Design docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Public API Design risks, rejected paths, and validation gaps are stated.

## Cross References

- BEFORE: library-placement-decision
- WITH: naming-consistency, typescript-api-conventions, code-documentation
