# CLI Workflows

Use this reference for Bricks consumer commands such as source management,
install, merge, diff, status, and doctor. It maps the command families and
agent posture; it is not a substitute for current command docs or code.

## Before Precise CLI Claims

Inspect the Bricks repo being operated on before giving exact flags, output
schema, or behavior:

- `docs/command-reference.md` for intended command surface,
- command registration for visible CLI names and options,
- command implementation for behavior and edge cases,
- tests when docs and implementation disagree.

## Command Families

- `bricks init`: initialize Bricks metadata in a consumer Nx workspace.
- `bricks source ...`: add, pull, list, inspect projects from, or remove a
  Git-backed Nx source repo.
- `bricks install ...`: copy a source project into the consumer workspace and
  record install metadata.
- `bricks merge ...`: merge newer source commits into installed local copies.
- `bricks merge continue ...`: finish a merge after manual conflict resolution.
- `bricks diff ...`: compare an installed local copy against source.
- `bricks status`: show configured sources and installed bricks.
- `bricks remove ...`: remove an installed-brick record without deleting copied
  source files.
- `bricks doctor`: validate Bricks state in the consumer workspace.
- `bricks contribute ...`: prepare source-repo contributions from consumer
  edits. Use `references/contribution-workflow.md` for this family.

## Agent Posture

- Run from the consumer Nx workspace root unless current docs say otherwise.
- Prefer `--json` for agent-readable inspection.
- Prefer `--dry-run` before mutating commands when supported.
- Use normal Git conflict resolution for Bricks merge conflicts.
- Inspect `.bricks/config.json` only as metadata; do not hand-edit it unless
  current Bricks docs or code explicitly require manual recovery.
- Validate with consumer repo commands after install, merge, or local conflict
  resolution.

## Out Of Scope

Nx release automation, npm publishing, package promotion, and source-maintainer
release process are not Bricks consumer workflows by default. If the user asks
for those, inspect the repo's release docs and apply the appropriate release or
Nx skills instead of forcing the task through Bricks.
