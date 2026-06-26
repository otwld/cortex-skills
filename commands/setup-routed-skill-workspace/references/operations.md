# Routed Workspace Operations

Use this reference when performing user-facing operations for a routed skill
workspace. Inspect repository state before asking questions; ask only for
product intent or risk decisions that files cannot answer.

## Initialize Workspace

1. Look for existing `routed-skills.yaml`, `.skills`, `skills`, entry folders,
   module-like folders, lifecycle files, generated artifacts, and scripts.
2. Choose the root from user intent. If unspecified and no manifest exists, use
   `.skills`.
3. Create `routed-skills.yaml` from the template and set `entry.path`.
4. Create exactly one entry skill under `entry/<entry-slug>/` with `SKILL.md`,
   `agents/openai.yaml`, and `skill.yaml`.
5. Create only user-requested routed modules. Active modules need structured
   facets and at least one lifecycle file.
6. Create `commands/`, `shared/`, `generated/`, and `scripts/`.
7. Copy or adapt bundled validation and rebuild scripts when the user wants
   local scripts.
8. Rebuild catalog, graph, and cascade.
9. Validate and report the exact command and result.

## Analyze Repository

Classify existing files as entry skill candidate, routed module candidate,
command skill candidate, shared resource, generated artifact, domain-specific
content, or local tooling noise.

Extract generic principles such as entry routing, facet metadata, lifecycle
artifacts, generated catalogs, generated graphs, validation architecture, and
local resource ownership. Exclude Cortex-specific names, domain modules,
package files unless requested, IDE files, caches, and generated output.

## Create Module

1. Scan existing module names, descriptions, facets, lifecycle files, and
   resources.
2. Detect overlap through same names, similar descriptions, duplicate facet
   values, or duplicated resources.
3. If overlap is low, choose a module artifact path from the workspace taxonomy
   and create `skill.yaml` plus at least `lifecycle/activate.md`.
4. Keep new modules in `status: draft` until facets and lifecycle behavior are
   concrete enough to validate.
5. If overlap is high, create a challenge report that recommends create, merge,
   update, or reject.
6. Rebuild generated artifacts.
7. Validate.

## Create Command Skill

Create `commands/<command-name>/` with `SKILL.md`, `agents/openai.yaml`, and
`skill.yaml`. Use `activation: explicit` and `visibility: public`. Commands do
not declare lifecycle files.

When the command owns setup, discovery, intake, or normalization that may
produce a router-ready follow-up request, document that command-specific handoff
in `SKILL.md` using a `Router handoff:` block.

## Rebuild Workspace

Run:

```bash
python3 scripts/rebuild-routed-skills.py routed-skills.yaml
```

The script regenerates catalog, graph, and cascade from metadata.

## Validate Workspace

Run:

```bash
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

Validation checks structure, metadata, lifecycle files, resources, routing
facets, generated freshness, public skill metadata, operator config when
present, and local run-trace ignore policy.

## Resolve Module Overlap

Compare descriptions, facet values, lifecycle behavior, and resources.
Recommend exactly one outcome: keep separate, merge, replace, narrow one module,
or split responsibilities.
