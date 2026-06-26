
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

- Each review item is verified against code, tests, CI, or docs before action.
- Feedback is classified as apply, adapt, defer, reject, or needs clarification with evidence.
- Responses address the reviewer's technical concern without introducing unrelated cleanup.

## Example

A suggestion to add a generic Candidate filter helper is checked for stable duplication
before extraction.

## Hard Stops

- Do not implement reviewer suggestions blindly when the claim is unverified or outdated.
- Do not reject feedback without citing the code, test, or requirement that contradicts it.
- Do not expand triage into unrelated refactors while addressing requested changes.

## Usage Checklist

- Review context, changed files, and relevant validation were inspected.
- Each item received an evidence-backed disposition.
- Applied fixes and reviewer responses were verified before completion.

## Cross References

- WITH: systematic-debugging, test-first-discipline, completion-verification, review-gate
