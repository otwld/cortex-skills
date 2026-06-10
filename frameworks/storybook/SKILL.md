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
- Derive story titles from meaningful path segments; omit structural folders such as `src` and `lib`.
- Keep named story exports unique when several files intentionally share a title.
- Use MDX docs blocks for narrative docs and API examples when stories alone are not enough.
- Centralize global preview setup and addons.
- Keep network mocks composable and reusable when multiple stories share the same API surface.
- Use deterministic data for visual regression stories; avoid unseeded randomness and current time.

## Legacy References

- `references/legacy-extracted-patterns.md` preserves non-normative helper names from the extracted source project.

## Usage Checklist

- Meta export and named stories are present.
- Title follows project path conventions.
- Args are explicit and minimal.
- Mocks are centralized or reusable when shared.
- Visual regression stories are deterministic.

## Cross-References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
