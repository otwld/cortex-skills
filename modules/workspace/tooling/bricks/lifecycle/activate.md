# Bricks Activate

## Overview

Confirm that the task is a Bricks consumer-workspace workflow and classify which
Bricks state must be protected.

## Workflow

1. Confirm the workspace is an Nx consumer repo using Bricks metadata such as
  `.bricks/config.json`.
2. Identify the Bricks command family: `init`, `source`, `install`,
  `merge`, `diff`, `status`, `remove`, `doctor`, or `contribute`.
3. Classify whether the task involves installed app or library files, recorded source provenance,
  incoming source updates, consumer edits, merge conflicts, or a contribution
  worktree.
4. Inspect current Bricks docs or command code when exact flags, JSON
  shape, or edge-case behavior matter.

## Reference Use

- Read `references/product-model.md` for ownership boundaries between source
  repo, consumer copy, `.bricks/config.json`, and `.bricks/sources/<source>`.
- Read `references/cli-workflows.md` for command family posture and inspection
  expectations.
- Read `references/contribution-workflow.md` when consumer edits may become
  source-repo changes.

## Quality Gates

- Consumer copy: installed source files owned by the consumer repo.
- Source cache: `.bricks/sources/<source>`, used for analysis and update
  planning, not contribution commits.
- Contribution worktree: the dedicated source worktree opened by Bricks for
  review, validation, commit, and push.
- Out of scope: Nx release automation, npm publishing, and source-maintainer
  release process unless direct Bricks consumer state is part of the request.

## Hard Stops

- Do not treat `.bricks/sources/<source>` as the writable contribution worktree.
- Do not classify release or publish tasks as Bricks work from package names
  alone.
- Do not run a mutating Bricks command until consumer Git status and Bricks state
  are understood.

## Phase Output

Return the selected Bricks workflow family, the inspected state files or command
outputs, the protected side of the workflow, required references, and any reason
the task is outside Bricks consumer scope.
