# Routed Workspace Contract

Use this reference when a task defines, audits, or changes the generic routed
skill workspace format. The contract is intentionally independent of Cortex
artifact names and taxonomy folders.

## Workspace Shape

A routed skill workspace contains one public entry skill, hidden routed modules,
optional explicit command modules, shared resources, generated artifacts,
validation scripts, and proposals.

Default layout:

```text
.skills/
  routed-skills.yaml
  entry/<entry-slug>/
    SKILL.md
    agents/openai.yaml
    skill.yaml
  modules/<module-name>/
  shared/
  generated/
  scripts/
  proposals/
```

Supported roots are `.skills`, `skills`, and `.`. The manifest makes those
layouts equivalent by defining paths relative to the manifest directory.

## Manifest

`routed-skills.yaml` is the workspace manifest. Required shape:

```yaml
name: routed-skills
root: .skills

paths:
  entry: entry
  modules: modules
  shared: shared
  generated: generated
  proposals: proposals

artifacts:
  metadata: skill.yaml
  instructions: instructions.md

entry:
  required: true
  path: entry/routed-skills

generated:
  catalog: generated/SKILL_CATALOG.md
  graph: generated/module-graph.md
  cascade: generated/module-cascade.md

validation:
  max_before_depth: 3
```

Use the manifest directory as the workspace root when resolving paths. Keep
`root` as a human-readable declaration of the chosen supported root.

## Entry Skill

Exactly one entry skill is mandatory. It lives under `entry/<entry-slug>/` and
contains `SKILL.md`, `agents/openai.yaml`, and `skill.yaml`.

`SKILL.md` is the public agent skill entry point. It contains the agent-skill
frontmatter (`name` and `description`) plus the runtime routing instructions
for the entry. Do not create a separate `instructions.md` for the public entry;
that duplicates the `SKILL.md` body and creates drift risk.

`agents/openai.yaml` is UI metadata. Explicit-only routed workspace entries
must set `policy.allow_implicit_invocation: false`.

Entry metadata:

```yaml
name: routed-skills
description: Public entry skill for this routed skill workspace.
activation: entry
visibility: public
status: active
```

`skill.yaml` is routed-workspace metadata consumed by local rebuild and
validation scripts. Keep custom routing fields out of `SKILL.md` frontmatter.

The entry skill must be publicly invokable through `SKILL.md`, route to hidden
modules, reference the generated catalog, graph, and cascade, explain that
modules are hidden, and explain that generated artifacts are derived from
metadata.

## Modules

Modules are folders and are the source of truth. Required files are `skill.yaml`
and `instructions.md`; optional folders are `references/`, `scripts/`,
`templates/`, and `assets/`.

Module metadata:

```yaml
name: testing
description: Guidance for test strategy and validation.
activation: routed
visibility: hidden
status: active

routing:
  priority: 5
  signals:
    strong:
      - user asks for a test plan
    medium:
      - mentions coverage
    weak:
      - mentions bugs

relations:
  before: []
  with: []
  after: []
  excludes: []
  replaces: []

uses: []

resources:
  references: []
  scripts: []
  templates: []
  assets: []
```

Supported activation values are `entry`, `routed`, and `explicit`. Supported
visibility values are `public` and `hidden`. Routed modules must be hidden.
Explicit commands are public, direct-invocation only, and excluded from routing.

## Instructions

Routed module and explicit command behavior belongs in `instructions.md`, not
in generated files. Public entry behavior belongs in `entry/<entry-slug>/SKILL.md`.
Use these sections unless the module has a narrower need:

```markdown
# Purpose

# When To Use

# Workflow

# Gates

# Hard Stops

# Output Format

# Checklist

# Cross References
```

Do not duplicate every routing signal in prose. Keep routing evidence in
metadata and execution behavior in instructions.

## Routing

Routing is heuristic and reviewable:

1. Collect direct evidence from the user request and relevant files.
2. Prefer strong signals over medium signals.
3. Prefer medium signals over weak signals.
4. Break ties using `routing.priority`.
5. Load `before` modules recursively up to `validation.max_before_depth`.
6. Load `with` modules only when they also have direct evidence.
7. Suggest `after` modules only when the later phase becomes relevant.
8. Reject combinations declared in `excludes`.
9. Prefer modules that declare a matched module in `replaces`.

Do not use embeddings, classifiers, scoring engines, vector databases,
inheritance, or hidden coupling.

## Relations

Use exactly these relation types:

- `before`: modules that must be loaded before this module.
- `with`: modules that may be loaded together only with independent evidence.
- `after`: modules likely useful in a later phase.
- `excludes`: modules that should not be active together.
- `replaces`: modules superseded by this module.

Relation targets must name existing entry, routed, or explicit modules.

## Resources

Shared resources live under `shared/`. Modules may reference shared resources or
other modules explicitly through `uses`. Module-owned files in `references/`,
`scripts/`, `templates/`, and `assets/` must be listed under `resources`.

No resource is automatically shared. Avoid implicit inheritance and hidden
resource coupling.

## Generated Artifacts

Generated files are disposable:

- `generated/SKILL_CATALOG.md`
- `generated/module-graph.md`
- `generated/module-cascade.md`

Regenerate them from entry and module metadata. Manual edits should be rejected
by validation or overwritten by rebuild.
