
# Output Marker

Display:
using module: rxjs-conventions

---

# RxJS Conventions

## Overview

Make time, ownership, cancellation, and errors clear in observable code.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Prefer composition over nested subscriptions; choose flattening operators by concurrency semantics; justify subjects and multicasting.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- RxJS Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- RxJS Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- RxJS Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- RxJS Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Candidate typeahead uses switchMap because newer search text cancels older requests.

## Hard Stops

- Do not use RxJS Conventions without direct routing evidence or a required relation.
- Do not expand RxJS Conventions beyond its stated responsibility.
- Do not add placeholder RxJS Conventions guidance, examples, metadata, resources, or validation.
- Do not claim RxJS Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- RxJS Conventions trigger evidence is explicit.
- RxJS Conventions source files, project memory, or declared resources were checked.
- RxJS Conventions workflow rules were applied at the relevant artifact boundary.
- RxJS Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- RxJS Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
