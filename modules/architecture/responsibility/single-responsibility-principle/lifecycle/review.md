# Single Responsibility Principle Review

## Overview

Review code changes for responsibility cohesion and actionable mixed-concern
risks.

## Workflow

1. Inspect the diff for touched code units and their named responsibility.
2. Identify mixed UI, validation, business behavior, orchestration, mapping,
   persistence, networking, configuration, or side-effect ownership.
3. Decide whether mixed concerns share one reason to change or represent
   independent change drivers.
4. Check whether splits improved ownership or only created shallow indirection.
5. Route extraction, placement, public API, or deepening concerns to the
   appropriate module instead of deciding them here.

## Quality Gates

- Findings name the unit, mixed responsibilities, independent change drivers,
  and smallest correction.
- Keep-together decisions explain the single use case, actor, or lifecycle that
  keeps the unit cohesive.
- Split findings avoid vague SRP claims and do not rely on size alone.
- Review distinguishes local cohesion defects from reusable abstraction or
  package-ownership decisions.

## Hard Stops

- Do not approve code that mixes independently changing UI, validation,
  persistence, networking, and business policy without a named owner boundary.
- Do not request splitting when no independent reason to change can be named.
- Do not accept generic helper, util, manager, or processor names that hide
  unrelated responsibilities.

## Phase Output

- Return SRP findings ordered by impact, cohesive keep-together evidence,
  split-required corrections, overlap handoffs, and validation still needed.

