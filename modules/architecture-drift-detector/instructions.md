
# Output Marker

Display:
using module: architecture-drift-detector

---

# Architecture Drift Detector

## Overview

Detect early structural risk from churn, repeated fixes, and ownership drift before it
becomes a rewrite.

## Reference Routing

- Use `shared/architecture-deepening.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Use concrete signals; escalate only when risk is tied to a module, seam, package, or project area; recommend focused review instead of broad rewrites.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Architecture Drift Detector guidance names the inspected source, request evidence, or declared resource that triggered it.
- Architecture Drift Detector output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Architecture Drift Detector decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Architecture Drift Detector validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Three changes touch Candidate search, Application persistence, and query helpers;
recommend reviewing the search seam before adding another filter.

## Hard Stops

- Do not use Architecture Drift Detector without direct routing evidence or a required relation.
- Do not expand Architecture Drift Detector beyond its stated responsibility.
- Do not add placeholder Architecture Drift Detector guidance, examples, metadata, resources, or validation.
- Do not claim Architecture Drift Detector is satisfied without evidence for its checklist.

## Usage Checklist

- Architecture Drift Detector trigger evidence is explicit.
- Architecture Drift Detector source files, project memory, or declared resources were checked.
- Architecture Drift Detector workflow rules were applied at the relevant artifact boundary.
- Architecture Drift Detector docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Architecture Drift Detector risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: architecture-deepening-review, library-placement-decision, nx-module-boundaries
