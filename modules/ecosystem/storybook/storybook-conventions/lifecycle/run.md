# Storybook Conventions Run

## Overview

Implement stories and docs so component behavior is reviewable, deterministic,
and validated in Storybook's runtime.

## Workflow

- Follow the local CSF version and story typing pattern. In TypeScript projects,
  prefer typed `Meta` and `StoryObj` with `satisfies` when local tooling already
  supports that style.
- Put stories near the component or in the existing feature story location. Keep
  titles and story names aligned with local hierarchy.
- Cover meaningful states: default, loading, empty, error, disabled, permission
  variation, long content, boundary values, and interaction states when those
  states exist for the component.
- Keep fixtures minimal, named, and deterministic. Use fixed dates and stable
  recruitment job board entities when inventing sample data.
- Mock data, modules, network calls, and providers at the smallest story boundary
  that still represents how consumers use the component.
- Keep args focused on the public component contract. Use argTypes and controls
  only when they make state exploration clearer.
- Use play functions for user-observable interactions and assertions, not for
  hidden setup that could live in fixtures, loaders, or decorators.
- Use MDX to explain setup constraints, compose existing stories, or document
  component states. Do not move unrelated product documentation into Storybook.
- Update story-adjacent docs or comments only when they clarify non-obvious setup
  constraints; avoid comments that restate story names.

## Quality Gates

- Run the narrowest Storybook build, dev runtime check, test-runner command,
  interaction test, accessibility check, visual check, or static story review
  that exercises the changed story behavior.
- When validation cannot run, provide static evidence: typed args, deterministic
  fixture path, mock boundary, covered states, and the Storybook command that
  would close the gap.

## Hard Stops

- Do not add a story that only renders the component's default props while
  claiming behavior coverage.
- Do not rely on live APIs, random values, current time, mutable shared fixtures,
  or environment-specific state.
- Do not use decorators or mocks to hide missing component dependencies or an
  invalid public contract.
- Do not make preview or addon changes without validating at least one affected
  story path.

## Phase Output

Return changed Storybook files, represented states, fixture and mock decisions,
docs scope, validation command or static proof, and any remaining review risk.
