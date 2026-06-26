# TypeScript Code Style Run

## Overview

Apply local TypeScript style in the smallest useful diff while preserving
strict typing, clear modules, readable names, and comments that explain
caller-visible or implementation-critical intent.

## Workflow

1. Match nearby project conventions first, then apply the selected owned
   references where local code is inconclusive.
2. Keep imports explicit and intentional. Prefer named imports and named
   exports in owned code, use `import type` for type-only symbols, and use
   public entry points instead of private files when an entry point owns the
   symbol.
3. Preserve strict narrowing. Prefer runtime checks, type guards,
   discriminated unions, and declared interfaces over `any`, broad casts,
   non-null assertions, and bracket access.
4. Use names that communicate domain meaning. Do not add interface prefixes,
   type-encoding prefixes, or acronym casing that conflicts with the local
   guide.
5. Keep implementation language features predictable: `const` by default,
   no `var`, ES modules instead of namespaces, ordinary `enum` instead of
   `const enum`, and explicit error handling for non-obvious failures.
6. Add or update JSDoc/TSDoc for touched exported symbols and reusable public
   surfaces. Use ordinary comments only for implementation reasoning that code
   and types cannot express.
7. Avoid unrelated reformatting. If broad cleanup is necessary to make the
   change reviewable, isolate it from behavior changes where possible.
8. Run `scripts/ts_style_preflight.py` on changed TypeScript paths when it is
   relevant, then run the nearest project typecheck, lint, or focused tests
   that cover the edited code.

## Quality Gates

- Changed imports, exports, names, type annotations, and comments match local
  convention or a cited owned reference.
- Each remaining cast, non-null assertion, compiler directive, dynamic access,
  or `any` has a narrow runtime reason.
- Public or reusable touched symbols have useful JSDoc/TSDoc, not placeholder
  comments.
- Validation evidence covers both mechanical preflight risks and project-level
  correctness when tooling exists.

## Hard Stops

- Do not use `@ts-ignore`, `@ts-expect-error`, or `@ts-nocheck` as a shortcut
  around a fixable type design problem.
- Do not introduce default exports, mutable exports, namespaces, `require()`,
  or `var` in owned TypeScript.
- Do not bypass TypeScript visibility through bracket access.
- Do not make generated code prettier by hand unless the checked-in source is
  explicitly maintained manually.
- Do not add style-only churn outside the files needed for the requested
  behavior or review finding.

## Phase Output

Return the edited style decisions, references applied, unsafe constructs
removed or justified, documentation updates, commands run, and any remaining
tooling or validation gaps.
