
# Output Marker

Display:
using module: library-placement-decision

---

# Library Placement Decision

## Overview

Choose code location by responsibility, dependency direction, and consumer scope instead
of convenience.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Classify domain, integration, feature, UI, utility, or adapter responsibility; use existing owners; split mixed responsibilities.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Library Placement Decision guidance names the inspected source, request evidence, or declared resource that triggered it.
- Library Placement Decision output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Library Placement Decision decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Library Placement Decision validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Candidate ranking shared by search and recommendations belongs in a domain-owned module;
a page-specific ranking panel stays in the feature.

## Hard Stops

- Do not use Library Placement Decision without direct routing evidence or a required relation.
- Do not expand Library Placement Decision beyond its stated responsibility.
- Do not add placeholder Library Placement Decision guidance, examples, metadata, resources, or validation.
- Do not claim Library Placement Decision is satisfied without evidence for its checklist.

## Usage Checklist

- Library Placement Decision trigger evidence is explicit.
- Library Placement Decision source files, project memory, or declared resources were checked.
- Library Placement Decision workflow rules were applied at the relevant artifact boundary.
- Library Placement Decision docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Library Placement Decision risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: nx-module-boundaries, public-api-design, naming-consistency
- AFTER: skill-evolution
