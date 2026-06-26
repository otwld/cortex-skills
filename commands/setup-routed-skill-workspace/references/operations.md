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
5. Create only user-requested routed modules. A generic scaffold may start with
   no routed modules; do not copy Cortex-specific always-loaded modules unless
   the user explicitly requests that policy.
6. Create `commands/`, `shared/`, `generated/`, `scripts/`, and `proposals/`.
7. Copy or adapt the bundled validation and rebuild scripts into the target
   workspace when the user wants local scripts.
8. Rebuild catalog, graph, and cascade.
9. Validate and report the exact command and result.

## Analyze Repository

Classify existing files as entry skill candidate, routed module candidate,
command skill candidate, shared resource, generated artifact, domain-specific
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
3. If overlap is low, choose the module artifact path from existing workspace
   convention and manifest depth settings, then create
   `modules/<category-path>/<module-name>/skill.yaml` and `instructions.md`
   from templates. Flat `modules/<module-name>/` paths are valid when the
   workspace allows them. Preserve the `using module: <module-name>` output
   marker.
4. Keep new modules in `status: draft` until at least one concrete routing
   signal and module-specific instruction behavior are written; active modules
   with empty signals, generated-looking strong signals, or title-swapped
   instruction gates fail validation.
5. If overlap is high, create a challenge report that recommends create, merge,
   update, or reject.
6. Rebuild generated artifacts.
7. Validate.

Creation should be direct when risk is low and routing evidence is concrete.
Challenge when overlap, ambiguity, missing signals, or routing risk is detected.

## Create Command Skill

Create `commands/<command-name>/` with `SKILL.md`, `agents/openai.yaml`, and
`skill.yaml`. Use `activation: explicit` and `visibility: public`. The skill
body must say it runs only when directly invoked and preserve the
`using skill: <command-name>` output marker. Do not include command skills in
routed cascade selection.

When the command owns setup, discovery, intake, or normalization phases that may
produce a router-ready follow-up request, document that command-specific
handoff in `SKILL.md`. The shared trigger is a `Router handoff:` block that
contains a literal entry invocation such as `$routed-skills ...`; all additional
fields and context are command-defined. Include any command-owned context the
entry router needs in the block; the entry router should otherwise inspect
resources through normal routing rules. Do not add handoff metadata to
`skill.yaml`, and do not switch silently into entry routing without the handoff
block.

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
constraints, active module reachability, instruction prose quality, generated
freshness, command skill exclusion, duplicate strong signals, direct strong
signal wording, public agent-skill shapes, and required public
`agents/openai.yaml` interface metadata.

## Propose Merge

Compare descriptions, routing signals, relations, instructions, and resources.
Recommend exactly one outcome: keep separate, merge, replace, narrow one module,
or split responsibilities. Store the proposal under `proposals/` only when the
user asks for a durable artifact.
