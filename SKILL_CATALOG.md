# Skill Catalog

Cortex Skills contains 39 skills grouped by reusable purpose. Each skill has a
`SKILL.md` trigger description and `agents/openai.yaml` metadata.

## Architecture

| Skill | Use when | Path |
| --- | --- | --- |
| `architecture-drift-detector` | Starting significant work, reviewing recent changes, planning refactors, or seeing commit bursts that may indicate structural drift. | `architecture/drift-detector/` |
| `bundle-performance` | Changes may affect bundle size, tree-shaking, side effects, UI dependencies, entry points, or broadly consumed runtime code. | `architecture/bundle-performance/` |
| `extraction-decision` | Repeated logic, DTOs, contracts, data-access patterns, UI composition, or orchestration suggest extracting a reusable abstraction. | `architecture/extraction-decision/` |
| `library-placement-decision` | Deciding where new code, shared abstractions, moved files, extracted logic, or public entry points belong inside a modular TypeScript workspace. | `architecture/library-placement-decision/` |
| `naming-consistency` | Creating or renaming files, classes, functions, exports, DTOs, contracts, events, commands, providers, factories, or reusable abstractions. | `architecture/naming-consistency/` |
| `nx-module-boundaries` | Working in an Nx workspace and adding, moving, or reviewing projects, tags, dependencies, or module-boundary rules. | `architecture/nx-module-boundaries/` |
| `public-api-design` | Adding or changing exports, shared contracts, DTOs, reusable abstractions, entry points, package boundaries, or import paths. | `architecture/public-api-design/` |

## Documentation

| Skill | Use when | Path |
| --- | --- | --- |
| `code-documentation` | Code generation, edits, moves, splits, refactors, material review, and public or reusable docs that require JSDoc/TSDoc, examples, stories, MDX docs, or API usage notes. | `documentation/code/` |

## Frameworks

| Skill | Use when | Path |
| --- | --- | --- |
| `angular-conventions` | Creating, modifying, or reviewing Angular components, directives, pipes, services, templates, styles, forms, inputs, outputs, or dependency injection. | `frameworks/angular/core/` |
| `angular-material-conventions` | Adding, modifying, or reviewing Angular Material or Angular CDK components, utilities, theming, overlays, accessibility, or density settings. | `frameworks/angular/material/` |
| `angular-tanstack-query-conventions` | Creating, modifying, or reviewing TanStack Query integration in Angular code, including query keys, query options, mutations, pagination, and skippable inputs. | `frameworks/angular/tanstack-query/` |
| `nestjs-conventions` | Creating, modifying, or reviewing NestJS modules, providers, controllers, interceptors, guards, pipes, application bootstrap, or microservice runtimes. | `frameworks/nestjs/core/` |
| `nestjs-mongoose-conventions` | Creating or reviewing NestJS Mongoose schemas, models, repositories, aggregation helpers, ObjectId handling, or persistence-facing DTO contracts. | `frameworks/nestjs/mongoose/` |
| `nx-conventions` | Creating, modifying, or reviewing Nx workspace configuration, generators, targets, project metadata, inferred tasks, or project graph behavior. | `frameworks/nx/` |
| `rxjs-conventions` | Creating, modifying, or reviewing RxJS observables, operators, subscriptions, subjects, multicasting, cleanup, or async stream composition. | `frameworks/rxjs/` |
| `storybook-angular-conventions` | Creating, modifying, or reviewing Angular Storybook stories, Angular story providers, module metadata, standalone story setup, or Angular story mocks. | `frameworks/angular/storybook/` |
| `storybook-conventions` | Creating, modifying, or reviewing Storybook stories, MDX docs, preview setup, addons, mocks, visual regression data, or story organization. | `frameworks/storybook/` |
| `vite-conventions` | Creating, modifying, or reviewing Vite configuration, library builds, aliases, plugins, source maps, dependency externalization, or dev-server settings. | `frameworks/vite/` |
| `vue-conventions` | Creating, modifying, or reviewing Vue 3 Single-File Components, Composition API code, `<script setup>`, props, emits, slots, or component naming. | `frameworks/vue/` |

## Governance

| Skill | Use when | Path |
| --- | --- | --- |
| `using-cortex` | Starting agent work in a Cortex skill library or deciding which Cortex governance, architecture, framework, testing, or maintenance skills should apply. | `governance/core/using-cortex/` |
| `design-intake` | Before ambiguous, creative, behavioral, user-facing, or architecture-affecting work where intent, constraints, or success criteria are not already clear. | `governance/intake/design-intake/` |
| `implementation-plan` | Requirements are known and the work is multi-step, cross-boundary, migration-related, high-risk, or needs a written execution path before edits. | `governance/planning/implementation-plan/` |
| `plan-execution` | Executing a written implementation plan task-by-task with validation checkpoints and no remaining design decisions. | `governance/execution/plan-execution/` |
| `agent-delegation` | Independent tasks, investigations, or review passes can be delegated without shared state or sequential dependencies. | `governance/delegation/agent-delegation/` |
| `workspace-state-guard` | Before substantial edits, plan execution, branch cleanup, publishing, or work that may collide with user changes or workspace isolation. | `governance/workspace/workspace-state-guard/` |
| `test-first-discipline` | Before behavior changes, bug fixes, or refactors where tests can prove the intended behavior or regression. | `governance/development/test-first-discipline/` |
| `systematic-debugging` | Encountering bugs, failing tests, build failures, performance problems, or unexpected behavior before proposing fixes. | `governance/debugging/systematic-debugging/` |
| `completion-verification` | Before success claims, final responses, commits, pushes, pull requests, task completion, or publishing decisions. | `governance/verification/completion-verification/` |
| `review-gate` | After major features or refactors, before merge, pull request, push, publish, or when a completed change needs independent quality review. | `governance/review/review-gate/` |
| `review-feedback-triage` | Receiving code review, CI review, agent review, or external technical feedback before implementing suggested changes. | `governance/review/feedback-triage/` |
| `branch-completion` | Implementation is complete and the user asks to merge, push, open a pull request, publish, discard, clean up, or finish branch work. | `governance/release/branch-completion/` |

## Maintenance

| Skill | Use when | Path |
| --- | --- | --- |
| `diary` | The user asks to log, journal, summarize, hand off, or preserve agent work history, decisions, blockers, validations, or completed outcomes. | `maintenance/diary/` |
| `example-universe-enforcer` | Producing examples, sample code, DTOs, API payloads, Storybook data, docs snippets, tests, or illustrative data. | `maintenance/example-universe-enforcer/` |
| `skill-evolution` | Repeated implementation patterns, technical discussions, refactors, reviews, or skill-library changes reveal a reusable agent workflow or doctrine gap. | `maintenance/skill-evolution/` |

## Testing

| Skill | Use when | Path |
| --- | --- | --- |
| `jest-conventions` | Creating, modifying, or reviewing Jest configuration, Jest tests, setup files, custom matchers, test environments, or Jest mocks. | `testing/jest/` |
| `playwright-conventions` | Creating, modifying, or reviewing Playwright configuration, browser projects, end-to-end tests, locators, assertions, fixtures, or setup projects. | `testing/playwright/` |
| `vitest-conventions` | Creating, modifying, or reviewing Vitest configuration, Vitest tests, setup files, environments, mocks, or Vite-integrated test behavior. | `testing/vitest/` |

## TypeScript

| Skill | Use when | Path |
| --- | --- | --- |
| `typescript-api-conventions` | Designing or reviewing TypeScript public APIs, exported types, DTOs, contracts, generics, strict typing, entry points, or reusable type surfaces. | `typescript/api/` |
| `typescript-code-style` | Writing, editing, generating, refactoring, or reviewing TypeScript or TSX source files, tests, build scripts, imports, exports, classes, functions, or interfaces. | `typescript/code-style/` |
