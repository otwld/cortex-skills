
# Output Marker

Display:
using module: nx-conventions

---

# Nx Conventions

## Overview

Treat Nx configuration as shared infrastructure for graph accuracy, target semantics,
and cache behavior.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect project metadata; preserve target inputs/outputs; avoid root config churn; coordinate project moves with boundaries.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Nx Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- Nx Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Nx Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Nx Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

A job-offer-search library gets project tags that match domain scope, not a vague
shared-search label.

## Hard Stops

- Do not use Nx Conventions without direct routing evidence or a required relation.
- Do not expand Nx Conventions beyond its stated responsibility.
- Do not add placeholder Nx Conventions guidance, examples, metadata, resources, or validation.
- Do not claim Nx Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- Nx Conventions trigger evidence is explicit.
- Nx Conventions source files, project memory, or declared resources were checked.
- Nx Conventions workflow rules were applied at the relevant artifact boundary.
- Nx Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Nx Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: nx-module-boundaries, library-placement-decision
