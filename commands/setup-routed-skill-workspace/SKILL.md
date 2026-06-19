---
name: setup-routed-skill-workspace
description: Use only when the user explicitly includes $setup-routed-skill-workspace; sets up, analyzes, validates, rebuilds, or evolves generic routed skill workspaces with one public entry skill, hidden routed modules, command skills, explicit routing metadata, local resources, generated catalogs and graphs, and deterministic integrity checks.
---

# Output Marker

Display:
using skill: setup-routed-skill-workspace

---

# Setup Routed Skill Workspace

## Overview

This command skill runs only when directly invoked as `$setup-routed-skill-workspace`.


Create and maintain routed skill workspaces without preserving Cortex-specific
structure. Treat module folders and their metadata as the source of truth, and
treat generated catalogs, graphs, and cascades as disposable outputs.

## Reference Routing

- Use `references/routed-workspace-contract.md` when defining workspace shape,
  metadata, routing, relations, generated artifacts, or validation rules.
- Use `references/operations.md` when initializing, analyzing, creating modules
  or command skills, rebuilding, validating, or proposing merges.
- Use `scripts/rebuild-routed-skills.py` to regenerate target workspace artifacts.
- Use `scripts/validate-routed-skills.py` to check target workspace integrity.

## Workflow

1. Inspect first: find any `routed-skills.yaml`, `.skills`, `skills`, entry
   folders, module-like folders, generated artifacts, and local validation
   scripts before asking the user for choices.
2. Identify the target root from user intent or the manifest; default to
   `.skills` only when no stronger evidence exists.
3. Apply the generic contract: exactly one public entry skill, hidden routed
   modules, command skills outside routing, explicit relations, and explicit
   resource ownership.
4. Use templates from `assets/templates/` for scaffolded files, then adapt names,
   descriptions, signals, and instructions to the user's requested workspace.
5. Rebuild generated artifacts from metadata with the bundled rebuild script.
6. Validate structure, metadata, relations, resources, routing constraints, and
   generated freshness with the bundled validator before reporting completion.
7. When overlap, ambiguity, or risk is detected, create a challenge or merge
   proposal instead of adding another module silently.

## Quality Gates

- The target workspace has exactly one public entry skill.
- The public entry skill is a valid agent skill folder with `SKILL.md`;
  routed metadata alone is not enough.
- The public entry uses `SKILL.md` as its instructions file; do not add entry
  `instructions.md`.
- Routed modules are hidden, command skills are public and direct-invocation
  only, and generated artifacts are derived from metadata.
- Routing remains reviewable through strong, medium, and weak signals plus
  priority and explicit relations.
- Active routed modules have at least one direct routing signal; draft modules
  may remain incomplete while trigger evidence is still being designed.
- Active module gates, hard stops, and checklists are concrete to the module
  responsibility rather than title-swapped scaffold text.
- Shared behavior is named through `uses` or resources; no implicit inheritance
  or hidden coupling is introduced.
- Public entry and command skills include complete `agents/openai.yaml`
  interface metadata and keep implicit invocation disabled.
- Generic scaffolds start with the public entry and user-requested modules only;
  Cortex-specific always-loaded modules are not copied into new workspaces by default.
- Validation evidence is current when claiming that a routed workspace is ready.

## Example

When asked to create `$ascend`, initialize `.skills/routed-skills.yaml`, create
one public entry skill under `entry/ascend/` with `SKILL.md`,
`agents/openai.yaml`, and `skill.yaml`, add only user-requested modules with
concrete routing signals or leave them as drafts, generate the catalog, graph,
and cascade, then validate the workspace.

## Hard Stops

- Do not create multiple entry skills.
- Do not require `MODULE.md`, Cortex naming, taxonomy folders, TypeScript
  assumptions, package registries, or domain starter packs in target workspaces.
- Do not hand-edit generated target artifacts as if they were source files.
- Do not add embeddings, classifiers, scoring engines, vector databases,
  inheritance, shims, compatibility layers, or hidden resource sharing.
- Do not create a new module when existing modules have high-overlap strong
  signals or responsibilities without presenting a challenge report.
- Do not claim a generated workspace is valid without running the routed
  workspace validator or naming the validation gap.

## Usage Checklist

- Existing workspace shape or absence was inspected.
- Root, entry slug, and manifest path are explicit.
- Entry, routed modules, command skills, resources, and generated artifacts
  follow the generic contract.
- Overlap, relation conflicts, and missing active-module signals were checked
  before creating modules.
- Catalog, graph, and cascade were rebuilt from metadata.
- Routed workspace validation was run or the remaining blocker is stated.

## Cross References

- None
