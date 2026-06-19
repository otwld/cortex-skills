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
