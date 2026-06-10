---
name: storybook-angular-conventions
description: Use when creating, modifying, or reviewing Angular Storybook stories, Angular story providers, module metadata, standalone story setup, or Angular story mocks.
---

# Output Marker

Display:
using skill: storybook-angular-conventions

---

# Storybook Angular Conventions

## Overview

Apply Angular-specific Storybook rules on top of generic Storybook conventions.
Keep this skill focused on Angular wiring, not generic story organization.

## Core Rules

- Apply `storybook-conventions` for title structure, MDX identity, duplicate-title handling, source-mirror docs, and deterministic story data.
- Use `moduleMetadata` when a story needs Angular imports or declarations.
- Use `applicationConfig` when a standalone story needs application-wide providers.
- Prefer colocated stories near the Angular component under test.
- Keep story templates and args explicit enough to reveal the component state.
- Compose mock handlers through the project's shared Storybook mock strategy.
- Keep generated data deterministic for visual regression stories.

## Usage Checklist

- Generic Storybook conventions were applied first.
- Angular dependencies are provided through `moduleMetadata` or `applicationConfig`.
- Story titles, MDX names, and shared-title exports follow generic Storybook identity rules.
- Source-mirror MDX is used for short Angular-facing source docs when the project has an approved source import resolver.
- Story args and templates are explicit.
- Mocks are composed through project-level setup.
- Visual data is deterministic.

## Cross-References

- BEFORE: storybook-conventions, angular-conventions
- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
