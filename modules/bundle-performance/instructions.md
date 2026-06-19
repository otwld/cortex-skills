
# Output Marker

Display:
using module: bundle-performance

---

# Bundle Performance

## Overview

Prevent shared imports from accumulating global bundle cost through side effects, broad
barrels, or heavy optional dependencies.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Keep root entry points narrow; isolate optional integrations; preserve tree-shaking; document intentional bundle tradeoffs.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Shared entry points stay narrow and preserve tree-shaking for unaffected consumers.
- Optional integrations remain isolated from core runtime paths unless product behavior requires them.
- Bundle, dependency, side-effect, and public API tradeoffs are documented when they change.

## Example

JobOffer charting helpers live behind a charts entry point so Candidate list pages avoid
charting dependencies.

## Hard Stops

- Do not add broad runtime dependencies to shared UI or library roots without naming consumers.
- Do not hide side effects in barrels, setup files, or default imports.
- Do not optimize bundle shape by breaking public import paths without an API plan.

## Usage Checklist

- Entry point, dependency, side-effect, and optional-integration changes were inspected.
- Tree-shaking and public import behavior were preserved or intentionally changed.
- Bundle validation or accepted measurement gap was recorded.

## Cross References

- WITH: public-api-design
