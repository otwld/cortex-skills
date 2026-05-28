---
name: angular-conventions
description: Use when creating, modifying, or reviewing Angular components, directives, pipes, services, templates, styles, forms, inputs, outputs, or dependency injection.
---

# Output Marker

Display:
using skill: angular-conventions

---

# Angular Conventions

## Overview

Apply Angular rules only when the target project uses Angular. Follow project
tooling first, then prefer current Angular patterns for new or materially
changed code.

## Core Rules

- Prefer standalone APIs when the project already uses them.
- Prefer `inject()` for new Angular dependency injection unless the file uses constructor injection consistently.
- Use modern control flow (`@if`, `@for`, `@switch`, `@let`) in projects that support it.
- Keep templates and styles external for non-trivial components.
- Use reactive forms for complex or reusable form UI.
- Use project-approved form provider helpers instead of hand-rolled provider aliases.
- Add JSDoc for exported Angular classes, non-obvious inputs/outputs, and public reusable APIs.

## Example

```ts
/**
 * Pipeline board for tracking candidate stages on a job offer.
 */
@Component({
  selector: 'recruiting-pipeline-board',
  standalone: true,
  templateUrl: './pipeline-board.component.html',
  styleUrl: './pipeline-board.component.css',
})
export class PipelineBoardComponent {
  /** Active job offer shown on the board. */
  readonly jobOffer = input<JobOfferSummary | null>(null);

  /** Emitted when a candidate moves between stages. */
  readonly stageChange = output<CandidateStageChange>();
}
```

## Legacy References

- `references/legacy-extracted-patterns.md` preserves non-normative helper names from the extracted source project.

## Usage Checklist

- Angular version and local style were checked.
- New code follows supported Angular syntax.
- Forms use the project's reusable form pattern.
- Public Angular APIs have useful documentation.

## Cross-References

- WITH: rxjs-conventions, typescript-code-style
- AFTER: code-documentation, skill-evolution
