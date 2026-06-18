![otwld cortex skills banner](./banner.png)

![GitHub License](https://img.shields.io/github/license/otwld/cortex-skills)
[![Discord](https://img.shields.io/badge/Discord-OTWLD-blue?logo=discord&logoColor=white)](https://discord.otwld.com)

# Cortex Skills

Give your coding agent a routing brain.

Cortex Skills is a governed skill library for TypeScript ecosystem work. You
invoke one public entry, `$cortex`, and it pulls in the smallest useful set of
hidden operating guides for the job: planning, debugging, architecture,
framework conventions, testing, documentation, review, and release completion.

It is not a package manager. It is not a prompt dump. It is a set of routing
rules and engineering habits that help an agent stop guessing and start working
with the right constraints.

- One public entry: [`$cortex`](entry/cortex/SKILL.md).
- 40+ hidden modules for real engineering situations.
- Generated routing maps you can inspect, review, and validate.
- Explicit setup commands for project memory, agent instructions, and routed
  skill workspaces.

## Copy These Prompts

Use `$cortex` when you want the agent to choose the right workflow instead of
forcing you to name every skill.

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
$cortex help me decide whether this DTO belongs in a shared library
```

```text
$cortex finish this branch: verify, review, and prepare the PR
```

Good `$cortex` requests usually say what kind of work is happening and what risk
you care about. The router uses that evidence to select modules.

## Use It When

Reach for Cortex when the task has shape, risk, or ambiguity:

| You are doing this | Cortex brings in |
| --- | --- |
| Turning a vague idea into a real change | intake, planning, scope control |
| Moving code across packages | placement, boundaries, public API design |
| Touching Angular, NestJS, Nx, Vue, Vite, RxJS, Storybook, or TypeScript | framework and language conventions |
| Changing behavior or fixing a bug | test-first discipline and debugging flow |
| Creating examples, docs, stories, or fixtures | documentation and example consistency |
| Finishing a branch | workspace safety, verification, review, branch completion |

The point is not to load everything. The point is to load enough judgment to
keep the agent on rails.

## How Routing Works

The public skill is only the front door. The work happens in hidden modules.

```text
your request
  -> $cortex entry
  -> routing signals
  -> required before modules
  -> evidence-backed with modules
  -> deferred after modules
  -> focused agent workflow
```

Routing follows a few plain rules:

- Strong signals beat medium signals; medium signals beat weak signals.
- `before` modules run first when another module depends on them.
- `with` modules join only when they have their own evidence.
- `after` modules wait until that phase is actually relevant.
- `excludes` and `replaces` keep bad combinations out.
- Explicit commands are public but direct-invocation only; they do not join
  normal `$cortex` routing.

The generated routing views are checked into the repo so you can inspect how the
library thinks:

- [Skill catalog](generated/SKILL_CATALOG.md)
- [Routing cascade](generated/module-cascade.md)
- [Relation graph](generated/module-graph.md)

## Real Scenarios

### The Messy Migration

Prompt:

```text
$cortex plan moving candidate matching logic out of the API app into a shared library
```

Likely routing:

- `implementation-plan`
- `workspace-state-guard`
- `library-placement-decision`
- `nx-module-boundaries`
- `public-api-design`
- `test-first-discipline`
- `code-documentation`

What changes: the agent should inspect the workspace, write a decision-complete
plan, respect package boundaries, define the public API, and name validation
before touching files.

### The Failing Test

Prompt:

```text
$cortex debug this flaky Playwright test; do not rewrite it until we know the cause
```

Likely routing:

- `systematic-debugging`
- `test-first-discipline`
- `playwright-conventions`
- `completion-verification`

What changes: the agent should reproduce, localize, reduce, fix, and add a
regression guard instead of trying random waits.

### The UI Change

Prompt:

```text
$cortex review this Angular Material dialog for keyboard flow, density, and bundle impact
```

Likely routing:

- `angular-conventions`
- `angular-material-conventions`
- `bundle-performance`
- `typescript-code-style`
- `code-documentation`

What changes: the agent should check template structure, accessibility, theming,
dependencies, public component surface, and docs or stories touched by the UI.

### The Public API Question

Prompt:

```text
$cortex should ApplicationReviewResult be exported from the shared contract package?
```

Likely routing:

- `library-placement-decision`
- `public-api-design`
- `naming-consistency`
- `typescript-api-conventions`

What changes: the agent should decide ownership first, keep exports minimal,
encode states clearly, and avoid creating a contract just because two files look
similar.

### The Ready-To-Ship Branch

Prompt:

```text
$cortex finish this branch and tell me what is still risky
```

Likely routing:

- `workspace-state-guard`
- `completion-verification`
- `review-gate`
- `branch-completion`

What changes: the agent should check dirty state, run relevant validation,
review the change against requirements, and report remaining risk before any
publish step.

## What Is Inside

Cortex covers reusable engineering workflows across:

- Architecture: placement, extraction, public APIs, naming, boundaries, bundle
  impact, and drift detection.
- Frameworks: Angular, Angular Material, Angular TanStack Query, NestJS,
  NestJS Mongoose, Nx, RxJS, Storybook, Vite, and Vue.
- Governance: intake, planning, execution, delegation, workspace safety,
  debugging, verification, review, and branch completion.
- Testing: Jest, Playwright, and Vitest.
- TypeScript: source style and public API conventions.
- Tools and maintenance: Bricks workflows, diary entries, example consistency,
  and skill evolution.

See the generated [skill catalog](generated/SKILL_CATALOG.md) for every module
and explicit command.

## Explicit Commands

Some workflows are public commands, but they are not selected by `$cortex`
routing. Invoke them directly when you want that setup job:

| Command | Use when |
| --- | --- |
| `$agent-instructions-bootstrap` | Creating or auditing durable agent instruction files such as `AGENTS.md`. |
| `$bootstrap-routed-skill-workspace` | Creating, validating, or evolving another routed skill workspace. |
| `$project-memory-setup` | Setting up project glossary, ADR, out-of-scope, or tracker memory. |

## Install Or Point Your Agent

The public Codex-facing surface is:

```text
entry/cortex/
|-- SKILL.md
|-- agents/openai.yaml
`-- skill.yaml
```

Compatible agent tooling should point at `entry/cortex/` for the `$cortex`
entry. Routed modules stay hidden under `modules/` and are selected through
metadata.

Clone the repository if you want the full workspace locally:

```bash
git clone git@github.com:otwld/cortex-skills.git
cd cortex-skills
```

Then inspect the generated map:

```bash
less generated/SKILL_CATALOG.md
less generated/module-cascade.md
less generated/module-graph.md
```

## Maintainer Commands

`skill.yaml` files are the source of truth. Generated files are rebuilt outputs.

Validate the routed workspace:

```bash
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

Rebuild generated artifacts after metadata changes:

```bash
python3 scripts/rebuild-routed-skills.py routed-skills.yaml
```

Check generated freshness without writing:

```bash
python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml
```

Run validator fixture tests after changing validation or rebuild behavior:

```bash
python3 scripts/test-validate-routed-skills.py
```

Workspace rules live in [AGENTS.md](AGENTS.md). Contribution rules live in
[CONTRIBUTING.md](CONTRIBUTING.md).

## Release Status

Current public seed: `v0.1.0`.

This release is practical and usable. The public contract is the routed
workspace shape, the `$cortex` entry, and the validation scripts.

## License

MIT. See [LICENSE](LICENSE).
