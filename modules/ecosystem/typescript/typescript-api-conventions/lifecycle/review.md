# TypeScript API Conventions Review

## Overview

Review exported TypeScript APIs for contract drift, invalid state modeling,
unsafe generics, and missing consumer evidence.

## Workflow

1. Compare the previous and new exported surfaces: names, fields, optionality,
   discriminants, generic parameters, entry points, and declaration output.
2. Trace at least one intended consumer path for each materially changed
   contract, including imports through public entry points when they exist.
3. Check whether the API encodes supported states directly instead of requiring
   callers to remember field combinations or runtime ordering.
4. Inspect generics for constraints, default type parameters, return-only
   assertions, and accidental widening to `any`, `{}`, or `object`.
5. Check type-only boundaries, runtime exports, and generated declarations for
   build-mode compatibility.
6. Confirm JSDoc/TSDoc explains caller-visible invariants, failure modes,
   migration notes, or deprecation paths when names and types are insufficient.
7. Verify that typecheck, API extraction, contract tests, or consumer compile
   examples cover the changed public surface.

## Quality Gates

- Review findings cite the exact exported symbol, file, and consumer impact.
- Compatibility concerns are separated from private implementation style.
- Every accepted assertion or cast at the boundary has a runtime reason and a
  narrower alternative was considered.
- Missing validation is reported as a risk tied to a specific contract.

## Hard Stops

- Do not approve an exported optional-field bag that admits impossible states
  when a discriminated union or split contract would remove the ambiguity.
- Do not approve an unconstrained generic that lets callers claim a result the
  implementation cannot prove.
- Do not approve public exports that are only internal plumbing.
- Do not approve undocumented breaking changes, deprecations, or contract
  removals.

## Phase Output

Return findings ordered by severity, each tied to a changed exported symbol and
consumer consequence, followed by validation evidence reviewed and any residual
contract risk.
