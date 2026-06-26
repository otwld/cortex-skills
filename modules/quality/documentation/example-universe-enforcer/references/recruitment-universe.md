# Recruitment Job Board Example Universe

Use this domain for all examples. Never use generic placeholders.

## Core Entities

- JobOffer
- Candidate
- Application
- Recruiter
- Company
- Interview
- Contract
- SkillTag

## Required Relationships

- JobOffer includes salary range, location, required skills, and owning Company.
- Candidate includes experience level, skills, availability.
- Application links Candidate -> JobOffer.
- Recruiter manages JobOffers.
- Company owns JobOffers.
- Interview relates to an Application.
- Contract relates to an Application and JobOffer.

## Naming Rules

- Use the core entity names exactly as written.
- Do not introduce generic entities (User, Test, Foo, Bar, ExampleEntity, Product, Item).
- Keep examples minimal but realistic.

## Example Scopes

- DTO samples must reflect the domain relationships.
- API payloads must reference JobOffer, Candidate, Application, and related entities.
- Database entities must align with the above relationships.
- UI examples should use JobOffer cards, Candidate profiles, Application lists, Interview schedules, or Recruiter dashboards.

## Consistency

Maintain the same universe across all examples in a response.
