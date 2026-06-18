![otwld cortex skills banner](./banner.png)

![GitHub License](https://img.shields.io/github/license/otwld/cortex-skills)
[![Discord](https://img.shields.io/badge/Discord-OTWLD-blue?logo=discord&logoColor=white)](https://discord.otwld.com)

# Cortex Skills

Governed AI skill library for reusable TypeScript ecosystem agent workflows.

Cortex Skills is a routed skill workspace with one public `$cortex` entry skill,
hidden routed modules, explicit command artifacts, generated routing views, and
deterministic validation.

## Quick Start

Clone the repository:

```bash
git clone git@github.com:otwld/cortex-skills.git
cd cortex-skills
```

Inspect the generated catalog:

```bash
less generated/SKILL_CATALOG.md
```

Validate the workspace:

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

Invoke `$cortex` explicitly to route work through hidden modules. Explicit
command artifacts such as `agent-instructions-bootstrap`,
`bootstrap-routed-skill-workspace`, and `project-memory-setup` are represented
in metadata but excluded from routed cascade selection.

## What Is Included

- Architecture modules for placement, extraction, public APIs, naming,
  boundaries, and bundle impact.
- Framework modules for Angular, Angular Material, Angular TanStack Query,
  NestJS, NestJS Mongoose, Nx, RxJS, Storybook, Vite, and Vue.
- Governance modules for intake, planning, execution, delegation, workspace
  safety, debugging, verification, review, and branch completion.
- Explicit setup command artifacts for agent instructions, project memory, and
  routed skill workspaces.
- Testing modules for Jest, Playwright, and Vitest.
- Tool modules for source-management CLI workflows such as Bricks.
- TypeScript modules for source style and public API conventions.
- Maintenance modules for diary entries, example consistency, and skill
  evolution.

See [generated/SKILL_CATALOG.md](generated/SKILL_CATALOG.md) for the generated
artifact list.

## Workspace Model

The workspace follows the contract in [AGENTS.md](AGENTS.md):

```text
routed-skills.yaml
entry/cortex/
|-- SKILL.md
|-- agents/openai.yaml
`-- skill.yaml
modules/<artifact-name>/
|-- instructions.md
`-- skill.yaml
shared/
generated/
scripts/
proposals/
```

`skill.yaml` files are the source of truth for names, descriptions, activation,
visibility, routing signals, relations, declared resources, and generated
catalog data. `instructions.md` files contain selected-module runtime guidance.
Files under `generated/` are rebuilt outputs and should not be hand-edited.

## Optional Codex Usage

The public Codex-facing surface is `entry/cortex/SKILL.md` plus
`entry/cortex/agents/openai.yaml`. Routed modules are hidden and selected by
the public entry using generated metadata views.

Common usage patterns:

- Point compatible tooling at `entry/cortex/` for the `$cortex` entry.
- Use `generated/module-cascade.md` and `generated/module-graph.md` to inspect
  routing decisions.
- Update module `skill.yaml` metadata when adding signals, relations, or
  resources.
- Run validation after copying, editing, or contributing artifacts.

## Contributing

Pull requests are welcome. Keep artifacts focused, project-agnostic, and
validated.

Before opening a PR:

```bash
python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution rules.

## Release Status

Current public seed: `v0.1.0`.

This release is practical and usable, but the public API is the repository
structure and validation contract, not a stable package interface.

## License

MIT. See [LICENSE](LICENSE).
