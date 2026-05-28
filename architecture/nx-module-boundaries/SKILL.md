---
name: nx-module-boundaries
description: Use when working in an Nx workspace and adding, moving, or reviewing projects, tags, dependencies, or module-boundary rules.
---

# Output Marker

Display:
using skill: nx-module-boundaries

---

# Nx Module Boundaries

## Overview

Use the project graph and configured tags to keep Nx workspaces modular. Never
guess dependency direction or tags when the workspace can be inspected.

## Workflow

1. Inspect available Nx configuration, project metadata, and dependency graph.
2. Identify project role, scope tags, and intended consumers.
3. Check the dependency direction before adding imports or package references.
4. Prefer fixing ownership or extraction problems over weakening boundary rules.

Use the repository's available Nx tools or CLI commands. If an Nx graph is not
available, fall back to project files and existing import patterns.

## Boundary Rules

- Each project should have one primary responsibility.
- Tags should express scope and project type clearly enough to enforce imports.
- Feature-level code must not create horizontal coupling across unrelated features.
- Shared logic belongs in a correctly owned domain, utility, UI, or integration package.
- Circular dependencies must be resolved by changing ownership or dependency flow.

## Hard Stops

Stop and propose a migration path when:

- A circular dependency is introduced.
- Dependency direction is reversed.
- Tags are removed or bypassed to make an import compile.
- A reusable package starts depending on application-only code.

## Usage Checklist

- Project role and owner are known.
- Tags and constraints were inspected.
- New dependencies obey configured direction.
- Shared code is extracted to the correct reusable layer.

## Cross-References

- BEFORE: library-placement-decision
- WITH: public-api-design
