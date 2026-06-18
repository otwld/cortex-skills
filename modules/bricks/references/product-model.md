# Product Model

Bricks is an Nx-only source manager. It registers Git-backed Nx repos as
sources, pulls them into Bricks-managed cache for analysis, copies selected apps
and libraries into a consumer Nx workspace, and records provenance for later
diff, merge, status, and contribution work.

## Ownership

- A source repo owns the original app or library source.
- The consumer repo owns the installed copy after Bricks copies it.
- `.bricks/config.json` records portable source and install metadata.
- `.bricks/sources/<name>` is operational cache for source analysis and update
  planning. Do not treat it as the consumer-owned copy or contribution branch.

## Mental Model

Installed bricks are ordinary source files in the consumer workspace. They are
not package dependencies, generated artifacts, submodules, or a live checkout of
the source repo. The consumer can edit, format, test, and commit them like any
other local source.

Bricks keeps enough source identity to answer:

- which source repo and project a copy came from,
- which source commit is the recorded base,
- which local files changed since install or merge,
- how incoming source changes merge into the installed copy.

## Product Boundaries

Bricks may coordinate package-manager and Nx metadata updates only to make
copied source usable in the consumer workspace. It is not an npm publishing
tool, Nx release workflow, package-sharing abstraction, or compatibility layer.

When current behavior matters, inspect the active Bricks docs and command code
instead of assuming older command shapes or internal models still apply.
