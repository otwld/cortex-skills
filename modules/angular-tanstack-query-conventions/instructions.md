
# Output Marker

Display:
using module: angular-tanstack-query-conventions

---

# Angular TanStack Query Conventions

## Overview

Treat query integration as a cache identity and data-contract concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Keys include every variable that changes data; skippable inputs are explicit; mutations name cache impact; pagination belongs in keys.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Angular TanStack Query Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- Angular TanStack Query Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Angular TanStack Query Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Angular TanStack Query Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Candidate search includes companyId, jobOfferId, filters, and page in the key because
each changes results.

## Hard Stops

- Do not use Angular TanStack Query Conventions without direct routing evidence or a required relation.
- Do not expand Angular TanStack Query Conventions beyond its stated responsibility.
- Do not add placeholder Angular TanStack Query Conventions guidance, examples, metadata, resources, or validation.
- Do not claim Angular TanStack Query Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- Angular TanStack Query Conventions trigger evidence is explicit.
- Angular TanStack Query Conventions source files, project memory, or declared resources were checked.
- Angular TanStack Query Conventions workflow rules were applied at the relevant artifact boundary.
- Angular TanStack Query Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Angular TanStack Query Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- BEFORE: angular-conventions
- WITH: rxjs-conventions, typescript-api-conventions, public-api-design, code-documentation
- AFTER: skill-evolution
