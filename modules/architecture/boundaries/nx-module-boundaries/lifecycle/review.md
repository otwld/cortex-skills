# Nx Module Boundaries Review

## Overview

Review Nx changes for responsibility-accurate tags, legal dependency direction,
supported entry points, and runtime-compatible imports.

## Workflow

1. Inspect diffs to `nx.json`, project configuration, ESLint boundary rules, tags,
   and path aliases.
2. Inspect new or changed imports across project boundaries.
3. Review Nx lint, graph inspection, or targeted import-search output.
4. Check runtime-specific dependencies introduced through shared projects.

## Quality Gates

- Tags describe the project as it exists after the change.
- Dependency constraints still encode the intended architecture direction.
- Public entry points are the only cross-project import surface.
- Nx validation was run or the skipped validation risk is explicit.

## Hard Stops

- Reject rule or tag changes that permit an import without changing project
  responsibility.
- Reject imports from another project's internals.
- Reject dependency direction from lower-level libraries into features, UI, apps,
  or runtime-specific code.

## Phase Output

- Return boundary findings with project names, tag or rule risks, illegal import
  paths, and required validation.
