# Angular Conventions Activate

## Overview

Decide whether Angular conventions apply and capture the local evidence needed
prior to Angular code changes.

## Workflow

1. Match the request or diff to Angular artifacts listed in Trigger Evidence.
2. Inspect local Angular versions, compiler settings, and same-feature code.
3. Identify the public template, form, service, or provider boundary affected.
4. Decide whether local style or a requested Angular API migration governs the
   change.
5. Return any blocked API, typing, or validation decision instead of guessing.

## Trigger Evidence

Activate for requests or diffs that touch Angular components, directives, pipes,
services, templates, styles, forms, inputs, outputs, dependency injection, or
template-facing tests.

Do not activate for plain TypeScript code that has no Angular decorator,
template binding, provider, or Angular test surface.

## Inspect

- Angular package versions and compiler strictness in `package.json`,
  `angular.json`, project config, and `tsconfig*`.
- Nearby same-feature files for standalone imports, NgModule usage, template and
  style file placement, provider scope, and dependency-injection style.
- The public template contract: selector, inputs, outputs, model values,
  exported services, and form controls consumed outside the class.
- Existing tests, stories, or docs that exercise the affected component
  behavior.

## Decisions

- Use the local Angular style unless the requested change is explicitly a
  migration to a newer supported Angular API.
- Prefer `inject()` and function-based `input()` or `output()` for new code only
  when local code and installed Angular version already support that style.
- Keep complex template expressions in TypeScript, usually as typed computed or
  protected template members.
- Treat forms as part of the public component contract when their value shape,
  validation, or submission behavior is consumed elsewhere.

## Quality Gates

- Local Angular version and compiler strictness are known when API choice depends
  on them.
- The affected selector, input, output, model value, form shape, or provider
  lifetime is named.
- The phase identifies the local style for standalone imports, templates, forms,
  and dependency injection.

## Hard Stops

- Angular dependencies or version support cannot be established and the task
  requires version-sensitive APIs.
- The requested change alters a selector, input, output, model value, provider
  scope, or form value shape without enough product or API expectation.
- The implementation plan relies on `$any`, untyped forms, broad `any`, or
  non-null assertions to bypass Angular template or form checking.

## Phase Output

Return the matched Angular evidence, the affected public boundary, the local
style decision, and any blocked API or validation decision.
