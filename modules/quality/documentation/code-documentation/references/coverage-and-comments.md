# Documentation Coverage And Comments

Use this reference when code is created, edited, moved, deleted, split,
refactored, or materially reviewed.

## Coverage Pass

Before changing code or issuing review conclusions, identify the touched
documentation surfaces:

- Exported symbols, public entry points, barrels, package APIs, SDK contracts,
  and reusable helpers.
- Public class members, component inputs and outputs, slots, emitted events,
  routes, controllers, commands, configuration options, hooks, services, and
  providers.
- DTOs, schemas, request and response payloads, validation rules, error types,
  state machines, generated docs, README usage, Storybook stories, MDX docs,
  fixtures, and examples.
- User-visible behavior, side effects, lifecycle rules, permissions, caching,
  ordering guarantees, retries, fallback behavior, and failure modes.

Treat a surface as public when a consumer can reach it through an import,
framework binding, template, route, command, configuration file, event, generated
documentation, or user-facing workflow, even if the source symbol is not
exported directly.

## Public Coverage Rules

Public, exported, reusable, and user-facing surfaces need documentation that
answers the consumer's questions:

- What responsibility does this surface own?
- When should a caller or user use it?
- Which states, invariants, constraints, units, ordering rules, lifecycle
  requirements, or permissions matter?
- What does it return, emit, persist, mutate, schedule, render, or reject?
- Which failure modes, edge cases, or side effects must the consumer handle?
- Which example, story, fixture, or usage note proves the contract when the
  behavior is not obvious from the signature?

For changed behavior, update the nearest owning documentation surface in the
same change. If a public or reusable touched surface remains undocumented,
record the reason as an explicit gap; do not silently pass the documentation
gate.

## Dense Function Comments

Use ordinary `//` comments for implementation reasoning inside dense functions.
Comments belong before a logical block when they would save a future maintainer
from re-deriving intent from control flow.

Add block-level line comments when a function contains any of these:

- Multiple phases such as validation, normalization, grouping, fetching,
  mutation, rendering, cleanup, or reporting.
- Nested loops, nested conditionals, early exits, or ordering-sensitive branches.
- Non-obvious invariants, framework constraints, lifecycle timing, concurrency,
  caching, debounce, retry, transaction, pagination, or performance choices.
- Error recovery or intentionally ignored failures.
- A long body whose structure is no longer obvious at a glance.

The comment should name the phase, invariant, or reason. It should not narrate
syntax. Prefer extraction when a block has a stable name, independent contract,
or useful test surface. Prefer a short line comment when extraction would hide
local context or create a shallow helper.

## Review And Validation

When reviewing or finishing work, missing or stale documentation on a touched
public surface is a finding, not an optional polish item. Dense logic with no
phase comments is also a finding when the intent cannot be read quickly.

Validation should name the documentation surfaces checked, the docs or comments
updated, and any remaining gap with its owner or blocker.
