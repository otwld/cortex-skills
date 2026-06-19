
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

- Storybook Conventions guidance names the inspected source, request evidence, or declared resource that triggered it.
- Storybook Conventions output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Storybook Conventions decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Storybook Conventions validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

JobOfferCard stories show draft, published, expired, and no-applications states with
fixed dates.

## Hard Stops

- Do not use Storybook Conventions without direct routing evidence or a required relation.
- Do not expand Storybook Conventions beyond its stated responsibility.
- Do not add placeholder Storybook Conventions guidance, examples, metadata, resources, or validation.
- Do not claim Storybook Conventions is satisfied without evidence for its checklist.

## Usage Checklist

- Storybook Conventions trigger evidence is explicit.
- Storybook Conventions source files, project memory, or declared resources were checked.
- Storybook Conventions workflow rules were applied at the relevant artifact boundary.
- Storybook Conventions docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Storybook Conventions risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
