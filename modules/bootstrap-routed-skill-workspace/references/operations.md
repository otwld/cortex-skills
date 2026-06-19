# Routed Workspace Operations

Use this reference when performing a user-facing operation for a routed skill
workspace. Inspect repository state before asking questions; ask only for
product intent or risk decisions that files cannot answer.

## Initialize Workspace

1. Look for existing `routed-skills.yaml`, `.skills`, `skills`, entry folders,
   module-like folders, generated artifacts, and scripts.
2. Choose the root from user intent. If unspecified and no manifest exists, use
   `.skills`.
3. Create `routed-skills.yaml` from the template and set `entry.path`.
4. Create exactly one entry skill under `entry/<entry-slug>/` with `SKILL.md`,
   `agents/openai.yaml`, and `skill.yaml`. Do not create entry
   `instructions.md`; the `SKILL.md` body is the public entry instructions.
5. Create only the minimum routed modules: `module-creation` and
   `quality-standard`.
6. Create `shared/`, `generated/`, `scripts/`, and `proposals/`.
7. Copy or adapt the bundled validation and rebuild scripts into the target
   workspace when the user wants local scripts.
8. Rebuild catalog, graph, and cascade.
9. Validate and report the exact command and result.

## Analyze Repository

Classify existing files as entry skill candidate, routed module candidate,
explicit command candidate, shared resource, generated artifact, domain-specific
content, or local tooling noise.

Extract generic principles such as entry routing, module metadata, instruction
artifacts, generated catalogs, generated graphs, validation architecture, and
local resource ownership. Exclude domain modules, Cortex-specific names,
TypeScript assumptions, package files unless requested, IDE files, caches, and
generated output.

## Create Module

1. Scan existing module names, descriptions, strong signals, instructions,
   resources, and relations.
2. Detect overlap through same names, duplicate strong signals, similar
   descriptions, shared relations, or duplicated resources.
3. If overlap is low, create `modules/<module-name>/skill.yaml` and
   `instructions.md` from templates, preserving the `using module:
   <module-name>` output marker.
4. If overlap is high, create a challenge report that recommends create, merge,
   update, or reject.
5. Rebuild generated artifacts.
6. Validate.

Creation should be direct when risk is low. Challenge only when overlap,
ambiguity, or routing risk is detected.

## Create Explicit Command

Create a module-shaped folder with `activation: explicit` and
`visibility: public`. Its instructions must say it runs only when directly
invoked and preserve the `using skill: <command-name>` output marker. Do not
include explicit commands in routed cascade selection.

## Rebuild Workspace

Run the rebuild script from the workspace root or pass the manifest path:

```bash
python3 scripts/rebuild-routed-skills.py routed-skills.yaml
```

The script regenerates the catalog, graph, and cascade from metadata and
overwrites manual edits in generated files.

## Validate Workspace

Run:

```bash
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

Validation checks structure, metadata, relations, resources, routing
constraints, generated freshness, explicit command exclusion, duplicate strong
signals, and the public entry's agent-skill shape.

## Propose Merge

Compare descriptions, routing signals, relations, instructions, and resources.
Recommend exactly one outcome: keep separate, merge, replace, narrow one module,
or split responsibilities. Store the proposal under `proposals/` only when the
user asks for a durable artifact.
