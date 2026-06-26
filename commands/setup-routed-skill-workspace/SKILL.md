---
name: setup-routed-skill-workspace
description: Use only when the user explicitly includes $setup-routed-skill-workspace; sets up, analyzes, validates, rebuilds, or evolves generic routed skill workspaces with lifecycle atoms, structured facets, local resources, generated catalogs and graphs, and deterministic integrity checks.
---

# Setup Routed Skill Workspace

## Overview

This command skill runs only when directly invoked as
`$setup-routed-skill-workspace`.

Create and maintain routed skill workspaces without preserving Cortex-specific
structure. Treat module folders and `skill.yaml` metadata as the source of
truth, lifecycle files as runtime behavior, and generated catalogs, graphs, and
cascades as disposable outputs.

## Local Inputs

- Use `references/routed-workspace-contract.md` when defining workspace shape,
  metadata, lifecycle phases, facets, generated artifacts, or validation rules.
- Use `references/operations.md` when initializing, analyzing, creating modules
  or command skills, rebuilding, validating, or resolving module overlap.
- Use `scripts/rebuild-routed-skills.py` to regenerate target workspace artifacts.
- Use `scripts/validate-routed-skills.py` to check target workspace integrity.

## Workflow

1. Inspect first: find any `routed-skills.yaml`, `.skills`, `skills`, entry folders, module-like folders, lifecycle files, generated artifacts, and local validation scripts before asking the user for choices.
2. Identify the target root from user intent or the manifest; default to `.skills` only when no stronger evidence exists.
3. Apply the generic contract: exactly one public entry skill, hidden routed modules, public command atoms, structured facets, lifecycle files, explicit resource ownership, and optional command handoff through a visible `Router handoff:` block.
4. Use templates from `assets/templates/` for scaffolded files, then adapt names, descriptions, facets, and lifecycle files to the requested workspace.
5. When creating or realigning command skills, define any command-owned entry handoff in `SKILL.md`; do not add handoff metadata to `skill.yaml`.
6. Rebuild generated artifacts from metadata with the bundled rebuild script.
7. Validate structure, metadata, lifecycle files, resources, routing facets, generated freshness, and ignored run traces before reporting completion.
8. When overlap, ambiguity, or risk is detected, present a challenge report instead of adding another module silently.

## Quality Gates

- The target workspace has exactly one public entry skill.
- The public entry skill is a valid agent skill folder with `SKILL.md`; routed metadata alone is not enough.
- Routed modules are hidden, command atoms are public, and generated artifacts are derived from metadata.
- Active routed modules have structured facets and at least one declared lifecycle file.
- Lifecycle files do not name peer modules or route other atoms.
- Routing remains reviewable through facets, lifecycle declarations, generated graph/cascade files, and local run traces.
- Shared behavior is named through `uses` or resources; no implicit inheritance or hidden coupling is introduced.
- Module category folders are readability containers only; they do not create routing behavior, inheritance, or implicit resources.
- Public entry and command skills include complete `agents/openai.yaml` interface metadata and keep implicit invocation disabled.
- Validation evidence is current when claiming that a routed workspace is ready.

## Example

When asked to create `$ascend`, initialize `.skills/routed-skills.yaml`, create
one public entry skill under `entry/ascend/` with `SKILL.md`,
`agents/openai.yaml`, and `skill.yaml`, add only requested modules with
structured facets and lifecycle files, generate the catalog, graph, and cascade,
then validate the workspace.

## Hard Stops

- Do not create multiple entry skills.
- Do not require `MODULE.md`, Cortex naming, Cortex category folders, TypeScript assumptions, package registries, or domain starter packs in target workspaces.
- Do not hand-edit generated target artifacts as if they were source files.
- Do not add module relations, relation language, inheritance, shims, compatibility layers, or hidden resource sharing.
- Do not create a new module when existing modules have high-overlap facets or responsibilities without presenting a challenge report.
- Do not claim a generated workspace is valid without running the routed workspace validator or naming the validation gap.

## Completion Checklist

- Existing workspace shape or absence was inspected.
- Root, entry slug, and manifest path are explicit.
- Entry, routed modules, command skills, resources, lifecycle files, and generated artifacts follow the generic contract.
- Command handoff behavior was preserved, added, or ruled out at the command instruction boundary.
- Overlap, facet ambiguity, and missing active-module lifecycle files were checked before creating modules.
- Catalog, graph, and cascade were rebuilt from metadata.
- Routed workspace validation was run or the remaining blocker is stated.
