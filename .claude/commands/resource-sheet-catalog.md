---
⚠️ **DEPRECATED** - This catalog is now integrated into MCP tool
---

# DEPRECATION NOTICE

**Status:** Deprecated as of 2026-01-03
**New Location:** Integrated into `mcp__coderef-docs__generate_resource_sheet`

This element type catalog is **deprecated** and kept for reference only.

## What Changed

The 20 element type classifications are now built into the MCP tool as **conditional modules**:
- ✅ **Auto-detection** via 3-stage algorithm (filename → code analysis → fallback)
- ✅ **Element-specific overlays** applied automatically based on detected type
- ✅ **Confidence scoring** for detection accuracy (80-95%)
- ✅ **Manual override** via `element_type` parameter if needed

## Migration

**No action required** - element types are auto-detected by MCP tool.

## Reference

- **Synthesis:** `C:\Users\willh\.mcp-servers\coderef\sessions\reference-sheet-reconciliation\orchestrator-output.md`
- **Papertrail Output:** `papertrail-output.md` (unified template schema with 20 element overlays)
- **Workorder:** WO-RESOURCE-SHEET-CONSOLIDATION-001

---

# Resource Sheet Catalog — Element Classification & Templates (LEGACY)

## Overview
This catalog defines **20 high-ROI code element types** for authoritative resource sheet documentation, ordered by impact on onboarding and maintenance. Each element type has a specialized focus template.

---

## Master Classification Table

| Rank | Element Type | Primary Focus Areas | Maintenance Impact |
|------|--------------|---------------------|-------------------|
| 1 | Top-level widgets/pages | Composition, orchestration, user workflows | Critical - entry points |
| 2 | Stateful containers/controllers | State ownership, coordination, persistence | Critical - state authority |
| 3 | Global state layer | Store shape, actions, derived state | Critical - app-wide contracts |
| 4 | Custom hooks library | Side effects, cleanup, dependencies | High - reuse patterns |
| 5 | API client layer | Endpoints, auth, error handling | High - external contracts |
| 6 | Data model & schemas | Canonical shapes, versioning, migrations | High - type safety |
| 7 | Persistence subsystem | Keys, hydration, conflict resolution | High - durability contracts |
| 8 | Eventing/messaging | Event contracts, ordering, cross-tab sync | High - async coordination |
| 9 | Routing & navigation | Route map, guards, transitions | Medium - UX flows |
| 10 | File/tree domain primitives | Path utilities, indexing, selection | Medium - core abstractions |
| 11 | Context menu/command system | Actions registry, permissions | Medium - user actions |
| 12 | Permission & authZ layer | Roles, capabilities, enforcement | Medium - security |
| 13 | Error handling system | Categories, recovery flows | Medium - resilience |
| 14 | Logging/telemetry/analytics | Event schemas, privacy | Medium - observability |
| 15 | Performance-critical UI | Budgets, profiling, virtualization | Medium - UX quality |
| 16 | Design system components | Props, a11y, variants | Medium - consistency |
| 17 | Theming & styling | Tokens, dark mode, customization | Low - visual layer |
| 18 | Build & tooling scripts | Inputs/outputs, CI integration | Low - DX automation |
| 19 | CI/CD pipelines | Stages, artifacts, debugging | Low - deployment |
| 20 | Testing harness & utilities | Patterns, mocks, golden paths | Low - quality infrastructure |

---

## Element-Specific Templates

### Template 1: Top-Level Widgets/Pages (Entry Components)

**Use for:** `CodeRefExplorerWidget`, `Dashboard`, `ProjectPage`, etc.

#### Focus Areas Checklist
- [ ] **Composition hierarchy** — Which subcomponents, what order, why
- [ ] **User workflows** — Primary task flows this widget enables
- [ ] **State orchestration** — What state this widget owns vs delegates
- [ ] **Integration points** — External systems/contexts consumed
- [ ] **Layout contracts** — Fixed dimensions, responsive behavior
- [ ] **Lifecycle events** — Mount/unmount side effects
- [ ] **Performance budget** — Target render times, bundle size
- [ ] **Accessibility root** — Focus management, keyboard navigation

#### Required Sections
1. **Role in UX** — What users accomplish here
2. **Component Hierarchy** (visual tree)
3. **State Ownership Table** (canonical)
4. **Layout Contracts** (dimensions, overflow, positioning)
5. **Event Flow Diagram** (user actions → state changes → side effects)
6. **Performance Characteristics** (tested limits, bottlenecks)
7. **Accessibility Guarantees** (roles, keyboard nav, screen reader)
8. **Common Integration Pitfalls**

---

### Template 2: Stateful Containers/Controllers

**Use for:** `useProjectManager`, `FileTreeController`, `AuthProvider`, etc.

#### Focus Areas Checklist
- [ ] **State ownership rules** — What state lives here vs elsewhere
- [ ] **Coordination logic** — How child state is reconciled
- [ ] **Persistence strategy** — What persists, when, where
- [ ] **Cache invalidation** — Staleness detection, refresh triggers
- [ ] **Error boundaries** — What errors are caught, how recovered
- [ ] **Subscription management** — Event listeners, cleanup guarantees
- [ ] **Initialization sequence** — Hydration, validation, migration
- [ ] **Testing isolation** — How to mock dependencies

#### Required Sections
1. **State Authority Table** (canonical source of truth)
2. **Lifecycle Diagram** (init → hydrate → validate → runtime → cleanup)
3. **Persistence Contract** (keys, schema, versioning)
4. **Event Subscriptions** (what events, cleanup guarantees)
5. **Error Handling** (failure modes, recovery paths)
6. **Testing Strategy** (mock boundaries, critical scenarios)
7. **Performance Considerations** (re-render triggers, memoization)
8. **Migration Playbook** (breaking changes, rollback)

---

### Template 3: Global State Layer (Redux/Zustand/Context)

**Use for:** `store.ts`, `AppContext`, `GlobalStateProvider`, etc.

#### Focus Areas Checklist
- [ ] **Store shape** — Full TypeScript schema
- [ ] **Actions catalog** — All actions, payloads, side effects
- [ ] **Selectors library** — Derived state, memoization strategy
- [ ] **Persistence mapping** — What slices persist, where
- [ ] **Middleware stack** — Logger, thunk, persistence, order matters
- [ ] **Devtools integration** — Time travel, action replay
- [ ] **Hydration strategy** — Server/client reconciliation
- [ ] **Testing approach** — Store mocking, action testing

#### Required Sections
1. **Store Schema** (full TypeScript interface)
2. **Actions Reference** (table: action → payload → reducer → side effects)
3. **Selectors Catalog** (derived state, memoization rules)
4. **Persistence Contract** (keys, serialization, hydration)
5. **Middleware Order** (execution sequence, why it matters)
6. **State Migration Playbook** (version bumps, data transforms)
7. **Performance Constraints** (selector re-compute budgets)
8. **Testing Patterns** (mock store, action creators, reducers)

---

### Template 4: Custom Hooks Library

**Use for:** `useLocalStorage`, `useFetch`, `useTreeExpansion`, etc.

#### Focus Areas Checklist
- [ ] **Side effects** — Network, storage, subscriptions, timers
- [ ] **Cleanup guarantees** — What happens on unmount
- [ ] **Dependency array** — What triggers re-run, common mistakes
- [ ] **Return contract** — Shape, loading states, error states
- [ ] **Stale closure bugs** — Known pitfalls with captured values
- [ ] **Composition patterns** — How hooks combine
- [ ] **Testing approach** — renderHook patterns
- [ ] **Performance gotchas** — Infinite loops, memory leaks

#### Required Sections
1. **Hook Signature** (TypeScript, JSDoc)
2. **Side Effects Catalog** (what runs, when, cleanup)
3. **Dependency Rules** (what triggers re-run, why)
4. **Return Contract** (loading/error/data states)
5. **Common Pitfalls** (stale closures, infinite loops)
6. **Composition Examples** (combining hooks safely)
7. **Testing Patterns** (renderHook, mocking dependencies)
8. **Performance Notes** (re-run frequency, optimization)

---

### Template 5: API Client Layer

**Use for:** `apiClient.ts`, `graphqlClient.ts`, `sdk.ts`, etc.

#### Focus Areas Checklist
- [ ] **Endpoint catalog** — All endpoints, methods, payloads
- [ ] **Auth strategy** — Token management, refresh flow
- [ ] **Retry logic** — Exponential backoff, max attempts
- [ ] **Error taxonomy** — Network, auth, validation, server errors
- [ ] **Response normalization** — Data transformation pipeline
- [ ] **Caching strategy** — What caches, TTL, invalidation
- [ ] **Rate limiting** — Client-side throttling
- [ ] **Testing mocks** — MSW patterns, fixture data

#### Required Sections
1. **Endpoint Reference** (table: endpoint → method → request → response)
2. **Auth Flow Diagram** (token acquisition, refresh, expiry)
3. **Error Taxonomy** (categories, user-facing messages, recovery)
4. **Retry Strategy** (backoff algorithm, max attempts, idempotency)
5. **Response Normalization** (transforms, versioning)
6. **Cache Contract** (keys, TTL, invalidation triggers)
7. **Rate Limiting** (client throttle, server limits)
8. **Testing Approach** (MSW setup, fixture management)

---

### Template 6: Data Model & Schemas

**Use for:** `types.ts`, `schema.ts`, `validators.ts`, etc.

#### Focus Areas Checklist
- [ ] **Canonical TypeScript types** — Full schema
- [ ] **Validation rules** — Runtime checks (zod/io-ts)
- [ ] **Versioning strategy** — Schema evolution, migrations
- [ ] **JSON Schema** — For tooling/docs
- [ ] **Default values** — Required vs optional, sensible defaults
- [ ] **Discriminated unions** — Type narrowing patterns
- [ ] **Serialization** — JSON, FormData, query params
- [ ] **Testing validation** — Edge cases, malformed data

#### Required Sections
1. **Schema Definition** (full TypeScript interfaces)
2. **Validation Rules** (runtime checks, error messages)
3. **Versioning Strategy** (version field, migration functions)
4. **Default Values Table** (field → default → rationale)
5. **Type Narrowing** (discriminated unions, type guards)
6. **Serialization Formats** (JSON, FormData, URL encoding)
7. **Migration Playbook** (v1 → v2 transforms)
8. **Testing Patterns** (valid/invalid fixtures)

---

### Template 7: Persistence Subsystem

**Use for:** `storage.ts`, `cache.ts`, `indexedDB.ts`, etc.

#### Focus Areas Checklist
- [ ] **Storage keys catalog** — All keys, formats, ownership
- [ ] **Hydration sequence** — Read → validate → migrate → init
- [ ] **Conflict resolution** — Cross-tab, server sync
- [ ] **Quota behavior** — Full disk, eviction policy
- [ ] **Versioning** — Schema migrations, rollback
- [ ] **Serialization** — JSON, binary, compression
- [ ] **Security** — What's sensitive, encryption needs
- [ ] **Testing approach** — Mock storage, quota simulation

#### Required Sections
1. **Keys Catalog** (table: key → schema → owner → persistence)
2. **Hydration Lifecycle** (read → validate → migrate → apply)
3. **Conflict Resolution** (cross-tab, last-write-wins, merge strategies)
4. **Quota Management** (limits, eviction, user warnings)
5. **Versioning Contract** (version field, migration functions)
6. **Serialization Format** (JSON, binary, compression)
7. **Security Considerations** (sensitive data, encryption)
8. **Testing Strategy** (mock storage, quota errors, migrations)

---

### Template 8: Eventing/Messaging

**Use for:** `eventBus.ts`, `messageHub.ts`, `storageSync.ts`, etc.

#### Focus Areas Checklist
- [ ] **Event catalog** — All event types, payloads
- [ ] **Ordering guarantees** — FIFO, causality, batching
- [ ] **Cross-tab sync** — Storage events, BroadcastChannel
- [ ] **Debouncing/throttling** — Rate limiting, coalescing
- [ ] **Subscription lifecycle** — Subscribe, unsubscribe, leaks
- [ ] **Error handling** — Handler failures, dead letters
- [ ] **Testing approach** — Event simulation, timing
- [ ] **Performance** — Handler execution budgets

#### Required Sections
1. **Event Catalog** (table: event → payload → handlers → side effects)
2. **Ordering Guarantees** (FIFO, batching, race conditions)
3. **Cross-Tab Sync** (mechanism, conflict resolution)
4. **Debounce/Throttle Strategy** (timeouts, coalescing)
5. **Subscription Management** (register, unregister, cleanup)
6. **Error Handling** (handler failures, retry, dead letters)
7. **Performance Budgets** (handler execution limits)
8. **Testing Patterns** (event simulation, async timing)

---

### Template 9: Routing & Navigation

**Use for:** `router.ts`, `routes.ts`, `navigation.ts`, etc.

#### Focus Areas Checklist
- [ ] **Route map** — All routes, params, query contracts
- [ ] **Route guards** — Auth, permissions, redirects
- [ ] **Deep linking** — URL structure, shareable links
- [ ] **Query param contracts** — Expected params, types
- [ ] **Transition lifecycle** — Before/after hooks
- [ ] **History management** — Back/forward, replace vs push
- [ ] **Testing approach** — Route rendering, guards
- [ ] **Performance** — Code splitting, lazy loading

#### Required Sections
1. **Route Map** (table: path → component → guards → params)
2. **Route Guards** (auth, permissions, redirect logic)
3. **Deep Link Schema** (URL structure, query params)
4. **Transition Lifecycle** (beforeEach, afterEach hooks)
5. **History Management** (push, replace, back/forward)
6. **Code Splitting** (lazy routes, bundle strategy)
7. **Testing Patterns** (route rendering, guard execution)
8. **SEO Considerations** (meta tags, canonical URLs)

---

### Template 10: File/Tree Domain Primitives

**Use for:** `TreeNode.ts`, `PathUtils.ts`, `FileIndex.ts`, etc.

#### Focus Areas Checklist
- [ ] **Data structures** — Tree shape, node schema
- [ ] **Path utilities** — Normalization, joining, resolution
- [ ] **Indexing strategy** — Map/Set structures, lookup perf
- [ ] **Selection semantics** — Single, multi, range
- [ ] **Favorites/bookmarks** — Storage, sync, limits
- [ ] **Sorting/filtering** — Algorithms, custom comparators
- [ ] **Testing approach** — Edge cases, deep trees
- [ ] **Performance** — Tree depth limits, node counts

#### Required Sections
1. **Tree Schema** (node structure, parent/child links)
2. **Path Utilities Reference** (functions, normalization rules)
3. **Indexing Strategy** (data structures, lookup complexity)
4. **Selection Semantics** (single/multi/range, keyboard nav)
5. **Favorites Contract** (storage, limits, sync)
6. **Sort/Filter Algorithms** (comparators, performance)
7. **Performance Limits** (tested depth/breadth)
8. **Testing Patterns** (edge cases, deep trees)

---

### Template 11: Context Menu/Command System

**Use for:** `contextMenu.ts`, `commandRegistry.ts`, `actions.ts`, etc.

#### Focus Areas Checklist
- [ ] **Actions catalog** — All actions, handlers, shortcuts
- [ ] **Permissions** — Who can see/trigger actions
- [ ] **Enable/disable logic** — Dynamic availability
- [ ] **Analytics hooks** — Tracking action usage
- [ ] **Positioning** — Menu placement, overflow handling
- [ ] **Keyboard shortcuts** — Key bindings, conflicts
- [ ] **Testing approach** — Action execution, permissions
- [ ] **Accessibility** — Focus trap, screen reader announcements

#### Required Sections
1. **Actions Catalog** (table: action → handler → permissions → shortcut)
2. **Permissions Model** (roles, capabilities, visibility rules)
3. **Enable/Disable Logic** (dynamic availability rules)
4. **Analytics Integration** (event tracking, payloads)
5. **Positioning Strategy** (viewport detection, overflow)
6. **Keyboard Shortcuts** (bindings, conflict resolution)
7. **Testing Patterns** (action execution, permissions checks)
8. **Accessibility** (focus management, ARIA roles)

---

### Template 12: Permission & AuthZ Layer

**Use for:** `permissions.ts`, `authz.ts`, `rbac.ts`, etc.

#### Focus Areas Checklist
- [ ] **Roles catalog** — All roles, inheritance
- [ ] **Capabilities** — Granular permissions
- [ ] **UI gating** — Component visibility rules
- [ ] **Server enforcement** — API-level checks
- [ ] **Policy language** — How rules are expressed
- [ ] **Testing approach** — Role simulation, edge cases
- [ ] **Performance** — Permission check frequency
- [ ] **Audit logging** — Access attempts, denials

#### Required Sections
1. **Roles Catalog** (table: role → capabilities → inheritance)
2. **Capabilities Reference** (granular permissions)
3. **UI Gating Strategy** (component-level checks)
4. **Server Enforcement** (API-level validation)
5. **Policy Language** (rule syntax, composition)
6. **Testing Patterns** (role simulation, matrix testing)
7. **Performance Considerations** (check caching, frequency)
8. **Audit Logging** (access tracking, compliance)

---

### Template 13: Error Handling System

**Use for:** `errorBoundary.tsx`, `errorHandler.ts`, `toasts.ts`, etc.

#### Focus Areas Checklist
- [ ] **Error categories** — Network, validation, auth, server
- [ ] **User-facing messages** — Copy, tone, actionability
- [ ] **Recovery flows** — Retry, reset, fallback
- [ ] **Error boundaries** — Scope, fallback UI
- [ ] **Logging integration** — Sentry, console, analytics
- [ ] **Testing approach** — Error simulation, boundary rendering
- [ ] **Performance** — Toast limits, memory leaks
- [ ] **Accessibility** — Screen reader announcements, focus

#### Required Sections
1. **Error Taxonomy** (categories, severity, user impact)
2. **User Messaging** (templates, tone, CTAs)
3. **Recovery Flows** (retry logic, fallback strategies)
4. **Error Boundaries** (scope, fallback UI, reset)
5. **Logging Integration** (Sentry, console, analytics)
6. **Testing Patterns** (error simulation, boundary rendering)
7. **Performance Constraints** (toast queue limits)
8. **Accessibility** (announcements, focus management)

---

### Template 14: Logging/Telemetry/Analytics

**Use for:** `analytics.ts`, `telemetry.ts`, `logger.ts`, etc.

#### Focus Areas Checklist
- [ ] **Event naming** — Conventions, taxonomy
- [ ] **Payload schemas** — Required/optional fields
- [ ] **Privacy constraints** — PII scrubbing, consent
- [ ] **Sampling strategy** — Rate limiting, quotas
- [ ] **Provider integration** — GA, Mixpanel, Sentry
- [ ] **Testing approach** — Event verification, mocks
- [ ] **Performance** — Async batching, quota limits
- [ ] **Debugging** — Console logging, debug mode

#### Required Sections
1. **Event Taxonomy** (naming conventions, categories)
2. **Payload Schemas** (table: event → required fields → optional)
3. **Privacy Constraints** (PII scrubbing, consent checks)
4. **Sampling Strategy** (rate limiting, quotas)
5. **Provider Integration** (GA, Mixpanel, Sentry setup)
6. **Testing Patterns** (event verification, mock analytics)
7. **Performance Considerations** (batching, quota management)
8. **Debugging Tools** (console logging, debug flags)

---

### Template 15: Performance-Critical UI Components

**Use for:** `VirtualTree.tsx`, `CodeEditor.tsx`, `Canvas.tsx`, etc.

#### Focus Areas Checklist
- [ ] **Performance budgets** — Target FPS, render time
- [ ] **Profiling setup** — React DevTools, Chrome profiling
- [ ] **Virtualization** — Window size, overscan, scroll perf
- [ ] **Memoization** — useMemo, React.memo, when to use
- [ ] **Bottleneck analysis** — Known slow paths
- [ ] **Testing approach** — Performance regression tests
- [ ] **Optimization history** — What was tried, what worked
- [ ] **Monitoring** — Production perf metrics

#### Required Sections
1. **Performance Budgets** (target FPS, render times, bundle size)
2. **Profiling Guide** (tools, metrics, interpretation)
3. **Virtualization Strategy** (window size, overscan, scroll)
4. **Memoization Rules** (when to memo, dependencies)
5. **Bottleneck Catalog** (known slow paths, fixes)
6. **Testing Approach** (regression tests, benchmarks)
7. **Optimization History** (timeline of improvements)
8. **Monitoring** (production metrics, alerting)

---

### Template 16: Design System Components

**Use for:** `Button.tsx`, `Modal.tsx`, `Input.tsx`, etc.

#### Focus Areas Checklist
- [ ] **Props API** — All props, types, defaults
- [ ] **Variants catalog** — Primary, secondary, sizes
- [ ] **Accessibility guarantees** — Roles, labels, keyboard
- [ ] **Theming tokens** — Colors, spacing, typography
- [ ] **Composition patterns** — How components combine
- [ ] **Testing approach** — Visual regression, a11y audits
- [ ] **Performance** — Re-render frequency
- [ ] **Migration notes** — Breaking changes from old versions

#### Required Sections
1. **Props Reference** (table: prop → type → default → description)
2. **Variants Catalog** (visual examples, use cases)
3. **Accessibility Guarantees** (ARIA roles, keyboard nav, labels)
4. **Theming Tokens** (colors, spacing, typography used)
5. **Composition Examples** (combining components safely)
6. **Testing Patterns** (visual regression, a11y audits)
7. **Performance Notes** (re-render triggers, optimization)
8. **Migration Guide** (breaking changes, deprecations)

---

### Template 17: Theming & Styling System

**Use for:** `theme.ts`, `tokens.css`, `tailwind.config.js`, etc.

#### Focus Areas Checklist
- [ ] **Token map** — All tokens, values, semantic meaning
- [ ] **Dark mode** — Toggle mechanism, token overrides
- [ ] **Customization points** — What users can override
- [ ] **Anti-patterns** — Avoid magic numbers, inline styles
- [ ] **Responsive strategy** — Breakpoints, mobile-first
- [ ] **Testing approach** — Visual regression, theme switching
- [ ] **Performance** — CSS bundle size, runtime overhead
- [ ] **Migration** — From old theme system

#### Required Sections
1. **Token Map** (table: token → light value → dark value → usage)
2. **Dark Mode Strategy** (toggle mechanism, overrides)
3. **Customization API** (what's overridable, how)
4. **Anti-Patterns** (avoid magic numbers, inline styles)
5. **Responsive Strategy** (breakpoints, mobile-first rules)
6. **Testing Patterns** (visual regression, theme switching)
7. **Performance Considerations** (bundle size, runtime cost)
8. **Migration Guide** (from old theme system)

---

### Template 18: Build & Tooling Scripts

**Use for:** `build.js`, `codegen.ts`, `scripts/`, etc.

#### Focus Areas Checklist
- [ ] **Purpose** — What the script does, why it exists
- [ ] **Inputs/outputs** — Files, env vars, CLI args
- [ ] **Safe usage** — Dry-run mode, validation
- [ ] **CI integration** — When it runs, dependencies
- [ ] **Error handling** — Failure modes, rollback
- [ ] **Testing approach** — Unit tests, integration tests
- [ ] **Performance** — Execution time, parallelization
- [ ] **Debugging** — Verbose mode, logs

#### Required Sections
1. **Script Purpose** (what it does, when to use)
2. **Inputs/Outputs** (files, env vars, CLI args)
3. **Usage Examples** (common invocations, dry-run)
4. **CI Integration** (when it runs, job dependencies)
5. **Error Handling** (failure modes, rollback strategies)
6. **Testing Strategy** (unit tests, integration tests)
7. **Performance Notes** (execution time, optimization)
8. **Debugging Guide** (verbose mode, log interpretation)

---

### Template 19: CI/CD Pipelines

**Use for:** `.github/workflows/`, `deploy.yml`, etc.

#### Focus Areas Checklist
- [ ] **Pipeline stages** — Build, test, deploy sequence
- [ ] **Artifacts** — What's produced, where stored
- [ ] **Environment variables** — Secrets, config
- [ ] **Rollback strategy** — How to revert deployments
- [ ] **Debugging failures** — Logs, re-run, local repro
- [ ] **Testing integration** — Test suites, coverage gates
- [ ] **Performance** — Build times, caching
- [ ] **Security** — Secret management, permissions

#### Required Sections
1. **Pipeline Overview** (stages, dependencies, triggers)
2. **Artifacts Catalog** (what's built, where stored, retention)
3. **Environment Variables** (secrets, config, usage)
4. **Rollback Playbook** (revert deployment, hotfix)
5. **Debugging Guide** (log interpretation, local repro)
6. **Testing Integration** (test suites, coverage requirements)
7. **Performance Optimization** (build times, caching strategy)
8. **Security Practices** (secret rotation, permissions)

---

### Template 20: Testing Harness & Utilities

**Use for:** `test-utils.tsx`, `mocks/`, `fixtures/`, etc.

#### Focus Areas Checklist
- [ ] **Standard patterns** — Setup, teardown, assertions
- [ ] **Mock boundaries** — What to mock, what to test real
- [ ] **Fixture management** — Realistic test data, generators
- [ ] **Golden-path suites** — Critical user flows
- [ ] **Async testing** — waitFor, act, timing issues
- [ ] **Coverage targets** — Line, branch, statement goals
- [ ] **Performance** — Test execution time, parallelization
- [ ] **Debugging** — Isolated runs, verbose output

#### Required Sections
1. **Standard Patterns** (setup, teardown, common assertions)
2. **Mock Boundaries** (what to mock, integration points)
3. **Fixture Catalog** (realistic test data, generators)
4. **Golden-Path Suites** (critical user flows, coverage)
5. **Async Testing** (waitFor patterns, timing gotchas)
6. **Coverage Targets** (line/branch/statement goals)
7. **Performance Optimization** (execution time, parallelization)
8. **Debugging Guide** (isolated runs, verbose mode)

---

## Master Checklist (All Element Types)

Use this checklist when creating any resource sheet to ensure comprehensive coverage:

### Core Documentation (Always Required)
- [ ] Executive Summary (2-4 sentences)
- [ ] Audience & Intent (authority hierarchy)
- [ ] Architecture Overview
- [ ] State Ownership Table (if stateful)
- [ ] Integration Points
- [ ] Common Pitfalls

### Element-Specific (Based on Type)
- [ ] Props/API Reference (components, hooks, APIs)
- [ ] Event Catalog (eventing, UI components)
- [ ] Lifecycle Diagram (stateful systems)
- [ ] Persistence Contract (storage, caching)
- [ ] Error Taxonomy (error handling, APIs)
- [ ] Performance Budgets (critical UI, builds)
- [ ] Accessibility Guarantees (UI components, pages)
- [ ] Testing Strategy (all types)

### Quality Gates
- [ ] No ambiguous "should" statements
- [ ] Tables for structured data
- [ ] Diagrams marked illustrative
- [ ] Failure modes documented
- [ ] Recovery paths specified
- [ ] Non-goals explicit
- [ ] Refactor-safe contracts
- [ ] Migration playbook (if versioned)

---

## Usage Workflow

1. **Identify element type** from classification table (1-20)
2. **Select template** matching element type
3. **Apply focus areas checklist** for that template
4. **Generate resource sheet** using `/create-resource-sheet`
5. **Validate against master checklist**
6. **Review for refactor safety** (can new dev refactor without breaking?)
7. **Commit to codebase** alongside code

---

## Integration with `/create-resource-sheet`

```bash
# Base command generates general resource sheet
/create-resource-sheet WorkflowEngine backend

# Specify element type for specialized template
/create-resource-sheet WorkflowEngine backend --type stateful-container

# Element type auto-detected from context
/create-resource-sheet useLocalStorage  # Detects: custom hook (Template 4)
/create-resource-sheet Button.tsx       # Detects: design system (Template 16)
/create-resource-sheet store.ts         # Detects: global state (Template 3)
```

---

## Maintenance Protocol

When element type changes (e.g., hook becomes service):
1. Update classification in catalog
2. Apply new template requirements
3. Archive old sections with `⚠️ DEPRECATED`
4. Add migration notes for consumers

---

**Maintained by:** CodeRef Assistant (Orchestrator Persona)
**Catalog Version:** 1.0.0
**Created:** 2026-01-02
**Total Element Types:** 20
