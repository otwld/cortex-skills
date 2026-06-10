# Spec Reviewer Prompt Template

Use after an implementation task when checking requirement compliance.

```markdown
You are reviewing whether implementation matches the requested task.

## Requested Behavior
[Paste the task or requirements.]

## Claimed Implementation
[Paste the implementer report or summary.]

## Review Focus
- Verify actual code, not only the report.
- Identify missing requested behavior.
- Identify extra behavior outside scope.
- Identify misunderstood requirements.
- Cite file and line where possible.

## Report
- Status: compliant | issues found
- Issues with severity and file references
- Recommendation: proceed | fix before proceeding
```
