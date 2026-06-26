# Changelog

## Unreleased

- Replaced module relations with atom-local structured facets and lifecycle
  phase files.
- Removed routed module `instructions.md`; runtime behavior now belongs in
  `lifecycle/<phase>.md`.
- Repurposed `generated/module-graph.md` as a bipartite module-to-facet and
  module-to-phase graph.
- Added `.codex/config.json` bootstrap behavior and the `$setup-cortex-config`
  command atom.
- Added local run traces under ignored `.cortex/runs/`.
- Removed public output marker requirements.
- Updated rebuild and validation scripts for facets, lifecycle declarations,
  operator config validation, and run-trace ignore policy.
