# Condition Based Waiting

Use for flaky async tests or workflows that rely on guessed delays.

## Principle

Wait for the condition that proves readiness, not for an arbitrary amount of
time.

## Patterns

- Wait for an event to appear.
- Wait for state to become ready.
- Wait for a count or queue length.
- Wait for a file or resource to exist.
- Wait for a predicate that combines several observable facts.

## Rules

- Include a timeout with an error message that names the missing condition.
- Poll at a reasonable interval instead of spinning continuously.
- Read fresh state inside the polling loop.
- Use fixed sleeps only when testing time itself, and document the timing basis.

## Warning

Increasing timeouts without identifying the condition usually hides the race
instead of fixing it.
