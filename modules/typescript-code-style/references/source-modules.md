# Source Files And Modules

Operational transformation of the Google TypeScript Style Guide sections on file basics, file structure, imports, exports, type-only imports, and modules.

## Contents

- Normative language
- Source file basics
- File structure
- Imports
- Exports
- Type-only imports and exports
- Modules instead of namespaces

## Normative Language

- Treat `must` and imperative statements as required.
- Treat `should`, `prefer`, and `avoid` as strong defaults unless project context justifies an exception.
- Treat examples as illustrative, not as extra formatting law.

## Source File Basics

- Encode source files as UTF-8.
- Use the ASCII horizontal space character for ordinary spacing. Do not introduce tabs or invisible Unicode whitespace.
- In string literals, use special escape sequences such as `\n`, `\t`, `\\`, `\"`, and `\'` instead of numeric escapes when such a named escape exists.
- Never use legacy octal escapes.
- For printable non-ASCII text, prefer the actual character when it is clearer to readers.
- For non-printable characters, use a hex or Unicode escape and add a short comment explaining the character.

## File Structure

Keep each file in this order, with exactly one blank line between present sections:

1. License or copyright block, if required.
2. `@fileoverview` JSDoc, if useful.
3. Imports.
4. Implementation.

Use a top-of-file JSDoc block for license or copyright content when the file needs it.

Use `@fileoverview` only when it adds useful context about the file's purpose, dependencies, or unusual behavior. Wrapped `@fileoverview` text should not be indented for visual alignment.

## Imports

Use import paths for TypeScript code:

- Relative paths such as `./candidate` and `../job-offer/candidate`.
- Project-root paths only when the project convention supports them.
- Relative imports for files in the same logical project so code can move without path churn.
- Avoid excessive `../../../` chains by reconsidering package boundaries or local barrel files where the project already uses them.

Use these import forms deliberately:

| Import form | Use |
| --- | --- |
| `import {Thing} from './thing';` | Preferred for clear, frequently used symbols. |
| `import * as thingApi from './thing_api';` | Good for large APIs or generic symbol names that benefit from namespacing. |
| `import Thing from 'external-package';` | Only for external code that requires a default import. |
| `import './side_effect';` | Only for real load-time side effects such as registration. |

Prefer named imports when symbols are clear at the call site. Alias named imports when an external or generated name is unclear, collides, or needs a project-local name:

```ts
import {from as observableFrom} from 'rxjs';
```

Prefer namespace imports for broad APIs or names like `Model`, `Controller`, or `State` that become more readable with a module qualifier:

```ts
import * as candidateTable from './candidate_table';

const row: candidateTable.Row = buildCandidateRow();
```

Do not hide poor naming with a long list of aliases. Prefer a namespace import or fix exported names when you own the source module.

For Google Apps JSPB proto imports, use named imports even if the import line becomes long, because this improves dependency precision and dead-code elimination.

## Exports

Use named exports in owned TypeScript:

```ts
export class InterviewScheduler {}
export function createInterviewScheduler() {}
export const DEFAULT_INTERVIEW_DURATION_MINUTES = 45;
```

Do not introduce default exports in owned code. Default exports have no canonical imported name, reduce refactor safety, and encourage artificial container objects.

Minimize exported API surface. Export only symbols that are needed outside the module.

Do not export mutable bindings:

```ts
// Avoid.
export let currentCandidate = undefined;

// Prefer.
let currentCandidate: Candidate | undefined;
export function getCurrentCandidate() {
  return currentCandidate;
}
```

When a value is conditional, compute it first and export a final binding:

```ts
const selectedNotificationClient = useMock() ? mockNotificationClient : liveNotificationClient;
export const notificationClient = selectedNotificationClient;
```

Do not create static-only container classes just to simulate namespaces. Use file scope and named exports:

```ts
export const INTERVIEW_RETRY_LIMIT = 3;
export function calculateInterviewReminderBackoff(attempt: number) {}
```

## Type-Only Imports And Exports

Use `import type` when a symbol is used only in type positions:

```ts
import type {ApplicationRequestContext} from './application_request_context';
import {createLogger} from './logger';
```

Inline `type` specifiers are also fine when a module provides both type and value imports:

```ts
import {type ApplicationRequestContext, createLogger} from './logger';
```

Use a regular import for runtime values. If a module must be loaded for side effects, use an explicit side-effect import.

Use `export type` for type re-exports:

```ts
export type {ApplicationRequestContext} from './application_request_context';
```

`export type` helps file-by-file transpilation and `isolatedModules`, but it is not an API boundary by itself. If callers must not treat something as both a value and a type, split the API into distinct symbols with clear names.

## Modules Instead Of Namespaces

Use ES modules with `import` and `export`.

Do not use TypeScript `namespace` or legacy `module CandidateModule {}` declarations in ordinary code. Use separate files and exports for namespacing.

Do not use triple-slash references in source files.

Do not use `import x = require('pkg')` or `require()` for TypeScript imports. Use ES module syntax.

Namespaces are only acceptable for required interop with third-party declarations that force that shape.
