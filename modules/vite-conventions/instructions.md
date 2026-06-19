
# Output Marker

Display:
using module: vite-conventions

---

# Vite Conventions

## Overview

Treat Vite config as a build contract for dev speed and published output.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Keep aliases aligned with public entry points; externalize peers for libraries; preserve source maps intentionally; document plugin order when important.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Vite aliases, plugins, library builds, source maps, and externals match the package's public entry points.
- Plugin ordering and environment-specific config are documented when behavior depends on them.
- Dependencies are bundled or externalized intentionally for apps versus libraries.

## Example

A Candidate UI package externalizes framework peers instead of bundling runtime into the
library output.

## Hard Stops

- Do not add aliases that bypass library public APIs or Nx/module boundaries.
- Do not bundle peer dependencies into library output without naming the consumer impact.
- Do not change plugin order, sourcemaps, or dev-server behavior without a validation path.

## Usage Checklist

- Vite config, aliases, plugins, build output, and dependency mode were inspected.
- Entry points, externals, source maps, and plugin order remain intentional.
- Build, dev-server, or source-map validation was run or blocked explicitly.

## Cross References

- WITH: bundle-performance, typescript-code-style, code-documentation
- AFTER: skill-evolution
