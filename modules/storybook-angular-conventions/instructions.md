
# Output Marker

Display:
using module: storybook-angular-conventions

---

# Storybook Angular Conventions

## Overview

Use Angular Storybook as executable documentation for component states and provider
contracts.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Match standalone or module setup; keep args typed; mock dependencies at the story boundary; use deterministic recruitment data.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Angular stories match standalone or module-based setup used by the component under test.
- Args, providers, mocks, and decorators are typed and scoped to the story boundary.
- Recruitment-domain story data covers meaningful Angular states without live services.

## Example

CandidateCard stories cover shortlisted, rejected, and interview-scheduled states with
stable Candidate fixtures.

## Hard Stops

- Do not use Storybook providers to hide missing component dependencies or incorrect Angular setup.
- Do not make Angular stories depend on live APIs, random data, or shared mutable state.
- Do not duplicate Storybook core guidance instead of addressing Angular-specific setup.

## Usage Checklist

- Component setup mode, providers, args, and dependency mocks were inspected.
- Stories cover meaningful Angular states with deterministic recruitment data.
- Storybook command, visual check, or validation gap was named.

## Cross References

- BEFORE: storybook-conventions, angular-conventions
- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
