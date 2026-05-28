# Comments, Tooling, And Policy

Operational transformation of the Google TypeScript Style Guide sections on toolchain expectations, comments, documentation, and style policy.

## Contents

- Compiler and conformance
- `@ts-` directives
- JSDoc and ordinary comments
- JSDoc formatting and tags
- Documentation expectations
- Parameter comments
- Decorators and documentation
- Consistency and reformatting policy
- Deprecation and generated code
- Style goals

## Compiler And Conformance

- TypeScript source must pass the project's standard typecheck.
- Treat typecheck failures as design feedback, not as noise to suppress.
- Follow applicable project conformance frameworks, lint rules, security rules, and framework-local restrictions.
- In Google-style environments, this can include tsetse, tsec, or equivalent conformance checks for globals, security-sensitive APIs, and framework restrictions.
- When this skill conflicts with local automated tooling, preserve the user's requested behavior and project policy first, then document any meaningful style tradeoff.

## `@ts-` Directives

Avoid:

- `@ts-ignore`
- `@ts-expect-error`
- `@ts-nocheck`

These suppressions often hide a larger type modeling issue and can cause nearby code to see misleading types.

If a unit test needs to exercise unchecked runtime values, prefer a narrow cast on the specific expression and an explanatory comment. If a directive is unavoidable under local policy, make it as narrow as possible and explain the exact reason.

## JSDoc Versus Ordinary Comments

Use JSDoc (`/** ... */`) for API documentation that users of a symbol should read in editors or generated docs.

Use `//` comments for implementation notes that explain internal reasoning.

For multi-line implementation comments, indent comments at the same level as the surrounding code and use multiple `//` lines rather than block comments. Do not create decorative boxed comments.

## JSDoc General Form

Use standard JSDoc blocks:

```ts
/**
 * Schedules an interview for an application.
 * @param startsAt Must fit the recruiter's availability window.
 */
function scheduleInterview(startsAt: Date) {}
```

Single-line JSDoc is fine when it stays short:

```ts
/** Returns the currently selected job offer. */
export function getSelectedJobOffer() {}
```

If a single-line JSDoc would wrap, use the multi-line form.

JSDoc is Markdown. Use real Markdown lists, paragraphs, and code spans instead of relying on plain-text spacing that renderers will collapse.

Keep JSDoc well-formed because editors, documentation generators, validators, and optimization tools may extract metadata from it.

## JSDoc Tags And Wrapping

- Most JSDoc tags occupy their own line.
- Do not combine multiple `@param` tags on one line.
- Wrapped block tag text is indented four spaces.
- Avoid visual alignment that exists only to line up columns.
- Do not indent wrapped `@desc` or `@fileoverview` text.
- Do not write TypeScript types in JSDoc tags for TypeScript source.
- Do not duplicate TypeScript keywords in JSDoc, such as `@private`, `@override`, `@implements`, or `@enum`, when the code already uses the corresponding syntax.

## Documentation Expectations

- Document all top-level exported symbols unless they are exported only for tooling that already documents their use.
- Document public APIs with enough information for a caller to know when and how to use them.
- Document properties and methods whose purpose is not obvious from name and type.
- Class comments should explain how and when to use the class, plus any constraints or lifecycle notes.
- Constructor descriptions may be omitted when the class documentation and parameter names are sufficient.
- Method and function descriptions should begin with a third-person verb phrase, as if preceded by "This method ...".
- Omit `@param` and `@return` text when it would merely restate a name or obvious type.
- Add parameter or return descriptions when they include constraints, units, side effects, failure modes, or non-obvious behavior.

## Parameter Property Comments

Constructor parameter properties declare both a parameter and a field. Document them with constructor `@param` tags when documentation is useful:

```ts
class InterviewScheduler {
  /**
   * @param calendar Provides available recruiter interview slots.
   */
  constructor(private readonly calendar: InterviewCalendar) {}
}
```

## Comments At Call Sites

Use parameter-name comments when a call's argument values are not self-explanatory:

```ts
scheduleInterview(application, /* shouldNotifyCandidate= */ true, /* recruiterNote= */ 'onsite loop');
```

Before adding parameter comments, consider whether the function should instead accept an options object.

Existing files may use the legacy trailing style for consistency:

```ts
scheduleInterview(application, true /* shouldNotifyCandidate */, 'onsite loop' /* recruiterNote */);
```

## Documentation Before Decorators

When a declaration has decorators and JSDoc, put JSDoc before the decorator:

```ts
/** Displays candidate interview activity. */
@Component({selector: 'candidate-interview-activity'})
export class CandidateInterviewActivityComponent {}
```

Do not put JSDoc between the decorator and the decorated declaration.

## Consistency Policy

For style questions not settled by this skill:

1. Match the surrounding file.
2. If the file is inconclusive, match nearby files in the same directory or package.
3. If still unclear, choose the clearer and more maintainable option.

New files should follow this skill fully unless project tooling or local instructions differ.

When changing an existing non-conforming file, do not mix large opportunistic style cleanup into focused functional changes. If broad style cleanup is valuable, separate it from behavioral edits.

If a change is substantial, it is reasonable to bring the touched file closer to this style, provided the diff remains reviewable.

## Deprecation

Mark deprecated classes, methods, interfaces, and exported values with `@deprecated`.

The deprecation comment must include clear migration guidance for callers.

## Generated Code

Generated code is mostly exempt from hand-written style. Do not hand-edit generated output just to satisfy this guide.

Generated identifiers that are referenced by hand-written code should still follow naming rules where the generator can reasonably enforce them. Generated identifiers may use underscores when needed to avoid collisions.

## Style Goals

Use global rules to avoid known footguns, reduce irrelevant variation, support automated refactoring, preserve long-term maintainability, and keep reviews focused on code quality.

Do not invent extra rules for obscure cases with low bug risk. When a rule can be enforced mechanically, prefer project tooling over repeated human debate.
