
# Output Marker

Display:
using skill: project-memory-setup

---

# Project Memory Setup

## Overview

This explicit command runs only when directly invoked as `$project-memory-setup`.


Establish durable project memory so agents can use shared language, decisions, and
tracker rules.

## Reference Routing

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

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the command skill changes behavior or workflow.

## Example

Configure GitHub labels for needs-triage and ready-for-agent while keeping actual label
strings project-specific.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this command skill's checklist.

## Usage Checklist

- Trigger signal is explicit.
- Relevant existing convention or memory was checked.
- Command-specific rules were applied.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining decisions, risks, or validation gaps are stated.

## Cross References

- None
