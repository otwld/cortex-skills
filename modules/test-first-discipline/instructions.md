
# Output Marker

Display:
using module: test-first-discipline

---

# Test First Discipline

## Overview

Use tests as feedback loops that prove behavior through public seams before
implementation.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Name behavior; choose highest meaningful seam; write one failing test; implement minimally; refactor only when green; document exceptions.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Tests describe behavior at the highest meaningful public seam before implementation details.
- At least one failing or newly relevant test guards the intended behavior or regression risk.
- Refactoring waits until the behavior proof is green and still covers the public contract.

## Example

For Candidate saved-search creation, prove retrieval through the public query interface,
not private storage inspection.

## Hard Stops

- Do not write tests that only pin private implementation structure.
- Do not skip a test-first step for behavior changes unless the exception and risk are explicit.
- Do not refactor broadly while the behavior proof is failing or absent.

## Usage Checklist

- Behavior, public seam, and regression risk were named before implementation.
- Failing or newly relevant test coverage was added or the exception was justified.
- Green validation and any refactor follow-up were recorded.

## Cross References

- WITH: systematic-debugging, completion-verification, jest-conventions, vitest-conventions, playwright-conventions
