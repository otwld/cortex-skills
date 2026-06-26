# Bundle Performance Run

## Overview

Shape implementation so shared imports stay narrow and optional cost stays out
of unaffected runtime paths.

## Workflow

1. Prefer direct imports or feature-specific entry points over root barrels for
   heavy or optional code.
2. Keep optional integrations behind lazy loading, dynamic imports, or separate
   package exports when they are not required by core behavior.
3. Avoid import-time side effects in shared modules; move registration, CSS,
   polyfills, and setup into explicit application boundaries.
4. Preserve existing public import paths unless the task includes a compatibility
   or migration plan.
5. Document any intentional bundle tradeoff in the owning code, package metadata,
   changelog, or review note that future maintainers will see.

## Quality Gates

- Shared entry points do not import optional feature dependencies for consumers
  that do not use the feature.
- Tree-shaking remains possible for unused exports and side-effect-free modules.
- Public API compatibility is preserved or the breaking import change is explicit.
- Measurement gaps are recorded when no bundle analyzer, build output, or size
  check is available.

## Hard Stops

- Do not add heavy runtime dependencies to package roots or shared UI roots
  without naming affected consumers.
- Do not hide side effects in barrels, default imports, or setup modules.
- Do not optimize bundle shape by silently breaking documented import paths.

## Phase Output

- Return entry points changed, dependencies moved or isolated, side effects
  removed or accepted, and measurement evidence or gap.
