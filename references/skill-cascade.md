# Skill Cascade

Use this reference from `using-cortex` when a request touches multiple domains
or when skill selection is not obvious from one named skill.

The cascade is evidence-driven. User examples, file paths, framework names, and
workflow verbs are signals to classify; they are not durable routes to copy into
the router.

## Cascade Algorithm

1. Collect direct signals from the user request, current diff, changed files,
   project configuration, and intended operation.
2. Convert direct signals to root skills through the signal rules below.
3. Expand each root through recursive `BEFORE` edges from
   `references/skill-graph.md`.
4. Add `WITH` targets only when the target has its own direct signal in the
   request, files, diff, or operation. Do not expand `WITH` targets
   transitively.
5. Hold `AFTER` targets until the work reaches that phase or the user asks for
   it explicitly.
6. Order the final set by process gates first, then architecture, framework,
   testing, documentation, and maintenance concerns.
7. If the cascade becomes broad, prefer a plan or review gate over loading more
   skills speculatively.

## Signal Rules

| Signal | Evidence | Start Skills |
| --- | --- | --- |
| Explicit skill request | User names a skill or asks for a known workflow | Named skill, `using-cortex` |
| Ambiguous or creative work | Goal, behavior, architecture, or user experience is not clear yet | `design-intake` |
| Multi-step work | Cross-boundary change, migration, risky refactor, or substantial implementation | `implementation-plan` |
| Written plan execution | Plan exists and no design decision remains open | `plan-execution` |
| Workspace collision risk | Substantial edits, branch cleanup, publish step, or dirty tree risk | `workspace-state-guard` |
| Behavior change | New behavior, bug fix, refactor with observable behavior, or regression risk | `test-first-discipline` |
| Code edit | Code is generated, edited, moved, split, refactored, or materially reviewed | `code-documentation` |
| Failure investigation | Failing test, build failure, bug report, performance problem, or unexpected behavior | `systematic-debugging` |
| Completion or publishing | Success claim, commit, push, pull request, merge, release, or finish decision | `completion-verification`, `branch-completion`, `review-gate` |
| Review feedback | User, CI, reviewer, or agent gives technical feedback to evaluate | `review-feedback-triage` |
| Monorepo structure | Workspace graph, project metadata, tags, boundaries, generators, or inferred targets matter | `nx-conventions`, `nx-module-boundaries`, `library-placement-decision` |
| Library surface | New library, moved shared code, public export, entry point, reusable contract, or import path change | `library-placement-decision`, `public-api-design`, `naming-consistency` |
| TypeScript implementation | TypeScript source, tests, imports, classes, functions, or strict typing are edited | `typescript-code-style` |
| TypeScript public API | Exported type, DTO, contract, generic, or reusable type surface changes | `typescript-api-conventions` |
| Angular surface | Angular component, directive, pipe, service, template, form, input, output, or dependency injection changes | `angular-conventions` |
| Angular Material or CDK | Material component, CDK utility, overlay, theme, accessibility, or density changes | `angular-material-conventions` |
| Angular TanStack Query | Query key, query options, mutation, pagination, or skippable input changes | `angular-tanstack-query-conventions` |
| RxJS surface | Observable, operator, subject, subscription, multicasting, or cleanup changes | `rxjs-conventions` |
| Storybook surface | Story, MDX docs, preview setup, addon, mock, or story organization changes | `storybook-conventions`, `storybook-angular-conventions` |
| NestJS surface | Module, provider, controller, guard, pipe, interceptor, bootstrap, or microservice runtime changes | `nestjs-conventions` |
| Mongoose persistence | Schema, model, repository, aggregation helper, ObjectId handling, or persistence DTO changes | `nestjs-mongoose-conventions` |
| Vue surface | Vue component, Composition API, script setup, prop, emit, slot, or component naming changes | `vue-conventions` |
| Vite surface | Vite config, library build, alias, plugin, source map, externalization, or dev server changes | `vite-conventions` |
| Test runner surface | Jest, Vitest, or Playwright config, tests, setup, mocks, fixtures, locators, or assertions change | `jest-conventions`, `vitest-conventions`, `playwright-conventions` |
| Documentation or examples | JSDoc/TSDoc, public docs, examples, stories, fixtures, sample payloads, or illustrative data change | `code-documentation`, `example-universe-enforcer` |
| Reusable doctrine gap | Repeated agent failure, recurring workflow, or durable convention emerges | `skill-evolution` |
| Work history | User asks to log, summarize, hand off, preserve decisions, or record validation | `diary` |

## Guardrails

- Do not create one-off signal rows from a single user example.
- Do not route from technology keywords alone when the touched files prove the
  technology is unrelated to the task.
- Do not make `using-cortex` a hard parent of every skill through `BEFORE`.
- Do not use `WITH` as an automatic expansion mechanism.
- When the user limits skills or tools explicitly, honor that instruction before
  applying this cascade.
