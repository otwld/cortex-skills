
# Output Marker

Display:
using module: nx-conventions

---

# Nx Conventions

## Overview

Treat Nx configuration as shared infrastructure for graph accuracy, target semantics,
and cache behavior.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect project metadata; preserve target inputs/outputs; avoid root config churn; coordinate project moves with boundaries.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Nx project metadata, inferred tasks, targets, inputs, and outputs remain aligned with actual build behavior.
- Workspace graph effects are understood before changing root config, generators, or project files.
- Moves or new projects coordinate with module-boundary and placement decisions.

## Example

A job-offer-search library gets project tags that match domain scope, not a vague
shared-search label.

## Hard Stops

- Do not change root Nx config to solve one project problem without checking local project metadata.
- Do not add targets, generators, or inferred-task overrides that duplicate existing behavior.
- Do not move projects without checking graph and boundary consequences.

## Usage Checklist

- Nx workspace files, project metadata, targets, and graph implications were inspected.
- Inputs, outputs, cache behavior, and inferred tasks remain intentional.
- Nx validation command or graph-inspection gap was recorded.

## Cross References

- WITH: nx-module-boundaries, library-placement-decision
