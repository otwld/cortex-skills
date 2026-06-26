# Storybook Angular Conventions Review

## Overview

Find regressions in Angular Storybook setup, provider scope, typed args, fixtures,
and Angular-specific state coverage.

## Workflow

- Compare story setup with the Angular component's standalone or NgModule mode,
  required imports, declarations, providers, directives, pipes, forms, inputs,
  outputs, and projected content.
- Verify `moduleMetadata` contains only component-tree dependencies and that
  `applicationConfig` is reserved for bootstrap-level providers.
- Check args against Angular input types, output handlers, form values, and
  template-facing members.
- Review provider mocks for deterministic behavior, correct token identity, and
  state isolation between stories.
- Check fixtures for stable recruitment job board data, fixed dates, and no live
  HTTP, router, storage, clock, or shared mutable state.
- Inspect Compodoc, autodocs, and Angular Storybook target changes for project
  consistency and build impact.

## Quality Gates

- Findings name the story, component setup mode, import, declaration, provider,
  input, output, form value, fixture, or Angular Storybook target that can
  regress.
- Review distinguishes Angular setup failures from generic story coverage gaps.
- Missing validation is actionable: name the Angular Storybook serve/build
  target, visual path, interaction check, accessibility check, or static setup
  proof needed.

## Finding Triggers

- A story compiles only because decorators provide dependencies that the
  component contract does not actually require or allow.
- `applicationConfig` is used for providers that should be story-local.
- Args omit required inputs, mistype outputs, or bypass form/template typing.
- Provider mocks share mutable state across stories or call live services.
- Standalone and NgModule setup patterns are mixed without local evidence.

## Hard Stops

- Do not approve Angular stories that cannot render without live services,
  current time, random data, or mutable shared fixtures.
- Do not accept provider setup that hides missing imports, declarations, required
  inputs, or invalid component contracts.
- Do not ignore missing Angular Storybook validation when decorators, providers,
  Compodoc, or build targets changed.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
specific Angular setup, provider, args, fixture, target, or validation evidence
needed to close it.
