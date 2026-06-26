# Angular Conventions Run

## Overview

Implement Angular changes so the public template contract, dependency boundary,
and validation evidence stay explicit.

## Workflow

- Preserve the established standalone or NgModule pattern in the affected
  feature. Add only the component, directive, pipe, and form imports the template
  actually uses.
- Type inputs, outputs, model values, form groups, form controls, emitted event
  payloads, and template-facing members. Required values must be enforced by the
  Angular API or by an explicit runtime state branch.
- Name outputs as camelCase events that describe the domain action, such as
  `stageChange`; do not use `on` as an output-name prefix or collide against
  native DOM events.
- Keep component and directive members that exist only for templates `protected`
  when local tooling permits it. Public members should represent an intentional
  class API.
- Use local dependency-injection style. For new `inject()` usage, keep injected
  dependencies near the top of the class and do not widen provider scope unless
  the lifetime change is intentional.
- Prefer reactive forms for complex or cross-field form behavior. Keep validators
  and value mappers typed and testable outside the template when they carry
  business behavior.
- Move repeated or conditional template logic into named TypeScript members.
  Template expressions should remain readable enough to review without executing
  the component.
- Keep large templates and styles external when the component already has
  external files or when inline metadata would obscure behavior.
- Update JSDoc or TSDoc for touched exported components, directives, pipes,
  services, public inputs, public outputs, and reusable form helpers.

## Quality Gates

- Run the narrowest Angular typecheck, unit test, component test, story, or
  harness that exercises the changed contract.
- When validation is unavailable, name the missing command and provide static
  evidence: typed boundary, template binding path, and consumer call site.

## Hard Stops

- Do not silence template or form errors using `$any`, broad casts, untyped form
  controls, or non-null assertions on externally supplied values.
- Do not change selector, input, output, model, provider scope, or form value
  semantics as a side effect of an internal cleanup.
- Do not subscribe in a component just to copy state that Angular can derive
  through template binding, async interop, or existing local state patterns.

## Phase Output

Return the files changed, public Angular contract choices, validation command or
static evidence, and any intentionally deferred Angular risk.
