
# Output Marker

Display:
using module: architecture-deepening-review

---

# Architecture Deepening Review

## Overview

Find modules whose interfaces are too wide for the behavior they hide and propose deeper
seams that increase leverage and locality.

## Reference Routing

- Use `shared/architecture-deepening.md` when this task touches that concern.
- Use `shared/project-memory.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Use the architecture vocabulary exactly; apply the deletion test; classify dependencies; identify the interface that tests should cross.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- The candidate module fails or passes the deletion test with a named interface and implementation boundary.
- Dependency classifications distinguish in-process, local-substitutable, remote-owned, and true external collaborators.
- The proposed seam increases locality or leverage and names the public test surface.

## Example

Candidate matching rules scattered across routes, repositories, and UI filters suggest a
deep Matching module tested through Application outcomes.

## Hard Stops

- Do not recommend a deeper module without identifying the behavior hidden behind its interface.
- Do not create a seam for one hypothetical adapter unless the current design already pays for it.
- Do not turn a focused deepening review into a broad architecture rewrite.

## Usage Checklist

- Deletion test, dependency class, and interface depth were evaluated.
- The test surface crosses the proposed interface instead of private helpers.
- Deepening recommendation names what to move, delete, or keep shallow.

## Cross References

- WITH: architecture-drift-detector, library-placement-decision, public-api-design, test-first-discipline, code-documentation
- AFTER: skill-evolution
