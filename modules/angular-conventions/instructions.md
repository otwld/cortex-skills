
# Output Marker

Display:
using module: angular-conventions

---

# Angular Conventions

## Overview

Apply Angular guidance only when the project uses Angular and local version support is
known.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Prefer supported standalone APIs; use local DI style; keep complex templates/styles external; type forms; document public inputs and outputs.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Angular Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- Angular Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Angular Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Angular Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

CandidatePipelineComponent exposes a documented jobOffer input and stageChange output
instead of reaching into route state directly.

## Hard Stops

- Do not use Angular Conventions without direct routing evidence or a required relation.
- Do not expand Angular Conventions beyond its stated responsibility.
- Do not add placeholder Angular Conventions guidance, examples, metadata, resources, or validation.
- Do not claim Angular Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- Angular Conventions trigger evidence is explicit.
- Angular Conventions source files, project memory, or declared resources were checked.
- Angular Conventions workflow rules were applied at the relevant artifact boundary.
- Angular Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Angular Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: rxjs-conventions, typescript-code-style, code-documentation
- AFTER: skill-evolution
