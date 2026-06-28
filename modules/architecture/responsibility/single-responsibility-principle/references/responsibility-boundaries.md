# Responsibility Boundaries

Use this reference when code is created, edited, moved, split, refactored, or
materially reviewed.

## Core Rule

A touched code unit should have one reason to change. A reason to change is a
stable actor, policy, workflow, integration, presentation, data, or lifecycle
driver that would force the unit to change independently from its neighbors.

SRP is about cohesive ownership, not smallness. A long unit can still be
cohesive when every branch serves one responsibility. A short unit can violate
SRP when it couples unrelated reasons to change.

## Responsibility Inventory

Identify the touched unit and the work it owns:

- Presentation: rendering, layout, copy, styling, accessibility, visual state,
  component composition, or user interaction.
- Input rules: parsing, validation, normalization, schema enforcement,
  permission checks, and invariant construction.
- Business behavior: domain policy, workflow decisions, state transitions,
  calculations, scheduling, or eligibility rules.
- Orchestration: sequencing one use case across collaborators, transactions,
  retries, events, logging, and cleanup.
- Integration: networking, persistence, third-party SDKs, storage, query
  building, cache writes, and adapter translation.
- Mapping: DTO conversion, view models, persistence models, API payloads, and
  serialization.
- Configuration: environment options, feature flags, dependency registration,
  bootstrap wiring, and runtime defaults.

Then ask which of those responsibilities would change independently. Multiple
implementation steps are acceptable when they serve one use case and one actor.
Multiple independent change drivers are a split candidate.

## Split Signals

Consider splitting when the same unit:

- Mixes UI rendering with business policy, persistence, networking, or
  validation rules that change outside the UI reason.
- Mixes schema parsing or DTO mapping with domain decisions that should be
  tested without transport shape.
- Mixes persistence queries or SDK calls with policy decisions that should
  survive a storage or provider change.
- Contains condition groups owned by different actors, features, workflows, or
  external systems.
- Forces tests to set up unrelated concerns to verify one behavior.
- Requires edits for unrelated bug classes such as layout fixes, authorization
  rules, cache invalidation, and database shape changes.
- Uses names such as manager, helper, util, service, handler, or processor to
  hide unrelated responsibilities.

Split only when the new units get clearer responsibilities, names, tests, and
call boundaries.

## Keep-Together Signals

Keep code together when:

- The steps are phases of one use case, such as validate input, load data,
  apply one policy, persist, and report one result.
- Separating the code would create pass-through wrappers, shallow helpers, or
  files named only after implementation mechanics.
- The concerns share one lifecycle and one reason to change.
- The current unit is small, private, and easier to read than the proposed
  split.
- The split would force callers to coordinate internals that one owner should
  control.

Prefer local extraction only when it gives a meaningful name to a coherent
sub-responsibility. Prefer a routed extraction or placement decision when the
split creates a reusable abstraction or changes package ownership.

## Review Language

A strong SRP finding names:

- The touched unit.
- The responsibilities currently mixed.
- The independent reasons they would change.
- The smallest split or boundary correction that removes the mixed reason.
- Why the recommendation is not merely file-count churn.

Do not cite SRP as a vague preference. If independent change drivers cannot be
named, record the unit as cohesive or defer the split.

