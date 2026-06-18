# Purpose

Run the explicit {{command_invocation}} command workflow.

# When To Use

Use this command only when the user directly invokes {{command_invocation}}.

# Workflow

1. Confirm the command was directly invoked.
2. Inspect the workspace state relevant to the command.
3. Apply the command workflow.
4. Validate command output before completion.

# Gates

- This command is public but excluded from routed module selection.

# Hard Stops

- Do not select this command through heuristic routing.

# Output Format

Report the command result and validation evidence.

# Checklist

- Direct invocation was present.
- Routed cascade did not select this command.
- Validation evidence was stated.

# Cross References

- None
