# Bricks Run

## Overview

Operate through Bricks commands while keeping consumer edits, source cache, and
contribution worktrees assigned to the correct owner.

## Workflow

1. Run from the consumer Nx workspace root unless current Bricks docs or command
  code specify another location.
2. Inspect consumer Git status and Bricks state. Prefer `--json` for
  machine-readable command output when supported.
3. Prefer dry-run modes for mutating install, merge, source update, remove, or
  contribution commands when current command support exists.
4. Use Bricks commands for provenance-aware install, merge, diff, status, doctor,
  and contribution work. Do not manually copy files to simulate those workflows.
5. Resolve Bricks merge conflicts using normal Git conflict resolution in the
  consumer copy, then continue through the documented Bricks command.

## Quality Gates

- Use `bricks contribute plan <source>` to inspect candidate consumer edits.
- Use `bricks contribute open <source>` to create the dedicated source worktree.
- Review the opened worktree as source code: keep reusable fixes, drop
  consumer-only branding, generated output, temporary files, local environment
  changes, and integration choices that do not belong upstream.
- Validate from the source worktree using that source repo's own targets.
- Commit or push through the Bricks contribution flow only from a clean,
  intentionally staged contribution worktree.

## Hard Stops

- Do not overwrite consumer edits during install or merge. Inspect diff or status
  evidence first.
- Do not edit `.bricks/config.json` manually unless current Bricks docs or code
  require manual recovery.
- Do not invent file-selection flags for contribution commands. Use current docs
  and command code as the source of truth.
- Do not commit or push from a dirty contribution worktree.

## Phase Output

Return the commands run or selected, mutation boundaries, consumer/source state
classification, conflict or dirty-worktree status, and validation checkpoints
needed next.
