
# Output Marker

Display:
using module: angular-material-conventions

---

# Angular Material And CDK Conventions

## Overview

Use Material and CDK narrowly while preserving accessibility, theming, and bundle
boundaries.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Import only used APIs; prefer CDK primitives for overlays and a11y; preserve focus and keyboard behavior; justify density changes.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Material and CDK usage imports only the APIs needed for the visible interaction.
- Focus, keyboard flow, labels, density, and overlay behavior are preserved or intentionally changed.
- Theme and bundle effects are explicit when a shared UI surface gains Material dependencies.

## Example

An Interview scheduling dialog uses CDK focus handling and a documented close result
instead of custom keyboard traps.

## Hard Stops

- Do not add a Material component when a CDK primitive or existing local component is the real owner.
- Do not ship dialogs, menus, overlays, or form controls without keyboard and focus checks.
- Do not broaden shared UI dependencies without naming the bundle and theming impact.

## Usage Checklist

- Material or CDK trigger evidence was tied to a concrete component or interaction.
- Accessibility, density, theming, and overlay implications were reviewed.
- Bundle or dependency impact was recorded for shared surfaces.

## Cross References

- BEFORE: angular-conventions
- WITH: bundle-performance, typescript-code-style, code-documentation
- AFTER: skill-evolution
