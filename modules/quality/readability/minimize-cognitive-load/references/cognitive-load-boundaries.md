# Cognitive Load Boundaries

Use this reference when code is created, edited, moved, split, refactored, or
materially reviewed.

## Core Rule

When multiple implementations satisfy the requirements, choose the one that is
easiest for the next maintainer to understand, modify, debug, and review.

Readable code is not always the shortest code. It is code where intent, inputs,
outputs, dependencies, state changes, side effects, and failure paths are
obvious from the local context.

## Reader Burden Inventory

Before changing code, identify what a future reader must hold in their head:

- Intent: what the code does, why it exists, and what problem it solves.
- Inputs and outputs: accepted values, returned values, thrown errors, emitted
  events, rendered output, or persisted changes.
- Data flow: how values move from input to transform to output.
- Control flow: branch order, early exits, async sequencing, retries,
  cancellation, and error handling.
- Dependencies: imports, injected collaborators, global state, configuration,
  framework lifecycle, generated inputs, and external services.
- Side effects: mutation, persistence, network calls, cache updates, DOM work,
  logging, scheduling, and event publication.
- Scope: which files, functions, exports, options, and public APIs must be
  understood together.

Reduce the number of unrelated facts a reader must remember at one time.

## Prefer Obvious Structure

Prefer implementation shapes that make the reader path direct:

- Use guard clauses and early returns to remove nesting.
- Use explicit branch names and intermediate values when they clarify intent.
- Keep related code together when one feature is easier to understand locally.
- Use local helper functions for meaningful substeps, not for every line group.
- Keep `try` blocks focused on operations that may throw when practical.
- Prefer direct imports, parameters, constructors, or providers over hidden
  dependency lookup.
- Keep one behavioral change reviewable without unrelated moves, renames,
  formatting churn, or cleanup.

Avoid cleverness that makes a reader simulate the runtime to understand the
code: dense expressions, hidden callbacks, implicit registries, magic
decorators, surprising mutation, overly generic utilities, and unnecessary
framework indirection.

## Abstraction Threshold

An abstraction should reduce cognitive load for current code, not promise
future elegance.

Before adding a helper, utility, service, interface, factory, base class,
configuration option, extension point, or public export, ask:

- Does this solve today's problem?
- Does it remove repeated current behavior, not hypothetical reuse?
- Does it make the caller and implementation easier to understand together?
- Does it have a clear owner and name?
- Is it simpler than keeping the logic local?

Prefer a small amount of local duplication over a shared abstraction when the
duplication is easy to read and the abstraction would force readers to jump
between unrelated concepts. Revisit extraction once a repeated pattern has a
stable owner, stable consumers, and a clear variation point.

## Data And Control Flow

A reader should be able to trace behavior without crossing unnecessary layers:

- Start with input validation or normalization at the boundary.
- Transform values in named, visible steps.
- Call collaborators where their effect is expected.
- Return, render, persist, emit, or throw through explicit paths.

Avoid paths like input to helper to service to utility to manager to factory to
output when a direct local function or owner-backed collaborator is clearer.

Nested and indirect control flow is acceptable when it models required behavior,
but isolate it and make the ordering, invariants, and side effects explicit.

## Public Surface Area

Every exported symbol, public method, interface, configuration option,
extension point, and callback increases maintenance cost.

Expose only what current consumers need. Keep implementation details private.
Prefer narrow, owner-backed public surfaces over convenience exports. Remove
new public surface introduced by the change if no current caller needs it.

When public API design, package boundaries, or compatibility semantics become
the main issue, defer to the public API module.

## Justified Complexity

Complexity can be correct when it is required by:

- Correctness or data integrity.
- Security, accessibility, concurrency, or error recovery.
- External API, wire protocol, browser, runtime, or framework contracts.
- Backward compatibility explicitly required by an external consumer.
- Measured performance constraints.

Keep justified complexity local, named, tested when possible, and documented at
the point where the reader needs the invariant or ordering rule. Do not spread
required complexity through generic helpers or hidden configuration.

## Review Language

A strong cognitive-load finding names:

- The touched code a reader must understand.
- The specific burden: extra jumps, hidden data flow, dense branching, public
  surface creep, speculative abstraction, unclear side effect, or noisy diff.
- Why the burden is unnecessary for the current behavior.
- The smallest correction that makes the code easier to read.

Avoid vague feedback such as "make this cleaner." Prefer precise language:

- "This helper forces readers to leave the component to understand one local
  branch. Keep the branch local until another current caller needs it."
- "This public option is not used by any current consumer. Removing it keeps the
  API smaller and makes the change easier to review."
- "The nested success and error branches can be guard clauses, which makes the
  main path visible without changing behavior."

## Neighboring Module Boundaries

This module owns overall reader effort and simplification pressure. It does not
replace neighboring modules:

- Naming consistency owns project vocabulary and rename decisions.
- TypeScript code style owns language-specific import, typing, and source-style
  conventions.
- Code documentation owns documentation coverage and comment quality.
- SRP owns independent reasons to change and responsibility splits.
- Extraction owns whether repeated behavior deserves a reusable abstraction.
- Public API design owns exported contracts and compatibility semantics.
- Composition over inheritance owns collaborator and hierarchy structure.
- Single Source of Truth owns duplicated facts and authoritative owners.
- Performance modules own measured performance and bundle tradeoffs.

Use this module to ask whether the code is easier to read and review. Use the
neighboring module when the correction changes that module's owned boundary.
