# Composition Boundaries

Use this reference when code is created, edited, moved, split, refactored, or
materially reviewed and behavior reuse, extension, or collaborator wiring is in
play.

## Core Rule

Prefer assembling behavior from explicit collaborators over inheriting behavior
from a base class. Composition should make variation points visible through
dependencies, functions, strategies, adapters, hooks, components, configuration,
or providers. Inheritance is acceptable only when the hierarchy represents a
real subtype relationship, required framework extension point, stable abstract
contract, or template method with clear invariants.

Composition is not automatically better when it only moves code into shallow
wrappers. The design should improve substitution, testability, locality, or
variation control.

## Composition Options

Prefer one of these when it makes the variation explicit:

- Constructor or dependency-injection collaborators for behavior that can vary by
  environment, implementation, lifetime, or test boundary.
- Strategy objects or functions for replaceable algorithms, policies,
  formatting, validation, mapping, retries, filtering, or ordering.
- Adapters for remote APIs, persistence engines, SDKs, transport shape, or
  external lifecycle differences.
- Hooks, composables, or services for reusable stateful behavior in frameworks
  that already use those patterns.
- Component composition, slots, children, render props, or content projection for
  UI variation and layout assembly.
- Pure functions for stateless reusable behavior that has no lifecycle,
  dependency ownership, or override needs.
- Configuration objects for data-only variation where behavior does not need its
  own collaborator.

Choose the smallest collaborator that names the variation point without hiding a
broader ownership decision.

## Inheritance Allowed Cases

Accept inheritance when one of these is true:

- A framework API requires extending a base class or implementing a class-based
  lifecycle.
- Subclasses are true substitutable variants of the base contract, and callers
  can use the base type without knowing the concrete subtype.
- The base class owns a stable template method where subclass hooks are narrow,
  documented, and order-independent enough to maintain safely.
- The hierarchy captures a durable domain taxonomy, not a convenience mechanism
  for sharing utilities.
- Compatibility requires retaining an existing hierarchy, and the task is not
  scoped to replace that contract.

Even when inheritance is valid, keep the base class small, document protected
hooks, avoid hidden mutable state, and test through the public contract.

## Inheritance Warning Signs

Challenge inheritance when:

- The base class mainly shares helper functions, constants, or incidental state.
- Subclasses must know protected fields, lifecycle order, initialization timing,
  or which base methods call which hooks.
- Override methods require calling `super` in a specific order that tests do not
  prove.
- Adding a variation requires editing the base class and many subclasses.
- Tests instantiate subclasses only to reach inherited helpers.
- A dependency, function parameter, strategy, adapter, hook, or component child
  would make the variation point explicit.
- The hierarchy combines unrelated responsibilities that would change for
  different reasons.

## Review Language

A strong composition finding names:

- The hierarchy, base class, subclass, mixin, or override at risk.
- The behavior currently inherited and the variation point it hides.
- The composition option that would make the dependency or behavior explicit.
- Why inheritance is not required by polymorphism, framework contract, stable
  template method, or compatibility.
- The smallest correction that avoids wrapper churn.

Do not request composition as a slogan. If inheritance is justified by a current
framework contract or true subtype relationship, record the justification and
review the stability of the base contract instead.

