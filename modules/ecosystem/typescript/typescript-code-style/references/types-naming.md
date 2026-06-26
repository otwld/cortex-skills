# Types And Naming

Operational transformation of the Google TypeScript Style Guide sections on naming and the type system.

## Contents

- Identifier rules
- Casing by identifier type
- Constants and aliases
- Type inference and return types
- Null and undefined
- Structural typing and interfaces
- Array and dictionary types
- Mapped and conditional types
- `any`, `unknown`, `{}`, tuples, wrappers, generics

## Identifier Rules

- Use ASCII letters, digits, underscores, and rare framework-required `$`.
- Do not encode type information in names when TypeScript already expresses it.
- Do not use leading or trailing underscores for private members.
- Do not use `opt_` for optional parameters.
- Do not prefix interfaces with `I` or suffix them with `Interface` unless required by the surrounding ecosystem.
- If an interface exists alongside a class, name it for its purpose rather than the fact that it is an interface.
- Observable `$` suffixes are allowed when they are a consistent project convention and improve clarity.
- Names must be descriptive to a new reader.
- Avoid ambiguous abbreviations and abbreviations formed by deleting letters inside words.
- Very short names are acceptable only for values scoped to a few lines, such as local loop variables or private helper parameters.
- Treat acronyms as words in camel case: `loadHttpUrl`, not `loadHTTPURL`, unless a platform name requires otherwise.

## Casing By Identifier Type

| Style | Use for |
| --- | --- |
| `UpperCamelCase` | Classes, interfaces, type aliases, enums, decorators, type parameters, TSX component functions, `JSXElement` type parameters. |
| `lowerCamelCase` | Variables, parameters, functions, methods, properties, module aliases. |
| `CONSTANT_CASE` | Module-level constant values, enum values, static readonly constants on module-level classes. |
| `#ident` | Do not use; ECMAScript private identifiers are disallowed. |

Type parameters may be a single uppercase letter such as `T` or a descriptive `UpperCamelCase` name.

xUnit-style test names may use underscores for structured scenarios, such as `testSave_whenOffline_retries()`.

Do not use `_` by itself to mean an unused parameter. If destructuring an array or tuple, skip unused positions with extra commas.

## Imports, Constants, And Aliases

Namespace imports are `lowerCamelCase` even when file names use `snake_case`:

```ts
import * as candidateEvents from './candidate_events';
```

Project exceptions may exist for extremely common external conventions, such as jQuery `$` or Three.js `THREE`.

Use `CONSTANT_CASE` only for module-level constants, enum values, and static readonly constants on module-level classes. A value can be technically mutable but named as constant to communicate "do not mutate this".

Do not use `CONSTANT_CASE` for local values created repeatedly over a program's lifetime.

When creating a local alias of an existing symbol, keep the original symbol's naming style. Use `const` for local aliases and `readonly` for class-field aliases.

If a class-field alias exists only to expose a symbol to a framework template, apply the correct access modifier for that framework-visible usage.

## Type Inference

Rely on TypeScript inference when the type is obvious:

- String, number, boolean, and RegExp literals.
- `new` expressions where the constructed type is clear.
- Simple local expressions that do not hide important information.

Add explicit types when they improve readability, prevent `unknown` inference for empty generic containers, or surface future type errors closer to the declaration.

```ts
const ids = new Set<string>();
const rows: readonly CandidateReportRow[] = await recruiterReportClient.loadRows();
```

Return type annotations are optional by default. Add them when a return type is complex, exported, important documentation, or likely to drift during refactors. Respect stricter local project policies.

## Null And Undefined

- Use `null` or `undefined` according to API context. There is no universal preference.
- Do not define aliases that include `|null` or `|undefined`.
- Add `|null` or `|undefined` at the usage site where absence actually occurs.
- Prefer optional parameters and optional fields over spelling `|undefined`.
- For classes, prefer initializing fields over keeping them optional when possible.

```ts
type ApplicationOutcome = ApplicationAccepted | ApplicationRejected;

function getApplicationOutcome(): ApplicationOutcome | undefined {
  return cache.get('applicationOutcome');
}

interface CandidateAvailability {
  readonly earliestStartDate?: Date;
}
```

## Structural Types

TypeScript is structurally typed: a value matches an interface if it has the required properties with compatible types.

When creating an object intended to satisfy a structural type, annotate the declaration so errors appear at the object definition rather than later call sites.

```ts
const candidate: Candidate = {
  id: 'candidate_123',
  name: 'Ada Lovelace',
};
```

Use interfaces to define structural object types. Do not use classes merely as structural type declarations.

## Interfaces Over Type Literal Aliases

Use `interface` for named object shapes:

```ts
interface CandidateSummary {
  readonly displayName: string;
  readonly primarySkill?: string;
}
```

Use type aliases for unions, primitives, tuples, function signatures where that is clearer, and repeated non-object expressions.

Prefer interfaces because they are conventional for object shapes, easier for tooling to display, and usually better for long-term refactoring.

## Array Types

For simple element types containing only alphanumeric names and dot-qualified names, use shorthand:

- `string[]`
- `readonly string[]`
- `candidateNs.Candidate[]`
- `string[][]`

For complex element types, use long form:

- `Array<{id: string; name: string}>`
- `Array<string | number>`
- `ReadonlyArray<string | number>`

Apply the rule at each nesting level. A simple array nested inside a complex generic can still use shorthand, such as `InjectionToken<string[]>`.

## Index Signatures And Dictionaries

Objects used as string-keyed dictionaries may use index signatures:

```ts
const applicationCounts: {[stageName: string]: number} = {};
```

Give index signature keys meaningful labels for documentation.

Prefer `Map` and `Set` when their semantics fit. They communicate intent, avoid object-prototype surprises, and can use non-string keys.

Use `Record<Keys, Value>` when the key set is statically known. Do not confuse `Record` with open-ended dictionary objects.

## Mapped And Conditional Types

Use the simplest type construct that expresses the code.

Mapped and conditional types are allowed, including built-ins such as `Record`, `Partial`, `Readonly`, and `Pick`, but they make readers mentally evaluate types and can weaken tool support.

Prefer explicit interfaces, interface extension, or small duplicated property lists when that improves readability and refactorability.

Use advanced type operators when they remove real duplication or preserve a relationship that would otherwise become incorrect by hand.

## `any`

Avoid `any`. It defeats type checking and can hide serious bugs.

Before using `any`, try:

- A declared interface for structured data.
- An inline object type for a local one-off shape.
- A union or type alias for repeated alternatives.
- A generic that represents caller-provided values.
- `unknown` for opaque values that must be narrowed before use.

When `any` is legitimate, such as a partial mock in a narrow test, suppress the lint warning as locally as possible and document why the unsafety is acceptable.

## `unknown`

Use `unknown` for values whose type is not known yet. It accepts any assigned value but requires narrowing before property access or calls.

Use type guards, `instanceof`, discriminants, schema validation, or runtime checks to narrow `unknown`.

## Avoid `{}` For Opaque Values

The `{}` type means any non-nullish value. That includes primitives and functions, and it usually communicates less than intended.

Prefer:

- `unknown` for any opaque value, including `null` and `undefined`.
- `Record<string, T>` for dictionary objects.
- `object` for non-nullish objects/functions while excluding primitives.

## Tuples

Use tuple types for small positional returns where positions are obvious:

```ts
function splitApplicationPair(input: string): [string, string] {}
```

If property names would improve readability, use an object type or interface instead.

## Wrapper Types

Never use `String`, `Boolean`, `Number`, or `Object` as types for normal values. Use `string`, `boolean`, `number`, `object`, `unknown`, or a better structured type.

Never instantiate primitive wrappers with `new`.

## Return-Type-Only Generics

Avoid APIs whose generic parameter appears only in the return type. They let callers assert an arbitrary return type without evidence.

When using an existing API with return-type-only generics, explicitly specify the type argument so the assertion is visible at the call site.
