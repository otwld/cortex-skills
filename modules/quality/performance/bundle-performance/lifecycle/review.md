# Bundle Performance Review

## Overview

Review diffs for bundle regressions that come from shared imports, side effects,
or dependency movement.

## Workflow

1. Inspect package manifests, lockfiles, export maps, build configuration, index
   files, barrels, CSS imports, global setup, and shared UI imports.
2. Follow new imports from shared entry points to identify heavy transitive
   dependencies.
3. Flag optional integrations that moved into core runtime paths.
4. Check side-effect metadata and import-time behavior against the bundler's
   ability to drop unused code.
5. Require measurement or a precise static argument for changes that broaden a
   commonly imported path.

## Quality Gates

- Findings name the import path, dependency, entry point, or side effect that
  creates measurable or likely bundle cost.
- Review distinguishes shipped runtime cost from test-only or build-only changes.
- Public import compatibility concerns are reported separately from size concerns.

## Hard Stops

- Do not approve broad root-export changes when their consumers and dependency
  cost are unknown.
- Do not accept "tree-shaking should handle it" without side-effect and import
  evidence.
- Do not ignore lockfile changes when the source diff adds a runtime import.

## Phase Output

- Return review findings with affected consumers, suspected bundle mechanism,
  required measurement, and compatibility risk.
