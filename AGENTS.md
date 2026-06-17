# AGENTS.md

## Purpose

This workspace contains the public `$cortex` AI skill and internal Cortex
modules. Treat each artifact as a small, self-contained operating guide for
agents. Keep instructions precise, maintainable, and easy to discover.

These rules primarily govern writing and maintaining Cortex skill and module
artifacts in this workspace. They are intentionally agent-neutral except where
the public Codex skill surface is described.

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

If the user provides a valid `/org/project` library ID, use it directly for the
docs command. For version-specific docs, use the versioned ID returned by the
library command.

If Context7 fails with a quota error, tell the user and suggest logging in or
setting a `CONTEXT7_API_KEY`. If your environment is sandboxed and Context7
fails with DNS, host resolution, or fetch errors, retry outside the default
sandbox.

## Workspace Taxonomy

Skills are grouped by reusable purpose:

- `architecture/` for boundaries, placement, public APIs, extraction, naming,
  and performance doctrine.
- `documentation/` for generated or maintained code documentation rules.
- `frameworks/` for framework-specific conventions.
- `governance/` for agent workflow gates, routing, planning, review,
  verification, workspace safety, and release completion.
- `maintenance/` for workspace maintenance skills and example policy.
- `testing/` for test-runner and end-to-end testing conventions.
- `tools/` for source-management CLIs, developer tools, and their workflow
  conventions.
- `typescript/` for TypeScript language, API, and style conventions.
- `references/` for workspace-wide references such as the module graph.
- `scripts/` for workspace-wide validation and maintenance scripts.

## Artifact Directory Standard

The public `cortex` skill is the only direct Codex skill surface. Every other
operating guide is an internal Cortex module selected by `$cortex`, not a
directly invocable Codex skill.

Every artifact must live in its own short directory slug under the relevant
taxonomy folder. Related ecosystems may introduce one grouping level before the
artifact slug:

```text
taxonomy[/group]/folder-slug/
`-- MODULE.md
```

The public skill uses this shape:

```text
governance/core/cortex/
|-- SKILL.md
`-- agents/
    `-- openai.yaml
```

The frontmatter `name` remains the canonical artifact name. The folder slug
should omit words already made obvious by the taxonomy and group path, such as
`frameworks/angular/core` for `angular-conventions`,
`frameworks/angular/material` for `angular-material-conventions`,
`governance/core/cortex` for `cortex`,
`testing/jest` for `jest-conventions`, and `typescript/api` for
`typescript-api-conventions`.

Optional supporting directories:

- `references/` for detailed reference material that should be loaded only when
  needed.
- `scripts/` for deterministic or repeated operations.
- `assets/` for templates, images, fixtures, or other output resources.

Do not add extra README, changelog, quick-reference, or installation files
unless the artifact genuinely needs them at runtime.

## SKILL.md and MODULE.md Standard

The only `SKILL.md` is `governance/core/cortex/SKILL.md`. All internal modules
must use `MODULE.md`, which is a Cortex workspace convention rather than an
official Codex skill format.

Every `SKILL.md` and `MODULE.md` must start with YAML frontmatter:

```markdown
---
name: artifact-name
description: Clear routing guidance explaining when this artifact should apply.
---
```

For the public skill, `description` is the Codex discovery surface and must
state that it applies only when the user explicitly includes `$cortex`. For
modules, `description` is internal routing guidance used after `$cortex` is
already selected.

After the frontmatter, every public skill must include this standardized output
marker:

```markdown
# Output Marker

Display:
using skill: cortex
```

Every module must use:

```markdown
# Output Marker

Display:
using module: <module-name>
```

Use the actual frontmatter `name` value in the marker.

Every `SKILL.md` and `MODULE.md` must also include:

- A purpose, overview, or operating policy section.
- The core workflow, rules, or decision process the artifact teaches.
- Any hard-stop conditions or precedence rules that affect behavior.
- A usage checklist when the artifact has validation or completion criteria.
- A `Cross-References` section, even if it is empty.

The `Cross-References` section should identify related modules, reference files,
or follow-on modules. If none apply, write `None`.

Use only these labels in `Cross-References`:

- `BEFORE` for modules that should be loaded or applied first. `BEFORE` edges
  may be followed recursively.
- `WITH` for modules that should be applied alongside this one only when the task
  or changed files already touch that area. Do not expand `WITH` transitively.
- `AFTER` for follow-on modules to consider once the task is complete. Do not
  expand `AFTER` transitively.

Inline cross-references must match `references/module-graph.md`. Keep the graph
and artifact body synchronized in the same change.

## OpenAI Metadata Standard

Only the public `cortex` skill may include `agents/openai.yaml`, with at least:

```yaml
interface:
  display_name: "(otwld) Human Readable Name"
  short_description: "Short description for skill lists"
  default_prompt: "Use $cortex when ..."
policy:
  allow_implicit_invocation: false
```

Rules:

- `interface.display_name` must include `(otwld)` for easy discovery in agent
  UIs and CLIs.
- `interface.short_description` must be brief and user-facing.
- `interface.default_prompt` must name `$cortex` and describe a realistic
  invocation.
- `policy.allow_implicit_invocation` must be `false` so `$cortex` is explicit.
- Internal modules must not include `agents/openai.yaml`.
- Keep metadata synchronized with `SKILL.md` whenever the public skill changes.

## Examples Policy

All illustrative examples must follow the `example-universe-enforcer` skill.
Use the recruitment agency job board universe for sample code, DTOs, API
payloads, Storybook data, docs snippets, and other examples.

Do not introduce unrelated example domains unless the user explicitly requests
one and the skill being edited requires that exception.

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
  any project-native docs, such as Storybook, MDX, README, API docs, or
  migration notes.
- Do not add placeholder comments or comments that merely restate the code.
  Prefer clearer names and stronger types where prose would be noise.

## Progressive Disclosure

Keep `SKILL.md` and `MODULE.md` focused on the essential procedure and decision
rules. There is no hard size limit, but large stable details should move into
supporting files:

- Put detailed documentation, schemas, policies, and examples in `references/`.
- Put fragile or repeated mechanical work in `scripts/`.
- Put reusable output resources in `assets/`.

When a supporting file exists, the owning `SKILL.md` or `MODULE.md` must say
when to read or use it. Avoid duplicating the same guidance in both the owning
artifact and a reference file.

Extracted project-specific APIs, package names, application names, helper names,
and workflow names are not active rules. Move retained historical details into a
`references/legacy-*.md` file whose first markdown heading includes `Legacy`.
Legacy files are non-normative: they may explain provenance, but active skill
instructions must remain project-agnostic and reusable across TypeScript
ecosystem projects.

## Maintenance Rules

- Preserve narrow artifact scope. Prefer small focused modules over broad doctrine
  documents.
- Follow the existing local style unless this file defines a stricter rule.
- Update related metadata, references, scripts, and cross-references when a
  skill or module changes.
- Update `SKILL_CATALOG.md` when adding, removing, moving, or renaming a skill
  or module.
- Avoid unrelated rewrites, formatting churn, and broad reorganization.
- Keep examples, names, and prompts consistent across the public `SKILL.md` and
  `agents/openai.yaml`; keep module names synchronized with `MODULE.md`.
- Keep source-project residue out of active skill instructions.
- If adding a script, make it deterministic and document the command or trigger
  in the owning `SKILL.md` or `MODULE.md`.
- If adding a reference file, make it directly discoverable from the owning
  `SKILL.md` or `MODULE.md`.
- Do not add per-module registries to validation scripts. Validation should
  derive discovery from taxonomy paths, frontmatter, metadata,
  `references/module-graph.md`, and `SKILL_CATALOG.md`.

## Validation Checklist

Before finishing any Cortex artifact change, verify:

- The public `governance/core/cortex/SKILL.md` exists and has valid YAML
  frontmatter with `name` and `description`.
- Every internal module uses `MODULE.md`, not `SKILL.md`.
- Each artifact includes the standardized `Output Marker`.
- Each artifact includes `Cross-References`, with `None` if empty.
- Only `governance/core/cortex/agents/openai.yaml` exists.
- Public metadata includes `interface.display_name`,
  `interface.short_description`, and `interface.default_prompt`.
- OpenAI metadata fields live under the top-level `interface:` block.
- `interface.display_name` contains `(otwld)`.
- `policy.allow_implicit_invocation` is `false`.
- `SKILL_CATALOG.md` lists each skill and module once under the correct taxonomy heading
  with the correct directory path.
- Any referenced files, scripts, or assets actually exist.
- Any touched scripts still run or have been validated appropriately.
- Examples follow `example-universe-enforcer`.
- The artifact remains focused on a clear task, domain, or workflow.

Run the workspace validator before finishing:

```bash
python3 scripts/validate-skills.py
```

When `scripts/validate-skills.py` or validation-facing routing contracts change,
also run:

```bash
python3 scripts/test-validate-skills.py
```
