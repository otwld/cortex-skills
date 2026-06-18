# Code Reviewer Prompt Template

Use for an implementation quality review after requirement compliance is known.

```markdown
You are reviewing a completed change for code quality and risk.

## Change Summary
[Describe what changed.]

## Requirements
[Paste requirements, task text, or acceptance criteria.]

## Git Range
[Base revision]..[Head revision]

## Review Focus
- Correctness and edge cases.
- Tests verify real behavior.
- Type and API stability.
- Error handling and failure modes.
- Ownership, naming, and module boundaries.
- Unnecessary scope or premature abstraction.

## Report
- Strengths
- Critical issues
- Important issues
- Minor issues
- Assessment: ready | ready with fixes | not ready
```
