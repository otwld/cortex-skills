# Storybook Angular Conventions Activate

## Overview

Decide whether Angular-specific Storybook conventions apply and capture component
setup, provider, and args evidence before story changes.

## Workflow

1. Match the request or diff to `@storybook/angular` story files, Angular story
   decorators, `moduleMetadata`, `applicationConfig`, provider mocks, args,
   Compodoc setup, or Angular Storybook targets.
2. Inspect installed Storybook and Angular versions, local standalone or NgModule
   style, component inputs and outputs, required directives or pipes, providers,
   forms, and existing Angular stories.
3. Name the component setup mode, required Angular dependencies, provider
   lifetime, args contract, and mocked services.
4. Decide whether each dependency belongs in story args, `moduleMetadata`,
   `applicationConfig`, a provider mock, a fixture, or shared preview setup.
5. Identify the Angular Storybook serve, build, visual, interaction, or static
   story check that can validate the setup.

## Trigger Evidence

Activate for Angular stories that use `@storybook/angular`, Angular component
fixtures, `moduleMetadata`, `applicationConfig`, Angular provider mocks, args
for inputs or outputs, form stories, Compodoc integration, or Angular Storybook
targets.

Do not activate for framework-agnostic Storybook changes that do not touch
Angular setup, providers, inputs, outputs, templates, forms, or Angular build
targets.

## Decisions

- Match the component's local setup style. Standalone dependencies belong in
  imports; NgModule-era dependencies use declarations and imports consistent
  with nearby stories.
- Use `moduleMetadata` for component-level Angular imports, declarations, and
  providers. Use `applicationConfig` for application-wide providers and
  environment providers required at bootstrap.
- Keep args aligned with Angular inputs, outputs, form values, and
  template-facing types.
- Mock Angular services, router state, HTTP data, stores, and time at the story
  boundary with deterministic fixtures.
- Use fixed recruitment job board data when inventing examples: candidates, job
  offers, applications, recruiters, interviews, and fixed dates.

## Quality Gates

- Activation names the Angular component, setup mode, required imports or
  declarations, provider scope, args contract, and validation command.
- The phase distinguishes component dependencies from application-wide providers.
- Missing validation is tied to a specific Angular Storybook target, runtime
  story, visual check, interaction check, or static setup proof.

## Hard Stops

- Standalone or NgModule setup cannot be determined and the story requires
  Angular dependency wiring.
- Required providers, imports, declarations, inputs, outputs, or form controls
  are unknown.
- The story requires live Angular services, current time, random data, or shared
  mutable state to render.

## Phase Output

Return matched Angular Storybook evidence, component setup mode, provider and
args decisions, fixture and mock boundary, and required validation evidence.
