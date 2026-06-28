# Minimize Cognitive Load Review

## Overview

Review touched code for avoidable reader burden that makes behavior harder to
understand, modify, debug, or review.

## Workflow

1. Trace the changed behavior from input to output, including state changes,
   side effects, error paths, and dependencies.
2. Flag code that requires unnecessary jumps across files, layers, helpers,
   utilities, services, managers, factories, callbacks, decorators, lifecycle
   hooks, or hidden configuration.
3. Flag avoidable nesting, broad branching, dense expressions, generic names,
   excessive parameters, public surface creep, speculative options, and
   abstraction layers without current reuse.
4. Separate readability findings from neighboring concerns owned by naming,
   TypeScript style, documentation, SRP, extraction, public API, composition,
   SSOT, performance, or framework conventions.
5. For each finding, name the reader burden and the smallest correction that
   makes the code more obvious without changing behavior.

## Quality Gates

- Findings are grounded in a concrete reader task or review risk.
- Findings prefer smaller, clearer code over broad refactor proposals.
- Accepted complexity names the constraint that justifies it.

## Hard Stops

- Do not ask for personal style changes that do not reduce reader burden.
- Do not request a new abstraction as the default fix for complex code.
- Do not reject a local duplicate when extraction would increase reader effort
  and reuse is not established.

## Phase Output

- Return cognitive-load findings, accepted complexity, simplification
  recommendations, overlap handoffs, and any reviewability risks.
