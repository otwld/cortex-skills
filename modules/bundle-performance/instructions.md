
# Output Marker

Display:
using module: bundle-performance

---

# Bundle Performance

## Overview

Prevent shared imports from accumulating global bundle cost through side effects, broad
barrels, or heavy optional dependencies.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Keep root entry points narrow; isolate optional integrations; preserve tree-shaking; document intentional bundle tradeoffs.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Bundle Performance guidance names the inspected source, request evidence, or declared resource that triggered it.
- Bundle Performance output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Bundle Performance decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Bundle Performance validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

JobOffer charting helpers live behind a charts entry point so Candidate list pages avoid
charting dependencies.

## Hard Stops

- Do not use Bundle Performance without direct routing evidence or a required relation.
- Do not expand Bundle Performance beyond its stated responsibility.
- Do not add placeholder Bundle Performance guidance, examples, metadata, resources, or validation.
- Do not claim Bundle Performance is satisfied without evidence for its checklist.

## Usage Checklist

- Bundle Performance trigger evidence is explicit.
- Bundle Performance source files, project memory, or declared resources were checked.
- Bundle Performance workflow rules were applied at the relevant artifact boundary.
- Bundle Performance docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Bundle Performance risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: public-api-design
