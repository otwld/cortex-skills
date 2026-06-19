
# Output Marker

Display:
using module: storybook-conventions

---

# Storybook Conventions

## Overview

Use Storybook to make behavior reviewable outside the application.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Cover meaningful states; use stable fixtures; mock at boundaries; write MDX for setup constraints; avoid random or live data.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Stories demonstrate meaningful states, edge cases, and setup constraints for the public component surface.
- Fixtures are deterministic, minimal, and consistent with recruitment-domain examples when examples are invented.
- MDX, addons, mocks, and visual-regression data stay scoped to story behavior.

## Example

JobOfferCard stories show draft, published, expired, and no-applications states with
fixed dates.

## Hard Stops

- Do not write stories that only mirror default props without showing behavior.
- Do not use random, live, or environment-dependent data in stories.
- Do not move product documentation into Storybook when another docs surface owns it.

## Usage Checklist

- Existing story organization, fixtures, addons, and docs surface were inspected.
- Meaningful component states and setup constraints are represented.
- Storybook validation or visual-review gap was recorded.

## Cross References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
