
# Output Marker

Display:
using module: architecture-deepening-review

---

# Architecture Deepening Review

## Overview

Find modules whose interfaces are too wide for the behavior they hide and propose deeper
seams that increase leverage and locality.

## Reference Routing

- Use `shared/architecture-deepening.md` when this task touches that concern.
- Use `shared/project-memory.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Use the architecture vocabulary exactly; apply the deletion test; classify dependencies; identify the interface that tests should cross.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Architecture Deepening Review guidance names the inspected source, request evidence, or declared resource that triggered it.
- Architecture Deepening Review output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Architecture Deepening Review decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Architecture Deepening Review validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Candidate matching rules scattered across routes, repositories, and UI filters suggest a
deep Matching module tested through Application outcomes.

## Hard Stops

- Do not use Architecture Deepening Review without direct routing evidence or a required relation.
- Do not expand Architecture Deepening Review beyond its stated responsibility.
- Do not add placeholder Architecture Deepening Review guidance, examples, metadata, resources, or validation.
- Do not claim Architecture Deepening Review is satisfied without evidence for its checklist.

## Usage Checklist

- Architecture Deepening Review trigger evidence is explicit.
- Architecture Deepening Review source files, project memory, or declared resources were checked.
- Architecture Deepening Review workflow rules were applied at the relevant artifact boundary.
- Architecture Deepening Review docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Architecture Deepening Review risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: architecture-drift-detector, library-placement-decision, public-api-design, test-first-discipline, code-documentation
- AFTER: skill-evolution
