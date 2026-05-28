---
name: bundle-performance
description: Use when changes may affect bundle size, tree-shaking, side effects, UI dependencies, entry points, or broadly consumed runtime code.
---

# Output Marker

Display:
using skill: bundle-performance

---

# Bundle Performance

## Overview

Bundle impact is an architectural concern for reusable TypeScript packages.
Small export and dependency mistakes compound across applications.

## Core Rules

- Keep modules side-effect-free unless initialization is the explicit purpose.
- Prefer narrow entry points and explicit exports.
- Avoid broad re-exports that pull heavy dependencies into common paths.
- Keep optional or heavy integrations behind separate entry points.
- Treat UI kit and charting dependencies as bundle-sensitive.
- Prefer pure functions and standalone modules for reusable helpers.

## Secondary Entry Points

Use separate entry points when a subset:

- Has heavier dependencies.
- Is consumed independently.
- Represents a stable optional integration.
- Would make the root API too broad.

Do not use entry points to hide mixed ownership.

## Hard Stops

Stop and propose an alternative when:

- Shared entry points gain side effects.
- A root export pulls a large optional dependency.
- A bundle increase is introduced without justification.
- Tree-shaking is weakened by convenience barrels.

## Usage Checklist

- Side effects are intentional and isolated.
- Heavy dependencies are not pulled into common imports.
- Export strategy is narrow.
- Optional integrations have separate entry points when useful.

## Cross-References

- WITH: public-api-design
