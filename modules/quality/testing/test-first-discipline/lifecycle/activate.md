# Test First Discipline Activate

## Overview

Identify behavior-changing work where a test can define the expected outcome
prior to implementation.

## Workflow

1. Match this module when the request or diff changes behavior, fixes a bug,
   refactors behavior, changes validation paths, adds e2e coverage, or modifies
   test harness setup.
2. Name the behavior, public seam, and regression risk that a test should prove.
3. Choose the highest meaningful seam available: public API, UI workflow,
   command, service interface, integration boundary, or e2e path.
4. Identify legitimate exceptions such as documentation-only edits, mechanical
   renames, generated snapshots, or urgent diagnostics where a red test is not
   currently feasible.

## Quality Gates

- Activation evidence names the behavior or regression, not only the files being
  edited.
- The proposed test seam observes externally meaningful behavior.
- Exceptions are explicit and include the residual risk.

## Hard Stops

- Do not activate for formatting-only or docs-only changes unless behavior
  examples are being tested.
- Do not accept private implementation structure as the primary test seam when a
  public seam can prove the behavior.
- Do not skip test-first reasoning for a behavior change without recording why.

## Phase Output

- Return the behavior, chosen public seam, expected failing proof or exception,
  and regression risk.
