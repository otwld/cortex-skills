# TypeScript Code Style Review

## Overview

Review TypeScript source changes for high-signal style issues that affect
correctness, maintainability, refactor safety, tooling, or API documentation.

## Workflow

1. Inspect the diff rather than the whole repository. Note any touched
   TypeScript files that were intentionally left out of style review.
2. Check imports and exports for private-file bypasses, accidental default
   exports, mutable exports, missing type-only imports, and dead or misleading
   aliases.
3. Check typing for `any`, `{}`, broad `object`, broad casts, double
   assertions, non-null assertions, unsafe dictionary access, and return-type
   annotations that hide inference problems.
4. Check naming and structure against the selected owned reference and nearby
   local convention.
5. Check comments and JSDoc/TSDoc: exported or reusable touched symbols should
   be documented, while ordinary comments should explain intent or constraints
   rather than restating syntax.
6. Run or request `scripts/ts_style_preflight.py` for relevant TypeScript paths
   and review project typecheck, lint, and focused test results when available.
7. Separate blocking style findings from optional cleanup so the review remains
   focused on risk.

## Quality Gates

- Findings cite exact files, lines, symbols, and the style or tooling risk.
- Mechanical findings are backed by preflight, compiler, lint, or visible diff
  evidence.
- Suggested fixes preserve user-requested behavior and local project policy.
- Optional cleanup is labeled as such and does not block unrelated behavior.

## Hard Stops

- Do not approve a change that suppresses TypeScript errors without a narrow,
  documented reason.
- Do not approve imports through private paths when the public entry point is
  the intended access path.
- Do not approve newly exposed symbols that lack useful API documentation when
  the surrounding project documents exported surfaces.
- Do not request broad restyling that is unrelated to a concrete risk in the
  touched code.

## Phase Output

Return review findings ordered by severity, selected reference files, validation
evidence examined, and any accepted deviations from the style guide with their
local justification.
