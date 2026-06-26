# Nx Module Boundaries Activate

## Overview

Activate only when Nx workspace evidence exists and the task changes or reviews
project ownership, project tags, dependency constraints, or imports crossing
project boundaries.

## Workflow

1. Inspect `nx.json`, project configuration, workspace ESLint configuration, and
   existing tag vocabulary.
2. Identify the source and target projects for each proposed dependency.
3. Inspect runtime expectations for browser-only, server-only, and shared
   TypeScript code.
4. Look for imports that bypass supported package or project entry points.
5. If no Nx configuration is present, report that Nx boundary constraints do not
   apply.

## Quality Gates

- Activation evidence names the projects, tags, dependency edge, runtime
  constraint, and boundary files involved.
- Tags are treated as responsibility metadata rather than permissions requested
  by a single import.
- The task actually changes or evaluates an Nx project boundary.

## Hard Stops

- Do not relax a dependency constraint until the ownership mismatch has been
  identified.
- Do not add a tag that describes desired access rather than actual project
  responsibility.
- Do not introduce internal project imports that skip supported entry points.

## Phase Output

- State the Nx evidence found, involved projects, current tags, dependency edge,
  runtime constraint, and boundary files requiring inspection.
