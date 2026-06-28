# Composition Over Inheritance Plan

## Overview

Plan code changes so behavior reuse is assembled through explicit composition
unless inheritance has a current, concrete justification.

## Workflow

1. For each touched reuse point, decide one outcome: keep inheritance, replace
   with composition, introduce a collaborator, keep local, or hand off to an
   extraction, public API, framework, SRP, or deepening module.
2. When keeping inheritance, name the allowed case: framework extension, true
   subtype polymorphism, stable abstract contract, template method, or
   compatibility.
3. When replacing inheritance, name the composition mechanism: injected
   collaborator, strategy, adapter, reusable function, hook, composable,
   component composition, or configuration object.
4. Plan caller updates, tests, docs, and examples affected by the reuse boundary.
5. Keep validation focused on substitution, variation behavior, lifecycle, and
   dependency wiring.

## Quality Gates

- The plan names the behavior currently inherited or composed.
- Inheritance has a concrete justification or a planned replacement.
- Composition choices expose a real variation point and avoid pass-through
  wrappers.
- Validation can prove the changed behavior without depending on protected
  internals.

## Hard Stops

- Do not plan composition as a mechanical rewrite when inheritance is required by
  a framework or true subtype contract.
- Do not introduce strategy, adapter, or provider surfaces without a named
  variation point.
- Do not leave subclass order, protected state, or `super` call requirements
  implicit when inheritance remains.

## Phase Output

- Return keep/replace/defer decisions, inheritance justifications, composition
  mechanisms, affected callers, tests, docs, overlap handoffs, and validation
  evidence required.

