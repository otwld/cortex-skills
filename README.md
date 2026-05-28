# Cortex Skills

Governed AI skill library for reusable TypeScript ecosystem agent workflows.

Cortex Skills is a public collection of agent-readable operating guides. It is
for AI builders and engineering teams who want reusable skills with clear
trigger rules, metadata, validation, and cross-skill coordination.

This is not a package manager, framework, or prompt dump. Each skill is a small
directory with a `SKILL.md`, OpenAI-facing metadata, and optional references or
scripts for deterministic checks.

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

Preview the skill cascade simulations:

```bash
python3 scripts/validate-skills.py --cascade
```

Use the repository as a complete skill library with compatible agent tooling, or
copy the skill directories you need into your own agent skill location.

## What Is Included

- Architecture skills for placement, extraction, public APIs, naming,
  boundaries, and bundle impact.
- Framework skills for Angular, Angular Material, Angular TanStack Query,
  NestJS, NestJS Mongoose, Nx, RxJS, Storybook, Vite, and Vue.
- Testing skills for Jest, Playwright, and Vitest.
- TypeScript skills for source style and public API conventions.
- Maintenance skills for diary entries, example consistency, and skill
  evolution.

See [SKILL_CATALOG.md](SKILL_CATALOG.md) for the full list.

## Governance Model

Every skill follows the structure defined in [AGENTS.md](AGENTS.md):

```text
taxonomy/skill-name/
|-- SKILL.md
`-- agents/
    `-- openai.yaml
```

The repository also includes:

- [references/skill-graph.md](references/skill-graph.md), the canonical
  non-transitive cross-skill graph.
- [scripts/validate-skills.py](scripts/validate-skills.py), the structural,
  metadata, residue, example, and cascade validator.
- A shared recruitment job-board example universe for all illustrative examples.
- Required `(otwld)` display names in `agents/openai.yaml` for easy discovery in
  agent UIs and CLIs.

## Optional Codex Usage

The skills are intentionally agent-neutral, but every skill includes
`agents/openai.yaml` metadata for OpenAI/Codex-style discovery surfaces.

Common usage patterns:

- Clone this repository and point compatible tooling at the skill directories.
- Copy selected taxonomy folders into your existing skill library.
- Use `SKILL_CATALOG.md` to find the skill names, then invoke them by name when
  your agent supports explicit skill prompts.

Always run the validator after copying, editing, or contributing skills.

## Contributing

Pull requests are welcome. Keep skills focused, project-agnostic, and validated.

Before opening a PR:

```bash
python3 scripts/validate-skills.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution rules.

## Release Status

Current public seed: `v0.1.0`.

This release is practical and usable, but the public API is the repository
structure and validation contract, not a stable package interface.

## Suggested GitHub Metadata

Description:

```text
Governed AI skill library for reusable TypeScript ecosystem agent workflows.
```

Topics:

```text
ai-skills, agent-skills, ai-agents, typescript, codex, openai,
developer-tools, engineering-conventions, nx, angular, nestjs, storybook,
vitest, playwright
```

## License

MIT. See [LICENSE](LICENSE).
