# Module Graph

Generated from routed module facets and lifecycle declarations. Do not edit by hand.

This graph is bipartite: modules link to facet values and lifecycle phases. It contains no module-to-module dependency edges.

## Module To Facets

| Module | Facet Key | Values |
| --- | --- | --- |
| `agent-delegation` | `intents` | delegate-independent-work<br>coordinate-parallel-review<br>scope-isolated-implementation-handoff |
| `agent-delegation` | `surfaces` | workflow-execution<br>subagent-briefing<br>evidence-reconciliation |
| `agent-delegation` | `risks` | shared-mutable-state-between-workers<br>overlapping-file-mutations<br>uncited-delegated-conclusions |
| `agent-delegation` | `artifacts` | delegation-brief<br>worker-report<br>review-findings |
| `agent-delegation` | `repo` | separable-files-or-behavioral-surfaces<br>validation-commands-can-be-named-per-task |
| `agent-delegation` | `request` | asks for subagents, workers, parallel investigation, parallel review, or isolated implementation handoff<br>work can be split into bounded tasks whose outputs are independently verifiable |
| `angular-conventions` | `intents` | Apply Angular implementation conventions to UI classes, templates, forms, and services<br>Review Angular public component and service surfaces for typed contracts |
| `angular-conventions` | `surfaces` | @angular/core components directives pipes and services<br>@angular/forms reactive and template-driven forms<br>Angular templates bindings control flow and component styles<br>Angular dependency injection providers and inject() usage |
| `angular-conventions` | `risks` | Untyped inputs outputs forms or template-facing members<br>Template logic hidden behind casts non-null assertions or broad public members<br>Standalone import provider or NgModule style drift from local project conventions<br>Public component behavior changed without consumer-facing evidence |
| `angular-conventions` | `artifacts` | *.component.ts<br>*.component.html<br>*.component.scss<br>*.directive.ts<br>*.pipe.ts<br>*.service.ts<br>*.spec.ts |
| `angular-conventions` | `repo` | package.json @angular/* versions<br>angular.json or project.json Angular targets<br>tsconfig* angularCompilerOptions<br>Existing same-feature Angular files |
| `angular-conventions` | `request` | Create or modify Angular component directive pipe service template style form input output or DI code<br>Review Angular code for typing standalone imports provider scope template behavior or public API |
| `angular-material-conventions` | `intents` | Apply Angular Material and CDK conventions to UI components and behavior primitives<br>Review Material/CDK accessibility theming density overlay and dependency impact |
| `angular-material-conventions` | `surfaces` | @angular/material component APIs<br>@angular/cdk a11y overlay portal testing and behavior utilities<br>Angular Material Sass theming density and token overrides<br>Material harnesses and Angular component tests |
| `angular-material-conventions` | `risks` | Keyboard focus labeling or screen-reader behavior regresses<br>Overlay positioning scroll backdrop or teardown behavior leaks<br>Material dependency added to shared UI without theme or bundle impact<br>Theme density or CSS override depends on private Material DOM |
| `angular-material-conventions` | `artifacts` | *.component.ts<br>*.component.html<br>*.component.scss<br>*.theme.scss<br>styles.scss<br>*.spec.ts<br>*harness*.ts |
| `angular-material-conventions` | `repo` | package.json @angular/material and @angular/cdk versions<br>Global Angular Material theme and styles<br>Existing Material imports components overlays and harness tests<br>Local design-system or shared UI components |
| `angular-material-conventions` | `request` | Add modify or review Angular Material component CDK utility overlay theme accessibility or density code<br>Assess whether a Material component CDK primitive or existing local component should own an interaction |
| `angular-tanstack-query-conventions` | `intents` | Apply TanStack Query conventions to Angular data fetching and cache contracts<br>Review Angular query keys options mutations pagination invalidation and skippable inputs |
| `angular-tanstack-query-conventions` | `surfaces` | TanStack Query Angular injectQuery injectMutation queryOptions and mutationOptions<br>QueryClient providers defaults invalidation and cache writes<br>Angular services and components that expose query state<br>Pagination filtering authorization and skippable input boundaries |
| `angular-tanstack-query-conventions` | `risks` | Query key omits data-changing input or authorization partition<br>Disabled query behavior is hidden behind nullable values<br>Mutation side effects leave stale or over-invalidated cache state<br>Pagination or filters reuse cache entries across distinct server results<br>Angular tests share QueryClient cache or wait on unstable query state |
| `angular-tanstack-query-conventions` | `artifacts` | *query*.ts<br>*queries*.ts<br>*.service.ts<br>*.component.ts<br>*.spec.ts<br>app.config.ts |
| `angular-tanstack-query-conventions` | `repo` | package.json TanStack Query Angular package and version<br>Application QueryClient provider and default options<br>Existing query key factories query option helpers and mutation helpers<br>Server API clients DTOs filters pagination and authorization context |
| `angular-tanstack-query-conventions` | `request` | Create modify or review Angular TanStack Query keys options mutations invalidation pagination or skip conditions<br>Debug stale cache cache collisions duplicate fetches mutation side effects or query test instability |
| `architecture-deepening-review` | `intents` | evaluate whether a module hides enough behavior behind its interface<br>find deeper seams that improve locality, leverage, or test surface |
| `architecture-deepening-review` | `surfaces` | module interface and implementation boundary<br>test surface<br>adapter or dependency boundary<br>responsibility locality<br>architecture decision memory |
| `architecture-deepening-review` | `risks` | wide interface hides little implementation<br>tests target private helpers instead of supported behavior<br>seam created for a hypothetical adapter<br>deepening review expands into an unbounded rewrite |
| `architecture-deepening-review` | `artifacts` | module interface<br>implementation boundary<br>adapter<br>test contract<br>architecture recommendation |
| `architecture-deepening-review` | `repo` | modular TypeScript workspace<br>codebase with durable architecture memory |
| `architecture-deepening-review` | `request` | reviews a shallow module, broad interface, weak test surface, or low-leverage abstraction<br>asks where behavior should be hidden or which interface tests should cross<br>plans architecture improvement based on locality, leverage, or dependency classification |
| `architecture-drift-detector` | `intents` | detect structural drift from concrete change evidence<br>scope architecture risk before it becomes a broad rewrite |
| `architecture-drift-detector` | `surfaces` | recent diffs or commit clusters<br>ownership boundaries<br>dependency direction<br>repeated fixes across files<br>responsibility spread |
| `architecture-drift-detector` | `risks` | architecture concern inferred from file count alone<br>same behavior changes across multiple owners<br>dependency direction erodes over repeated edits<br>drift response becomes an unbounded rewrite |
| `architecture-drift-detector` | `artifacts` | diff or commit range<br>changed file cluster<br>dependency edge<br>drift finding<br>bounded follow-up constraint |
| `architecture-drift-detector` | `repo` | repository with recent code churn<br>modular workspace |
| `architecture-drift-detector` | `request` | reviews recent changes for churn, ownership spread, dependency erosion, or structural risk<br>plans a refactor and needs drift evidence scoped to a named area<br>mentions repeated fixes, broad change clusters, or responsibility moving across owners |
| `branch-completion` | `intents` | Finish local branch work<br>Create a durable branch handoff<br>Publish or clean up completed repository work |
| `branch-completion` | `surfaces` | git branch lifecycle<br>commit preparation<br>remote publishing<br>pull request preparation<br>release handoff |
| `branch-completion` | `risks` | unrelated dirty files may be committed or discarded<br>publish, merge, release, and discard actions may be hard to reverse<br>stale validation may make branch readiness claims false<br>local branch state may diverge from the expected remote or base |
| `branch-completion` | `artifacts` | git status output<br>scoped diff<br>validation output<br>commit message<br>remote branch<br>pull request metadata<br>release notes |
| `branch-completion` | `repo` | dirty tree<br>staged changes<br>current branch<br>upstream tracking<br>unpushed commits<br>untracked files |
| `branch-completion` | `request` | commit changes<br>push this branch<br>open or update a pull request<br>merge this work<br>publish or release this change<br>discard or clean up branch work<br>finish this branch |
| `bricks` | `intents` | Inspect Bricks consumer workspace state<br>Run Bricks install or source-update workflow<br>Prepare Bricks contribution worktree |
| `bricks` | `surfaces` | Consumer Nx workspace<br>Bricks metadata<br>Installed brick source files<br>Bricks source cache<br>Bricks contribution worktree |
| `bricks` | `risks` | Consumer edits are overwritten<br>Source cache is mistaken for editable contribution worktree<br>Release workflow is mistaken for consumer workflow<br>Manual file copy bypasses Bricks provenance |
| `bricks` | `artifacts` | .bricks/config.json<br>.bricks/sources/<source><br>Installed app or library files<br>Source contribution branch |
| `bricks` | `repo` | apps/**<br>libs/**<br>packages/** |
| `bricks` | `request` | bricks init, source, install, merge, diff, status, remove, doctor, or contribute<br>Installed brick local edits, source update, merge conflict, or contribution session<br>Compare consumer copy to source or push consumer fixes upstream through Bricks |
| `bundle-performance` | `intents` | control bundle size impact<br>preserve tree-shaking<br>isolate optional runtime dependencies<br>review shared entry point changes |
| `bundle-performance` | `surfaces` | package entry points and exports<br>barrel files and shared UI roots<br>dynamic imports and lazy-loaded integrations<br>bundler configuration and side-effect declarations |
| `bundle-performance` | `risks` | shared import path pulls heavy dependency for unaffected consumers<br>import-time side effect prevents dead-code elimination<br>optional integration becomes part of the core runtime path<br>public import path changes without compatibility handling<br>bundle impact is accepted without measurement or static evidence |
| `bundle-performance` | `artifacts` | package.json and lockfiles<br>index files, barrels, and package export maps<br>build configuration and sideEffects metadata<br>bundle analyzer output, chunk reports, and size-limit results |
| `bundle-performance` | `repo` | diff adds runtime dependency or broad import in shared code<br>diff expands root exports or package entry points<br>diff changes side-effectful setup, global registration, CSS imports, or polyfills<br>diff moves optional charting, editor, date, i18n, analytics, or SDK code into a common path |
| `bundle-performance` | `request` | evaluate bundle size, chunking, tree-shaking, side effects, or dependency cost<br>add, remove, or move a runtime dependency<br>change package exports, barrels, shared imports, lazy loading, or build configuration |
| `code-documentation` | `intents` | keep code-adjacent documentation current<br>enforce strong documentation coverage for touched code<br>document public, reusable, structural, and behavioral code surfaces<br>explain long or dense implementation flow |
| `code-documentation` | `surfaces` | exported symbols, package entry points, interfaces, type aliases, classes, enums, methods, fields, and properties<br>component props, inputs, outputs, slots, emitted events, routes, commands, hooks, services, and providers<br>DTOs, schemas, payloads, validation rules, config options, generated docs, README usage, Storybook, and MDX<br>named functions, methods, callbacks, long functions, and branch-heavy implementation blocks |
| `code-documentation` | `risks` | changed behavior lacks consumer-facing documentation<br>types, interface properties, config fields, or schema fields are reachable but undocumented<br>functions and methods hide responsibility, side effects, constraints, or failure modes<br>comments narrate syntax instead of preserving intent<br>stale examples or docs remain reachable when code has moved |
| `code-documentation` | `artifacts` | JSDoc and TSDoc<br>README, Storybook, MDX, and generated documentation<br>fixtures, payload samples, stories, and usage examples |
| `code-documentation` | `repo` | diff creates, edits, moves, splits, deletes, or materially reviews code<br>diff changes a public import, framework binding, configuration, command, or user workflow<br>diff changes interfaces, type members, component contracts, schemas, DTOs, config fields, or examples<br>diff touches ordering-sensitive, lifecycle-sensitive, cached, concurrent, retrying, paginated, or error-recovery logic |
| `code-documentation` | `request` | implement, create, edit, move, delete, split, refactor, or review code<br>add, update, or review JSDoc, TSDoc, examples, stories, fixtures, payloads, or usage notes<br>ask whether comments, API docs, or generated documentation are sufficient |
| `completion-verification` | `intents` | Verify a completion claim<br>Prove acceptance against the latest request<br>Name remaining gaps prior to success wording |
| `completion-verification` | `surfaces` | task completion<br>acceptance evidence<br>validation summary<br>release readiness<br>final response |
| `completion-verification` | `risks` | success may be claimed from stale output<br>partial requirements may be overlooked<br>skipped checks may be hidden<br>current workspace may contradict earlier evidence |
| `completion-verification` | `artifacts` | latest user request<br>requirements checklist<br>test output<br>inspected diff<br>runtime evidence<br>blocked validation note |
| `completion-verification` | `repo` | modified files<br>generated outputs<br>test suite<br>runtime artifacts<br>documentation changes |
| `completion-verification` | `request` | is this done<br>claim the task is complete<br>show validation proof<br>confirm acceptance criteria<br>ready to ship<br>summarize completion evidence |
| `design-intake` | `intents` | clarify-ambiguous-request<br>stabilize-user-facing-outcome |
| `design-intake` | `surfaces` | workflow-intake<br>requirements-clarification<br>scope-definition |
| `design-intake` | `risks` | repo-answerable-question-sent-to-user<br>public-behavior-chosen-by-assumption<br>implementation-starts-from-unstable-intent |
| `design-intake` | `artifacts` | intake-summary<br>clarifying-question<br>success-criteria |
| `design-intake` | `repo` | existing-source-docs-or-memory-may-answer-context<br>target-artifact-or-audience-is-unclear |
| `design-intake` | `request` | desired outcome, audience, task type, constraints, non-goals, or success criteria are missing<br>request concerns creative, behavioral, user-facing, architecture-affecting, or scope-sensitive work |
| `diary` | `intents` | Record work history<br>Prepare a handoff log<br>Preserve decisions or validation evidence |
| `diary` | `surfaces` | repo-local diary<br>work summary<br>handoff notes<br>decision log<br>validation record |
| `diary` | `risks` | secrets or unnecessary personal data may be persisted<br>unverified assumptions may become durable history<br>diary entries may duplicate authoritative docs or issues<br>future agents may rely on incomplete context |
| `diary` | `artifacts` | .diary/YYYY-MM-DD.md<br>diary dry-run output<br>recent diary entries<br>validation summary<br>changed file list<br>blocker list |
| `diary` | `repo` | project root<br>.diary directory<br>current working directory<br>changed files |
| `diary` | `request` | log this work<br>write a diary entry<br>journal progress<br>prepare a handoff summary<br>record this decision<br>preserve validation results<br>show recent diary entries |
| `example-universe-enforcer` | `intents` | normalize invented examples to one domain<br>replace generic placeholders in sample data<br>keep illustrative data relationships coherent |
| `example-universe-enforcer` | `surfaces` | sample code<br>DTOs and schemas<br>API payloads<br>tests, fixtures, Storybook data, and docs snippets |
| `example-universe-enforcer` | `risks` | generic Foo, Bar, User, Product, Item, or ExampleEntity placeholders<br>mixed illustrative domains in one response or artifact<br>invented sample data overwrites real user-provided project data<br>oversized fixtures obscure the behavior being demonstrated |
| `example-universe-enforcer` | `artifacts` | code examples<br>JSON payload samples<br>fixtures and test data<br>stories, MDX, README snippets, and docs examples |
| `example-universe-enforcer` | `repo` | diff adds or changes illustrative entities, mock records, sample payloads, or example snippets<br>changed examples introduce generic names or an unrelated sample domain |
| `example-universe-enforcer` | `request` | create examples, sample code, DTOs, API payloads, tests, stories, fixtures, or docs snippets<br>replace placeholder sample data<br>review whether examples are coherent and minimal |
| `extraction-decision` | `intents` | decide whether repeated code should become an owned abstraction<br>separate stable shared behavior from coincidental similarity |
| `extraction-decision` | `surfaces` | duplicated logic, DTOs, contracts, and orchestration<br>UI composition and data-access patterns<br>consumer variation points<br>abstraction owner and public API<br>dependency direction |
| `extraction-decision` | `risks` | shared helper extracted from coincidental shape<br>new abstraction has no stable owner<br>dependency direction is inverted for convenience<br>extraction creates a shallow common module |
| `extraction-decision` | `artifacts` | duplicated code cluster<br>extracted function, component, service, contract, or adapter<br>consumer inventory<br>variation analysis<br>reusable-abstraction decision record |
| `extraction-decision` | `repo` | TypeScript workspace<br>modular application codebase |
| `extraction-decision` | `request` | mentions repeated logic, duplicated DTO shape, copied orchestration, reusable data access, or repeated UI composition<br>asks whether code should be extracted, shared, kept local, or moved to an owner<br>plans a reusable abstraction from multiple current consumers |
| `grill-with-docs` | `intents` | challenge-known-decision<br>stress-test-domain-language |
| `grill-with-docs` | `surfaces` | workflow-intake<br>docs-grounded-questioning<br>decision-alignment |
| `grill-with-docs` | `risks` | questions-not-grounded-in-project-memory<br>broad-interview-instead-of-blocking-tradeoff<br>durable-vocabulary-drift |
| `grill-with-docs` | `artifacts` | challenge-question<br>decision-record-candidate<br>glossary-update-candidate |
| `grill-with-docs` | `repo` | project-memory-glossary-or-adrs-can-ground-the-question<br>known-plan-term-or-decision-is-available-to-examine |
| `grill-with-docs` | `request` | asks to grill, challenge, go deeper, stress-test, or ask decision-changing questions<br>target is a stated plan, vocabulary term, domain rule, ADR candidate, or documented decision |
| `implementation-plan` | `intents` | draft-decision-complete-plan<br>sequence-known-work |
| `implementation-plan` | `surfaces` | workflow-planning<br>implementation-sequencing<br>migration-planning |
| `implementation-plan` | `risks` | generic-phase-list<br>hidden-design-decisions<br>tests-docs-or-compatibility-omitted |
| `implementation-plan` | `artifacts` | written-execution-plan<br>validation-matrix<br>migration-notes |
| `implementation-plan` | `repo` | requirements-and-non-goals-are-known<br>affected-files-interfaces-or-commands-can-be-mapped |
| `implementation-plan` | `request` | asks for a plan, full plan, phases, roadmap, migration path, or execution sequence<br>work is substantial or cross-boundary and requirements are stable enough to plan |
| `issue-decomposition` | `intents` | decompose-large-work<br>prepare-agent-briefs<br>produce-tracker-issues |
| `issue-decomposition` | `surfaces` | workflow-planning<br>vertical-slicing<br>issue-tracker-preparation |
| `issue-decomposition` | `risks` | layer-only-slices<br>afk-brief-open-decisions<br>unconfigured-tracker-publishing |
| `issue-decomposition` | `artifacts` | issue-brief<br>vertical-slice<br>acceptance-criteria<br>tracker-label-map |
| `issue-decomposition` | `repo` | source-context-or-prd-can-support-slices<br>tracker-mode-or-local-markdown-output-can-be-identified |
| `issue-decomposition` | `request` | asks to turn a PRD, plan, roadmap, or large request into issues, briefs, slices, or implementation units<br>work spans multiple behaviors that need independently verifiable acceptance criteria |
| `jest-conventions` | `intents` | author or review Jest unit and integration tests<br>change Jest configuration, setup, environment, matcher, mock, or fixture behavior<br>diagnose flaky, slow, over-mocked, or implementation-coupled Jest tests |
| `jest-conventions` | `surfaces` | javascript-test-runner<br>jest<br>node-or-jsdom-test-environment<br>unit-and-integration-test-conventions |
| `jest-conventions` | `risks` | mock replaces private implementation instead of an external boundary<br>global setup or custom matcher added for one local test<br>test environment does not match the code under test<br>async work, fake timers, module mocks, or globals leak across tests<br>snapshot or call-count assertion hides the user-visible behavior being protected |
| `jest-conventions` | `artifacts` | jest.config.*<br>package.json jest configuration or Jest npm scripts<br>__tests__/**, *.test.*, *.spec.*, and Jest project testMatch/testRegex targets<br>__mocks__/** and manual module mocks<br>setupFiles, setupFilesAfterEnv, testEnvironment, moduleNameMapper, transform, and projects config<br>expect.extend custom matchers and Jest environment files |
| `jest-conventions` | `repo` | dependencies or scripts invoke jest, @jest/globals, jest-environment-jsdom, ts-jest, babel-jest, or swc/jest transforms<br>tests import from @jest/globals or rely on Jest global APIs<br>repository has Jest setup, matcher, environment, or manual mock files |
| `jest-conventions` | `request` | mentions Jest, jest.config, jest.mock, jest.fn, @jest/globals, testEnvironment, setupFilesAfterEnv, __mocks__, or custom Jest matchers<br>asks to add, repair, review, or stabilize unit tests that are run by Jest |
| `library-placement-decision` | `intents` | decide durable ownership for new, moved, or extracted code<br>choose whether code stays local or becomes a library or package surface |
| `library-placement-decision` | `surfaces` | project and package layout<br>library, feature, domain, integration, adapter, utility, and UI ownership<br>import paths and public entry points |
| `library-placement-decision` | `risks` | shared library created for convenience rather than stable ownership<br>dependency direction changes because code moved<br>mixed responsibilities hidden behind a broad common package |
| `library-placement-decision` | `artifacts` | new library or package<br>moved source file or folder<br>extracted abstraction<br>public export<br>ownership decision |
| `library-placement-decision` | `repo` | TypeScript monorepo<br>modular workspace<br>library-oriented source tree |
| `library-placement-decision` | `request` | asks where new code should live<br>adds, moves, or extracts reusable logic, DTOs, adapters, UI, or utilities<br>changes import location, package ownership, or library boundaries |
| `naming-consistency` | `intents` | choose names that encode domain role, lifecycle, and ownership<br>review public and reusable names for project vocabulary alignment |
| `naming-consistency` | `surfaces` | files, folders, exports, classes, functions, and constants<br>DTOs, contracts, events, commands, providers, and factories<br>domain glossary and project memory<br>tests, stories, fixtures, docs, and generated references |
| `naming-consistency` | `risks` | generic name forces readers to inspect implementation<br>role suffix describes a pattern instead of the local responsibility<br>public rename leaves old imports or docs behind<br>term conflicts with the project glossary |
| `naming-consistency` | `artifacts` | new or renamed symbol<br>file or folder name<br>public export<br>domain term<br>rename audit |
| `naming-consistency` | `repo` | TypeScript workspace<br>codebase with domain vocabulary |
| `naming-consistency` | `request` | creates or renames files, classes, functions, exports, DTOs, contracts, events, commands, providers, factories, or abstractions<br>asks for a better name or naming consistency review<br>changes public names that consumers, docs, tests, fixtures, or generated references may mention |
| `nestjs-conventions` | `intents` | Apply NestJS conventions to modules, controllers, providers, and runtime boundaries<br>Review NestJS request lifecycle behavior, dependency injection, validation, and bootstrap changes |
| `nestjs-conventions` | `surfaces` | @nestjs/common modules controllers providers and decorators<br>Dependency injection tokens custom providers factories and provider scopes<br>Pipes validation DTOs guards interceptors filters middleware and request lifecycle<br>Application bootstrap global providers adapters and microservice runtime setup<br>Nest testing modules e2e setup and framework-facing tests |
| `nestjs-conventions` | `risks` | Controller contains business behavior that belongs behind an injectable provider<br>Provider token or scope is implicit when implementations or lifetimes can vary<br>Validation transformation authorization or interception is bypassed with ad hoc code<br>Global pipe guard interceptor filter or bootstrap change alters routes not covered by evidence<br>Request-scoped or transient provider widens runtime cost or state lifetime unexpectedly |
| `nestjs-conventions` | `artifacts` | *.module.ts<br>*.controller.ts<br>*.service.ts and provider files<br>*.guard.ts *.pipe.ts *.interceptor.ts *.filter.ts middleware files<br>*.dto.ts and validation classes<br>main.ts application bootstrap and microservice setup files<br>*.spec.ts *.e2e-spec.ts Nest testing module files |
| `nestjs-conventions` | `repo` | Installed @nestjs/* versions and platform adapter packages<br>Existing same-feature module controller provider and DTO patterns<br>Global bootstrap pipes guards interceptors filters and exception handling<br>Testing module setup and e2e runtime configuration |
| `nestjs-conventions` | `request` | Create or modify NestJS module provider controller guard pipe interceptor filter middleware bootstrap or runtime code<br>Review NestJS code for request lifecycle behavior dependency injection validation scope or transport separation |
| `nestjs-mongoose-conventions` | `intents` | Apply NestJS Mongoose conventions to schemas, models, repositories, and persistence contracts<br>Review Mongoose query, ObjectId, aggregation, and plain-result boundaries in NestJS code |
| `nestjs-mongoose-conventions` | `surfaces` | @nestjs/mongoose MongooseModule forRoot forFeature forFeatureAsync and InjectModel<br>Schema Prop SchemaFactory raw schema definitions hooks plugins virtuals indexes and discriminators<br>Mongoose Model Query Aggregate populate lean sessions transactions and ObjectId handling<br>Repository providers mappers persistence DTOs and API-facing return contracts |
| `nestjs-mongoose-conventions` | `risks` | Hydrated document or raw ObjectId leaks across a public API or transport boundary<br>Schema class is reused as a domain model DTO or response contract where shapes differ<br>Aggregation result is untyped or assumes schema casting that Mongoose does not perform<br>Lean/plain query result is used where getters virtuals document methods or save behavior are required<br>Hook plugin index or discriminator registration happens after model compilation<br>Index synchronization can drop existing database indexes without diff evidence<br>Repository exposes model internals instead of behavior-oriented persistence methods |
| `nestjs-mongoose-conventions` | `artifacts` | *.schema.ts<br>*.repository.ts and persistence provider files<br>*.module.ts MongooseModule registration<br>*.dto.ts persistence-facing contracts and mappers<br>aggregation helper files and query builders<br>index diff or sync evidence<br>*.spec.ts *.e2e-spec.ts persistence tests |
| `nestjs-mongoose-conventions` | `repo` | Installed @nestjs/mongoose and mongoose versions<br>Existing schema and repository patterns<br>Connection registration model tokens and named connection usage<br>Persistence tests fixtures indexes migrations and database setup |
| `nestjs-mongoose-conventions` | `request` | Create or modify NestJS Mongoose schema model repository aggregation ObjectId mapper or persistence DTO code<br>Review Mongoose persistence for schema shape query typing document leakage ObjectId conversion or repository boundaries |
| `no-transitional-architecture` | `intents` | force direct replacement of changed architecture surfaces<br>evaluate whether compatibility is an externally required contract |
| `no-transitional-architecture` | `surfaces` | public APIs, exports, routes, events, commands, options, and DTOs<br>source-of-truth files, services, adapters, factories, and registries<br>tests, fixtures, docs, examples, and generated outputs<br>runtime registrations and dependency injection providers |
| `no-transitional-architecture` | `risks` | old and new implementations remain reachable<br>alias, shim, wrapper, or fallback hides incomplete caller updates<br>placeholder or stub creates false completion<br>obsolete name remains in docs, fixtures, schema, or registration |
| `no-transitional-architecture` | `artifacts` | replacement ledger<br>compatibility exception<br>renamed or moved file<br>deleted export or public name<br>deletion audit |
| `no-transitional-architecture` | `repo` | codebase undergoing rename, move, extraction, or behavior replacement |
| `no-transitional-architecture` | `request` | renames, moves, extracts, or replaces a source of truth<br>adds a compatibility alias, legacy adapter, migration shim, wrapper, fallback, stub, or placeholder<br>keeps old and new APIs, event names, option names, DTO fields, routes, services, adapters, factories, or registries side by side<br>asks to preserve old behavior while introducing a new public surface |
| `nx-conventions` | `intents` | Apply Nx workspace conventions to project metadata, task targets, generators, and cache behavior<br>Review Nx project graph changes for accurate inputs, outputs, and affected execution |
| `nx-conventions` | `surfaces` | nx.json targetDefaults namedInputs plugins and workspace layout<br>project.json package.json Nx targets and inferred task configuration<br>Nx generators executors plugins migrations and workspace scripts<br>Project graph tags implicit dependencies affected commands and cache outputs |
| `nx-conventions` | `risks` | Root workspace config changed to solve a project-local problem<br>Cache inputs omit runtime files environment values or upstream production inputs<br>Target outputs do not match files produced by the task<br>Manual target duplicates an inferred task or weakens plugin-managed caching<br>Project move changes graph ownership tags or affected execution without evidence |
| `nx-conventions` | `artifacts` | nx.json<br>project.json<br>package.json<br>tsconfig.base.json and tsconfig*.json<br>workspace generator migration and plugin files<br>Nx graph affected command target log and cache output evidence |
| `nx-conventions` | `repo` | Installed nx and @nx/* versions<br>Existing project metadata for nearby projects<br>Target defaults namedInputs plugins cache settings and output folders<br>Tool configuration files used by Nx plugins to infer tasks |
| `nx-conventions` | `request` | Create or modify Nx workspace configuration project metadata targets generators executors inferred tasks cache settings or project graph behavior<br>Review Nx config for target correctness cache safety affected execution project movement or graph metadata |
| `nx-module-boundaries` | `intents` | preserve Nx project ownership and dependency direction<br>design or review Nx tags and dependency constraints |
| `nx-module-boundaries` | `surfaces` | Nx project graph<br>apps and libs project layout<br>project tags and dependency constraints<br>module-boundary lint rules<br>Node and browser runtime boundaries |
| `nx-module-boundaries` | `risks` | tag added to grant access instead of describing responsibility<br>module-boundary rule relaxed to hide an ownership mismatch<br>runtime-specific dependency crosses into an incompatible project<br>internal project path imported instead of a supported entry point |
| `nx-module-boundaries` | `artifacts` | nx.json<br>project.json<br>workspace ESLint configuration<br>project tag<br>dependency constraint<br>Nx app or library |
| `nx-module-boundaries` | `repo` | Nx workspace<br>TypeScript monorepo |
| `nx-module-boundaries` | `request` | adds, moves, or reviews an Nx app or library<br>changes project tags, dependency constraints, or module-boundary lint rules<br>fixes or evaluates an Nx module-boundary violation<br>changes dependency direction between Node, browser, feature, domain, or utility projects |
| `plan-execution` | `intents` | execute-existing-plan<br>continue-decision-complete-work |
| `plan-execution` | `surfaces` | workflow-execution<br>implementation-sequencing<br>validation-checkpoints |
| `plan-execution` | `risks` | silent-replanning<br>stale-plan-vs-current-repo<br>unrelated-dirty-worktree-changes |
| `plan-execution` | `artifacts` | implementation-plan<br>task-checklist<br>validation-report |
| `plan-execution` | `repo` | written-plan-or-goal-is-available<br>planned-files-and-tests-can-be-identified |
| `plan-execution` | `request` | asks to implement, execute, continue, or finish a written plan<br>plan already fixes scope, order, acceptance checks, and validation commands |
| `playwright-conventions` | `intents` | author or review Playwright end-to-end and browser integration tests<br>change Playwright config, browser projects, fixtures, locators, assertions, setup projects, traces, or retries<br>diagnose flaky browser tests, unstable selectors, timing waits, or shared browser state |
| `playwright-conventions` | `surfaces` | browser-test-runner<br>playwright<br>end-to-end-tests<br>browser-project-matrix<br>user-observable-web-behavior |
| `playwright-conventions` | `risks` | locator depends on DOM structure instead of user-facing contract<br>fixed timeout hides missing readiness condition<br>test data or storage state leaks across specs or browser projects<br>retry or trace settings mask product regression instead of exposing evidence<br>assertion checks implementation timing rather than visible browser state |
| `playwright-conventions` | `artifacts` | playwright.config.*<br>tests/e2e/**, e2e/**, *.e2e.*, and Playwright *.spec.* files<br>browser projects, use options, storageState, webServer, retries, trace, screenshot, and video config<br>Playwright fixtures, setup projects, page objects, locators, and expect assertions<br>CI browser install, browser cache, and Playwright report artifacts |
| `playwright-conventions` | `repo` | dependencies or scripts invoke @playwright/test or playwright test<br>tests import test, expect, Page, Locator, or devices from @playwright/test<br>repository has Playwright setup projects, fixtures, storage state, reports, traces, or browser project definitions |
| `playwright-conventions` | `request` | mentions Playwright, playwright.config, browser project, locator, page fixture, setup project, trace, storageState, e2e, or end-to-end test<br>asks to add, repair, review, or stabilize browser automation that runs through Playwright |
| `prototype` | `intents` | answer-design-question-with-prototype<br>compare-ui-variants<br>test-state-model |
| `prototype` | `surfaces` | workflow-planning<br>throwaway-prototype<br>design-learning |
| `prototype` | `risks` | prototype-becomes-production-dependency<br>multiple-unrelated-questions<br>persistent-state-added-without-need |
| `prototype` | `artifacts` | prototype-question<br>throwaway-shell<br>learning-report |
| `prototype` | `repo` | safe-isolated-workspace-can-be-used<br>one-runnable-command-can-demonstrate-learning |
| `prototype` | `request` | asks for a prototype, spike, UI variant comparison, or state-model experiment<br>goal is learning or decision support rather than production-ready code |
| `public-api-design` | `intents` | design supported public exports and entry points<br>shape shared contracts, DTOs, and reusable abstraction boundaries |
| `public-api-design` | `surfaces` | package entry points<br>public exports<br>shared DTOs and contracts<br>consumer import paths<br>SDK or library surface |
| `public-api-design` | `risks` | implementation detail exported as a convenience<br>public contract allows invalid state<br>consumer migration impact is hidden<br>entry point grows broader than the owning module supports |
| `public-api-design` | `artifacts` | index or barrel file<br>exported type, class, function, or constant<br>DTO or schema<br>SDK contract<br>package import path |
| `public-api-design` | `repo` | TypeScript workspace<br>package or library boundary |
| `public-api-design` | `request` | adds or changes exports, entry points, DTOs, schemas, or contracts<br>changes package import paths or consumer-facing abstractions<br>asks whether a symbol should be public |
| `review-feedback-triage` | `intents` | Triage external technical feedback<br>Respond to reviewer comments<br>Decide whether a suggested change is valid |
| `review-feedback-triage` | `surfaces` | code review comment<br>CI finding<br>agent review<br>reviewer bug report<br>suggested patch |
| `review-feedback-triage` | `risks` | reviewer claim may be stale or context-free<br>blind patch may damage established design<br>fix may expand beyond the requested concern<br>feedback may contradict requirements |
| `review-feedback-triage` | `artifacts` | review comment text<br>pull request diff<br>CI log<br>changed file<br>test output<br>review response draft |
| `review-feedback-triage` | `repo` | reviewed files<br>changed files<br>failing checks<br>line references<br>local diff |
| `review-feedback-triage` | `request` | address review feedback<br>triage review comments<br>fix reviewer finding<br>respond to CI review<br>apply requested changes<br>evaluate this suggested patch |
| `review-gate` | `intents` | Review completed work<br>Gate implementation quality<br>Audit change risk |
| `review-gate` | `surfaces` | code review<br>diff review<br>quality gate<br>pre-merge inspection<br>acceptance review |
| `review-gate` | `risks` | requirement may be missed<br>behavior may regress<br>tests may be inadequate<br>public contract may break<br>documentation may drift<br>security or data handling risk may be introduced |
| `review-gate` | `artifacts` | user requirements<br>git diff<br>test result<br>API contract<br>documentation<br>review findings |
| `review-gate` | `repo` | changed files<br>test files<br>public interfaces<br>generated outputs<br>dependency or configuration changes |
| `review-gate` | `request` | review this implementation<br>audit completed change<br>list findings<br>quality check<br>pre-merge review<br>inspect code smell |
| `rxjs-conventions` | `intents` | Design or review observable stream behavior<br>Make RxJS time, ownership, cancellation, and error semantics explicit |
| `rxjs-conventions` | `surfaces` | RxJS Observable, Subject, BehaviorSubject, ReplaySubject, Subscription, Scheduler, and operator chains<br>pipe composition, subscribe calls, flattening operators, multicasting, caching, and teardown<br>Framework services, components, stores, effects, and tests that expose or consume streams |
| `rxjs-conventions` | `risks` | Nested subscription hides ordering, cancellation, or error propagation<br>Subject acts as an unowned event bus or leaks mutation methods to consumers<br>Flattening operator does not match concurrency, cancellation, or ordering requirements<br>Long-lived subscription lacks a teardown path<br>Error handling swallows failures or terminates a shared stream unexpectedly |
| `rxjs-conventions` | `artifacts` | *.ts and *.tsx files importing rxjs or rxjs/operators<br>Observable-returning services, effects, components, stores, and tests<br>Marble tests, fake timer tests, integration tests, and subscription cleanup assertions |
| `rxjs-conventions` | `repo` | Existing stream naming, $ suffix, and subscription ownership conventions<br>Lifecycle or disposal mechanism for the surrounding framework<br>Tests that prove ordering, cancellation, teardown, and error behavior |
| `rxjs-conventions` | `request` | Create, modify, or review an Observable, operator chain, subscription, subject, or multicasted stream<br>Choose between switchMap, mergeMap, concatMap, exhaustMap, share, shareReplay, or manual subscription<br>Fix a stream leak, stale request, duplicate emission, cancellation bug, or swallowed error |
| `skill-evolution` | `intents` | Evolve Cortex skill behavior<br>Codify recurring agent failure<br>Close durable workflow doctrine gap |
| `skill-evolution` | `surfaces` | Routed skill metadata<br>Lifecycle phase guidance<br>Skill-owned references<br>Skill workspace conventions |
| `skill-evolution` | `risks` | One-off preference becomes reusable doctrine<br>Overlapping ownership across skill artifacts<br>Metadata, lifecycle, and resource declarations drift<br>Routing evidence is too broad to audit |
| `skill-evolution` | `artifacts` | skill.yaml<br>lifecycle/*.md<br>references/*.md<br>templates/*<br>assets/* |
| `skill-evolution` | `repo` | entry/*/skill.yaml<br>commands/*/skill.yaml<br>modules/*/*/*/skill.yaml<br>modules/*/*/*/lifecycle/*.md |
| `skill-evolution` | `request` | User asks to create, split, retire, narrow, or rewrite Cortex skill behavior<br>Repeated agent failure, recurring workflow pattern, or durable doctrine gap needs reusable guidance<br>Routing facets, lifecycle files, declared resources, or validation expectations need synchronized changes |
| `storybook-angular-conventions` | `intents` | Apply Angular-specific Storybook conventions to stories, providers, module metadata, and typed args<br>Review Angular Storybook setup for standalone or NgModule correctness and deterministic component states |
| `storybook-angular-conventions` | `surfaces` | @storybook/angular Meta StoryObj render moduleMetadata applicationConfig and decorators<br>Angular standalone imports NgModule declarations providers and environment providers in stories<br>Angular inputs outputs forms template dependencies pipes directives and service mocks<br>Compodoc docs setup angular.json project targets and build-storybook configuration |
| `storybook-angular-conventions` | `risks` | Story setup hides missing Angular imports declarations providers or required inputs<br>applicationConfig provider scope is broader than the story state requires<br>Args do not match Angular inputs outputs form values or template-facing types<br>Story depends on live Angular services HTTP router state current time or shared mutable state<br>Standalone and NgModule setup styles are mixed without local project evidence |
| `storybook-angular-conventions` | `artifacts` | *.stories.ts files using @storybook/angular<br>.storybook/main.* .storybook/preview.* Angular Storybook config<br>angular.json project.json Storybook targets<br>Compodoc documentation.json and docs integration files<br>Angular fixture mock provider and decorator files |
| `storybook-angular-conventions` | `repo` | Installed @storybook/angular storybook @angular/* and builder versions<br>Existing Angular story setup for standalone or NgModule components<br>Angular component inputs outputs providers forms directives and pipes under story<br>Storybook Angular serve build and docs commands |
| `storybook-angular-conventions` | `request` | Create or modify Angular Storybook stories provider mocks moduleMetadata applicationConfig args fixtures or Compodoc setup<br>Review Angular Storybook for component setup provider scope typed args deterministic data or Storybook Angular validation |
| `storybook-conventions` | `intents` | Apply Storybook conventions to component stories, docs, mocks, and preview configuration<br>Review stories for meaningful states, deterministic fixtures, typed args, and validation evidence |
| `storybook-conventions` | `surfaces` | CSF story files Meta StoryObj args argTypes parameters decorators loaders and play functions<br>MDX docs doc blocks autodocs tags and story organization<br>.storybook main preview manager addon builder and project annotations<br>Story fixtures network mocks module mocks providers and visual regression data<br>Storybook build test-runner interaction accessibility and visual test outputs |
| `storybook-conventions` | `risks` | Story only mirrors default props without demonstrating behavior or state<br>Random live or environment-dependent data makes stories non-repeatable<br>Mocks hide missing component dependencies instead of modeling external boundaries<br>MDX becomes product documentation unrelated to story setup or component behavior<br>Play function decorator loader or addon change is not validated in Storybook runtime |
| `storybook-conventions` | `artifacts` | *.stories.ts *.stories.tsx *.stories.js *.stories.jsx *.stories.mdx<br>*.mdx Storybook docs files<br>.storybook/main.* .storybook/preview.* .storybook/manager.*<br>storybook fixture mock and decorator files<br>visual snapshots interaction-test output accessibility output and build-storybook output |
| `storybook-conventions` | `repo` | Installed storybook @storybook/* framework builder and addon versions<br>Existing story naming organization fixture and docs patterns<br>Preview annotations global decorators loaders parameters and addon setup<br>Storybook commands for dev build test-runner accessibility and visual checks |
| `storybook-conventions` | `request` | Create or modify Storybook stories MDX docs preview setup addons mocks fixtures decorators loaders play functions or story organization<br>Review Storybook behavior for meaningful states typed args deterministic mocks docs scope interaction tests or visual evidence |
| `systematic-debugging` | `intents` | reproduce or localize a failure<br>test falsifiable debugging hypotheses<br>fix root cause instead of symptom<br>stabilize flaky asynchronous behavior |
| `systematic-debugging` | `surfaces` | failing tests and CI logs<br>runtime errors and stack traces<br>performance regressions and unexpected behavior<br>async waits, integration boundaries, and data validation |
| `systematic-debugging` | `risks` | symptom patch leaves earlier invalid state path open<br>multiple suspected causes change at once<br>failure cannot be reproduced or reduced<br>temporary diagnostics remain in delivered code<br>fixed sleep hides a readiness race |
| `systematic-debugging` | `artifacts` | failure logs, traces, and stack traces<br>minimal reproductions and focused probes<br>temporary instrumentation<br>regression tests and validation guards |
| `systematic-debugging` | `repo` | test, build, CI, runtime, or performance failure is present<br>diff changes code while investigating a reported bug<br>workflow contains sleeps, polling, retries, or flaky async behavior<br>invalid data flows across entry point, domain, integration, or environment boundaries |
| `systematic-debugging` | `request` | debug, investigate, diagnose, reproduce, or fix a failure<br>fix a failing test, build failure, bug, flaky workflow, performance problem, or unexpected behavior<br>explain why a failure occurs prior to changing code |
| `test-first-discipline` | `intents` | define behavior proof prior to implementation<br>add regression coverage for a bug fix<br>protect public behavior during refactor<br>verify test harness changes through a smoke path |
| `test-first-discipline` | `surfaces` | public APIs and service interfaces<br>UI workflows and command behavior<br>integration boundaries and e2e paths<br>test framework setup and harness configuration |
| `test-first-discipline` | `risks` | implementation-only test pins private structure<br>behavior change ships without failing or newly relevant coverage<br>refactor changes behavior without public seam protection<br>test setup change lacks a smoke proof<br>exception to test-first discipline is undocumented |
| `test-first-discipline` | `artifacts` | unit, integration, and e2e tests<br>fixtures, test harnesses, and assertions<br>test framework configuration<br>regression tests |
| `test-first-discipline` | `repo` | diff changes behavior, bug fix, refactor, validation path, or public contract<br>diff adds or changes tests, fixtures, test harnesses, or e2e workflows<br>diff changes test runner, setup files, mocks, or framework configuration |
| `test-first-discipline` | `request` | implement new behavior, fix a bug, refactor behavior, or add regression protection<br>add or update tests, e2e workflows, fixtures, mocks, or test framework setup<br>decide what test should prove a requested behavior |
| `typescript-api-conventions` | `intents` | Design or review an exported TypeScript contract<br>Model public TypeScript states, DTOs, or reusable type utilities |
| `typescript-api-conventions` | `surfaces` | TypeScript exported interfaces, type aliases, classes, functions, constants, and enums<br>DTOs, service contracts, SDK shapes, declaration files, and package entry points<br>Generic helpers, discriminated unions, branded values, nullability, and readonly contracts |
| `typescript-api-conventions` | `risks` | Optional-field state bag permits invalid combinations<br>Unconstrained or return-only generic lets callers assert unsupported shapes<br>Private helper type is exported to satisfy an internal import<br>Runtime export and type-only export boundaries are unclear<br>Contract change lacks consumer migration, typecheck, or public documentation evidence |
| `typescript-api-conventions` | `artifacts` | *.ts, *.tsx, *.mts, *.cts, and *.d.ts files that expose exported symbols<br>index files, barrel files, package exports, generated declaration surfaces, and API docs<br>Tests or examples that compile against the public TypeScript contract |
| `typescript-api-conventions` | `repo` | Existing imports of the changed export<br>Package entry points and declaration output<br>Typecheck, API extraction, contract tests, or compile-time examples |
| `typescript-api-conventions` | `request` | Add, remove, rename, or redesign an exported TypeScript symbol<br>Change a DTO, public interface, SDK type, service contract, generic utility, or declaration file<br>Review whether a TypeScript API makes invalid states, nullability, or generic constraints explicit |
| `typescript-code-style` | `intents` | Apply TypeScript source style and strictness rules<br>Review TypeScript implementation clarity, imports, naming, and comments |
| `typescript-code-style` | `surfaces` | TypeScript and TSX source files, tests, scripts, and framework components<br>Imports, exports, type-only imports, file structure, public entry points, and module boundaries<br>Names, type annotations, narrowing, assertions, JSDoc, ordinary comments, and compiler directives |
| `typescript-code-style` | `risks` | Broad cast, non-null assertion, any, or bracket access hides a type modeling issue<br>Private-file import bypasses the package entry point that owns a symbol<br>Style-only churn obscures the functional change under review<br>Comment repeats syntax instead of documenting intent, invariants, or tool constraints<br>Generated, framework-owned, or locally non-conforming code is reformatted without a focused reason |
| `typescript-code-style` | `artifacts` | *.ts, *.tsx, *.mts, and *.cts source files<br>TypeScript tests, build scripts, config-adjacent helpers, and generated-type consumers<br>Owned references under references/ and the ts_style_preflight.py helper |
| `typescript-code-style` | `repo` | Nearest project lint, format, typecheck, and test commands<br>Neighboring TypeScript files in the same package or component tree<br>Public package entry points used by imports in the touched code |
| `typescript-code-style` | `request` | Write, edit, refactor, generate, or review TypeScript or TSX implementation code<br>Change imports, exports, names, classes, functions, comments, type annotations, assertions, or compiler directives<br>Decide whether local TypeScript style, strict typing, or tooling should block a change |
| `vite-conventions` | `intents` | Apply Vite configuration conventions to dev server behavior, plugins, aliases, and production builds<br>Review Vite library and application builds for public entry point and dependency correctness |
| `vite-conventions` | `surfaces` | vite.config.* defineConfig config loading and environment modes<br>resolve.alias publicDir define envDir optimizeDeps and CSS handling<br>plugins plugin order transform behavior and framework integrations<br>build.lib output formats source maps externals and bundler options<br>server proxy HMR allowed hosts watch settings and preview behavior |
| `vite-conventions` | `risks` | Alias bypasses package public entry points or TypeScript path contracts<br>Library build bundles framework or peer dependencies into published output<br>Plugin order changes transform semantics for dev or build<br>Source maps dev server proxy or HMR changes are not validated in the mode they affect<br>Version-sensitive bundler options are changed without checking installed Vite |
| `vite-conventions` | `artifacts` | vite.config.*<br>vitest.config.* when shared Vite config affects tests<br>package.json dependencies peerDependencies exports and scripts<br>tsconfig*.json paths and module settings<br>dist build output source maps and generated package artifacts<br>.storybook main or preview files when Vite builder config is changed |
| `vite-conventions` | `repo` | Installed vite @vitejs/* and framework plugin versions<br>Existing Vite config for nearby projects<br>Package exports public entry points and TypeScript path aliases<br>Build dev preview and Storybook commands that consume the config |
| `vite-conventions` | `request` | Create or modify Vite config aliases plugins library build source maps dependency externalization or dev server settings<br>Review Vite behavior for build output dev server HMR plugin order public entry points or dependency bundling |
| `vitest-conventions` | `intents` | author or review Vitest unit, component, and Vite-integrated tests<br>change Vitest config, setup files, environments, globals, mocks, timers, workspaces, or isolation<br>diagnose flaky, over-mocked, environment-mismatched, or Vite-alias-sensitive Vitest tests |
| `vitest-conventions` | `surfaces` | vite-integrated-test-runner<br>vitest<br>unit-and-component-test-conventions<br>node-jsdom-happydom-or-browser-test-environment |
| `vitest-conventions` | `risks` | test environment does not match Node, DOM, browser, or Vite behavior under test<br>hoisted module mock changes imports beyond the intended boundary<br>setup file import cache prevents intended module mocking<br>fake timers, stubbed env, globals, or module mocks leak across tests<br>disabled isolation or shared worker state hides order dependence |
| `vitest-conventions` | `artifacts` | vitest.config.*<br>vite.config.* test property and Vite aliases used by tests<br>package.json Vitest scripts and workspace project config<br>setupFiles, globalSetup, environment, globals, isolate, pool, sequence, and projects config<br>vi.fn, vi.spyOn, vi.mock, vi.doMock, vi.hoisted, vi.useFakeTimers, vi.setSystemTime, vi.stubEnv, and vi.stubGlobal usage<br>import.meta.vitest guarded test code |
| `vitest-conventions` | `repo` | dependencies or scripts invoke vitest or @vitest packages<br>tests import test, expect, vi, beforeEach, or afterEach from vitest<br>repository has Vite config, Vitest setup files, workspace projects, DOM environment types, or Vite alias-dependent tests |
| `vitest-conventions` | `request` | mentions Vitest, vitest.config, Vite test config, vi.fn, vi.mock, import.meta.vitest, setupFiles, globals, fake timers, or test environment<br>asks to add, repair, review, or stabilize tests that run through Vitest |
| `vue-conventions` | `intents` | Design or review a Vue component surface<br>Keep Vue reactive ownership, public props, events, and slots explicit |
| `vue-conventions` | `surfaces` | Vue 3 Single-File Components, templates, script setup, Composition API, and composables<br>Props, emits, slots, defineExpose, defineModel, component names, refs, computed state, and watchers<br>Component tests, stories, examples, and docs that describe public component behavior |
| `vue-conventions` | `risks` | Template-facing state, prop, emit, or slot contract is untyped or cast around<br>Component mutates props or exposes more instance state than consumers need<br>Watcher duplicates derived state that should be computed<br>Composable extraction hides single-component behavior instead of capturing shared lifecycle<br>Vue macro or v-model pattern is used without checking the project Vue version and local style |
| `vue-conventions` | `artifacts` | *.vue files and TypeScript files importing from vue<br>Composable files, component tests, stories, fixture components, and component docs<br>Router, store, or service integration code that passes reactive values into components |
| `vue-conventions` | `repo` | Neighboring SFC structure, naming, prop, emit, slot, and composable conventions<br>Vue version, compiler macro support, lint rules, and typecheck command<br>Tests or stories that exercise public component behavior |
| `vue-conventions` | `request` | Create, modify, or review a Vue SFC, Composition API function, script setup block, prop, emit, slot, or composable<br>Type a Vue component public API or reactive state path<br>Review Vue naming, local SFC structure, derived state, watcher usage, or component extraction |
| `workspace-state-guard` | `intents` | Protect existing workspace changes<br>Classify dirty tree prior to edits<br>Control cleanup or destructive command scope |
| `workspace-state-guard` | `surfaces` | git status<br>local workspace<br>generated files<br>ignored files<br>branch cleanup<br>formatting or write operation |
| `workspace-state-guard` | `risks` | user changes may be overwritten<br>unrelated files may be staged or formatted<br>destructive git command may discard work<br>baseline failures may be misattributed<br>generated output may be hand-edited accidentally |
| `workspace-state-guard` | `artifacts` | git status output<br>scoped diff<br>ignored file listing<br>baseline validation output<br>cleanup plan |
| `workspace-state-guard` | `repo` | dirty tree<br>untracked files<br>ignored files<br>staged changes<br>current branch<br>generated outputs |
| `workspace-state-guard` | `request` | start substantial edits<br>clean up workspace<br>discard changes<br>format files<br>publish branch<br>handle dirty tree |

## Module To Lifecycle Phases

| Module | Phase | File |
| --- | --- | --- |
| `agent-delegation` | `activate` | `lifecycle/activate.md` |
| `agent-delegation` | `run` | `lifecycle/run.md` |
| `angular-conventions` | `activate` | `lifecycle/activate.md` |
| `angular-conventions` | `run` | `lifecycle/run.md` |
| `angular-conventions` | `review` | `lifecycle/review.md` |
| `angular-material-conventions` | `activate` | `lifecycle/activate.md` |
| `angular-material-conventions` | `run` | `lifecycle/run.md` |
| `angular-material-conventions` | `review` | `lifecycle/review.md` |
| `angular-tanstack-query-conventions` | `activate` | `lifecycle/activate.md` |
| `angular-tanstack-query-conventions` | `run` | `lifecycle/run.md` |
| `angular-tanstack-query-conventions` | `review` | `lifecycle/review.md` |
| `architecture-deepening-review` | `activate` | `lifecycle/activate.md` |
| `architecture-deepening-review` | `plan` | `lifecycle/plan.md` |
| `architecture-deepening-review` | `review` | `lifecycle/review.md` |
| `architecture-drift-detector` | `activate` | `lifecycle/activate.md` |
| `architecture-drift-detector` | `plan` | `lifecycle/plan.md` |
| `architecture-drift-detector` | `review` | `lifecycle/review.md` |
| `branch-completion` | `activate` | `lifecycle/activate.md` |
| `branch-completion` | `verify` | `lifecycle/verify.md` |
| `branch-completion` | `finalize` | `lifecycle/finalize.md` |
| `bricks` | `activate` | `lifecycle/activate.md` |
| `bricks` | `run` | `lifecycle/run.md` |
| `bricks` | `verify` | `lifecycle/verify.md` |
| `bundle-performance` | `activate` | `lifecycle/activate.md` |
| `bundle-performance` | `run` | `lifecycle/run.md` |
| `bundle-performance` | `review` | `lifecycle/review.md` |
| `bundle-performance` | `verify` | `lifecycle/verify.md` |
| `code-documentation` | `activate` | `lifecycle/activate.md` |
| `code-documentation` | `run` | `lifecycle/run.md` |
| `code-documentation` | `review` | `lifecycle/review.md` |
| `code-documentation` | `verify` | `lifecycle/verify.md` |
| `completion-verification` | `activate` | `lifecycle/activate.md` |
| `completion-verification` | `verify` | `lifecycle/verify.md` |
| `completion-verification` | `finalize` | `lifecycle/finalize.md` |
| `design-intake` | `activate` | `lifecycle/activate.md` |
| `design-intake` | `plan` | `lifecycle/plan.md` |
| `diary` | `activate` | `lifecycle/activate.md` |
| `diary` | `finalize` | `lifecycle/finalize.md` |
| `example-universe-enforcer` | `activate` | `lifecycle/activate.md` |
| `example-universe-enforcer` | `run` | `lifecycle/run.md` |
| `example-universe-enforcer` | `review` | `lifecycle/review.md` |
| `example-universe-enforcer` | `verify` | `lifecycle/verify.md` |
| `extraction-decision` | `activate` | `lifecycle/activate.md` |
| `extraction-decision` | `plan` | `lifecycle/plan.md` |
| `extraction-decision` | `review` | `lifecycle/review.md` |
| `grill-with-docs` | `activate` | `lifecycle/activate.md` |
| `grill-with-docs` | `plan` | `lifecycle/plan.md` |
| `implementation-plan` | `activate` | `lifecycle/activate.md` |
| `implementation-plan` | `plan` | `lifecycle/plan.md` |
| `issue-decomposition` | `activate` | `lifecycle/activate.md` |
| `issue-decomposition` | `plan` | `lifecycle/plan.md` |
| `jest-conventions` | `activate` | `lifecycle/activate.md` |
| `jest-conventions` | `run` | `lifecycle/run.md` |
| `jest-conventions` | `review` | `lifecycle/review.md` |
| `jest-conventions` | `verify` | `lifecycle/verify.md` |
| `library-placement-decision` | `activate` | `lifecycle/activate.md` |
| `library-placement-decision` | `plan` | `lifecycle/plan.md` |
| `library-placement-decision` | `review` | `lifecycle/review.md` |
| `naming-consistency` | `activate` | `lifecycle/activate.md` |
| `naming-consistency` | `plan` | `lifecycle/plan.md` |
| `naming-consistency` | `review` | `lifecycle/review.md` |
| `nestjs-conventions` | `activate` | `lifecycle/activate.md` |
| `nestjs-conventions` | `run` | `lifecycle/run.md` |
| `nestjs-conventions` | `review` | `lifecycle/review.md` |
| `nestjs-mongoose-conventions` | `activate` | `lifecycle/activate.md` |
| `nestjs-mongoose-conventions` | `run` | `lifecycle/run.md` |
| `nestjs-mongoose-conventions` | `review` | `lifecycle/review.md` |
| `no-transitional-architecture` | `activate` | `lifecycle/activate.md` |
| `no-transitional-architecture` | `plan` | `lifecycle/plan.md` |
| `no-transitional-architecture` | `review` | `lifecycle/review.md` |
| `nx-conventions` | `activate` | `lifecycle/activate.md` |
| `nx-conventions` | `run` | `lifecycle/run.md` |
| `nx-conventions` | `review` | `lifecycle/review.md` |
| `nx-module-boundaries` | `activate` | `lifecycle/activate.md` |
| `nx-module-boundaries` | `plan` | `lifecycle/plan.md` |
| `nx-module-boundaries` | `review` | `lifecycle/review.md` |
| `plan-execution` | `activate` | `lifecycle/activate.md` |
| `plan-execution` | `run` | `lifecycle/run.md` |
| `playwright-conventions` | `activate` | `lifecycle/activate.md` |
| `playwright-conventions` | `run` | `lifecycle/run.md` |
| `playwright-conventions` | `review` | `lifecycle/review.md` |
| `playwright-conventions` | `verify` | `lifecycle/verify.md` |
| `prototype` | `activate` | `lifecycle/activate.md` |
| `prototype` | `plan` | `lifecycle/plan.md` |
| `public-api-design` | `activate` | `lifecycle/activate.md` |
| `public-api-design` | `plan` | `lifecycle/plan.md` |
| `public-api-design` | `review` | `lifecycle/review.md` |
| `review-feedback-triage` | `review` | `lifecycle/review.md` |
| `review-gate` | `review` | `lifecycle/review.md` |
| `rxjs-conventions` | `activate` | `lifecycle/activate.md` |
| `rxjs-conventions` | `run` | `lifecycle/run.md` |
| `rxjs-conventions` | `review` | `lifecycle/review.md` |
| `skill-evolution` | `activate` | `lifecycle/activate.md` |
| `skill-evolution` | `plan` | `lifecycle/plan.md` |
| `skill-evolution` | `run` | `lifecycle/run.md` |
| `skill-evolution` | `review` | `lifecycle/review.md` |
| `storybook-angular-conventions` | `activate` | `lifecycle/activate.md` |
| `storybook-angular-conventions` | `run` | `lifecycle/run.md` |
| `storybook-angular-conventions` | `review` | `lifecycle/review.md` |
| `storybook-conventions` | `activate` | `lifecycle/activate.md` |
| `storybook-conventions` | `run` | `lifecycle/run.md` |
| `storybook-conventions` | `review` | `lifecycle/review.md` |
| `systematic-debugging` | `activate` | `lifecycle/activate.md` |
| `systematic-debugging` | `run` | `lifecycle/run.md` |
| `systematic-debugging` | `review` | `lifecycle/review.md` |
| `systematic-debugging` | `verify` | `lifecycle/verify.md` |
| `test-first-discipline` | `activate` | `lifecycle/activate.md` |
| `test-first-discipline` | `run` | `lifecycle/run.md` |
| `test-first-discipline` | `review` | `lifecycle/review.md` |
| `test-first-discipline` | `verify` | `lifecycle/verify.md` |
| `typescript-api-conventions` | `activate` | `lifecycle/activate.md` |
| `typescript-api-conventions` | `run` | `lifecycle/run.md` |
| `typescript-api-conventions` | `review` | `lifecycle/review.md` |
| `typescript-code-style` | `activate` | `lifecycle/activate.md` |
| `typescript-code-style` | `run` | `lifecycle/run.md` |
| `typescript-code-style` | `review` | `lifecycle/review.md` |
| `vite-conventions` | `activate` | `lifecycle/activate.md` |
| `vite-conventions` | `run` | `lifecycle/run.md` |
| `vite-conventions` | `review` | `lifecycle/review.md` |
| `vitest-conventions` | `activate` | `lifecycle/activate.md` |
| `vitest-conventions` | `run` | `lifecycle/run.md` |
| `vitest-conventions` | `review` | `lifecycle/review.md` |
| `vitest-conventions` | `verify` | `lifecycle/verify.md` |
| `vue-conventions` | `activate` | `lifecycle/activate.md` |
| `vue-conventions` | `run` | `lifecycle/run.md` |
| `vue-conventions` | `review` | `lifecycle/review.md` |
| `workspace-state-guard` | `activate` | `lifecycle/activate.md` |
