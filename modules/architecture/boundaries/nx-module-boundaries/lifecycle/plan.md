# Nx Module Boundaries Plan

## Overview

Plan Nx boundary changes so tags, dependency constraints, and imports continue to
encode real project ownership.

## Workflow

1. Identify the importing project, imported project, and runtime for each edge.
2. Compare current tags and dependency constraints to the actual responsibility
   of both projects.
3. Prefer moving ownership or changing the import path over loosening rules.
4. Change tags only when the project's responsibility has changed.
5. Name the lint, graph, or affected validation that will prove the edge is legal.

## Quality Gates

- Cross-project consumers use a supported entry point.
- Browser projects do not gain server-only or Node-only dependencies through a
  shared import path.
- Boundary configuration changes describe architecture intent, not a one-off
  exception.
- Tag, export, import, and validation changes are planned together.

## Hard Stops

- Do not make utility projects import feature, UI, or application internals.
- Do not use a boundary rule change as the first fix for misplaced ownership.
- Do not skip validation when tags or dependency constraints changed.

## Phase Output

- Return the intended dependency edge, tag or rule changes, import rewrites,
  validation command, and unresolved ownership decisions.
