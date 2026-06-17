---
name: vite-conventions
description: Internal Cortex module applied when creating, modifying, or reviewing Vite configuration, library builds, aliases, plugins, source maps, dependency externalization, or dev-server settings.
---

# Output Marker

Display:
using module: vite-conventions

---

# Vite Conventions

## Overview

Treat Vite config as a build contract for dev speed and published output.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Keep aliases aligned with public entry points; externalize peers for libraries; preserve source maps intentionally; document plugin order when important.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

A Candidate UI package externalizes framework peers instead of bundling runtime into the
library output.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this module's checklist.

## Usage Checklist

- Trigger signal is explicit.
- Relevant existing convention or memory was checked.
- Module-specific rules were applied.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining decisions, risks, or validation gaps are stated.

## Cross-References

- WITH: bundle-performance, typescript-code-style, code-documentation
- AFTER: skill-evolution
