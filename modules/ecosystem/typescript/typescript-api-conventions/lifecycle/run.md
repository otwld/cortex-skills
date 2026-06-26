# TypeScript API Conventions Run

## Overview

Design the exported TypeScript surface so callers can see supported states,
invalid combinations are hard to express, and runtime values match the declared
contract.

## Workflow

1. Map each changed export to its consumers, entry point, declaration output,
   and documentation or compile-time examples.
2. Encode exclusive states as discriminated unions instead of optional-field
   state bags. Keep absence at the usage site through optional properties,
   `null`, or `undefined` according to the surrounding API convention.
3. Use interfaces for named object contracts and type aliases for unions,
   primitives, tuples, function signatures, and repeated type expressions.
4. Constrain generics where the implementation depends on required properties,
   keys, or relationships. Avoid generic parameters that appear only in return
   positions.
5. Keep type-only imports and exports explicit through `import type` and
   `export type` where the symbol has no runtime use.
6. Keep private helper types private. If a helper must become public, document
   the caller use case and choose a name that describes the public concept.
7. Document exported symbols and non-obvious invariants in JSDoc/TSDoc in the
   same change that edits the contract.
8. Run the narrowest validation that proves the contract and any affected
   consumers.

## Quality Gates

- Each exported object shape, union, generic, DTO, and public function signature
  has a clear consumer use case.
- Required, optional, nullable, readonly, and mutable fields match the runtime
  behavior.
- Generic constraints prevent unsupported property access, key usage, and
  caller-chosen return shapes.
- Public entry points expose intentional names and do not leak private helper
  implementation types.
- Documentation and tests cover changed invariants, migration requirements, or
  compile-time usage examples.

## Hard Stops

- Do not use `any`, broad casts, or non-null assertions to make an exported API
  compile.
- Do not publish a bag of optional fields when only specific combinations are
  valid.
- Do not export a helper only to avoid fixing an internal import path.
- Do not collapse value exports and type-only exports when build mode or
  `isolatedModules` can observe the difference.
- Do not change a public contract without either compatibility evidence or a
  stated migration requirement.

## Phase Output

Return the designed API shape, rejected alternatives where they affect
compatibility, changed exported symbols, required documentation updates, and
validation evidence or unresolved validation gaps.
