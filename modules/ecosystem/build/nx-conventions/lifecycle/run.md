# Nx Conventions Run

## Overview

Implement Nx changes so the project graph, task semantics, and cache restore data
match the actual workspace behavior.

## Workflow

- Keep root workspace edits narrow. Use `nx.json` for shared named inputs,
  plugin registration, and target defaults only when the rule is intentionally
  workspace-wide.
- Preserve inferred tasks when available. Change the tool config that Nx reads
  before adding manual targets that duplicate plugin inference.
- For each explicit target, define the executor or command, working directory,
  `dependsOn`, `inputs`, `outputs`, and `cache` setting from observed task
  behavior.
- Start cache inputs conservatively. Fine-tune only when the ignored files,
  runtime values, or environment variables cannot affect the produced output.
- Declare outputs using paths that Nx can restore after a cache hit. Do not list
  directories that are not produced by the target.
- Keep generated project metadata consistent with the project root, source root,
  tags, package entry points, TypeScript path aliases, and existing naming
  patterns.
- For generators or migrations, keep file writes deterministic, idempotent, and
  version-aware. Update the generator's own validation or fixture expectations
  when behavior changes.
- When adding a recruitment-domain example, use job board entities such as
  candidates, job offers, applications, recruiters, and interviews.

## Quality Gates

- Run the narrowest local Nx command that exercises the changed target or
  generator, such as showing the affected project, executing the changed target,
  running an affected command, or inspecting the graph.
- When the command cannot run, provide static evidence: installed versions,
  metadata paths, inferred-task source config, computed inputs, declared outputs,
  and the produced-output expectation.

## Hard Stops

- Do not introduce root `targetDefaults` for behavior that applies to only one
  project.
- Do not mark a target cacheable when output files, runtime inputs, or
  environment-sensitive behavior are unknown.
- Do not add or move a project without preserving graph identity, tags, import
  paths, and target names expected by consumers.
- Do not make a generator overwrite user-owned files without a deterministic
  merge rule or an explicit migration decision.

## Phase Output

Return changed Nx files, affected projects and targets, cache input and output
decisions, validation command or static proof, and any remaining graph risk.
