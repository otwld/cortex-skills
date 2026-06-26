# Routed Workspace Contract

Use this reference when a task defines, audits, or changes the generic routed
skill workspace format. The contract is independent of Cortex artifact names
and category names.

## Workspace Shape

A routed skill workspace contains one public entry skill, hidden routed modules,
optional public command skills, shared resources, generated artifacts, and
validation scripts.

Default layout:

```text
.skills/
  routed-skills.yaml
  entry/<entry-slug>/
    SKILL.md
    agents/openai.yaml
    skill.yaml
  modules/<category>/<module-name>/
    skill.yaml
    lifecycle/<phase>.md
  commands/<command-name>/
    SKILL.md
    agents/openai.yaml
    skill.yaml
  shared/
  generated/
  scripts/
```

Category folders under `modules/` are browsing containers only. They do not
create routing behavior, inheritance, default resources, or implicit coupling.

## Manifest

`routed-skills.yaml` is the workspace manifest. Required shape:

```yaml
name: routed-skills
root: .skills

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
  path: entry/routed-skills

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

The manifest owns allowed facet keys and lifecycle phase names. Facet values
remain module-local strings, but validators should reject empty, mechanical, or
module-name-only values.

## Entry Skill

Exactly one entry skill is mandatory. It lives under `entry/<entry-slug>/` and
contains `SKILL.md`, `agents/openai.yaml`, and `skill.yaml`.

`SKILL.md` is the public agent entry point and owns router behavior: config
bootstrap, lifecycle phase progress, atom selection, command invocation, and
run trace handoff. Do not create entry `instructions.md`.

`agents/openai.yaml` is UI metadata. Public entry and command skills must set
`interface.display_name`, `interface.short_description`,
`interface.default_prompt`, and `policy.allow_implicit_invocation: false`.

Entry metadata:

```yaml
name: routed-skills
description: Public entry skill for this routed skill workspace.
activation: entry
visibility: public
status: active
```

## Routed Modules

Routed modules are hidden atoms. Required source files are `skill.yaml` and at
least one declared lifecycle file when the module is active. Routed modules do
not have `instructions.md`.

Module metadata:

```yaml
name: testing
description: Guidance for test strategy and validation.
activation: routed
visibility: hidden
status: active

routing:
  priority: 5
  facets:
    intents:
      - test
    surfaces:
      - test-runner
    risks:
      - regression
    artifacts:
      - test-plan
    repo:
      - package.json
    request:
      - asks for test coverage

lifecycle:
  activate: lifecycle/activate.md
  verify: lifecycle/verify.md

uses: []

resources:
  references: []
  scripts: []
  templates: []
  assets: []
```

Lifecycle files must live under the owning module's `lifecycle/` folder and use
manifest phase names. Each file contains phase-specific runtime behavior, gates,
hard stops, and a `## Phase Output` contract. Lifecycle files must not name peer
modules or route other atoms.

## Command Skills

Command skills are public command atoms. Required files are `SKILL.md`,
`agents/openai.yaml`, and `skill.yaml`. They may own optional `references/`,
`scripts/`, `templates/`, and `assets/` folders.

Command metadata uses `activation: explicit` and `visibility: public`. Commands
do not declare lifecycle files. The entry router may invoke a command when
orchestration requires it, such as bootstrapping `.codex/config.json`.

Command skills may define command-specific handoff behavior in `SKILL.md`. A
handoff is an instruction boundary, not metadata. A valid handoff uses a
`Router handoff:` block containing exactly one router-ready request beginning
with the literal entry invocation.

## Runtime Config And Traces

The entry router reads `.codex/config.json` before normal routing. The file is
operator-local and may define phase-specific always atoms:

```json
{
  "phases": {
    "activate": { "always": [] },
    "plan": { "always": [] },
    "run": { "always": [] },
    "review": { "always": [] },
    "verify": { "always": [] },
    "finalize": { "always": [] }
  }
}
```

Each routed request writes a local run trace under `.cortex/runs/{date-slug}/`.
Run traces are ignored by git and may contain full local evidence.

## Generated Artifacts

Generated files are disposable:

- `generated/SKILL_CATALOG.md`
- `generated/module-graph.md`
- `generated/module-cascade.md`

`module-graph.md` is a bipartite facet/lifecycle graph. It must not contain
module-to-module dependency edges.

## Prohibited Legacy Surface

Do not add module relations, relation columns, relation graphs, routed module
`instructions.md`, strong/medium/weak signal blocks, output marker blocks, or
hidden resource coupling.
