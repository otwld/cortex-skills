# Example Universe Enforcer Verify

## Overview

Verify that final illustrative examples are coherent, minimal, and free of
generic placeholders.

## Workflow

1. Scan changed example artifacts for placeholder names, unrelated invented
   domains, and oversized fixtures.
2. Compare recruitment examples against `references/recruitment-universe.md` for
   entity names and required relationships.
3. Confirm each sample field, record, or story state contributes to the behavior
   being demonstrated.
4. Confirm real user-provided data remains unchanged unless the task explicitly
   requested anonymization or transformation.
5. Record any accepted exception and the user or project evidence that justifies
   it.

## Quality Gates

- No invented durable example uses generic placeholders or a mixed sample domain.
- Recruitment examples use Candidate, JobOffer, Application, Recruiter, Company,
  Interview, Contract, or SkillTag coherently.
- Remaining exceptions are explicit and tied to real task context.

## Hard Stops

- Do not finish while known placeholder examples remain unmentioned.
- Do not treat a broad search for placeholder names as sufficient when entity
  relationships were also changed.
- Do not expand fixtures during verification unless the behavior cannot be proven
  by smaller data.

## Phase Output

- Return the scans or manual checks performed, artifacts inspected, remaining
  exceptions, and any placeholder or domain-coherence gap.
