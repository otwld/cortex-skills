# TypeScript Code Style Activate

## Overview

Use this phase when the task writes, edits, generates, refactors, or reviews
TypeScript or TSX implementation code. The phase selects the local references
needed for the touched concern and identifies the project tooling that can
enforce the decision.

## Workflow

1. Inspect touched paths for `.ts`, `.tsx`, `.mts`, or `.cts` files, including
   tests, framework components, build helpers, and code-generation consumers.
2. Identify the style concern being changed: file structure, imports, exports,
   type-only imports, names, type constructs, language features, assertions,
   comments, compiler directives, or generated-code boundaries.
3. Open only the owned references that match the concern:
   `references/source-modules.md`, `references/types-naming.md`,
   `references/language-features.md`, or
   `references/comments-tooling-policy.md`.
4. Check whether `scripts/ts_style_preflight.py` can scan the changed paths
   usefully. If not, name the reason, such as no TypeScript files or a
   generated-only change.
5. Identify the nearest project typecheck, lint, format, and test commands
   without broadening the task into unrelated cleanup.

## Quality Gates

- Activation names the TypeScript files or file families that need style
  handling.
- Selected references correspond to the actual touched concern.
- The phase records the local project convention or tooling that has priority
  over the general guide.
- Preflight applicability is explicit.

## Hard Stops

- Do not activate for non-TypeScript code solely because the project uses
  TypeScript elsewhere.
- Do not open every reference when the task touches only one narrow style area.
- Do not treat generated output as hand-written source unless the generator or
  checked-in consumer requires manual style control.
- Do not turn a focused functional change into broad style cleanup.

## Phase Output

Return the activation decision, touched TypeScript surfaces, selected local
references, tooling to run or skip, and style risks that need attention in the
run or review phase.
