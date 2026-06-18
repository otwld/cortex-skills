# Contribution Workflow

Use this reference when local installed-brick edits in a consumer repo may need
to become source-repo changes.

## Required Flow

1. Inspect consumer Git status and Bricks state. Protect unrelated user work.
2. Run or reason from `bricks contribute plan <source>` to see candidate local
   edits. Use `--json` when machine-readable output helps.
3. Run `bricks contribute open <source>` to create a dedicated source worktree
   and apply every candidate edit as source changes.
4. Review the opened worktree with normal Git and IDE tools:
   - keep generic source improvements,
   - edit changes that need cleanup before source contribution,
   - drop consumer-only tracked changes with `git restore -- <path>`,
   - drop consumer-only untracked files with `git clean -f -- <path>`,
   - resolve any conflict markers in the worktree.
5. Validate from the source worktree using the source repo's own docs and
   available targets.
6. Use `bricks contribute status <source>` to inspect the active session.
7. Use `bricks contribute commit <source>` after review and validation.
8. Use `bricks contribute push <source>` when the contribution branch is ready.

## Rules

- Do not ask for upfront file selection as the main contribution interface.
  Bricks opens all candidates, then Git review keeps or drops changes.
- Do not invent `--select`, `--reject`, or file-filter flags unless current
  Bricks docs and code actually provide them.
- Do not hardcode ignored file exclusions. Bricks planning must respect the
  consumer workspace's Git ignore rules.
- Do not edit `.bricks/sources/<name>` to prepare contribution commits. It is
  source cache, not the writable contribution worktree.
- Do not commit or push from a dirty contribution worktree. Resolve conflicts,
  stage intentionally, and verify the source worktree first.

## Review Standard

The goal is source-quality changes, not copying every consumer customization
back to the source repo. Keep reusable fixes and improvements. Drop local
branding, environment, generated output, temporary files, and consumer-only
integration choices during worktree review.
