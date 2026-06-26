# Bundle Performance Verify

## Overview

Verify that bundle-sensitive changes are measured or supported by clear static
evidence.

## Workflow

1. Run the repository's available build, bundle analyzer, size-limit, or chunk
   report for the affected package or application when practical.
2. Compare changed chunks, entry points, dependency graphs, or analyzer output
   against the expected impact.
3. When no measurement tool is available, inspect manifests, export maps, barrels,
   side-effect declarations, and import paths to show why unaffected consumers do
   not pull the new cost.
4. Confirm optional integrations remain lazy or separately addressable.
5. Record any accepted bundle increase and the product reason it is required.

## Quality Gates

- Verification evidence names the command, analyzer output, changed chunk, or
  static import path inspected.
- Unaffected consumers are protected by a narrow entry point, lazy boundary, or
  side-effect-free import graph.
- Remaining measurement gaps are explicit and tied to missing tooling or runtime
  constraints.

## Hard Stops

- Do not report bundle safety from a successful type check or unit test alone.
- Do not finish broad shared-import changes without measurement or static import
  evidence.
- Do not leave unexplained package, lockfile, export-map, or side-effect changes.

## Phase Output

- Return bundle commands run, analyzer or static evidence, accepted size tradeoffs,
  and unresolved measurement gaps.
