# Example Universe Enforcer Activate

## Overview

Identify tasks that create or review invented examples so they use the workspace
recruitment job board universe consistently.

## Workflow

1. Match this module when the request or diff creates sample code, DTOs, API
   payloads, fixtures, test data, Storybook data, docs snippets, or illustrative
   records.
2. Load `references/recruitment-universe.md` for invented examples or sample
   data.
3. Distinguish invented examples from real user-provided project data; preserve
   real data when it is the subject of the task.
4. Identify any generic placeholders or unrelated sample domains already present
   in the target artifact.

## Quality Gates

- Activation evidence names the example artifact or requested sample output.
- The reference is used only for illustrative data, not to rewrite real project
  facts supplied by the user.
- Existing placeholder names or mixed domains are captured for correction.

## Hard Stops

- Do not activate for production domain modeling when no illustrative examples
  are being created or reviewed.
- Do not replace user-provided real entities with recruitment examples.
- Do not accept generic placeholder names as harmless when they are part of a
  durable artifact.

## Phase Output

- Return the example surfaces found, whether they are invented or user-provided,
  the reference loaded, and the placeholder or domain-coherence risks to check.
