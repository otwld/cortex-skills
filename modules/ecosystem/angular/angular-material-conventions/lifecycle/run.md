# Angular Material Conventions Run

## Overview

Implement Material/CDK changes narrowly while preserving accessible interaction,
supported theming, and dependency boundaries.

## Workflow

- Import only the Material components or CDK utilities used by the affected
  standalone component, NgModule, test, or provider. Do not introduce a broad
  catch-all Material module unless the local project already centralizes imports
  that way.
- Prefer CDK a11y and overlay primitives for custom visual designs. Prefer
  Material components when the request expects Material behavior, states, and
  styling.
- For dialogs, menus, popovers, tooltips, and custom overlays, specify the
  trigger, focus entry, focus restoration, keyboard dismissal, scroll behavior,
  backdrop behavior, result payload, and teardown path.
- Keep labels, descriptions, error text, disabled state, and required state wired
  through the component API so assistive technology receives the same state a
  sighted user sees.
- Apply themes through the project theme file using supported Material Sass APIs,
  `mat.theme`, component mixins, strong focus indicators, or documented token
  overrides. Avoid selectors that target private internal Material structure.
- Density changes must name the affected component family and why compact sizing
  is acceptable for pointer, keyboard, and assistive-technology users.
- Use Material/CDK harnesses or equivalent user-level tests for Material controls
  whose DOM is implementation-owned by the library.
- Update public docs for reusable components that expose Material/CDK behavior,
  especially close results, selected values, aria labeling requirements, and
  density/theme expectations.

## Quality Gates

- Run a focused component test, harness test, or browser check covering keyboard
  navigation, focus movement, labels, and close behavior.
- For theme or density changes, inspect the compiled or rendered state across
  light/dark mode and the component states touched by the diff.
- For shared surfaces, name the dependency or bundle effect even when no bundle
  tooling is available.

## Hard Stops

- Do not ship a new dialog, menu, overlay, select, autocomplete, or custom focus
  trap without keyboard and focus validation.
- Do not customize Material internals through private DOM selectors, private CSS
  classes, or arbitrary `::ng-deep` overrides.
- Do not use Material as a styling shortcut when the existing local component or
  CDK primitive owns the interaction more directly.

## Phase Output

Return the files changed, imported Material/CDK APIs, interaction and a11y
validation performed, and any theme, density, overlay, or dependency risk left
for follow-up.
