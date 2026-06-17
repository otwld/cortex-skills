# Skill Catalog

Cortex Skills contains 46 skills grouped by reusable purpose. Each skill has a
`SKILL.md` trigger description and `agents/openai.yaml` metadata.

## Architecture

| Skill | Use when | Path |
| --- | --- | --- |
| `architecture-drift-detector` | Detect structural drift signals before broad changes compound architecture risk. | `architecture/drift-detector/` |
| `architecture-deepening-review` | Find shallow modules and propose deepening candidates using module, interface, seam, adapter, leverage, and locality language. | `architecture/deepening-review/` |
| `bundle-performance` | Protect bundle size, tree-shaking, and side-effect boundaries in broadly consumed runtime code. | `architecture/bundle-performance/` |
| `extraction-decision` | Decide whether repeated logic should become a reusable abstraction and where it belongs. | `architecture/extraction-decision/` |
| `library-placement-decision` | Place new or moved code by responsibility, ownership, dependency direction, and consumer scope. | `architecture/library-placement-decision/` |
| `naming-consistency` | Keep names aligned with domain vocabulary, ownership, and public API responsibilities. | `architecture/naming-consistency/` |
| `nx-module-boundaries` | Use Nx project metadata and dependency rules to preserve modular workspace boundaries. | `architecture/nx-module-boundaries/` |
| `public-api-design` | Design minimal, stable, typed, documented public surfaces for reusable packages and contracts. | `architecture/public-api-design/` |

## Documentation

| Skill | Use when | Path |
| --- | --- | --- |
| `code-documentation` | Keep JSDoc, TSDoc, Storybook, MDX, and usage documentation synchronized with code changes. | `documentation/code/` |

## Frameworks

| Skill | Use when | Path |
| --- | --- | --- |
| `angular-conventions` | Apply Angular conventions for components, templates, forms, dependency injection, and public Angular APIs. | `frameworks/angular/core/` |
| `angular-material-conventions` | Use Angular Material and CDK deliberately while preserving accessibility, theming, density, and bundle boundaries. | `frameworks/angular/material/` |
| `storybook-angular-conventions` | Write Angular Storybook stories with realistic providers, deterministic states, and Angular-compatible setup. | `frameworks/angular/storybook/` |
| `angular-tanstack-query-conventions` | Keep Angular TanStack Query keys, options, mutations, pagination, and skippable inputs stable and typed. | `frameworks/angular/tanstack-query/` |
| `nestjs-conventions` | Apply NestJS conventions for modules, providers, controllers, guards, pipes, interceptors, and runtime setup. | `frameworks/nestjs/core/` |
| `nestjs-mongoose-conventions` | Keep NestJS Mongoose schemas, ObjectId handling, repositories, aggregations, and persistence contracts explicit. | `frameworks/nestjs/mongoose/` |
| `nx-conventions` | Maintain Nx workspace configuration, projects, targets, generators, inferred tasks, and graph behavior. | `frameworks/nx/` |
| `rxjs-conventions` | Design RxJS streams with clear ownership, cancellation, multicasting, error handling, and cleanup. | `frameworks/rxjs/` |
| `storybook-conventions` | Use Storybook as deterministic executable documentation for public, reusable, and user-facing UI states. | `frameworks/storybook/` |
| `vite-conventions` | Maintain Vite configuration, library builds, aliases, plugins, source maps, externalization, and dev-server behavior. | `frameworks/vite/` |
| `vue-conventions` | Apply Vue 3 conventions for Single-File Components, Composition API, props, emits, slots, and names. | `frameworks/vue/` |

## Governance

| Skill | Use when | Path |
| --- | --- | --- |
| `using-cortex` | Route tasks to the smallest evidence-backed set of Cortex skills using direct signals and graph edges. | `governance/core/using-cortex/` |
| `design-intake` | Clarify goals, success criteria, constraints, and tradeoffs before implementation starts. | `governance/intake/design-intake/` |
| `grill-with-docs` | Interview the user deeply while updating project glossary and ADR artifacts as decisions crystallize. | `governance/intake/grill-with-docs/` |
| `implementation-plan` | Turn stable requirements into a decision-complete execution path with validations and scope boundaries. | `governance/planning/implementation-plan/` |
| `issue-decomposition` | Break plans into vertical issue slices and durable agent briefs for configurable issue trackers. | `governance/planning/issue-decomposition/` |
| `prototype` | Create clearly throwaway logic or UI prototypes that answer one design question quickly. | `governance/prototyping/prototype/` |
| `agent-instructions-bootstrap` | Bootstrap AGENTS.md-first workspace instructions with strict assumption grilling. | `governance/setup/agent-instructions-bootstrap/` |
| `project-memory-setup` | Set up or verify glossary, ADR, out-of-scope, issue tracker, and triage-label project memory artifacts. | `governance/setup/project-memory-setup/` |
| `plan-execution` | Execute a decision-complete plan in order while preserving scope, validation, and workspace safety. | `governance/execution/plan-execution/` |
| `agent-delegation` | Delegate independent investigation, implementation, or review work with clear prompts and verification expectations. | `governance/delegation/agent-delegation/` |
| `workspace-state-guard` | Protect user work by inspecting branch and dirty state before substantial edits or cleanup. | `governance/workspace/workspace-state-guard/` |
| `test-first-discipline` | Prefer a failing test or characterization before behavior changes, bug fixes, and risky refactors. | `governance/development/test-first-discipline/` |
| `systematic-debugging` | Diagnose failures through reproduction, falsifiable hypotheses, targeted probes, fixes, and regression checks. | `governance/debugging/systematic-debugging/` |
| `completion-verification` | Verify completion claims with current evidence before reporting success or publishing work. | `governance/verification/completion-verification/` |
| `review-gate` | Review significant work for requirement fit, correctness, tests, APIs, boundaries, docs, and migration risk. | `governance/review/review-gate/` |
| `review-feedback-triage` | Triage review feedback before implementing it, separating required fixes from optional or incorrect suggestions. | `governance/review/feedback-triage/` |
| `branch-completion` | Finish branch work safely with verification, review, intentional commits, pushes, PRs, or cleanup. | `governance/release/branch-completion/` |

## Maintenance

| Skill | Use when | Path |
| --- | --- | --- |
| `diary` | Record durable work history, decisions, blockers, validations, and handoff context when requested. | `maintenance/diary/` |
| `example-universe-enforcer` | Keep all illustrative examples in the recruitment agency job board universe. | `maintenance/example-universe-enforcer/` |
| `skill-evolution` | Evolve skills from repeated reusable patterns, doctrine gaps, and agent failure modes. | `maintenance/skill-evolution/` |

## Testing

| Skill | Use when | Path |
| --- | --- | --- |
| `jest-conventions` | Write and maintain Jest tests, setup, mocks, matchers, and environments around behavior-focused assertions. | `testing/jest/` |
| `playwright-conventions` | Write Playwright tests with accessible locators, deterministic setup, clear fixtures, and condition-based waits. | `testing/playwright/` |
| `vitest-conventions` | Maintain Vitest tests, environments, mocks, and Vite-integrated configuration with behavior-focused assertions. | `testing/vitest/` |

## Tools

| Skill | Use when | Path |
| --- | --- | --- |
| `bricks` | Operate Bricks consumer workflows for installed source copies, merges, diffs, doctor checks, and contributions. | `tools/bricks/` |

## TypeScript

| Skill | Use when | Path |
| --- | --- | --- |
| `typescript-api-conventions` | Design TypeScript exported types, DTOs, generics, and reusable contracts with strict public surfaces. | `typescript/api/` |
| `typescript-code-style` | Apply TypeScript implementation style for modules, imports, comments, language features, naming, and tooling preflight. | `typescript/code-style/` |
