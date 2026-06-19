
# Output Marker

Display:
using module: diary

---

# Diary

## Overview

Preserve useful work history without replacing authoritative plans, issues, ADRs, or
commits.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Determine log type; reference existing artifacts; redact sensitive data; record scope, decisions, validation, blockers, and next steps.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Diary guidance names the inspected source, request evidence, or declared resource that triggered it.
- Diary output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Diary decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Diary validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Log that Candidate search refactor passed validation and link the ADR rather than
copying it.

## Hard Stops

- Do not use Diary without direct routing evidence or a required relation.
- Do not expand Diary beyond its stated responsibility.
- Do not add placeholder Diary guidance, examples, metadata, resources, or validation.
- Do not claim Diary is satisfied without evidence for its checklist.

## Usage Checklist

- Diary trigger evidence is explicit.
- Diary source files, project memory, or declared resources were checked.
- Diary workflow rules were applied at the relevant artifact boundary.
- Diary docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Diary risks, rejected paths, and validation gaps are stated.

## Cross References

- None
