---
name: setup-project-memory
description: Use only when the user explicitly includes $setup-project-memory; sets up or verifies project-memory artifacts such as domain glossary, ADR location, out-of-scope decisions, issue tracker config, or triage label mapping.
---


# Setup Project Memory

## Overview

This command skill runs only when directly invoked as `$setup-project-memory`.


Establish durable project memory so agents can use shared language, decisions, and
tracker rules.

## Local Inputs

- Use `shared/project-memory.md` when this task touches that concern.
- Use `shared/issue-tracker-setup.md` when this task touches that concern.
- Use `shared/out-of-scope-decisions.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this command skill governs.
3. Apply the command-specific rules: Inspect existing files; choose single or multi-context shape; create files lazily; support GitHub, GitLab, or local markdown; map labels.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this command skill's scope and ask for the missing decision.

## Quality Gates

- Project-memory guidance names the inspected files or explicit user decision that justifies each memory artifact.
- Glossary, ADR, out-of-scope, and tracker guidance uses this workspace's terms and the recruitment example universe only when examples are needed.
- Durable decisions are written to the selected memory artifact instead of remaining only in chat.
- Validation names the created or verified memory file and any unresolved user decision.

## Example

Configure GitHub labels for needs-triage and ready-for-agent while keeping actual label
strings project-specific.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this command skill's checklist.

## Completion Checklist

- Direct `$setup-project-memory` invocation is explicit.
- Existing glossary, ADR, out-of-scope, tracker, and label memory was checked.
- Project-memory setup rules were applied to the selected artifact shape.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining memory decisions, ownership questions, or validation gaps are stated.

## Source Artifacts

- None
