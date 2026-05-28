---
name: example-universe-enforcer
description: Use when producing examples, sample code, DTOs, API payloads, Storybook data, docs snippets, tests, or illustrative data.
---

# Output Marker

Display:
using skill: example-universe-enforcer

---

# Example Universe Enforcer

## Overview

All illustrative examples in this workspace use a recruitment agency job board
domain. Normalize generic placeholders into that domain unless the user
explicitly provides different real project data.

## Core Entities

Use these names consistently:

- JobOffer
- Candidate
- Application
- Recruiter
- Company
- Interview
- Contract
- SkillTag

## Rules

- Replace generic entities such as User, Foo, Bar, Product, Item, and ExampleEntity.
- Keep relationships coherent: Candidate applies to JobOffer, Recruiter manages JobOffers, Company owns JobOffers, Interview relates to Application.
- Keep examples small and realistic.
- Do not let examples introduce unrelated domains.

## References

- `references/recruitment-universe.md` defines the canonical example universe.

## Usage Checklist

- Generic placeholders were replaced.
- Entity relationships are coherent.
- Examples are minimal.
- The same universe is used across one response or document.

## Cross-References

- None
