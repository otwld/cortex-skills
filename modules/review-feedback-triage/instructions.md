
# Output Marker

Display:
using module: review-feedback-triage

---

# Review Feedback Triage

## Overview

Classify feedback before applying it so correct principles do not become bad patches.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Read context; classify each item; verify the claim; apply, adapt, defer, or reject; respond with evidence.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Review Feedback Triage guidance names the inspected source, request evidence, or declared resource that triggered it.
- Review Feedback Triage output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Review Feedback Triage decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Review Feedback Triage validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

A suggestion to add a generic Candidate filter helper is checked for stable duplication
before extraction.

## Hard Stops

- Do not use Review Feedback Triage without direct routing evidence or a required relation.
- Do not expand Review Feedback Triage beyond its stated responsibility.
- Do not add placeholder Review Feedback Triage guidance, examples, metadata, resources, or validation.
- Do not claim Review Feedback Triage is satisfied without evidence for its checklist.

## Usage Checklist

- Review Feedback Triage trigger evidence is explicit.
- Review Feedback Triage source files, project memory, or declared resources were checked.
- Review Feedback Triage workflow rules were applied at the relevant artifact boundary.
- Review Feedback Triage docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Review Feedback Triage risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: systematic-debugging, test-first-discipline, completion-verification, review-gate
