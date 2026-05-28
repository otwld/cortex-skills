---
name: naming-consistency
description: Use when creating or renaming files, classes, functions, exports, DTOs, contracts, events, commands, providers, factories, or reusable abstractions.
---

# Output Marker

Display:
using skill: naming-consistency

---

# Naming Consistency

## Overview

Names are part of the architecture. Clear, explicit names make APIs easier to
discover, refactor, and reuse across projects.

## Rules

- Use complete words for public or reusable symbols.
- Avoid abbreviations unless they are established ecosystem terms.
- Match existing project vocabulary when it is clear and consistent.
- Prefer names that reveal responsibility, ownership, and layer.
- Do not hide unclear ownership behind names like `shared`, `common`, or `utils`.

## Common Patterns

- `createX`: factory creators.
- `provideX`: dependency-injection provider builders.
- `withX`: composition helpers.
- `parseX` / `formatX`: pure transforms.
- `isX` / `assertX`: type guards and invariants.
- `XDto`, `XEntity`, `XSchema`, `XRepository`, `XAdapter`: use only when those roles are real in the project.

## Hard Stops

Stop and rename when:

- A public API uses shorthand that readers must decode.
- A reusable package exports generic names with unclear ownership.
- A suffix claims a role the type does not perform.

## Usage Checklist

- Names use project vocabulary consistently.
- Public names are readable without surrounding context.
- Suffixes and prefixes describe real responsibilities.
- New names do not collide with existing concepts.

## Cross-References

- WITH: public-api-design, typescript-api-conventions
