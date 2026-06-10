---
name: typescript-code-style
description: Use when writing, editing, generating, refactoring, or reviewing TypeScript or TSX source files, tests, build scripts, imports, exports, classes, functions, or interfaces.
---

# Output Marker

Display:
using skill: typescript-code-style

---

# TypeScript Code Style

## Overview

Apply a Google TypeScript Style Guide based workflow for TypeScript source.
Preserve local tooling and surrounding style first, then use this skill to keep
new code readable, maintainable, and easy to refactor.

## Operating Order

1. Read the nearest project instructions, `tsconfig`, formatter, ESLint, test setup, and surrounding files.
2. Follow project-enforced rules when they are stricter or intentionally different.
3. Apply `code-documentation` before and during any TypeScript code edit.
4. Apply the core defaults to new or materially rewritten TypeScript.
5. Load only the reference file that matches the current question or code area.
6. Run the project's normal formatter, typecheck, and tests when feasible.

## Core Defaults

- Use UTF-8, ordinary spaces, semicolons, `const` by default, `let` only for reassignment, and never `var`.
- Use ES module syntax with named exports in owned code.
- Use `import type` and `export type` for type-only symbols.
- Keep exported APIs small and stable.
- Prefer readable type expressions, `unknown` over `any`, and interfaces for object shapes.
- Use function declarations for named functions and arrows for callbacks.
- Throw and reject only `Error` instances.
- Use JSDoc/TSDoc for every touched exported symbol, reusable API, and owning
  surface for touched private code paths.
- Use `//` comments only for implementation notes that JSDoc/TSDoc cannot
  express cleanly.

## Reference Map

| Need | Read |
| --- | --- |
| Source files, imports, exports, modules | [references/source-modules.md](references/source-modules.md) |
| Variables, objects, classes, functions, control flow, errors | [references/language-features.md](references/language-features.md) |
| Naming, inference, nullability, interfaces, arrays, generics | [references/types-naming.md](references/types-naming.md) |
| Compiler expectations, JSDoc, comments, generated code | [references/comments-tooling-policy.md](references/comments-tooling-policy.md) |

## Mechanical Preflight

Run the optional preflight from this skill directory:

```bash
python3 scripts/ts_style_preflight.py path/to/file.ts path/to/dir
```

The script catches high-signal mechanical issues. It does not replace
TypeScript, ESLint, Prettier, or human review.

## Usage Checklist

- Local project rules were checked first.
- New TypeScript uses named exports and type-only imports where appropriate.
- Touched code has relevant JSDoc/TSDoc at the symbol or owning-surface level.
- Mechanical preflight was run for broad TypeScript edits when feasible.

## Cross-References

- WITH: code-documentation
