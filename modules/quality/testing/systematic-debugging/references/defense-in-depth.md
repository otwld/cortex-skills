# Defense In Depth Validation

Use after finding a bug caused by invalid or unsafe data flowing through several
layers.

## Validation Layers

- Entry point: reject invalid caller input early.
- Domain or business logic: preserve operation-specific invariants.
- Integration boundary: validate data before persistence, transport, file, or
  process operations.
- Environment guard: prevent dangerous behavior in test or automation contexts.
- Diagnostic context: log enough information to investigate future violations.

## Rules

- Add checks where the invariant is owned, not only where it crashed.
- Test at least one lower layer when upper layers can be bypassed by mocks,
  alternate entry points, or future refactors.
- Keep errors specific enough to guide the next investigation.

## Warning

One validation point may be enough for correctness but not enough for safety when
multiple call paths reach the dangerous operation.
