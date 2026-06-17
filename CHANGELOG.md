# Changelog

## Unreleased

### Added

- Added the `bricks` tool skill for Bricks consumer workflows and
  worktree-based source contribution guidance.
- Added catalog synchronization and taxonomy-heading checks to the workspace
  validator.
- Added validator fixture regression tests for skill discovery, catalog
  taxonomy, and support-file references.
- Added validation that OpenAI metadata fields live under the required
  `interface:` block.

### Changed

- Converted Cortex routing to an explicit public `$cortex` skill backed by internal
  `MODULE.md` files, hiding non-public guidance from direct Codex skill
  invocation.
- Converted setup workflows into explicit-only command skills under
  `governance/setup/`, with OpenAI metadata that disables implicit invocation
  and excludes them from `$cortex` module routing.
- Replaced the skill graph and cascade references with module routing references.
- Replaced the validator's closed per-skill directory registry with generic
  taxonomy path validation.

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
