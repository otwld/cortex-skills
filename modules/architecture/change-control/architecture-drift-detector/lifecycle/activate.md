# Architecture Drift Detector Activate

## Overview

Activate when recent work, a proposed refactor, or a review request suggests
architecture risk from churn, ownership spread, dependency erosion, or repeated
fixes across project areas.

## Workflow

1. Read `shared/architecture-deepening.md` when evaluating module depth,
   interface leverage, or dependency classification.
2. Inspect the current diff, changed file set, commit range, or user-provided
   change summary.
3. Look for repeated edits to the same behavior across owners or layers.
4. Look for new dependencies that point opposite the existing architecture
   direction.
5. Localize responsibility movement across modules, packages, apps,
   integrations, or UI.

## Quality Gates

- At least one concrete drift indicator is tied to a named area.
- Broad file count, personal preference, or unfamiliar code is not treated as
  sufficient evidence.
- The output stays diagnostic unless the task also asks for implementation.

## Hard Stops

- Do not escalate drift without naming the owner, module, package, workflow, or
  dependency edge at risk.
- Do not propose new architecture layers before inspecting existing owners.
- Do not turn drift detection into an unbounded rewrite plan.

## Phase Output

- State the drift evidence, affected area, risk type, confidence level, resource
  usage, and missing inspection needed.
