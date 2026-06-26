# Language Features

Operational transformation of the Google TypeScript Style Guide sections on JavaScript and TypeScript language feature usage.

## Contents

- Local variables
- Arrays
- Objects
- Classes
- Functions and `this`
- Primitive literals and coercion
- Control structures
- Exceptions
- Assertions
- Decorators
- Disallowed features

## Local Variables

- Use `const` by default.
- Use `let` only for reassignment.
- Never use `var`.
- Do not use variables before declaration.
- Declare one local variable per declaration.

```ts
const candidate = loadCandidate();
let retryCount = 0;
```

## Arrays

- Do not use `Array()` or `new Array()`. Use literals or `Array.from` when size-based construction is clearer.
- If code specifically needs an array with empty slots, create `[]` and assign `length` explicitly rather than using the array constructor.
- Do not attach non-numeric properties to arrays. Use `Map`, `Set`, or an object with a declared shape.
- Use spread syntax for shallow copies or concatenation only when the spread value is iterable.
- Do not spread primitives, `null`, or `undefined` into arrays.
- Use array destructuring for unpacking. Omit unused positions with empty slots and use a final rest element when needed.
- For optional destructured array parameters, default the parameter to `[]` and put element defaults on the left side.
- Prefer object destructuring for multi-value returns or parameters when names would improve readability.

```ts
function normalizeSalaryRange([minimum = 0, maximum = 0] = []) {}
const [primarySkill, , tertiarySkill] = requiredSkills;
```

## Objects

- Do not use the `Object` constructor. Use object literals.
- Avoid unfiltered `for...in`. It includes enumerable prototype properties.
- Prefer `Object.keys`, `Object.values`, or `Object.entries` with `for...of` when possible.
- If `for...in` is necessary, filter with `Object.prototype.hasOwnProperty` or the project's approved equivalent.
- Use object spread only with object values. Avoid spreading arrays, primitives, `null`, `undefined`, class instances, functions, or objects with surprising prototypes.
- Later object spread entries override earlier keys. Put defaults first and overrides later when that order matters.
- Computed object property names are allowed. Treat non-symbol computed keys as dictionary-style keys and do not mix them with ordinary keys casually.
- Keep function parameter object destructuring shallow: one level, unquoted shorthand keys, defaults on the left side, and `{}` as the default for optional object parameters.
- Do not use nested or computed property destructuring in parameters.

```ts
interface CandidateListOptions {
  readonly pageSize?: number;
  readonly emptyLabel?: string;
}

function listCandidates({pageSize = 20, emptyLabel = 'No candidates'}: CandidateListOptions = {}) {}
```

## Classes

- Do not add semicolons after class declarations.
- Do add semicolons after statements that contain class expressions.
- Do not separate class methods with semicolons.
- Separate methods, constructors, and surrounding field groups with a single blank line when it improves scanning.
- `toString()` may be overridden only when it always succeeds and has no visible side effects.

### Static Members

- Prefer module-local helper functions over private static methods when readability stays good.
- Do not rely on dynamic dispatch of static methods.
- Call a static method on the class that declares it, not through a subclass that merely inherits it or through a constructor-typed variable.
- If legacy Google-style code must dynamically call a static method through a constructor value, that method requires the local toolchain's preservation annotation such as `@nocollapse`; avoid introducing this pattern in new code.
- Do not use `this` in static methods or static field initializers.
- Avoid substantial static state because it is hard to test and easy to override accidentally.

### Constructors

- Always call constructors with parentheses: `new CandidateCard()`.
- Omit empty constructors and constructors that only delegate to `super(...)`, unless parameter properties, visibility modifiers, parameter decorators, or non-instantiability require the constructor to exist.
- Keep constructors visually separated from fields and methods.

### Fields And Members

- Do not use ECMAScript `#private` fields. Use TypeScript visibility modifiers.
- Mark properties `readonly` when they are not reassigned outside construction.
- Use parameter properties for obvious constructor-to-field plumbing.
- Document parameter properties with `@param` on the constructor when documentation is needed.
- Initialize non-parameter fields where they are declared when practical.
- Avoid adding or deleting instance properties after construction. Initialize delayed optional fields to `undefined` if they will exist later.
- Properties used by templates, decorators, or framework reflection are not lexically private. Use `protected` or `public` as appropriate rather than bypassing privacy with bracket access.
- Angular and AngularJS template-facing properties should generally be `protected`; Polymer template-facing properties should generally be `public`.
- Never use `obj['privateName']` to bypass TypeScript visibility.

### Accessors

- Getters must be pure: no observable state changes and stable results for the same state.
- Use accessors to hide internal details only when at least one accessor does meaningful work.
- Do not create trivial get/set pass-throughs just to hide a property.
- If an accessor hides a backing property, use a descriptive whole-word prefix or suffix such as `internal` or `wrapped`.
- Prefer accessing the value through the accessor rather than the backing field when both exist.
- Do not define accessors with `Object.defineProperty` in ordinary source.

### Class Computed Properties

- Use computed class properties only for symbols, such as `[Symbol.iterator]`.
- Avoid dict-style computed class properties.
- Use built-in symbols sparingly because compiler polyfills may not cover older targets.

### Visibility

- Limit visibility as much as practical.
- Prefer non-exported file-local functions over private methods when the helper does not need class state.
- TypeScript members are public by default. Do not write `public` except for non-readonly public parameter properties where the modifier is part of the declaration.

### Disallowed Class Patterns

- Do not manipulate prototypes directly in ordinary implementation code.
- Do not use mixin/prototype mutation patterns unless framework code forces them and the workaround would be worse.

## Functions And `this`

- Prefer function declarations for named functions.
- Use arrow functions or function declarations for nested functions as appropriate. In methods, arrows are usually better when the nested function needs the outer `this`.
- Do not use function expressions, except for generator functions or the rare case where dynamic `this` rebinding is intentional.
- Use concise arrow bodies only when the return value is actually used.
- Use block arrow bodies when the callback is for side effects.
- Use `void expression` only when it clearly documents an intentionally discarded value.
- Do not use `this` in function declarations or function expressions unless the function has an explicit `this` parameter or exists specifically to rebind `this`.
- Prefer arrows over `.bind(this)`, `const self = this`, and similar patterns.
- Prefer callback arrows that explicitly forward arguments to named functions, especially when a callback API may pass extra optional parameters.
- Avoid passing bare instance method references. Use an arrow at the call site so `this` is clear.
- Classes usually should not contain properties initialized to arrow functions. They make call sites depend on non-local knowledge that the method is already bound.
- Use an arrow function property only when it makes a framework template or removable event-handler pattern clearer and safer than alternatives.

```ts
experienceYears.map(year => parseInt(year, 10));
candidateCard.onclick = () => this.openCandidateProfile();
```

### Event Handlers

- Anonymous arrows are fine when the event source has the same lifetime as the object and removal is unnecessary.
- If a handler must be removed later, store a stable arrow function property and pass the same reference to add/remove calls.
- Do not install event handlers with `this.method.bind(this)` inline because removal will not see the same function reference.

### Parameters, Rest, And Formatting

- Default parameter initializers must be simple and free of observable side effects.
- Avoid shared mutable default values.
- Prefer destructured object parameters when several optional parameters do not have a natural order.
- Use rest parameters instead of `arguments`.
- Do not name variables or parameters `arguments`.
- Use spread syntax instead of `Function.prototype.apply`.
- Do not put a space after `...`.
- Do not leave blank lines at the start or end of a function body.
- Use internal blank lines sparingly to group statements.
- Write generators as `function* name()` and `yield* value`.
- Parentheses around a single arrow parameter are recommended but not required.

## `this`

Use `this` only in:

- Class constructors and methods.
- Functions with an explicit `this` type parameter.
- Arrow functions inside a scope where `this` is allowed.

Never use `this` for the global object, `eval` context, event target context, or unnecessary `call`/`apply` rebinding.

## Primitive Literals And Coercion

### Strings

- Use single quotes for ordinary string literals.
- Use template literals for interpolation and complex concatenation.
- Do not use line continuations in strings or template literals.
- If a long string must remain searchable as one literal, a single long line can be better than splitting it.

### Numbers

- Use decimal, `0x`, `0o`, and `0b` forms as needed.
- Use lowercase prefixes for hex, octal, and binary.
- Do not use leading zeroes except in those prefixed forms.

### Coercion

- Use `String(value)`, `Boolean(value)`, template literals, or `!!value` for explicit coercion when appropriate.
- Do not use `Boolean()` or `!!` on enum values. Compare enum values explicitly.
- Use `Number(value)` for base-10 numeric parsing, then check `Number.isFinite`, `isFinite`, or `Number.isNaN` as appropriate for the project runtime.
- Be aware that whitespace strings and empty strings become `0`, and very large exponential notation can become infinity.
- Do not use unary `+` for numeric parsing.
- Do not use `parseInt` or `parseFloat` for base-10 parsing. They accept trailing junk.
- When non-base-10 parsing is required, validate the allowed digits before `parseInt(value, radix)`.
- For integer parsing, parse with `Number()`, check for failure, then use `Math.floor` or `Math.trunc` where available.
- Do not use explicit boolean coercion in `if`, `while`, or `for` conditions when implicit coercion is already happening.
- Enums in conditions must still be compared explicitly.

## Control Structures

- Use braces for control-flow bodies, even one-line bodies, except that a very short same-line `if` may omit braces when local style allows it.
- Start the first statement of a non-empty block on its own line.
- Avoid assignment inside control conditions. If intentional, wrap the assignment in an extra pair of parentheses.
- Prefer `for...of` for arrays.
- Use indexed loops when the index is needed, or `array.entries()` for index/value iteration.
- Use `for...in` only for dictionary-style objects, not arrays.
- Prefer `Object.keys`, `Object.values`, and `Object.entries` over `for...in`.
- Use grouping parentheses when they prevent any reasonable misread of operator precedence.
- Do not add unnecessary parentheses around whole expressions after `delete`, `typeof`, `void`, `return`, `throw`, `case`, `in`, `of`, or `yield`.

## Exceptions

- Use exceptions for exceptional cases.
- Prefer custom `Error` subclasses when native `Error` lacks needed context.
- Prefer throwing over ad hoc error containers when an actual exceptional condition occurred.
- Instantiate errors with `new Error(...)`.
- Throw and reject only `Error` instances or subclasses.
- When catching, normally assume thrown values are `Error` instances and narrow `unknown` accordingly.
- Handle non-`Error` thrown values only when a known dependency violates the rule; add a comment naming that dependency behavior.
- Do not leave catch blocks empty. If intentionally ignored, explain why in a comment.
- Keep `try` blocks focused on the statements that may throw, unless widening the block avoids a real readability or performance problem.

## Switch And Equality

- Every `switch` must include a `default`, and `default` must be last.
- Each non-empty `case` group must end abruptly with `break`, `return`, or `throw`.
- Empty case groups may fall through to a non-empty group.
- Use `===` and `!==`.
- The only normal exception is `value == null` or `value != null` when intentionally matching both `null` and `undefined`.

## Type And Non-Null Assertions

- Treat `value as Type` and `value!` as unsafe. They silence TypeScript without runtime checks.
- Prefer runtime checks, type guards, discriminated unions, and better control-flow narrowing.
- When an assertion is justified by local knowledge, make the reason obvious in code or with a short comment.
- Use `as` syntax, never angle-bracket assertions.
- For double assertions, cast through `unknown`, not `any` or `{}`.
- Use object literal type annotations or function return types instead of `as Type` on object literals so TypeScript catches renamed or extra properties.

## Decorators

- Do not define new decorators.
- Use decorators only when framework APIs require them, such as Angular or Polymer.
- Put decorators immediately before the symbol they decorate.
- Put JSDoc before decorators, not between a decorator and the decorated declaration.

## Disallowed Features

- Do not construct primitive wrappers with `new String`, `new Boolean`, or `new Number`.
- Do not rely on automatic semicolon insertion. End statements explicitly.
- Do not use `const enum`; use ordinary `enum`.
- Do not leave `debugger` statements in production code.
- Do not use `with`.
- Do not use `eval` or `new Function(string)` except in true code loaders.
- Do not use non-standard ECMAScript or Web Platform features in portable code.
- Code targeting an explicit runtime such as a current browser-only extension, Node.js, or Electron may use APIs for that runtime, but be cautious with proprietary browser APIs and consider a common abstraction library.
- Do not modify built-in objects or their prototypes.
- Do not add globals unless a third-party API makes it unavoidable.
