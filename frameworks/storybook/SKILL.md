---
name: storybook-conventions
description: Use when creating, modifying, or reviewing Storybook stories, MDX docs, preview setup, addons, mocks, visual regression data, or story organization.
---

# Output Marker

Display:
using skill: storybook-conventions

---

# Storybook Conventions

## Overview

Use Storybook as executable UI documentation. Stories should be colocated,
focused on behavior or state, deterministic, and organized by stable project
structure.

## Core Rules

- Use Component Story Format with a typed default meta export and named story exports.
- Colocate story files with the component or example they document.
- Use one strict title format for stories and MDX: `<feature>/<technology>/<subject...>`.
- Derive titles from meaningful ownership and path segments; omit structural folders such as `src` and `lib`.
- Keep named story exports unique when several files intentionally share a title; avoid repeated generic exports such as `Primary` or `Playground` across that shared title.
- Use MDX docs blocks for narrative docs and API examples when stories alone are not enough.
- Centralize global preview setup and addons.
- Keep network mocks composable and reusable when multiple stories share the same API surface.
- Use deterministic data for visual regression stories; avoid unseeded randomness and current time.

## Title Format

All Storybook story and MDX titles must use:

```text
<feature>/<technology>/<subject...>
```

- `feature` is the owning package, domain, or product area without organization
  scope or technology prefix.
- `technology` is the short runtime or framework segment, such as `ts`, `ng`,
  `nest`, `storybook`, `react`, or `vue`.
- `subject` is the documented component, API, example, tool, or nested grouping.
- Use lowercase kebab-case for every segment.
- Do not include broad collection labels, display taxonomy labels, package scopes,
  or structural folders such as `packages`, `src`, and `lib`.
- Strip technology prefixes from package names before building the title.

Examples:

- `sdk/ts/object`
- `ui/ng/banner`
- `feature-flags/nest/feature-flags-service`
- `storybook/ng/http-client-search-example`

## MDX Identity

MDX page identity must be stable enough to avoid duplicate Storybook docs IDs.

- Keep `Meta` titles aligned with the same ownership/title convention as stories.
- Use `name="Documentation"` for MDX pages associated with a story file.
- Use a stable camelCase code name for MDX pages associated with a source file or API surface.
- When multiple MDX pages share one title or use story-associated metadata, choose names that remain unique within that title group.

## Source-Mirror Docs

When a project already has a configured source import resolver, use source-mirror
MDX for short API docs, types, small utilities, tokens, and source references.

- Import the canonical source file and render it through the project's Storybook docs source block.
- Treat JSDoc/TSDoc in the source file as the canonical explanation.
- Add prose only for usage constraints or integration notes that comments cannot express clearly.
- Do not inline long source snapshots or add ad hoc raw-file imports when the project has an approved source import path.

## Deterministic Stories

- Use stable seeds, dates, IDs, and generated data in visual-regression stories.
- Prefer reusable mock and data factories when several stories share the same API surface.
- Keep per-story mocks focused on scenario-specific payloads, statuses, or handler overrides.

## Legacy References

- `references/legacy-extracted-patterns.md` preserves non-normative helper names from the extracted source project.

## Usage Checklist

- Meta export and named stories are present.
- Story and MDX titles follow `<feature>/<technology>/<subject...>`.
- MDX `Meta` title and name avoid duplicate docs IDs.
- Shared story titles have unique story export names.
- Source-mirror MDX is used for short source docs when the project has an approved source import resolver.
- Args are explicit and minimal.
- Mocks are centralized or reusable when shared.
- Visual regression stories are deterministic.

## Cross-References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
