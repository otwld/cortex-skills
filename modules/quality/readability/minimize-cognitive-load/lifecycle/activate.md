# Minimize Cognitive Load Activate

## Overview

Activate for code work where implementation choices may affect how quickly a
future reader can understand, modify, debug, or review the touched code.

## Workflow

1. Load `references/cognitive-load-boundaries.md` for code creation, edit,
   refactor, split, move, or material review tasks.
2. Inventory the touched files, functions, classes, components, hooks, services,
   commands, adapters, modules, tests, scripts, and public surfaces.
3. Identify cognitive-load drivers: nested control flow, indirect data flow,
   hidden dependencies, generic helpers, excessive parameters, broad public
   surface, scattered feature logic, clever language features, and mixed
   refactor or feature diffs.
4. Name the reader task that becomes harder: understanding intent, following
   inputs to outputs, locating side effects, debugging failures, reviewing the
   behavioral change, or safely modifying the code later.
5. Note overlap with naming, TypeScript style, documentation, SRP, extraction,
   public API, composition, SSOT, performance, or framework conventions when
   the durable decision belongs to those modules.

## Quality Gates

- Activation evidence names concrete touched code or a code-review target.
- A concern names the reader burden, not just personal style preference.
- Broad code requests activate this module, while non-code workspace work stays
  out unless the user asks for readability or cognitive-load guidance.

## Hard Stops

- Do not demand simplification that removes required behavior, validation,
  compatibility, accessibility, security, or correctness.
- Do not reject complexity that is forced by a proven external contract,
  framework lifecycle, or measured performance constraint.
- Do not decide vocabulary, type style, documentation coverage, reusable
  extraction, responsibility boundaries, or public API ownership when another
  routed module owns that decision.

## Phase Output

- Return touched units, reader burdens, complexity drivers, justified
  complexity, overlap risks, loaded reference, and next-phase simplification
  decisions needed.
