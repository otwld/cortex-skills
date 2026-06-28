# Documentation Coverage And Comments

Use this reference when code is created, edited, moved, deleted, split,
refactored, or materially reviewed.

## Coverage Pass

Before changing code or issuing review conclusions, identify the touched
documentation surfaces:

- Public and reusable entry points: exported symbols, barrels, package APIs,
  SDK contracts, framework-bound classes, route handlers, controllers, commands,
  hooks, services, providers, and helpers reused outside a single local block.
- Structural types: interfaces, type aliases, object shapes, class members,
  fields, properties, enums, discriminants, DTOs, schemas, validation rules,
  config options, request payloads, response payloads, error types, events, and
  state-machine states.
- Component contracts: props, inputs, outputs, slots, emitted events, exposed
  methods, templates, stories, examples, and user-visible states.
- Behavior and workflow: user-visible behavior, side effects, lifecycle rules,
  permissions, units, ordering guarantees, caching, concurrency, retries,
  pagination, fallback behavior, persistence, mutation, cleanup, and failure
  modes.
- Documentation artifacts: generated-doc inputs, README usage, MDX docs,
  Storybook stories, fixtures, payload samples, code examples, migration notes,
  and screenshots or snapshots that describe behavior.

Treat a surface as public when a consumer can reach it through an import,
framework binding, template, route, command, configuration file, event, generated
documentation, or user-facing workflow, even if the source symbol is not
exported directly.

## Required Documentation

Document touched code at the nearest durable owner. Use JSDoc/TSDoc in
TypeScript and JavaScript, language-native docstrings in other languages, and
project-native docs for examples, stories, generated documentation, and public
usage notes.

Required coverage for touched code:

- Public, exported, reusable, framework-bound, or user-facing surfaces need
  documentation.
- Interfaces, interface properties, type members, schema fields, DTO fields,
  config fields, public class fields, public methods, enum values, events, and
  payload fields need member-level documentation.
- Named functions and methods with more than five body lines need documentation,
  even when private. If the language cannot attach documentation directly, add
  the documentation to the nearest owning surface.
- Shorter functions still need documentation when they are public, reusable,
  encode business behavior, perform side effects, hide constraints, or can fail
  in ways callers must handle.
- Inline callbacks, local closures, and small render helpers need documentation
  when they contain non-obvious branching, async sequencing, mutation,
  filtering, mapping, cleanup, or error handling.
- Moved, split, renamed, or deleted code must carry its documentation forward or
  remove stale documentation from reachable docs, examples, stories, fixtures,
  and generated outputs.

Good documentation answers the reader's actual questions:

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

## Flow Comments

Use ordinary line or block comments for implementation reasoning inside long or
dense functions. Comments belong before a logical block when they would save a
future maintainer from re-deriving intent from control flow.

Add flow comments when a function contains any of these:

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

## Avoid Documentation Noise

Do not add placeholder comments, line-by-line narration, or docs that merely
repeat a symbol name. If the code is required to be documented but the first
draft would restate syntax, improve the symbol names or extract a named helper
before documenting the resulting responsibility.

Documentation is optional only when the touched code is private, at most five
body lines, self-evident, has no independent contract, and is already covered by
a nearby owning surface. Record that reason when review or verification
evaluates the gap.

## Review And Validation

When reviewing or finishing work, missing or stale required documentation on a
touched surface is a required fix, not optional polish. Dense or long logic with
no flow comments is also a required fix when the reader must infer phases,
ordering, side effects, or failure handling from control flow.

Validation should name the documentation surfaces checked, the docs or comments
updated, and any remaining gap with its owner or blocker.
