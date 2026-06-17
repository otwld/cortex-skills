# Skill Cascade

Use this reference from `using-cortex` when a request touches multiple domains or when skill selection is not obvious from one named skill.

## Cascade Algorithm

1. Collect direct signals from the request, files, diff, config, and intended operation.
2. Convert direct signals to root skills through the signal rules below.
3. Expand recursive `BEFORE` edges from `references/skill-graph.md`.
4. Add `WITH` targets only when the target has its own direct signal.
5. Hold `AFTER` targets until that phase or explicit user request.
6. Order process gates first, then architecture, framework, testing, documentation, and maintenance.

## Signal Rules

| Signal | Evidence | Start Skills |
| --- | --- | --- |
| Explicit skill request | User names a skill or asks for a known workflow | `using-cortex`, named skill |
| Ambiguous or creative work | Goal, behavior, architecture, or user experience is not clear | `design-intake` |
| Deep questioning with memory | Vocabulary is fuzzy, ADRs matter, or decisions should update memory | `grill-with-docs` |
| Multi-step work | Cross-boundary change, migration, risky refactor, or substantial implementation | `implementation-plan` |
| Issue breakdown | Plan, PRD, or large request must become vertical slices or briefs | `issue-decomposition` |
| Throwaway design learning | User wants to prototype, compare UI variants, or test a state model | `prototype` |
| Agent instruction bootstrap | AGENTS.md, nested agent instructions, or tool-specific AI guidance files are created, audited, or reconciled | `agent-instructions-bootstrap` |
| Project memory setup | Glossary, ADR, out-of-scope, tracker, or label docs are created or verified | `project-memory-setup` |
| Written plan execution | Plan exists and no design decision remains open | `plan-execution` |
| Workspace collision risk | Substantial edits, cleanup, publish step, or dirty tree risk | `workspace-state-guard` |
| Behavior change | New behavior, bug fix, refactor, or regression risk | `test-first-discipline` |
| Code edit | Code is generated, edited, moved, split, refactored, or materially reviewed | `code-documentation` |
| Failure investigation | Failing test, build failure, bug, performance problem, or unexpected behavior | `systematic-debugging` |
| Completion or publishing | Success claim, commit, push, pull request, merge, release, or finish decision | `completion-verification`, `branch-completion`, `review-gate` |
| Review feedback | User, CI, reviewer, or agent gives technical feedback | `review-feedback-triage` |
| Architecture drift or deepening | Broad churn, shallow modules, weak seams, poor locality, or low leverage | `architecture-drift-detector`, `architecture-deepening-review` |
| Monorepo structure | Workspace graph, metadata, tags, boundaries, generators, or inferred targets matter | `nx-conventions`, `nx-module-boundaries`, `library-placement-decision` |
| Library surface | New library, shared code, public export, entry point, contract, or import path change | `library-placement-decision`, `public-api-design`, `naming-consistency` |
| TypeScript implementation | TypeScript source, tests, imports, classes, functions, or strict typing are edited | `typescript-code-style` |
| TypeScript public API | Exported type, DTO, contract, generic, or reusable type surface changes | `typescript-api-conventions` |
| Angular surface | Angular component, directive, pipe, service, template, form, input, output, or DI changes | `angular-conventions` |
| Angular Material or CDK | Material component, CDK utility, overlay, theme, accessibility, or density changes | `angular-material-conventions` |
| Angular TanStack Query | Query key, options, mutation, pagination, or skippable input changes | `angular-tanstack-query-conventions` |
| RxJS surface | Observable, operator, subject, subscription, multicasting, or cleanup changes | `rxjs-conventions` |
| Storybook surface | Story, MDX docs, preview setup, addon, mock, or story organization changes | `storybook-conventions`, `storybook-angular-conventions` |
| NestJS surface | Module, provider, controller, guard, pipe, interceptor, bootstrap, or runtime changes | `nestjs-conventions` |
| Mongoose persistence | Schema, model, repository, aggregation, ObjectId, or persistence DTO changes | `nestjs-mongoose-conventions` |
| Vue surface | Vue component, Composition API, script setup, prop, emit, slot, or component naming changes | `vue-conventions` |
| Vite surface | Vite config, library build, alias, plugin, source map, externalization, or dev server changes | `vite-conventions` |
| Test runner surface | Jest, Vitest, or Playwright config, tests, setup, mocks, fixtures, locators, or assertions change | `jest-conventions`, `vitest-conventions`, `playwright-conventions` |
| Documentation or examples | JSDoc, TSDoc, public docs, examples, stories, fixtures, payloads, or illustrative data change | `code-documentation`, `example-universe-enforcer` |
| Reusable doctrine gap | Repeated agent failure, recurring workflow, or durable convention emerges | `skill-evolution` |
| Work history | User asks to log, summarize, hand off, preserve decisions, or record validation | `diary` |

## Guardrails

- Do not create one-off signal rows from a single user example.
- Do not route from technology keywords alone when files prove they are unrelated.
- Do not make `using-cortex` a hard parent of every skill through `BEFORE`.
- Do not use `WITH` as automatic expansion.
- Honor explicit user limits on skills or tools.
