# Storybook Angular Conventions Run

## Overview

Implement Angular Storybook stories so component setup, provider scope, typed
args, and fixtures match Angular runtime expectations.

## Workflow

- Type stories with the local `@storybook/angular` `Meta` and `StoryObj` pattern.
  Use `satisfies` when nearby Angular stories already use it.
- Match the component's Angular setup. For standalone components, include the
  component, directives, pipes, and modules through imports. For NgModule-based
  components, use declarations and imports consistent with local stories.
- Use `moduleMetadata` for dependencies scoped to the story's component tree:
  declarations, imports, and provider mocks needed by that component state.
- Use `applicationConfig` only for bootstrap-level providers or environment
  providers such as animations, router setup, HTTP providers, or module
  providers that represent application configuration.
- Keep args typed to component inputs, outputs, and form-facing values. Use local
  Storybook action or test-function conventions for output handlers.
- Mock Angular services with provider values or factories that return
  deterministic data. Do not call live HTTP, router navigation, storage, or clock
  APIs from stories.
- Cover Angular-specific states: required input missing branch, disabled form
  control, validation error, async loading, provider error, projected content,
  and long translated or formatted text when those states exist.
- Keep Compodoc and autodocs setup aligned with existing Angular Storybook config
  instead of adding per-story documentation workarounds.
- Update story-adjacent docs only when they explain Angular setup constraints
  that are not obvious from the decorators.

## Quality Gates

- Run the narrowest Angular Storybook serve, build-storybook, interaction,
  accessibility, visual, or static setup check that exercises the changed story.
- When validation cannot run, provide static evidence: component setup mode,
  imports or declarations, provider scope, typed args, fixture data, and the
  Angular Storybook target that would close the gap.

## Hard Stops

- Do not use `moduleMetadata` or `applicationConfig` to hide missing required
  inputs, invalid provider contracts, or incorrect component setup.
- Do not mix standalone and NgModule setup styles in one story without matching
  the component and nearby local stories.
- Do not use live services, random data, wall-clock time, shared mutable state,
  or real navigation to make a story render.
- Do not widen providers into preview or application config when a story-local
  provider is sufficient.

## Phase Output

Return changed Angular Storybook files, setup mode, provider and args choices,
fixture and mock decisions, validation command or static proof, and any
remaining Angular setup risk.
