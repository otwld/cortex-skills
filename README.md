![otwld cortex skills banner](./banner.png)

![GitHub License](https://img.shields.io/github/license/otwld/cortex-skills)
[![Discord](https://img.shields.io/badge/Discord-OTWLD-blue?logo=discord&logoColor=white)](https://discord.otwld.com)

# Cortex Skills

Governed AI skill library for reusable TypeScript ecosystem agent workflows.

Cortex Skills is a public `$cortex` skill backed by agent-readable internal
modules. It is for AI builders and engineering teams who want reusable guidance
with explicit invocation, validation, and cross-module coordination.

This is not a package manager, framework, or prompt dump. The public Codex
surface is one `SKILL.md` with OpenAI-facing metadata; each internal module is a
small directory with `MODULE.md` plus optional references or scripts for
deterministic checks.

## Quick Start

Clone the repository:

```bash
git clone git@github.com:otwld/cortex-skills.git
cd cortex-skills
```

Inspect the catalog:

```bash
less SKILL_CATALOG.md
```

Validate the library:

```bash
python3 scripts/validate-skills.py
```

Preview the module cascade simulations:

```bash
python3 scripts/validate-skills.py --cascade
```

Run validator fixture tests after changing validator behavior:

```bash
python3 scripts/test-validate-skills.py
```

Use the repository as a complete Cortex library with compatible agent tooling.
Invoke `$cortex` explicitly to route a task through the internal modules.

## What Is Included

- Architecture modules for placement, extraction, public APIs, naming,
  boundaries, and bundle impact.
- Framework modules for Angular, Angular Material, Angular TanStack Query,
  NestJS, NestJS Mongoose, Nx, RxJS, Storybook, Vite, and Vue.
- Governance modules for Cortex routing, intake, planning, execution,
  delegation, workspace safety, debugging, verification, review, and branch
  completion.
- Testing modules for Jest, Playwright, and Vitest.
- Tool modules for source-management CLI workflows such as Bricks.
- TypeScript modules for source style and public API conventions.
- Maintenance modules for diary entries, example consistency, and skill
  evolution.

See [SKILL_CATALOG.md](SKILL_CATALOG.md) for the full list.

## Governance Model

The public skill follows the structure defined in [AGENTS.md](AGENTS.md):

```text
governance/core/cortex/
|-- SKILL.md
`-- agents/
    `-- openai.yaml
```

Internal modules use:

```text
taxonomy[/group]/folder-slug/
`-- MODULE.md
```

The repository also includes:

- [references/module-graph.md](references/module-graph.md), the canonical
  non-transitive module graph.
- [scripts/validate-skills.py](scripts/validate-skills.py), the structural,
  OpenAI metadata, catalog taxonomy, residue, example, and cascade validator.
- [scripts/test-validate-skills.py](scripts/test-validate-skills.py), fixture
  regression tests for validator behavior.
- A shared recruitment job-board example universe for all illustrative examples.
- Required `(otwld)` display name in the public `agents/openai.yaml` for easy
  discovery in agent UIs and CLIs.

## Optional Codex Usage

The module instructions are intentionally agent-neutral, but only the public
`cortex` skill includes `agents/openai.yaml` metadata for OpenAI/Codex-style
discovery.

Common usage patterns:

- Clone this repository and point compatible tooling at the public `cortex`
  skill directory.
- Keep internal modules with the public skill so `$cortex` can route work
  through `references/module-cascade.md`.
- Use `SKILL_CATALOG.md` to inspect the module names selected by `$cortex`.

Always run the validator after copying, editing, or contributing Cortex
artifacts.

## Contributing

Pull requests are welcome. Keep the public skill and internal modules focused,
project-agnostic, and validated.

Before opening a PR:

```bash
python3 scripts/validate-skills.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution rules.

## Release Status

Current public seed: `v0.1.0`.

This release is practical and usable, but the public API is the repository
structure and validation contract, not a stable package interface.

## License

MIT. See [LICENSE](LICENSE).
