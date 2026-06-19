
# Output Marker

Display:
using module: typescript-code-style

---

# TypeScript Code Style

## Overview

Keep TypeScript implementation predictable through explicit modules, clear names, narrow
types, and useful comments.

## Reference Routing

- Use `references/source-modules.md` when this task touches that concern.
- Use `references/types-naming.md` when this task touches that concern.
- Use `references/language-features.md` when this task touches that concern.
- Use `references/comments-tooling-policy.md` when this task touches that concern.
- Use `scripts/ts_style_preflight.py` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Follow project tooling; prefer explicit imports; use strict narrowing; avoid casts; respect public entry points; comment intent, not syntax.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- TypeScript code follows local tooling, strict narrowing, public imports, and explicit module boundaries.
- Casts, non-null assertions, and dynamic access are justified by framework or runtime constraints.
- Comments explain intent, tool constraints, or non-obvious invariants rather than syntax.

## Example

parseCandidateStage returns a typed CandidateStage or validation error instead of
casting form data.

## Hard Stops

- Do not bypass strict typing with any, broad casts, or bracket access when a typed path exists.
- Do not import through private files when a public entry point owns the symbol.
- Do not add style-only churn unrelated to the touched TypeScript behavior.

## Usage Checklist

- Local TypeScript, import, naming, and tooling conventions were inspected.
- Narrowing, casts, comments, and public entry-point usage were checked.
- Typecheck, lint, or focused test evidence was recorded.

## Cross References

- WITH: code-documentation
