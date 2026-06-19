
# Output Marker

Display:
using module: extraction-decision

---

# Extraction Decision

## Overview

Decide whether duplication is stable enough to extract, and whether extraction improves
ownership, leverage, and locality.

## Reference Routing

- Use `shared/architecture-deepening.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inventory consumers; separate stable behavior from coincidental shape; choose owner before API; preserve dependency direction.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Extraction Decision guidance names the inspected source, request evidence, or declared resource that triggered it.
- Extraction Decision output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Extraction Decision decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Extraction Decision validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Three Application status mappers with identical business rules may become one domain
mapper; similar Candidate cards may remain local if behavior differs.

## Hard Stops

- Do not use Extraction Decision without direct routing evidence or a required relation.
- Do not expand Extraction Decision beyond its stated responsibility.
- Do not add placeholder Extraction Decision guidance, examples, metadata, resources, or validation.
- Do not claim Extraction Decision is satisfied without evidence for its checklist.

## Usage Checklist

- Extraction Decision trigger evidence is explicit.
- Extraction Decision source files, project memory, or declared resources were checked.
- Extraction Decision workflow rules were applied at the relevant artifact boundary.
- Extraction Decision docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Extraction Decision risks, rejected paths, and validation gaps are stated.

## Cross References

- BEFORE: library-placement-decision, nx-module-boundaries
- WITH: public-api-design, naming-consistency, bundle-performance, code-documentation
- AFTER: skill-evolution
