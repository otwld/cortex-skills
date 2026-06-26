# Angular Conventions Review

## Overview

Find Angular regressions in public contracts, template typing, provider lifetime,
and consumer-visible behavior.

## Workflow

- Compare selector, input, output, model value, and form value shape changes
  against every touched template and exported consumer.
- Verify required inputs are enforced, optional inputs include `undefined` in the
  type or have defaults, and transform functions are pure.
- Check output names for camelCase domain events, native event collisions, and
  unnecessary aliases.
- Confirm template-facing members are typed and do not rely on `$any`, broad
  casts, untyped forms, or non-null assertions over externally supplied data.
- Confirm standalone imports, NgModule declarations, and providers match local
  structure and do not introduce unused Angular dependencies.
- Check that template logic remained reviewable and that complex computations,
  validation rules, and data transforms moved to named TypeScript code.
- Verify exported Angular symbols and public component behavior have current
  JSDoc, TSDoc, tests, stories, or consumer docs when the behavior is relied on
  outside the file.

## Quality Gates

- Every finding names the public Angular contract or template path that can
  regress.
- Type-safety findings distinguish compile-time template/form erosion from
  runtime behavior changes.
- Missing validation is reported only when a specific test, story, harness, or
  static proof would close the risk.

## Finding Triggers

- A component compiles only because template type checking was bypassed.
- A provider scope changes the lifetime of stateful services without a stated
  reason.
- A public input, output, selector, or form contract changes without validation
  evidence.
- A template now performs business branching or data shaping that cannot be
  isolated in a unit test.

## Hard Stops

- Do not approve public selector, input, output, model, provider, or form
  contract changes without consumer-facing evidence.
- Do not accept template type bypasses as a substitute for typed Angular
  boundaries.
- Do not treat missing Angular validation as low risk when behavior changed.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
specific Angular contract or validation evidence needed to close it.
