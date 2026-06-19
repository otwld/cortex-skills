
# Output Marker

Display:
using module: review-gate

---

# Review Gate

## Overview

Review major work before publishing, starting with requirement fit before code quality.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Identify requirements and diff; review coverage; inspect correctness, tests, APIs, docs, and boundaries; classify findings; verify fixes.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Review Gate guidance names the inspected source, request evidence, or declared resource that triggered it.
- Review Gate output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Review Gate decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Review Gate validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

A module catalog review checks discoverability, routing, metadata, graph, and validation,
not just Markdown formatting.

## Hard Stops

- Do not use Review Gate without direct routing evidence or a required relation.
- Do not expand Review Gate beyond its stated responsibility.
- Do not add placeholder Review Gate guidance, examples, metadata, resources, or validation.
- Do not claim Review Gate is satisfied without evidence for its checklist.

## Usage Checklist

- Review Gate trigger evidence is explicit.
- Review Gate source files, project memory, or declared resources were checked.
- Review Gate workflow rules were applied at the relevant artifact boundary.
- Review Gate docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Review Gate risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: agent-delegation, completion-verification, review-feedback-triage, public-api-design, architecture-drift-detector
