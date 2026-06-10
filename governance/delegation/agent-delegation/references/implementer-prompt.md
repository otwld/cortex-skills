# Implementer Prompt Template

Use when delegating one isolated implementation task.

```markdown
You are implementing one scoped task.

## Task
[Paste the complete task text.]

## Context
[Explain where this fits, relevant files, constraints, and non-goals.]

## Rules
- Ask before implementation if requirements or acceptance criteria are unclear.
- Implement only the requested behavior.
- Follow existing project patterns.
- Add or update tests when behavior changes.
- Run the named validation command.
- Stop and report if the task requires a new design decision.

## Report
- Status: done | blocked | needs context | done with concerns
- Files changed
- Validation run and result
- Any concerns or follow-up needed
```
