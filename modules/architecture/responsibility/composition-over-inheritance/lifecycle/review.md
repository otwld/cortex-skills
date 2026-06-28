# Composition Over Inheritance Review

## Overview

Review code changes for unjustified inheritance, hidden base-class coupling, and
composition that improves or harms the design.

## Workflow

1. Inspect diffs for changed classes, base classes, abstract classes, mixins,
   overrides, protected members, DI providers, functions, hooks, components,
   strategies, adapters, and collaborators.
2. Identify inherited behavior used for code reuse rather than polymorphism,
   framework extension, stable template method, or compatibility.
3. Check whether composition makes variation explicit through a named
   collaborator, function, component, hook, adapter, strategy, or configuration.
4. Reject composition that adds shallow wrappers, generic utilities, or unclear
   ownership.
5. Route extraction, public API, framework-specific, SRP, or deepening concerns
   to the appropriate module instead of deciding them here.

## Quality Gates

- Findings name the hierarchy or collaborator, hidden coupling, and practical
  correction.
- Inheritance findings explain why the allowed inheritance cases do not apply.
- Composition findings explain the variation point and why the collaborator
  boundary improves substitution, testing, or locality.
- Review distinguishes principle violations from framework-required hierarchy.

## Hard Stops

- Do not approve inheritance used only to share helpers, constants, or incidental
  state.
- Do not approve subclasses that depend on undocumented protected state,
  override order, or `super` call timing.
- Do not request composition when it creates more indirection without a named
  variation point.

## Phase Output

- Return composition findings ordered by impact, inheritance kept with
  justification, required corrections, overlap handoffs, and validation still
  needed.

