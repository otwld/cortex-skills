![otwld cortex skills banner](./banner.png)

![GitHub License](https://img.shields.io/github/license/otwld/cortex-skills)
[![Discord](https://img.shields.io/badge/Discord-OTWLD-blue?logo=discord&logoColor=white)](https://discord.otwld.com)

# Cortex Skills

Give your coding agent a routing brain.

Cortex Skills is a governed skill library for TypeScript ecosystem work. You
invoke one public entry, `$cortex`, and it orchestrates hidden atoms through
structured facets, lifecycle phases, command atoms, and local run traces.

It is not a package manager. It is not a prompt dump. It is a routed workspace
with inspectable metadata, generated views, validation, and phase-specific
runtime guidance.

## Copy These Prompts

```text
$cortex plan this migration before editing
```

```text
$cortex review this Angular Material change for accessibility, bundle impact, and docs
```

```text
$cortex debug this failing Vitest test from reproduction to regression guard
```

```text
$cortex finish this branch: verify, review, and prepare the PR
```

## How Routing Works

The public skill is the front door. Hidden modules are atoms selected by
structured facets and lifecycle phase coverage.

```text
your request
  -> $cortex entry
  -> .codex/config.json bootstrap
  -> .cortex/runs/{date-slug}/ trace
  -> activate
  -> plan
  -> run
  -> review
  -> verify
  -> finalize
```

Routing follows a few plain rules:

- `$cortex` reads `.codex/config.json` first and scaffolds it when missing.
- Each run writes local trace files under `.cortex/runs/`.
- Modules expose structured facets in `skill.yaml`.
- Runtime behavior lives in `lifecycle/<phase>.md` files.
- A phase can be delegated to one subagent that owns that whole phase.
- Phase traces carry selected modules, matched facets, lifecycle files used,
  unresolved questions, and next-phase inputs.
- Modules do not name peer modules or declare relations.
- Command skills are public atoms and may be invoked by `$cortex` when
  orchestration requires it.

## Workspace Shape

```text
routed-skills.yaml
entry/cortex/
|-- SKILL.md
|-- agents/openai.yaml
`-- skill.yaml
modules/<area>/<cluster>/<artifact-name>/
|-- lifecycle/
|   |-- activate.md
|   |-- plan.md
|   |-- run.md
|   |-- review.md
|   |-- verify.md
|   `-- finalize.md
`-- skill.yaml
commands/<command-name>/
|-- SKILL.md
|-- agents/openai.yaml
`-- skill.yaml
shared/
generated/
scripts/
```

Lifecycle files are optional per phase, but every active routed module must
declare at least one lifecycle file.

## Generated Views

Generated views are checked in for review and validation:

- [Skill catalog](generated/SKILL_CATALOG.md)
- [Facet and lifecycle graph](generated/module-graph.md)
- [Routing cascade](generated/module-cascade.md)

`module-graph.md` is a bipartite module-to-facet and module-to-phase graph. It
does not contain module-to-module dependency edges.

## Command Skills

Invoke setup commands directly when you want that operation:

| Command | Use when |
| --- | --- |
| `$setup-agent-instructions` | Creating or auditing durable agent instruction files such as `AGENTS.md`. |
| `$setup-cortex-config` | Creating or repairing operator-local `.codex/config.json`. |
| `$setup-routed-skill-workspace` | Creating, validating, or evolving another routed skill workspace. |
| `$setup-project-memory` | Setting up project glossary, ADR, out-of-scope, or tracker memory. |

## Quality Bar

Every active routed module must earn its place:

- facets use direct request or repository evidence;
- lifecycle files are phase-specific and concrete;
- modules do not route other modules;
- resources are explicitly declared;
- generated artifacts are fresh;
- local run traces are ignored.

## Maintainer Commands

Check generated freshness without writing:

```bash
python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml
```

Validate the routed workspace:

```bash
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

Rebuild generated artifacts after metadata changes:

```bash
python3 scripts/rebuild-routed-skills.py routed-skills.yaml
```

Run validator fixture tests after changing validation or rebuild behavior:

```bash
python3 scripts/test-validate-routed-skills.py
```

Workspace rules live in [AGENTS.md](AGENTS.md). Contribution rules live in
[CONTRIBUTING.md](CONTRIBUTING.md).
