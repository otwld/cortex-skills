---
name: bricks
description: "Use when working with Bricks in consumer Nx repositories: inspecting or running Bricks init, source, install, merge, diff, status, doctor, or contribute commands; reviewing installed-brick edits; updating installed copies; or helping contribute consumer edits back to source repos through Bricks worktree workflows. Do not use for Nx release, npm publishing, or source-repo maintainer release workflows unless Bricks consumer state is directly involved."
---

# Output Marker

Display:
using skill: bricks

---

# Bricks

## Overview

Use Bricks as a source-management CLI for consumer Nx workspaces. Bricks moves
real source code from Git-backed Nx repos into a consumer repo, records where it
came from, and helps merge or contribute source-level changes later.

## Operating Policy

- Inspect the current Bricks docs or command code before making precise CLI,
  flag, output, config-schema, or behavior claims. Bricks is under active
  development, and stale assumptions are worse than a short source read.
- Treat installed bricks as consumer-owned source after install. The consumer
  owns edits, validation, commits, and conflict resolution.
- Treat `.bricks/sources/<name>` as Bricks-managed source cache, not the place
  to author contributions.
- Respect the consumer repo's Git ignore rules. Do not invent hardcoded
  exclusion lists for generated files, dependencies, or local artifacts.
- Challenge bad workflows directly: Bricks is not package sharing, npm release
  orchestration, a source checkout replacement, or a compatibility shim.
- Do not resurrect selection-based contribution UX. Contribution review happens
  in a Git worktree with normal Git and IDE tools.

## Reference Routing

- Read `references/product-model.md` for Bricks mental model, ownership
  boundaries, and product non-goals.
- Read `references/cli-workflows.md` for command families, agent usage, and
  when to inspect `docs/command-reference.md` or command implementation.
- Read `references/contribution-workflow.md` for contributing consumer edits
  back to source repos through `bricks contribute`.

Read only the reference that matches the task. When the user asks for exact
syntax or behavior, read the relevant reference and then inspect current
Bricks docs or code in the repo being operated on.

## Workflow

1. Classify the request:
   - Product model, ownership, or "what is Bricks": use the product model
     reference.
   - Install, update, diff, status, source, or doctor work in a consumer repo:
     use the CLI workflow reference.
   - Preparing source contributions from consumer edits: use the contribution
     workflow reference.
   - Nx workspace structure affected by copied source: also apply
     `nx-conventions` when the task directly touches Nx configuration.
2. Check the workspace state before mutating files or running mutating Bricks
   commands. Protect unrelated user changes.
3. Inspect local Bricks documentation or command code for exact commands and
   flags. Prefer `docs/command-reference.md`, command registration, and the
   command implementation closest to the behavior in question.
4. Use `--json` for agent-readable inspection and `--dry-run` for mutating
   command planning when the command supports it.
5. For contribution workflows, use
   `bricks contribute plan <source> -> bricks contribute open <source> -> Git
   worktree review -> bricks contribute commit <source> -> bricks contribute
   push <source>`.
6. Verify results from command output, Git state, and relevant consumer or
   source-repo checks before reporting completion.

## Hard Stops

- Do not claim an exact Bricks CLI surface from memory when current docs or
  command code are available.
- Do not model Bricks as package installation, npm publishing, source
  submodules, vendoring without provenance, or shared package release flow.
- Do not bypass `bricks contribute open` and Git worktree review when preparing
  a source contribution from consumer edits.
- Do not ask the user to preselect or reject contribution files as the primary
  flow. Open the worktree, then keep or drop changes with Git review.
- Do not manually hardcode ignored paths. Use Git ignore semantics and Bricks'
  own candidate planning.
- Do not edit `.bricks/sources` as though it were the contribution branch.
- Do not handle Nx release, package publishing, or source-maintainer release
  process as Bricks work unless Bricks consumer metadata or installed bricks
  are directly involved.

## Usage Checklist

- The relevant Bricks reference was read for the request type.
- Current Bricks docs or command code were inspected before exact CLI claims.
- Workspace state and user changes were protected before mutation.
- Git ignore behavior was respected instead of duplicated manually.
- Contribution work used the worktree flow and normal Git review.
- Verification evidence matches the final claim.

## Cross-References

- WITH: workspace-state-guard, nx-conventions, completion-verification
