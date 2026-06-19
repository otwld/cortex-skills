
# Output Marker

Display:
using module: nestjs-conventions

---

# NestJS Conventions

## Overview

Keep NestJS modules explicit without letting framework structure swallow domain
ownership.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Controllers handle transport; providers hold application behavior; pipes validate boundaries; tokens are explicit when adapters vary.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- NestJS Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- NestJS Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- NestJS Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- NestJS Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

ApplicationsController validates Candidate application requests and delegates decision
logic to an Application intake provider.

## Hard Stops

- Do not use NestJS Conventions without direct routing evidence or a required relation.
- Do not expand NestJS Conventions beyond its stated responsibility.
- Do not add placeholder NestJS Conventions guidance, examples, metadata, resources, or validation.
- Do not claim NestJS Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- NestJS Conventions trigger evidence is explicit.
- NestJS Conventions source files, project memory, or declared resources were checked.
- NestJS Conventions workflow rules were applied at the relevant artifact boundary.
- NestJS Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- NestJS Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: rxjs-conventions, typescript-code-style, code-documentation
- AFTER: skill-evolution
