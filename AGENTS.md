# AGENTS.md

## Purpose

This workspace is a routed Cortex skill workspace. It has exactly one public
entry skill, `$cortex`, and hidden routed modules selected through explicit
metadata. Treat `skill.yaml` files and instruction files as source artifacts;
treat generated catalogs and routing views as disposable rebuild outputs.

These rules govern writing and maintaining routed skill artifacts in this
repository. Keep guidance precise, project-agnostic, and easy to validate.

## Documentation Lookup

Use the `ctx7` CLI to fetch current documentation whenever a task asks about a
library, framework, SDK, API, CLI tool, or cloud service. This includes API
syntax, configuration, version migration, library-specific debugging, setup
instructions, and CLI usage.

Do not use Context7 for refactoring, writing scripts from scratch, debugging
business logic, code review, or general programming concepts.

Context7 workflow:

1. Resolve the library:

   ```bash
   npx ctx7@latest library <name> "<user's question>"
   ```

2. Pick the best match by exact name, description relevance, snippet count,
   source reputation, and benchmark score.

3. Fetch docs:

   ```bash
   npx ctx7@latest docs <libraryId> "<user's question>"
   ```

4. Answer using the fetched documentation.

Use the official library name with proper punctuation. Use the user's full
question as the query. Do not run more than three Context7 commands per
question. Do not include secrets, tokens, credentials, or private values in
Context7 queries.

If Context7 fails with a quota error, tell the user and suggest logging in or
setting a `CONTEXT7_API_KEY`. If the environment is sandboxed and Context7 fails
with DNS, host resolution, or fetch errors, retry outside the default sandbox.

## Workspace Shape

The routed workspace root is this repository root:

```text
routed-skills.yaml
entry/cortex/
|-- SKILL.md
|-- agents/openai.yaml
`-- skill.yaml
modules/<area>/<cluster>/<artifact-name>/
|-- instructions.md
|-- skill.yaml
`-- references/ or scripts/ or templates/ or assets/ when declared
commands/<command-name>/
|-- SKILL.md
|-- agents/openai.yaml
`-- skill.yaml
shared/
generated/
scripts/
```

Rules:

- `entry/cortex/SKILL.md` is the only public routed entry skill.
- Routed modules live under non-semantic category folders in `modules/` with
  `activation: routed` and `visibility: hidden`.
- Command skills live under `commands/` with `activation: explicit` and
  `visibility: public`; they are direct-invocation only and excluded from routed
  cascade selection.
- Category folders under `modules/` are for readability only; they do not create
  inheritance, routing behavior, implicit resources, or hidden coupling.
- Do not add `MODULE.md`, compatibility shims, hidden inheritance, or implicit
  resource sharing.
- Do not hand-edit files under `generated/`.

## Metadata And Instructions

Every entry, module, and command skill has a `skill.yaml` metadata file.
Routed module behavior belongs in `instructions.md`. Public entry and command
skill behavior belongs in `SKILL.md`; do not add `entry/cortex/instructions.md`
or command `instructions.md` files.

Use `skill.yaml` for:

- `name`, `description`, `activation`, `visibility`, and `status`.
- Routing priority and strong, medium, and weak signals.
- `relations.before`, `relations.with`, `relations.after`, `relations.excludes`,
  and `relations.replaces`.
- Explicit `uses` and `resources` declarations.

Use `instructions.md` for:

- Purpose, usage, workflow, gates, hard stops, output format, checklist, and
  cross-reference prose.
- Concise runtime behavior that agents need after the module is selected.

Keep routing evidence in metadata and execution guidance in instructions. Do not
duplicate every routing signal in prose.

## Resources

Artifact-owned support files live inside the owning module or command skill
under `references/`, `scripts/`, `templates/`, or `assets/`, and must be
declared in `skill.yaml`.

Cross-cutting files live under `shared/`. An artifact that uses a shared file
must declare it, usually as a `resources.references` entry such as
`shared/project-memory.md`.

No resource is shared automatically. If an artifact depends on another
artifact's behavior, declare it in `uses` instead of linking to private files.

## Generated Artifacts

The following files are generated from `routed-skills.yaml` and module
metadata:

- `generated/SKILL_CATALOG.md`
- `generated/module-graph.md`
- `generated/module-cascade.md`

Rebuild them after metadata, relation, signal, or artifact changes:

```bash
python3 scripts/rebuild-routed-skills.py routed-skills.yaml
```

Check freshness without writing:

```bash
python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml
```

## Examples Policy

All illustrative examples must follow the `example-universe-enforcer` module.
Use the recruitment agency job board universe for sample code, DTOs, API
payloads, Storybook data, docs snippets, and other examples.

Do not introduce unrelated example domains unless the user explicitly requests
one and the selected module requires that exception.

## Code Documentation Policy

Documentation is part of every code edit. When code is generated, edited, moved,
split, refactored, or materially reviewed, update the relevant JSDoc/TSDoc in
the same change. Do not treat documentation as an optional final pass.

Document the touched code at the right level:

- Add or update JSDoc/TSDoc for every touched exported symbol, public API,
  reusable helper, component, service, hook, provider, command, adapter, DTO,
  contract, or module-level behavior.
- When private code is touched, document the nearest owning function, class,
  module, or public surface when that code path would otherwise be undocumented.
- When code is moved or split, move or update the associated JSDoc/TSDoc and
  any project-native docs.
- Do not add placeholder comments that restate the code.

## Maintenance Rules

- Preserve narrow artifact scope.
- Use metadata relations instead of inline graph maintenance.
- Update `skill.yaml` and `instructions.md` together when behavior changes.
- Add new routed modules only after checking existing names, descriptions,
  strong signals, relations, and resources for overlap.
- Present a challenge report when responsibilities overlap materially.
- If adding a script, make it deterministic and declare or document its use.
- If adding a reference, template, or asset, make it discoverable from the
  owning artifact metadata.

## Validation Checklist

Before finishing any routed workspace change, verify:

- There is exactly one public entry skill under `entry/cortex/`.
- No `MODULE.md` files or obsolete flat module artifact directories remain.
- Routed modules are hidden and command skills are public direct-invocation
  artifacts under `commands/`.
- Relation targets name existing entry, routed module, or command skill
  artifacts.
- Shared and module-owned resources are declared and not orphaned.
- Active routed modules have direct routing signals.
- Active instruction files avoid copied template prose and repeated low-value
  checklist bullets.
- Generated artifacts were rebuilt from metadata and are fresh.
- Examples follow `example-universe-enforcer`.

Run:

```bash
python3 scripts/rebuild-routed-skills.py routed-skills.yaml
python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

When validation-facing routing contracts or scripts change, also run:

```bash
python3 scripts/test-validate-routed-skills.py
```
