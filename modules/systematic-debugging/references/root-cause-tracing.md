# Root Cause Tracing

Use when a failure appears far from the code that introduced the bad value or
state.

## Process

1. Start at the visible symptom.
2. Identify the immediate failing operation.
3. Ask what called it and what value or state was passed.
4. Repeat upward until the original invalid input, state transition, or missing
   invariant is found.
5. Fix at the source and add guards where later layers can still be reached.

## Instrumentation

When static reading is not enough, add temporary diagnostics that record:

- Input value entering the boundary.
- Output value leaving the boundary.
- Current working directory or environment when relevant.
- Stack trace before the dangerous operation.

Remove or convert temporary diagnostics before completion unless permanent
observability is intentionally part of the fix.

## Warning

Do not patch only the function where the error appears if earlier layers can
still pass invalid state into it.
