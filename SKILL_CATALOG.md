# Skill Catalog

Cortex Skills contains 27 skills grouped by reusable purpose. Each skill has a
`SKILL.md` trigger description and `agents/openai.yaml` metadata.

## Architecture

| Skill | Use when | Path |
| --- | --- | --- |
| `architecture-drift-detector` | Starting significant work, reviewing recent changes, planning refactors, or seeing commit bursts that may indicate structural drift. | `architecture/architecture-drift-detector/` |
| `bundle-performance` | Changes may affect bundle size, tree-shaking, side effects, UI dependencies, entry points, or broadly consumed runtime code. | `architecture/bundle-performance/` |
| `extraction-decision` | Repeated logic, DTOs, contracts, data-access patterns, UI composition, or orchestration suggest extracting a reusable abstraction. | `architecture/extraction-decision/` |
| `library-placement-decision` | Deciding where new code, shared abstractions, moved files, extracted logic, or public entry points belong inside a modular TypeScript workspace. | `architecture/library-placement-decision/` |
| `naming-consistency` | Creating or renaming files, classes, functions, exports, DTOs, contracts, events, commands, providers, factories, or reusable abstractions. | `architecture/naming-consistency/` |
| `nx-module-boundaries` | Working in an Nx workspace and adding, moving, or reviewing projects, tags, dependencies, or module-boundary rules. | `architecture/nx-module-boundaries/` |
| `public-api-design` | Adding or changing exports, shared contracts, DTOs, reusable abstractions, entry points, package boundaries, or import paths. | `architecture/public-api-design/` |

## Documentation

| Skill | Use when | Path |
| --- | --- | --- |
| `code-documentation` | Adding or changing public, reusable, or user-facing code that needs documentation, examples, stories, MDX docs, or API usage notes. | `documentation/code-documentation/` |

## Frameworks

| Skill | Use when | Path |
| --- | --- | --- |
| `angular-conventions` | Creating, modifying, or reviewing Angular components, directives, pipes, services, templates, styles, forms, inputs, outputs, or dependency injection. | `frameworks/angular-conventions/` |
| `angular-material-conventions` | Adding, modifying, or reviewing Angular Material or Angular CDK components, utilities, theming, overlays, accessibility, or density settings. | `frameworks/angular-material-conventions/` |
| `angular-tanstack-query-conventions` | Creating, modifying, or reviewing TanStack Query integration in Angular code, including query keys, query options, mutations, pagination, and skippable inputs. | `frameworks/angular-tanstack-query-conventions/` |
| `nestjs-conventions` | Creating, modifying, or reviewing NestJS modules, providers, controllers, interceptors, guards, pipes, application bootstrap, or microservice runtimes. | `frameworks/nestjs-conventions/` |
| `nestjs-mongoose-conventions` | Creating or reviewing NestJS Mongoose schemas, models, repositories, aggregation helpers, ObjectId handling, or persistence-facing DTO contracts. | `frameworks/nestjs-mongoose-conventions/` |
| `nx-conventions` | Creating, modifying, or reviewing Nx workspace configuration, generators, targets, project metadata, inferred tasks, or project graph behavior. | `frameworks/nx-conventions/` |
| `rxjs-conventions` | Creating, modifying, or reviewing RxJS observables, operators, subscriptions, subjects, multicasting, cleanup, or async stream composition. | `frameworks/rxjs-conventions/` |
| `storybook-angular-conventions` | Creating, modifying, or reviewing Angular Storybook stories, Angular story providers, module metadata, standalone story setup, or Angular story mocks. | `frameworks/storybook-angular-conventions/` |
| `storybook-conventions` | Creating, modifying, or reviewing Storybook stories, MDX docs, preview setup, addons, mocks, visual regression data, or story organization. | `frameworks/storybook-conventions/` |
| `vite-conventions` | Creating, modifying, or reviewing Vite configuration, library builds, aliases, plugins, source maps, dependency externalization, or dev-server settings. | `frameworks/vite-conventions/` |
| `vue-conventions` | Creating, modifying, or reviewing Vue 3 Single-File Components, Composition API code, `<script setup>`, props, emits, slots, or component naming. | `frameworks/vue-conventions/` |

## Maintenance

| Skill | Use when | Path |
| --- | --- | --- |
| `diary` | The user asks to log, journal, summarize, hand off, or preserve agent work history, decisions, blockers, validations, or completed outcomes. | `maintenance/diary/` |
| `example-universe-enforcer` | Producing examples, sample code, DTOs, API payloads, Storybook data, docs snippets, tests, or illustrative data. | `maintenance/example-universe-enforcer/` |
| `skill-evolution` | Repeated implementation patterns, technical discussions, refactors, reviews, or skill-library changes reveal a reusable agent workflow or doctrine gap. | `maintenance/skill-evolution/` |

## Testing

| Skill | Use when | Path |
| --- | --- | --- |
| `jest-conventions` | Creating, modifying, or reviewing Jest configuration, Jest tests, setup files, custom matchers, test environments, or Jest mocks. | `testing/jest-conventions/` |
| `playwright-conventions` | Creating, modifying, or reviewing Playwright configuration, browser projects, end-to-end tests, locators, assertions, fixtures, or setup projects. | `testing/playwright-conventions/` |
| `vitest-conventions` | Creating, modifying, or reviewing Vitest configuration, Vitest tests, setup files, environments, mocks, or Vite-integrated test behavior. | `testing/vitest-conventions/` |

## TypeScript

| Skill | Use when | Path |
| --- | --- | --- |
| `typescript-api-conventions` | Designing or reviewing TypeScript public APIs, exported types, DTOs, contracts, generics, strict typing, entry points, or reusable type surfaces. | `typescript/typescript-api-conventions/` |
| `typescript-code-style` | Writing, editing, generating, refactoring, or reviewing TypeScript or TSX source files, tests, build scripts, imports, exports, classes, functions, or interfaces. | `typescript/typescript-code-style/` |
