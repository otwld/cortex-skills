# Module Graph

Generated from routed module and command skill relation metadata. Do not edit by hand.

| Artifact | Activation | Before | With | After | Excludes | Replaces |
| --- | --- | --- | --- | --- | --- | --- |
| `agent-delegation` | `routed` | None | `plan-execution`, `review-gate`, `systematic-debugging`, `completion-verification` | None | None | None |
| `angular-conventions` | `routed` | None | `rxjs-conventions`, `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `angular-material-conventions` | `routed` | `angular-conventions` | `bundle-performance`, `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `angular-tanstack-query-conventions` | `routed` | `angular-conventions` | `rxjs-conventions`, `typescript-api-conventions`, `public-api-design`, `code-documentation` | `skill-evolution` | None | None |
| `architecture-deepening-review` | `routed` | None | `architecture-drift-detector`, `library-placement-decision`, `public-api-design`, `test-first-discipline`, `code-documentation` | `skill-evolution` | None | None |
| `architecture-drift-detector` | `routed` | None | `architecture-deepening-review`, `library-placement-decision`, `nx-module-boundaries` | None | None | None |
| `branch-completion` | `routed` | `workspace-state-guard`, `completion-verification` | `review-gate` | None | None | None |
| `bricks` | `routed` | None | `workspace-state-guard`, `nx-conventions`, `completion-verification` | None | None | None |
| `bundle-performance` | `routed` | None | `public-api-design` | None | None | None |
| `code-documentation` | `routed` | None | `example-universe-enforcer`, `storybook-conventions` | `skill-evolution` | None | None |
| `completion-verification` | `routed` | None | `review-gate`, `branch-completion` | None | None | None |
| `design-intake` | `routed` | None | `grill-with-docs`, `prototype`, `architecture-drift-detector`, `library-placement-decision`, `public-api-design` | `implementation-plan` | None | None |
| `diary` | `routed` | None | None | None | None | None |
| `example-universe-enforcer` | `routed` | None | None | None | None | None |
| `extraction-decision` | `routed` | `library-placement-decision`, `nx-module-boundaries` | `public-api-design`, `naming-consistency`, `bundle-performance`, `code-documentation` | `skill-evolution` | None | None |
| `grill-with-docs` | `routed` | None | `design-intake`, `implementation-plan` | `issue-decomposition` | None | None |
| `implementation-plan` | `routed` | None | `design-intake`, `grill-with-docs`, `issue-decomposition`, `workspace-state-guard`, `test-first-discipline`, `architecture-drift-detector`, `library-placement-decision`, `public-api-design`, `code-documentation` | `plan-execution` | None | None |
| `issue-decomposition` | `routed` | None | `implementation-plan`, `grill-with-docs` | `plan-execution` | None | None |
| `jest-conventions` | `routed` | None | `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `library-placement-decision` | `routed` | None | `nx-module-boundaries`, `public-api-design`, `naming-consistency` | `skill-evolution` | None | None |
| `naming-consistency` | `routed` | None | `public-api-design`, `typescript-api-conventions`, `code-documentation` | None | None | None |
| `nestjs-conventions` | `routed` | None | `rxjs-conventions`, `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `nestjs-mongoose-conventions` | `routed` | `nestjs-conventions` | `typescript-api-conventions`, `public-api-design`, `code-documentation` | `skill-evolution` | None | None |
| `nx-conventions` | `routed` | None | `nx-module-boundaries`, `library-placement-decision` | None | None | None |
| `nx-module-boundaries` | `routed` | `library-placement-decision` | `public-api-design` | None | None | None |
| `plan-execution` | `routed` | `workspace-state-guard` | `agent-delegation`, `test-first-discipline`, `code-documentation`, `review-gate`, `completion-verification` | `branch-completion` | None | None |
| `playwright-conventions` | `routed` | None | `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `prototype` | `routed` | None | `design-intake`, `test-first-discipline`, `code-documentation` | `issue-decomposition` | None | None |
| `public-api-design` | `routed` | `library-placement-decision` | `naming-consistency`, `typescript-api-conventions`, `code-documentation` | None | None | None |
| `review-feedback-triage` | `routed` | None | `systematic-debugging`, `test-first-discipline`, `completion-verification`, `review-gate` | None | None | None |
| `review-gate` | `routed` | None | `agent-delegation`, `completion-verification`, `review-feedback-triage`, `public-api-design`, `architecture-drift-detector` | None | None | None |
| `rxjs-conventions` | `routed` | None | `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `skill-evolution` | `routed` | None | None | None | None | None |
| `storybook-angular-conventions` | `routed` | `storybook-conventions`, `angular-conventions` | `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `storybook-conventions` | `routed` | None | `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `systematic-debugging` | `routed` | None | `test-first-discipline`, `completion-verification`, `architecture-drift-detector` | `skill-evolution` | None | None |
| `test-first-discipline` | `routed` | None | `systematic-debugging`, `completion-verification`, `jest-conventions`, `vitest-conventions`, `playwright-conventions` | None | None | None |
| `typescript-api-conventions` | `routed` | None | `public-api-design`, `naming-consistency`, `typescript-code-style`, `code-documentation` | None | None | None |
| `typescript-code-style` | `routed` | None | `code-documentation` | None | None | None |
| `vite-conventions` | `routed` | None | `bundle-performance`, `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `vitest-conventions` | `routed` | None | `vite-conventions`, `typescript-code-style`, `code-documentation` | `skill-evolution` | None | None |
| `vue-conventions` | `routed` | None | `typescript-code-style`, `rxjs-conventions`, `code-documentation` | `skill-evolution` | None | None |
| `workspace-state-guard` | `routed` | None | `branch-completion`, `completion-verification` | None | None | None |
| `setup-agent-instructions` | `explicit` | None | None | None | None | None |
| `setup-project-memory` | `explicit` | None | None | None | None | None |
| `setup-routed-skill-workspace` | `explicit` | None | None | None | None | None |
