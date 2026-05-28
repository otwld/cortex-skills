---
name: vite-conventions
description: Use when creating, modifying, or reviewing Vite configuration, library builds, aliases, plugins, source maps, dependency externalization, or dev-server settings.
---

# Output Marker

Display:
using skill: vite-conventions

---

# Vite Conventions

## Overview

Keep Vite configuration typed, explicit, and friendly to tree-shaking and
library consumers.

## Core Rules

- Use `defineConfig` for typed configuration.
- Keep aliases explicit and aligned with the project's TypeScript path mapping.
- Externalize peer dependencies in library mode.
- Preserve module structure when the package expects tree-shaking.
- Enable source maps for library builds unless the project explicitly disables them.
- Keep plugins purposeful and documented by name or local convention.

## Usage Checklist

- `defineConfig` is used.
- Aliases are intentional.
- Peer dependencies are externalized for libraries.
- Source maps and output format match project policy.

## Cross-References

- WITH: bundle-performance, typescript-code-style
- AFTER: skill-evolution
