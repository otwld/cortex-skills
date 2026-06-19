
# Output Marker

Display:
using module: typescript-api-conventions

---

# TypeScript API Conventions

## Overview

Design TypeScript public APIs that make invalid states hard and supported states
obvious.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Identify consumers; use explicit exports; prefer discriminated unions; constrain generics; avoid optional-field state bags; document invariants.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- TypeScript API Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- TypeScript API Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- TypeScript API Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- TypeScript API Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

CandidateApplicationState as submitted, interviewing, offered, or rejected variants is
safer than one loose object.

## Hard Stops

- Do not use TypeScript API Conventions without direct routing evidence or a required relation.
- Do not expand TypeScript API Conventions beyond its stated responsibility.
- Do not add placeholder TypeScript API Conventions guidance, examples, metadata, resources, or validation.
- Do not claim TypeScript API Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- TypeScript API Conventions trigger evidence is explicit.
- TypeScript API Conventions source files, project memory, or declared resources were checked.
- TypeScript API Conventions workflow rules were applied at the relevant artifact boundary.
- TypeScript API Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- TypeScript API Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: public-api-design, naming-consistency, typescript-code-style, code-documentation
