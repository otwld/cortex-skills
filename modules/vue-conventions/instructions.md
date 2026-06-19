
# Output Marker

Display:
using module: vue-conventions

---

# Vue Conventions

## Overview

Keep Vue component public surfaces small, typed, and aligned with reactive ownership.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Use local Vue style; type props and emits; prefer computed derived state; extract composables only for real reuse; document slots.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Vue Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- Vue Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Vue Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Vue Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

CandidateStagePicker emits stageSelected with a typed stage payload and documents
disabled-stage behavior.

## Hard Stops

- Do not use Vue Conventions without direct routing evidence or a required relation.
- Do not expand Vue Conventions beyond its stated responsibility.
- Do not add placeholder Vue Conventions guidance, examples, metadata, resources, or validation.
- Do not claim Vue Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- Vue Conventions trigger evidence is explicit.
- Vue Conventions source files, project memory, or declared resources were checked.
- Vue Conventions workflow rules were applied at the relevant artifact boundary.
- Vue Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Vue Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: typescript-code-style, rxjs-conventions, code-documentation
- AFTER: skill-evolution
