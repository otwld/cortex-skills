
# Output Marker

Display:
using module: nestjs-mongoose-conventions

---

# NestJS Mongoose Conventions

## Overview

Keep persistence shape behind a seam so Mongoose details do not leak upward.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Separate schema, domain, and transport shapes; centralize ObjectId conversion; type aggregations; return plain contracts when callers need them.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- NestJS Mongoose Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- NestJS Mongoose Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- NestJS Mongoose Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- NestJS Mongoose Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

ApplicationRepository.findActiveForJobOffer returns ApplicationSummary records, not raw
hydrated documents.

## Hard Stops

- Do not use NestJS Mongoose Conventions without direct routing evidence or a required relation.
- Do not expand NestJS Mongoose Conventions beyond its stated responsibility.
- Do not add placeholder NestJS Mongoose Conventions guidance, examples, metadata, resources, or validation.
- Do not claim NestJS Mongoose Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- NestJS Mongoose Conventions trigger evidence is explicit.
- NestJS Mongoose Conventions source files, project memory, or declared resources were checked.
- NestJS Mongoose Conventions workflow rules were applied at the relevant artifact boundary.
- NestJS Mongoose Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- NestJS Mongoose Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- BEFORE: nestjs-conventions
- WITH: typescript-api-conventions, public-api-design, code-documentation
- AFTER: skill-evolution
