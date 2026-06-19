
# Output Marker

Display:
using module: naming-consistency

---

# Naming Consistency

## Overview

Treat names as part of the interface and align them with project vocabulary and real
responsibilities.

## Reference Routing

- Use `shared/domain-glossary.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Read project memory; prefer complete public names; use role suffixes only when true; rename vague shared/common/helper names.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Naming Consistency guidance names the inspected source, request evidence, or declared resource that triggered it.
- Naming Consistency output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Naming Consistency decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Naming Consistency validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

CandidateStageTransition is better than StatusChange when the transition is specific to
recruiting pipeline movement.

## Hard Stops

- Do not use Naming Consistency without direct routing evidence or a required relation.
- Do not expand Naming Consistency beyond its stated responsibility.
- Do not add placeholder Naming Consistency guidance, examples, metadata, resources, or validation.
- Do not claim Naming Consistency is satisfied without evidence for its checklist.

## Usage Checklist

- Naming Consistency trigger evidence is explicit.
- Naming Consistency source files, project memory, or declared resources were checked.
- Naming Consistency workflow rules were applied at the relevant artifact boundary.
- Naming Consistency docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Naming Consistency risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: public-api-design, typescript-api-conventions, code-documentation
