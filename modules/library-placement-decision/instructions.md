
# Output Marker

Display:
using module: library-placement-decision

---

# Library Placement Decision

## Overview

Choose code location by responsibility, dependency direction, and consumer scope instead
of convenience.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Classify domain, integration, feature, UI, utility, or adapter responsibility; use existing owners; split mixed responsibilities.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- New or moved code has a named domain, integration, feature, UI, utility, or adapter owner.
- Placement preserves existing dependency direction, tags, entry points, and package responsibilities.
- Mixed responsibilities are split or kept local rather than hidden in a shared library.

## Example

Candidate ranking shared by search and recommendations belongs in a domain-owned module;
a page-specific ranking panel stays in the feature.

## Hard Stops

- Do not create a shared library before proving stable ownership and consumers.
- Do not move code across a boundary to avoid updating imports or tests.
- Do not weaken module boundaries when the real problem is misplaced ownership.

## Usage Checklist

- Existing owners, project graph, tags, and public entry points were inspected.
- Responsibility class and dependency direction were chosen before file moves.
- Placement decision includes exports, tests, docs, and boundary validation impact.

## Cross References

- WITH: nx-module-boundaries, public-api-design, naming-consistency
- AFTER: skill-evolution
