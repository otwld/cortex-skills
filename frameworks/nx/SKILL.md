---
name: nx-conventions
description: Use when creating, modifying, or reviewing Nx workspace configuration, generators, targets, project metadata, inferred tasks, or project graph behavior.
---

# Output Marker

Display:
using skill: nx-conventions

---

# Nx Conventions

## Overview

Use Nx as the workspace orchestration layer when a repository already uses Nx.
Prefer project-approved generators and configured targets over hand-written
workspace wiring.

## Core Rules

- Use Nx generators or local workspace generators for new projects when available.
- Run work through Nx targets when the repository defines them.
- Keep target names predictable, such as `build`, `serve`, `test`, and `lint`, unless local conventions differ.
- Keep projects single-responsibility and tagged when module-boundary rules use tags.
- Do not weaken dependency constraints to make a new import pass.
- Prefer reusable packages over repeated feature-local utilities when ownership is clear.

## Legacy References

- `references/legacy-extracted-patterns.md` preserves non-normative naming conventions from the extracted source project.

## Usage Checklist

- Nx configuration and local generators were inspected.
- Targets follow workspace conventions.
- Tags and boundary rules are preserved.
- New projects have clear responsibility.

## Cross-References

- WITH: nx-module-boundaries, library-placement-decision
