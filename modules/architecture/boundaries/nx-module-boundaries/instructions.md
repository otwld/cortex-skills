
# Output Marker

Display:
using module: nx-module-boundaries

---

# Nx Module Boundaries

## Overview

Use Nx graph metadata and tags as executable architecture, not paperwork to bypass.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect tags and graph; keep dependency direction valid; fix ownership instead of weakening rules; update tags only when responsibility changes.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Tags, dependency constraints, and project relationships preserve intended ownership direction.
- Boundary fixes change ownership or imports before weakening lint rules.
- New projects or moves include matching tags, exports, and dependency validation.

## Example

Interview scheduling consumes Candidate domain contracts through an approved entry
point, not another feature project internals.

## Hard Stops

- Do not silence module-boundary violations by relaxing rules before finding the ownership mismatch.
- Do not add tags that describe desired access rather than actual project responsibility.
- Do not introduce imports that bypass public entry points or project graph constraints.

## Usage Checklist

- Existing tags, dependency constraints, and graph edges were inspected.
- Boundary changes preserve or intentionally correct dependency direction.
- Nx lint, graph, or affected validation was named.

## Cross References

- BEFORE: library-placement-decision
- WITH: public-api-design
