
# Output Marker

Display:
using module: completion-verification

---

# Completion Verification

## Overview

Treat completion as a current-state claim that requires authoritative evidence for every
requirement.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Derive requirements; identify proof; run or inspect fresh evidence; compare evidence to claim; report gaps and risks.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Completion Verification guidance names the inspected source, request evidence, or declared resource that triggered it.
- Completion Verification output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Completion Verification decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Completion Verification validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

After a module migration, validation ok is necessary but also confirm new modules,
references, catalog, graph, and tests exist.

## Hard Stops

- Do not use Completion Verification without direct routing evidence or a required relation.
- Do not expand Completion Verification beyond its stated responsibility.
- Do not add placeholder Completion Verification guidance, examples, metadata, resources, or validation.
- Do not claim Completion Verification is satisfied without evidence for its checklist.

## Usage Checklist

- Completion Verification trigger evidence is explicit.
- Completion Verification source files, project memory, or declared resources were checked.
- Completion Verification workflow rules were applied at the relevant artifact boundary.
- Completion Verification docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Completion Verification risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: review-gate, branch-completion
