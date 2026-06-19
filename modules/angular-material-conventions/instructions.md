
# Output Marker

Display:
using module: angular-material-conventions

---

# Angular Material And CDK Conventions

## Overview

Use Material and CDK narrowly while preserving accessibility, theming, and bundle
boundaries.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Import only used APIs; prefer CDK primitives for overlays and a11y; preserve focus and keyboard behavior; justify density changes.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Angular Material And CDK Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- Angular Material And CDK Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Angular Material And CDK Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Angular Material And CDK Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

An Interview scheduling dialog uses CDK focus handling and a documented close result
instead of custom keyboard traps.

## Hard Stops

- Do not use Angular Material And CDK Conventions without direct routing evidence or a required relation.
- Do not expand Angular Material And CDK Conventions beyond its stated responsibility.
- Do not add placeholder Angular Material And CDK Conventions guidance, examples, metadata, resources, or validation.
- Do not claim Angular Material And CDK Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- Angular Material And CDK Conventions trigger evidence is explicit.
- Angular Material And CDK Conventions source files, project memory, or declared resources were checked.
- Angular Material And CDK Conventions workflow rules were applied at the relevant artifact boundary.
- Angular Material And CDK Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Angular Material And CDK Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- BEFORE: angular-conventions
- WITH: bundle-performance, typescript-code-style, code-documentation
- AFTER: skill-evolution
