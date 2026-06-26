# Storybook Conventions Activate

## Overview

Decide whether Storybook conventions apply and capture the story, docs, fixture,
mock, and runtime evidence needed before changing component examples.

## Workflow

1. Match the request or diff to CSF stories, MDX docs, preview annotations,
   addons, decorators, loaders, play functions, mocks, fixtures, story
   organization, or Storybook validation outputs.
2. Inspect installed Storybook framework, builder, addon versions, existing story
   patterns, preview configuration, and commands.
3. Name the component or story surface affected, the public props or args shown,
   the states covered, and the external dependencies mocked.
4. Decide whether the change belongs in a story file, shared fixture, MDX doc,
   preview annotation, addon config, or validation artifact.
5. Identify the Storybook build, runtime observation, interaction test, visual
   check, accessibility check, or static story review that can validate it.

## Trigger Evidence

Activate for changes to story files, MDX docs, `.storybook` configuration,
addons, global decorators, loaders, parameters, play functions, args, argTypes,
fixtures, network mocks, module mocks, provider mocks, visual snapshots, or
Storybook test outputs.

Do not activate for product documentation or component code changes that do not
change Storybook examples, docs, configuration, mocks, or validation evidence.

## Decisions

- Use CSF stories to demonstrate component states. Use MDX when setup context,
  composition, or docs blocks need structure around those stories.
- Keep args and argTypes typed and serializable enough for controls and docs to
  represent the component contract.
- Mock external dependencies at the story boundary. Prefer project-level mock
  registration only when multiple stories need the same module or network mock.
- Use deterministic recruitment job board data when inventing examples:
  candidates, job offers, applications, recruiters, interviews, and fixed dates.
- Treat decorators, loaders, play functions, and preview annotations as runtime
  behavior that needs Storybook validation, not just TypeScript validation.

## Quality Gates

- Activation names the story files, component state coverage, fixture source,
  mock boundary, and Storybook command or observation needed.
- The phase distinguishes story behavior from product documentation and
  application runtime behavior.
- Missing validation is tied to a specific Storybook runtime, build, interaction,
  accessibility, visual, or static review path.

## Hard Stops

- The requested story only mirrors default props and no meaningful state,
  interaction, edge case, or setup constraint is identified.
- The story needs live services, random data, wall-clock time, or environment
  state to render.
- A preview, addon, decorator, loader, or play-function change lacks a way to
  observe Storybook runtime behavior.

## Phase Output

Return matched Storybook evidence, affected component or docs surface, state and
fixture decisions, mock boundary, and validation evidence required for run or
review.
