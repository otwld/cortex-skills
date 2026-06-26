# Angular Material Conventions Review

## Overview

Find regressions caused by Material/CDK adoption, overlay behavior, accessibility
state, theming, density, and dependency scope.

## Workflow

- Confirm each Material/CDK import is used and scoped to the smallest local
  artifact that needs it.
- Verify dialogs, menus, overlays, tooltips, and popovers define focus entry,
  keyboard dismissal, backdrop or outside-click behavior, scroll behavior, close
  result, and teardown.
- Check labels, aria descriptions, error text, disabled state, required state,
  and live announcements against the user-visible state.
- Check focus indicators remain visible and theme-aware in normal, hover, focus,
  disabled, selected, error, high-contrast, and dark-mode states touched by the
  diff.
- Confirm density changes are intentional, limited to the correct component
  family or theme scope, and do not shrink task-based or pop-up interactions
  without a user need.
- Reject styling that reaches into private Material DOM, generated class names,
  or unsupported CSS variables. Use supported Sass APIs or token overrides.
- Verify Material harnesses, CDK harnesses, or user-level tests cover controls
  whose DOM should not be asserted directly.
- Confirm shared surfaces record theme and dependency impact when Material/CDK
  enters a new package, route, or bundle.

## Quality Gates

- Every finding names the affected interaction state, theme surface, overlay
  behavior, density scope, or dependency boundary.
- A11y findings include the user action or assistive-technology state that can
  fail.
- Theme findings distinguish supported Material APIs from private implementation
  selectors.

## Finding Triggers

- A Material component is used only for visual styling while behavior belongs to
  local UI or a CDK primitive.
- A custom overlay can trap focus, lose focus restoration, ignore scroll, or fail
  to close through keyboard interaction.
- A theme or density change depends on private selectors or alters global
  Material appearance without naming the affected surfaces.
- Tests assert Material internal DOM instead of a harness or user-observable
  behavior.

## Hard Stops

- Do not approve a dialog, menu, overlay, select, autocomplete, or custom focus
  trap without keyboard and focus evidence.
- Do not accept private Material DOM or CSS selectors as a theming strategy.
- Do not ignore dependency or theme impact when Material/CDK enters a shared
  surface.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
specific Material/CDK interaction, theme, density, dependency, or validation
evidence needed to close it.
