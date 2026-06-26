# Angular Material Conventions Activate

## Overview

Decide whether Material/CDK conventions apply and capture the interaction,
theme, and accessibility evidence needed for the change.

## Workflow

1. Match the request or diff to a Material/CDK import, selector, Sass API,
   provider, harness, or interaction.
2. Inspect installed Material/CDK versions, theme entry points, and local UI
   ownership for the affected surface.
3. Identify focus, keyboard, label, overlay, density, theme, and dependency
   consequences.
4. Decide whether Material, CDK, or an existing local component owns the
   interaction.
5. Return required a11y, theme, density, overlay, and dependency constraints.

## Trigger Evidence

Activate for requests or diffs that touch `@angular/material`, `@angular/cdk`,
Material Sass theming, density settings, overlays, dialogs, menus, tooltips,
focus management, live announcements, or Material component harnesses.

Do not activate merely because the project uses Angular. The request must touch
a Material/CDK import, selector, provider, style API, test harness, or UI
interaction normally owned by Material/CDK.

## Inspect

- Installed `@angular/material` and `@angular/cdk` versions plus the existing
  global theme, density, typography, focus-indicator, and style entry points.
- Nearby UI surfaces to see whether the project already uses a Material
  component, a CDK primitive, or a local design-system component for this
  interaction.
- Current focus order, keyboard actions, aria labels/descriptions, disabled
  states, and screen-reader announcements for the affected UI.
- Overlay or dialog ownership: origin element, positioning strategy, scroll
  strategy, backdrop behavior, close result, teardown, and focus restoration.
- Whether the change lands in a shared UI package, lazy route, feature shell, or
  global style file where dependency and bundle effects matter.

## Decisions

- Use a Material component when the Material design behavior is the requested
  product surface; use CDK primitives when the behavior is needed but the visual
  design is local.
- Keep theming and density changes in Material-supported Sass APIs or token
  overrides rather than component DOM selectors.
- Treat density below the default as an accessibility decision, not a visual
  cleanup.
- Require harness or keyboard/focus validation for dialogs, menus, overlays,
  form controls, tabs, selects, tooltips, and custom CDK interactions.

## Quality Gates

- The affected Material/CDK API or theme surface is named.
- The interaction owner is chosen from Material, CDK, or local UI.
- Required focus, keyboard, label, theme, density, overlay, and dependency
  checks are explicit.

## Hard Stops

- The change adds Material to a shared surface without identifying the theme and
  dependency impact.
- A dialog, menu, overlay, or focus trap lacks keyboard, focus, and close-state
  expectations.
- The plan depends on styling private Material DOM structure or CSS classes
  instead of supported theming, density, or override APIs.

## Phase Output

Return the matched Material/CDK evidence, chosen owner for the interaction,
accessibility checks required, and any theme, density, overlay, or dependency
constraint.
