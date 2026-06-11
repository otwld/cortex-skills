# Skill Graph

This graph is the canonical dependency map for skills in this workspace.
Inline `Cross-References` sections in each `SKILL.md` must match this table.
Routing signal rules live in `references/skill-cascade.md`; keep signal
selection separate from graph edge expansion.

Use only these non-transitive advisory edge labels:

- `BEFORE`: load or apply the listed skill first. `BEFORE` edges may be
  followed recursively because ordering is part of correctness.
- `WITH`: apply alongside the current skill only when the user task or changed
  files already touch that area. Do not load `WITH` targets solely because this
  graph mentions them, and do not expand `WITH` targets transitively.
- `AFTER`: consider after the current work is complete. Do not load `AFTER`
  targets during the main task, and do not expand them transitively.
- `None`: the skill has no related skill edges.

| Skill | BEFORE | WITH | AFTER |
| --- | --- | --- | --- |
| `architecture-drift-detector` | None | `library-placement-decision`, `nx-module-boundaries` | None |
| `bundle-performance` | None | `public-api-design` | None |
| `extraction-decision` | `library-placement-decision`, `nx-module-boundaries` | `public-api-design`, `naming-consistency`, `bundle-performance`, `code-documentation` | `skill-evolution` |
| `library-placement-decision` | None | `nx-module-boundaries`, `public-api-design`, `naming-consistency` | `skill-evolution` |
| `naming-consistency` | None | `public-api-design`, `typescript-api-conventions`, `code-documentation` | None |
| `nx-module-boundaries` | `library-placement-decision` | `public-api-design` | None |
| `public-api-design` | `library-placement-decision` | `naming-consistency`, `typescript-api-conventions`, `code-documentation` | None |
| `code-documentation` | None | `example-universe-enforcer`, `storybook-conventions` | `skill-evolution` |
| `angular-conventions` | None | `rxjs-conventions`, `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `angular-material-conventions` | `angular-conventions` | `bundle-performance`, `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `angular-tanstack-query-conventions` | `angular-conventions` | `rxjs-conventions`, `typescript-api-conventions`, `public-api-design`, `code-documentation` | `skill-evolution` |
| `nestjs-conventions` | None | `rxjs-conventions`, `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `nestjs-mongoose-conventions` | `nestjs-conventions` | `typescript-api-conventions`, `public-api-design`, `code-documentation` | `skill-evolution` |
| `nx-conventions` | None | `nx-module-boundaries`, `library-placement-decision` | None |
| `rxjs-conventions` | None | `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `storybook-angular-conventions` | `storybook-conventions`, `angular-conventions` | `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `storybook-conventions` | None | `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `vite-conventions` | None | `bundle-performance`, `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `vue-conventions` | None | `typescript-code-style`, `rxjs-conventions`, `code-documentation` | `skill-evolution` |
| `bricks` | None | `workspace-state-guard`, `nx-conventions`, `completion-verification` | None |
| `using-cortex` | None | `design-intake`, `implementation-plan`, `plan-execution`, `agent-delegation`, `workspace-state-guard`, `test-first-discipline`, `systematic-debugging`, `completion-verification`, `review-gate`, `review-feedback-triage`, `branch-completion`, `code-documentation` | None |
| `design-intake` | None | `architecture-drift-detector`, `library-placement-decision`, `public-api-design` | `implementation-plan` |
| `implementation-plan` | None | `design-intake`, `workspace-state-guard`, `test-first-discipline`, `architecture-drift-detector`, `library-placement-decision`, `public-api-design`, `code-documentation` | `plan-execution` |
| `plan-execution` | `workspace-state-guard` | `agent-delegation`, `test-first-discipline`, `code-documentation`, `review-gate`, `completion-verification` | `branch-completion` |
| `agent-delegation` | None | `plan-execution`, `review-gate`, `systematic-debugging`, `completion-verification` | None |
| `workspace-state-guard` | None | `branch-completion`, `completion-verification` | None |
| `test-first-discipline` | None | `systematic-debugging`, `completion-verification`, `jest-conventions`, `vitest-conventions`, `playwright-conventions` | None |
| `systematic-debugging` | None | `test-first-discipline`, `completion-verification`, `architecture-drift-detector` | `skill-evolution` |
| `completion-verification` | None | `review-gate`, `branch-completion` | None |
| `review-gate` | None | `agent-delegation`, `completion-verification`, `review-feedback-triage`, `public-api-design`, `architecture-drift-detector` | None |
| `review-feedback-triage` | None | `systematic-debugging`, `test-first-discipline`, `completion-verification`, `review-gate` | None |
| `branch-completion` | `workspace-state-guard`, `completion-verification` | `review-gate` | None |
| `diary` | None | None | None |
| `example-universe-enforcer` | None | None | None |
| `skill-evolution` | None | None | None |
| `jest-conventions` | None | `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `playwright-conventions` | None | `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `vitest-conventions` | None | `vite-conventions`, `typescript-code-style`, `code-documentation` | `skill-evolution` |
| `typescript-api-conventions` | None | `public-api-design`, `naming-consistency`, `typescript-code-style`, `code-documentation` | None |
| `typescript-code-style` | None | `code-documentation` | None |
