# Nx Conventions Activate

## Overview

Decide whether Nx conventions apply and capture the workspace evidence needed
before changing project metadata, targets, generators, or cache behavior.

## Workflow

1. Match the request or diff to Nx workspace files, project metadata, task
   configuration, generator code, migration code, or graph behavior.
2. Inspect the installed `nx` and `@nx/*` versions, `nx.json`, affected
   `project.json` or package metadata, and the tool configuration that may
   produce inferred tasks.
3. Name the affected projects, targets, generated outputs, cache inputs, and
   graph edges that can change.
4. Decide whether the change belongs in project-local metadata, shared
   `targetDefaults`, generator code, or the underlying tool configuration.
5. Identify the narrow Nx command or graph inspection that can prove the
   resulting metadata is accurate.

## Trigger Evidence

Activate for changes to `nx.json`, project metadata, workspace targets,
generators, executors, inferred-task configuration, project movement, tags,
affected execution, task caching, named inputs, or declared outputs.

Do not activate for a plain package script or tool config change unless Nx reads
that file for a target, generator, project graph edge, or cache decision.

## Decisions

- Prefer project-local target metadata unless the same target semantics apply to
  multiple projects through `targetDefaults`.
- Preserve inferred tasks when the installed Nx plugin can model the tool
  configuration. Add explicit targets only when inference is absent or
  demonstrably wrong for the local workspace.
- Treat cache inputs as correctness data. Include source files, relevant
  transitive inputs, runtime files, and environment values that affect target
  output.
- Treat outputs as restore data. They must match the files the target actually
  writes, not a guessed convention.
- For project moves, capture the project name, root, source root, tags, import
  paths, and affected graph edges before proposing metadata changes.

## Quality Gates

- Activation names concrete files, projects, targets, and graph or cache effects.
- The phase distinguishes inferred task behavior from explicit executor or
  command configuration.
- Validation needs are stated as a specific command, graph view, or static
  metadata check.

## Hard Stops

- The task changes root Nx config before the affected project-local metadata is
  inspected.
- A cacheable target is added or changed while its true inputs or outputs are
  unknown.
- An inferred-task override is proposed without checking the installed plugin and
  the tool config it reads.
- A project move or rename lacks graph, tag, and import-path evidence.

## Phase Output

Return the matched Nx evidence, affected projects and targets, metadata location
decision, cache or graph risk, and validation evidence required for the run or
review phase.
