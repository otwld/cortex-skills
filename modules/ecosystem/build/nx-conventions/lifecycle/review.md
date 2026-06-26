# Nx Conventions Review

## Overview

Find regressions in Nx project metadata, graph behavior, task execution, and
cache correctness.

## Workflow

- Compare `nx.json`, project metadata, package scripts, tool configuration, and
  generated files against the affected project's existing target behavior.
- Verify each target's command or executor, `dependsOn`, cache flag, inputs, and
  outputs describe the actual task.
- Check whether an inferred task was duplicated, disabled, or overridden without
  a local reason tied to the installed Nx plugin.
- Trace root config changes to every project that inherits them. Root defaults
  are risky when the diff only demonstrates one consumer.
- For project movement or naming changes, check project root, source root, tags,
  import paths, target names, and graph visibility.
- Confirm generator and migration changes are deterministic, idempotent, and
  covered by fixture or snapshot evidence when available.

## Quality Gates

- Findings identify the project, target, graph edge, cache input, or output path
  that can regress.
- Cache findings distinguish incorrect restore behavior from missed optimization.
- Missing validation is actionable: name the Nx command, graph inspection, or
  static metadata proof that would close the risk.

## Finding Triggers

- A cacheable target omits files, env values, or upstream inputs that affect its
  output.
- A target declares outputs that are not written or omits outputs that must be
  restored from cache.
- A root default changes target behavior for projects not discussed in the diff.
- An explicit target duplicates plugin-inferred behavior without adding needed
  semantics.
- A project move changes graph identity, tags, or import paths without evidence.

## Hard Stops

- Do not approve root workspace config churn without demonstrated inherited
  impact.
- Do not accept cache configuration when the reviewer cannot tell what changes
  invalidate the target or what files are restored.
- Do not approve graph-affecting project moves or generator rewrites without a
  validation path.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
specific Nx project, target, graph edge, cache behavior, or validation evidence
needed to close it.
