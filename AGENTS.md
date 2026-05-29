# AGENTS.md

## Purpose

This workspace contains homemade AI skills. Treat each skill as a small,
self-contained operating guide for agents. Keep instructions precise,
maintainable, and easy to discover.

These rules primarily govern writing and maintaining skills in this workspace.
They are intentionally agent-neutral.

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
- `maintenance/` for workspace maintenance skills and example policy.
- `testing/` for test-runner and end-to-end testing conventions.
- `typescript/` for TypeScript language, API, and style conventions.
- `references/` for workspace-wide references such as the skill graph.
- `scripts/` for workspace-wide validation and maintenance scripts.

## Skill Directory Standard

Every skill must live in its own short directory slug under the relevant
taxonomy folder. Related ecosystems may introduce one grouping level before the
skill slug:

```text
taxonomy[/group]/folder-slug/
|-- SKILL.md
`-- agents/
    `-- openai.yaml
```

The frontmatter `name` remains the canonical skill name. The folder slug should
omit words already made obvious by the taxonomy and group path, such as
`frameworks/angular/core` for `angular-conventions`,
`frameworks/angular/material` for `angular-material-conventions`,
`testing/jest` for `jest-conventions`, and `typescript/api` for
`typescript-api-conventions`.

Optional supporting directories:

- `references/` for detailed reference material that should be loaded only when
  needed.
- `scripts/` for deterministic or repeated operations.
- `assets/` for templates, images, fixtures, or other output resources.

Do not add extra README, changelog, quick-reference, or installation files
unless the skill genuinely needs them at runtime.

## SKILL.md Standard

Every `SKILL.md` must start with YAML frontmatter:

```markdown
---
name: skill-name
description: Clear trigger guidance explaining when this skill should be used.
---
```

The `description` is the main discovery surface. It must explain the task,
domain, trigger conditions, and important exclusions clearly enough that an
agent can decide whether to load the skill.

After the frontmatter, every skill must include this standardized output marker:

```markdown
# Output Marker

Display:
using skill: <skill-name>
```

Use the actual frontmatter `name` value in the marker.

Every `SKILL.md` must also include:

- A purpose, overview, or operating policy section.
- The core workflow, rules, or decision process the skill teaches.
- Any hard-stop conditions or precedence rules that affect behavior.
- A usage checklist when the skill has validation or completion criteria.
- A `Cross-References` section, even if it is empty.

The `Cross-References` section should identify related skills, reference files,
or follow-on skills. If none apply, write `None`.

Use only these labels in `Cross-References`:

- `BEFORE` for skills that should be loaded or applied first. `BEFORE` edges
  may be followed recursively.
- `WITH` for skills that should be applied alongside this one only when the task
  or changed files already touch that area. Do not expand `WITH` transitively.
- `AFTER` for follow-on skills to consider once the task is complete. Do not
  expand `AFTER` transitively.

Inline cross-references must match `references/skill-graph.md`. Keep the graph
and the skill body synchronized in the same change.

## OpenAI Metadata Standard

Every skill must include `agents/openai.yaml` with at least:

```yaml
interface:
  display_name: "(otwld) Human Readable Name"
  short_description: "Short description for skill lists"
  default_prompt: "Use $skill-name when ..."
```

Rules:

- `interface.display_name` must include `(otwld)` for easy discovery in agent
  UIs and CLIs.
- `interface.short_description` must be brief and user-facing.
- `interface.default_prompt` must name the skill and describe a realistic
  invocation.
- Keep metadata synchronized with `SKILL.md` whenever a skill changes.

## Examples Policy

All illustrative examples must follow the `example-universe-enforcer` skill.
Use the recruitment agency job board universe for sample code, DTOs, API
payloads, Storybook data, docs snippets, and other examples.

Do not introduce unrelated example domains unless the user explicitly requests
one and the skill being edited requires that exception.

## Progressive Disclosure

Keep `SKILL.md` focused on the essential procedure and decision rules. There is
no hard size limit, but large stable details should move into supporting files:

- Put detailed documentation, schemas, policies, and examples in `references/`.
- Put fragile or repeated mechanical work in `scripts/`.
- Put reusable output resources in `assets/`.

When a supporting file exists, `SKILL.md` must say when to read or use it. Avoid
duplicating the same guidance in both `SKILL.md` and a reference file.

Extracted project-specific APIs, package names, application names, helper names,
and workflow names are not active rules. Move retained historical details into a
`references/legacy-*.md` file whose first markdown heading includes `Legacy`.
Legacy files are non-normative: they may explain provenance, but active skill
instructions must remain project-agnostic and reusable across TypeScript
ecosystem projects.

## Maintenance Rules

- Preserve narrow skill scope. Prefer small focused skills over broad doctrine
  documents.
- Follow the existing local style unless this file defines a stricter rule.
- Update related metadata, references, scripts, and cross-references when a
  skill changes.
- Avoid unrelated rewrites, formatting churn, and broad reorganization.
- Keep examples, names, and prompts consistent across `SKILL.md` and
  `agents/openai.yaml`.
- Keep source-project residue out of active skill instructions.
- If adding a script, make it deterministic and document the command or trigger
  in `SKILL.md`.
- If adding a reference file, make it directly discoverable from `SKILL.md`.

## Validation Checklist

Before finishing any skill change, verify:

- `SKILL.md` exists and has valid YAML frontmatter with `name` and
  `description`.
- `SKILL.md` includes the standardized `Output Marker`.
- `SKILL.md` includes `Cross-References`, with `None` if empty.
- `agents/openai.yaml` exists.
- `agents/openai.yaml` includes `interface.display_name`,
  `interface.short_description`, and `interface.default_prompt`.
- `interface.display_name` contains `(otwld)`.
- Any referenced files, scripts, or assets actually exist.
- Any touched scripts still run or have been validated appropriately.
- Examples follow `example-universe-enforcer`.
- The skill remains focused on a clear task, domain, or workflow.

Run the workspace validator before finishing:

```bash
python3 scripts/validate-skills.py
```
