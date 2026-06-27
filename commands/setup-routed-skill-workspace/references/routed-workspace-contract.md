# Routed Workspace Contract

Use this reference when creating or extending a Cortex-like routed skill
workspace. The entry name is user-chosen; do not hard-code `cortex` into
generated workspaces unless that is the requested entry slug.

## Workspace Shape

A workspace contains one public entry skill, hidden routed modules, public
command atoms, shared resources, generated artifacts, and validation scripts.
The checkout root owns `.gitignore`; the routed workspace root owns the skill
artifacts.

```text
<checkout-root>/
  .gitignore
  <root>/
    routed-skills.yaml
    entry/<entry-slug>/
      SKILL.md
      agents/openai.yaml
      skill.yaml
    modules/<area>/<cluster>/<module-name>/
      skill.yaml
      lifecycle/activate.md
      lifecycle/plan.md
      lifecycle/run.md
      lifecycle/review.md
      lifecycle/verify.md
      lifecycle/finalize.md
    commands/setup-routed-skill-workspace/
      SKILL.md
      agents/openai.yaml
      skill.yaml
      assets/
      references/
    commands/setup-<entry-slug>-config/
      SKILL.md
      agents/openai.yaml
      skill.yaml
    shared/
    generated/
    scripts/
```

The module path convention is three levels for clarity, but validators must
accept any non-nested module artifact under `modules/`.

## Manifest

`routed-skills.yaml` defines the workspace root, artifact paths, facet keys,
lifecycle phases, and generated artifact paths.

```yaml
name: <entry-slug>
root: <root>

paths:
  entry: entry
  modules: modules
  commands: commands
  shared: shared
  generated: generated

artifacts:
  metadata: skill.yaml

entry:
  required: true
  path: entry/<entry-slug>

routing:
  facets:
    keys:
      - intents
      - surfaces
      - risks
      - artifacts
      - repo
      - request

lifecycle:
  phases:
    - activate
    - plan
    - run
    - review
    - verify
    - finalize

generated:
  catalog: generated/SKILL_CATALOG.md
  graph: generated/module-graph.md
  cascade: generated/module-cascade.md
```

## Entry Runtime

The public entry skill owns routing behavior. For entry `ascend`, runtime state
uses:

- `.ascend/config.json`
- `.ascend/runs/{date-slug}/`

The runtime directory is operator-local and ignored as `.<entry>/`.

When the routed workspace root is the checkout root, `.gitignore` contains
`.<entry>/`. When the routed workspace root is a nested `skills/` or `.skills/`
directory, the checkout-root `.gitignore` contains `skills/.<entry>/` or
`.skills/.<entry>/`. Do not create `skills/.gitignore` to satisfy this policy.

Entry skills contain `SKILL.md`, `agents/openai.yaml`, and `skill.yaml`. Do not
create entry `instructions.md`.

## Routed Modules

Routed modules are hidden atoms. New modules are scaffolded as drafts with empty
facets and every lifecycle phase file. The user then fills useful lifecycle
files and removes phases that do not apply.

```yaml
name: module-name
description: Draft routed atom for a specific responsibility.
activation: routed
visibility: hidden
status: draft

routing:
  priority: 5
  facets:
    intents: []
    surfaces: []
    risks: []
    artifacts: []
    repo: []
    request: []

lifecycle:
  activate: lifecycle/activate.md
  plan: lifecycle/plan.md
  run: lifecycle/run.md
  review: lifecycle/review.md
  verify: lifecycle/verify.md
  finalize: lifecycle/finalize.md

uses: []

resources:
  references: []
  scripts: []
  templates: []
  assets: []
```

Active modules must have concrete facets and at least one declared lifecycle
file. Lifecycle files must contain `## Overview`, `## Workflow`,
`## Quality Gates`, `## Hard Stops`, and `## Phase Output`.

## Command Atoms

Command atoms are public direct commands. They contain `SKILL.md`,
`agents/openai.yaml`, and `skill.yaml`; they do not declare lifecycle files.

Initialization creates:

- `setup-routed-skill-workspace` for future workspace/module/command authoring.
- `setup-<entry>-config` for creating or repairing `.<entry>/config.json`.

Do not add Router handoff sections by default.

## Generated Artifacts

Generated files are disposable and rebuilt from metadata:

- `generated/SKILL_CATALOG.md`
- `generated/module-graph.md`
- `generated/module-cascade.md`

Validation must fail stale generated output.

## Prohibited Surface

Do not add migration branches, legacy compatibility language, relation metadata,
relation graphs, strong/medium/weak signals, routed module `instructions.md`,
output markers, shims, placeholder completion claims, or hidden resource
coupling.
