
# Output Marker

Display:
using module: vitest-conventions

---

# Vitest Conventions

## Overview

Keep Vitest aligned with Vite while testing behavior through stable seams.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect config; choose correct environment; prefer real modules; mock boundaries; control timers deliberately; keep setup minimal.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Vitest tests use the project's configured environment, setup files, timers, and mock boundaries deliberately.
- Mocks preserve module contracts and avoid freezing private implementation details.
- Assertions are deterministic and aligned with Vite-integrated module behavior.

## Example

A pure JobOffer ranking function runs in node; a Candidate filter component using DOM
APIs uses the configured DOM environment.

## Hard Stops

- Do not copy Jest-specific setup or globals into Vitest without checking config support.
- Do not mock modules that should be exercised through their public contract.
- Do not leave fake timers, module mocks, or global state dirty across tests.

## Usage Checklist

- Vitest config, environment, setup, mocks, and timer usage were inspected.
- Public seam, fixture determinism, and mock boundaries were chosen deliberately.
- Focused Vitest command or validation gap was recorded.

## Cross References

- WITH: vite-conventions, typescript-code-style, code-documentation
- AFTER: skill-evolution
