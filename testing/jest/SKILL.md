---
name: jest-conventions
description: Use when creating, modifying, or reviewing Jest configuration, Jest tests, setup files, custom matchers, test environments, or Jest mocks.
---

# Output Marker

Display:
using skill: jest-conventions

---

# Jest Conventions

## Overview

Keep Jest configuration explicit and tests focused on observable behavior.
When a task asks about Jest APIs, configuration options, CLI behavior, setup, or
migration details, follow the AGENTS.md Context7 workflow before relying on
memory.

## Core Rules

- Keep Jest configuration in the project's established config location.
- Use setup files only for shared test environment behavior.
- Prefer `setupFilesAfterEnv` for custom matchers and environment extensions.
- Keep mocks local unless a reusable mock factory removes real duplication.
- Avoid tests that assert implementation details instead of behavior.

## Usage Checklist

- Config is discoverable by the test command.
- Setup files are scoped to real shared behavior.
- Tests are behavior-focused.
- Reusable mocks are typed and intentional.

## Cross-References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
