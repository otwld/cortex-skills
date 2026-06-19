
# Output Marker

Display:
using module: angular-conventions

---

# Angular Conventions

## Overview

Apply Angular guidance only when the project uses Angular and local version support is
known.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Prefer supported standalone APIs; use local DI style; keep complex templates/styles external; type forms; document public inputs and outputs.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Angular changes match the project's standalone, template, style, and dependency-injection conventions.
- Inputs, outputs, forms, and template-facing members are typed at the component boundary.
- Public component behavior is covered by tests, stories, or docs when consumers depend on it.

## Example

CandidatePipelineComponent exposes a documented jobOffer input and stageChange output
instead of reaching into route state directly.

## Hard Stops

- Do not introduce a component, directive, pipe, or service pattern that conflicts with the local Angular style.
- Do not hide template or form type problems with casts or untyped reactive forms.
- Do not document internal Angular wiring instead of the public behavior a consumer sees.

## Usage Checklist

- Local Angular usage was inspected before choosing component or service shape.
- Template, form, input, output, and DI effects were accounted for.
- Relevant Angular tests, stories, or docs were named when behavior changed.

## Cross References

- WITH: rxjs-conventions, typescript-code-style, code-documentation
- AFTER: skill-evolution
