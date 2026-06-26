# Storybook Conventions Review

## Overview

Find regressions in story coverage, determinism, mocks, docs scope, and
Storybook runtime behavior.

## Workflow

- Compare changed stories with the component's public props, events, slots,
  children, states, setup requirements, and existing story organization.
- Verify each story demonstrates a meaningful state, edge case, interaction, or
  setup constraint. Default-only stories should not be counted as behavior
  coverage.
- Check fixtures for stable IDs, fixed dates, deterministic ordering, minimal
  data, and recruitment job board coherence when examples are invented.
- Review mocks, decorators, loaders, and preview annotations to ensure they model
  external dependencies without hiding invalid component contracts.
- Inspect MDX docs for direct connection to stories, setup constraints, or docs
  blocks. Product documentation that does not depend on Storybook belongs
  elsewhere.
- Check play functions for deterministic user interactions, cleanup, and
  validation evidence in the Storybook runtime.

## Quality Gates

- Findings name the story, component state, fixture, mock boundary, docs block,
  or runtime annotation that can regress.
- Review distinguishes missing state coverage from broken runtime setup or
  nondeterministic validation.
- Missing validation is actionable: name the Storybook build, runtime path,
  interaction test, accessibility check, visual check, or static proof needed.

## Finding Triggers

- A story is effectively the component's default props under a new name.
- Fixtures use random values, current dates, live APIs, or mutable shared state.
- A mock or decorator supplies dependencies that the real component contract does
  not allow.
- MDX docs describe product behavior without tying it to a rendered story or
  setup constraint.
- A play function is flaky because it depends on timing, external services, or
  shared state.

## Hard Stops

- Do not approve Storybook coverage that cannot render deterministically outside
  the application.
- Do not accept mocks that mask invalid required props, missing providers, or
  broken component setup.
- Do not ignore missing Storybook runtime validation when preview, addon,
  decorator, loader, or play behavior changed.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
specific story state, fixture, mock, docs scope, runtime behavior, or validation
evidence needed to close it.
