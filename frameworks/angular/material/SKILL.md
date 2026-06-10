---
name: angular-material-conventions
description: Use when adding, modifying, or reviewing Angular Material or Angular CDK components, utilities, theming, overlays, accessibility, or density settings.
---

# Output Marker

Display:
using skill: angular-material-conventions

---

# Angular Material And CDK Conventions

## Overview

Use Angular Material and CDK deliberately. Keep imports narrow, preserve
accessibility defaults, and avoid hiding large dependency costs in shared paths.

## Core Rules

- Import only the Material/CDK modules that are actually used.
- Use CDK primitives for custom overlay, portal, a11y, drag-drop, and virtual-scroll behavior.
- Do not disable accessibility behavior to simplify implementation.
- Centralize theming through the project's Material theming approach.
- Treat density reductions as user-experience decisions that need justification.

## Usage Checklist

- Imports are scoped to used components.
- CDK primitives are used instead of custom low-level behavior where appropriate.
- Theming changes are centralized.
- Accessibility remains intact.
- Bundle impact is considered for reusable UI.

## Cross-References

- BEFORE: angular-conventions
- WITH: bundle-performance, typescript-code-style, code-documentation
- AFTER: skill-evolution
