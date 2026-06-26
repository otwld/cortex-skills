
# Output Marker

Display:
using module: rxjs-conventions

---

# RxJS Conventions

## Overview

Make time, ownership, cancellation, and errors clear in observable code.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Prefer composition over nested subscriptions; choose flattening operators by concurrency semantics; justify subjects and multicasting.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Observable composition uses operators that match concurrency, cancellation, ordering, and error semantics.
- Subjects, multicasting, and subscriptions are justified by ownership and cleanup requirements.
- Angular or service boundaries expose streams without leaking internal mutation paths.

## Example

Candidate typeahead uses switchMap because newer search text cancels older requests.

## Hard Stops

- Do not nest subscriptions when composition can express the data flow.
- Do not add Subjects as event buses without a clear owner and lifecycle.
- Do not ignore teardown, cancellation, or error propagation in long-lived streams.

## Usage Checklist

- Observable sources, operators, subscriptions, and lifecycle were inspected.
- Concurrency, cancellation, multicasting, and cleanup semantics are intentional.
- Stream behavior is covered by tests or a named validation gap.

## Cross References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
