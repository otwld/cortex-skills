# Changelog

## Unreleased

### Added

- Added the `$setup-routed-skill-workspace` command skill for
  creating and maintaining generic routed skill workspaces.
- Added the `bricks` tool skill for Bricks consumer workflows and
  worktree-based source contribution guidance.
- Added routed workspace rebuild and validation scripts.
- Added validator fixture regression tests for routed workspace structure,
  metadata, generated freshness, resources, and command skill handling.
- Added always-loaded module support through `routing.always`, used by Cortex
  for `no-transitional-architecture`.
- Added validator checks for active module reachability, legacy-only declared
  resources, required instruction sections, copied template prose, and repeated
  instruction bullets.
- Added validator checks for direct strong signal wording, title-swapped module
  instruction boilerplate, and required public `agents/openai.yaml` interface
  metadata.
- Added setup workspace template fixture coverage for empty generic workspaces,
  active modules with concrete signals, and active modules missing signals.

### Changed

- Aggressively realigned the repository to the generic routed skill workspace
  contract: one public `$cortex` entry, hidden routed modules, command skill
  metadata, shared resources, and generated routing artifacts.
- Replaced hand-maintained root catalog, graph, and cascade files with
  `generated/` outputs rebuilt from `skill.yaml` metadata.
- Replaced the Cortex taxonomy validator with routed workspace rebuild and
  validation scripts.
- Moved direct-invocation setup workflows into full public command skills under
  `commands/` with `SKILL.md` and `agents/openai.yaml`.
- Renamed setup command skills to the `$setup-*` naming convention.
- Replaced taxonomy folders and `MODULE.md` files with `modules/<name>/`
  folders containing `instructions.md` and `skill.yaml`.
- Narrowed broad routing signals for architecture drift, architecture
  deepening, test runners, verification, review, and branch completion.
- Removed legacy-only extracted pattern resources from active routed modules.
- Replaced repeated routed-module instruction boilerplate with concrete
  module-specific quality gates, hard stops, and usage checklist items.
- Aligned `$setup-routed-skill-workspace` templates and contract references with
  stricter active-module signal and instruction-quality validation.

## v0.1.0 Public Seed - 2026-05-28

Initial public seed of Cortex Skills.

### Added

- 27 governed AI skills for architecture, documentation, frameworks,
  maintenance, testing, and TypeScript workflows.
- OpenAI-facing `agents/openai.yaml` metadata for every skill.
- Central cross-skill graph in `references/skill-graph.md`.
- Workspace validator in `scripts/validate-skills.py`.
- Recruitment job-board example universe for illustrative examples.
- Public README, skill catalog, contribution guide, MIT license, and validation
  CI workflow.

### Notes

- This is a practical v0.1 release. The repository structure and validator are
  the main public contract.
- Skills are project-agnostic even though the public brand is Cortex Skills.
