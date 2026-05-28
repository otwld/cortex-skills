---
name: vitest-conventions
description: Use when creating, modifying, or reviewing Vitest configuration, Vitest tests, setup files, environments, mocks, or Vite-integrated test behavior.
---

# Output Marker

Display:
using skill: vitest-conventions

---

# Vitest Conventions

## Overview

Keep Vitest close to the project's Vite and TypeScript configuration. Verify
current Vitest APIs, configuration options, CLI behavior, setup, and migration
details with the AGENTS.md Context7 workflow whenever the task asks about them.

## Core Rules

- Keep Vitest config aligned with Vite aliases and TypeScript paths.
- Put shared setup in explicit setup files.
- Prefer behavior-focused tests with clear names.
- Use fake timers, mocks, and globals only when they make the behavior testable.
- Avoid copying Jest-only patterns without checking Vitest support.

## Usage Checklist

- Vitest config follows project Vite settings.
- Setup files are explicit.
- Tests are behavior-focused.
- Timers and mocks are reset when used.

## Cross-References

- WITH: vite-conventions, typescript-code-style
- AFTER: skill-evolution
