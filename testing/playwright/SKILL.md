---
name: playwright-conventions
description: Use when creating, modifying, or reviewing Playwright configuration, browser projects, end-to-end tests, locators, assertions, fixtures, or setup projects.
---

# Output Marker

Display:
using skill: playwright-conventions

---

# Playwright Conventions

## Overview

Prefer user-visible behavior, resilient locators, and web-first assertions in
Playwright tests.

## Core Rules

- Use Playwright config for shared browser, timeout, reporter, and project settings.
- Prefer role, label, text, and test-id locators over brittle CSS selectors.
- Prefer web-first assertions such as visibility, URL, text, and accessibility state.
- Use setup projects or fixtures for repeated authentication and environment setup.
- Keep tests independent and avoid relying on execution order.

## Usage Checklist

- Tests use resilient locators.
- Assertions wait through Playwright's web-first expectations.
- Setup is shared through fixtures or setup projects.
- Tests can run independently.

## Cross-References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
