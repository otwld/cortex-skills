---
name: setup-routed-skill-workspace
description: Use only when the user explicitly includes $setup-routed-skill-workspace; creates entry-named Cortex-like routed skill workspaces and authors new routed modules or command atoms with lifecycle phases, facets, generated routing views, and validation scripts.
---

# Setup Routed Skill Workspace

## Overview

Create and extend Cortex-like routed skill workspaces. A generated workspace has
one public entry skill chosen by the user, hidden routed modules selected by
structured facets and lifecycle phase files, public command atoms, generated
catalog/graph/cascade views, and local runtime state under `.<entry>/`.

This command is an authoring command, not a migration tool.

## Local Inputs

- Use `references/routed-workspace-contract.md` for the current workspace
  shape, metadata, lifecycle, runtime, and validation contract.
- Use `references/operations.md` for init, module authoring, command authoring,
  rebuild, and validation workflows.
- Use `assets/templates/` as the source for generated files.
- Use `scripts/rebuild-routed-skills.py`, `scripts/validate-routed-skills.py`,
  and `scripts/test-validate-routed-skills.py` as the scripts copied into new
  workspaces.

## Workflow

1. Classify the request as initialize workspace, create routed module, create
   command atom, rebuild, validate, or a combination of those operations.
2. For initialization, require an explicit target root and entry slug before
   creating files.
3. For initialization, create the manifest, entry skill, default commands,
   empty module/shared/generated/script folders, generated placeholders, copied
   scripts, and `.gitignore` entry for `.<entry>/`.
4. For module creation, inspect existing module names, descriptions, facets,
   lifecycle files, and resources for overlap before adding a new module.
5. For module creation, prefer `modules/<area>/<cluster>/<module-name>/` when
   the user provides taxonomy; do not enforce depth when the target workspace
   already uses a different valid layout.
6. Create new modules as hidden routed draft atoms with empty facets and all
   lifecycle phase files so the user can fill, remove, or narrow files after
   scaffold.
7. Create new command atoms with only `SKILL.md`, `agents/openai.yaml`, and
   `skill.yaml`.
8. Rebuild generated catalog, graph, and cascade from metadata.
9. Validate before claiming the workspace or new atom is ready.

## Quality Gates

- Initialization creates exactly one public entry skill named by the user.
- Runtime config and traces are operator-local under `.<entry>/`.
- `.gitignore` ignores `.<entry>/`.
- New workspaces include `setup-routed-skill-workspace` and
  `setup-<entry>-config` command atoms by default.
- New workspaces include rebuild, validate, and validator fixture-test scripts.
- New modules are draft until their facets and lifecycle behavior are concrete.
- Command atoms do not declare lifecycle files.
- Generated artifacts are rebuilt from metadata, not hand-edited.

## Hard Stops

- Do not handle migration, legacy layouts, compatibility shims, relation graphs,
  strong/medium/weak signals, output markers, or `instructions.md` module
  files.
- Do not create starter routed modules during initialization unless the user
  explicitly asks for them.
- Do not create or commit `.<entry>/config.json` or run traces during scaffold.
- Do not create Router handoff sections in command atoms by default.
- Do not add hidden resource sharing or implicit inheritance.

## Completion Checklist

- Requested operation, target root, and entry slug are explicit.
- Created files came from current templates or copied current scripts.
- Module overlap was checked before creating a new module.
- Catalog, graph, and cascade were rebuilt.
- Workspace validation was run, or the exact blocker is stated.
