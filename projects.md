# Projects

> Last updated: 2025-12-24
> Next STUB-ID: STUB-057

---

## Active Projects

| ID | Name | Description | Path | Git | Deploy |
|----|------|-------------|------|-----|--------|
| STUB-013 | app-documents | Selector engine | `C:\Users\willh\Desktop\app_documents` | — | [local](file:///C:/Users/willh/Desktop/App_Documents/index.html) |
| STUB-014 | mcp-servers | MCP servers home | `C:\Users\willh\.mcp-servers` | — | [local](file:///C:/Users/willh/.mcp-servers/index.html) |
| STUB-015 | scrapper | NFL stats database | `C:\Users\willh\Desktop\scrapper` | — | [vercel](https://scrapper-teamhart.vercel.app/) |
| STUB-016 | assistant | Orchestrator CLI | `C:\Users\willh\Desktop\assistant` | — | [local](file:///C:/Users/willh/Desktop/assistant/index.html) |
| STUB-017 | gridiron-franchise | Football sim | `C:\Users\willh\Desktop\latest-sim\gridiron-franchise` | — | [vercel](https://gridiron-franchise.vercel.app/) |
| STUB-018 | noted | Notes app | `C:\Users\willh\Desktop\projects\noted` | — | [vercel](https://noted-bay-three.vercel.app/auth) |
| STUB-019 | scriptboard | Desktop utility + LLM workflows | `C:\Users\willh\Desktop\clipboard_compannion\next` | — | [vercel](https://frontend-ten-delta-77.vercel.app/) |
| STUB-021 | coderef-system | CodeRef system | `C:\Users\willh\Desktop\projects\coderef-system` | — | — |
| STUB-022 | next-multi-tenant | Multi-tenant app | `C:\Users\willh\Desktop\Business-Dash\latest-app` | — | — |

---

## Stubs - High Priority

| STUB-ID | Name | Category | Description |
|---------|------|----------|-------------|
| STUB-001 | scriptboard-assistant-integration | feature | Make Scriptboard the primary visual UI for this CLI assistant |
| STUB-002 | tool-inventory-workflow | feature | Orchestrator to delegate documentation to embedded agents |
| STUB-003 | saas-mvp-candidates | idea | Identify monetizable app/SAAS ideas |
| STUB-007 | mcp-saas-platform | feature | Lloyd.ai - full SaaS platform (has SPEC.md) |
| STUB-008 | workorder-handoff-protocol | feature | Standard protocol for delegating to project agents |
| STUB-009 | plan-progress-tracking | fix | Agents should update plan.json task status |
| STUB-023 | workorder-tracker-ui | feature | Orchestrator workflow + Scriptboard dashboard for tracking workorders via communication.json |
| STUB-027 | orchestrator-mcp | feature | MCP server with orchestrator tools (stub, delegate, track) + assistant persona |
| STUB-028 | plan-audit-workflow | feature | Audit all plan.json across projects, surface stale/active plans via file indexer |
| STUB-029 | gridiron-pages-needed | feature | Core gameplay pages for Gridiron (box score, stats, trades, draft, etc.) |
| STUB-030 | internal-plan-tracking | feature | Track plans that originate inside projects without orchestrator delegation |
| STUB-031 | agent-git-branches | feature | Git branches per agent/workorder via git manager, orchestrator manages merges |
| STUB-032 | enforce-plan-json | improvement | Agents must save plans as plan.json in standard format for orchestrator discovery |
| STUB-034 | uds-review-update | improvement | Review and update UDS to match current system documents |
| STUB-049 | agent-completion-workflow | improvement | Clarify agent archives features, orchestrator only verifies |
| STUB-053 | mcp-docs-workflow-refactor | refactor | Refactor docs-mcp to separate concerns: coderef-context, coderef-docs, coderef-workorder |
| STUB-054 | persona-role-context-system | feature | Build role-specific personas with dynamic context loading (Widget Architect proof-of-concept) |
| STUB-055 | personas-ecosystem-architecture | feature | Comprehensive personas ecosystem: standardize structure, update all personas with coderef awareness, finalize architecture |
| STUB-056 | known-issues-utility | feature | Known issues registry: agents log bugs + fixes for future reference, searchable by error/tag/project |

---

## Stubs - Medium Priority

| STUB-ID | Name | Category | Description |
|---------|------|----------|-------------|
| STUB-004 | reorganize-gits-projects | refactor | Consolidate scattered git repos |
| STUB-005 | consolidate-project-directories | refactor | Logical directory structure |
| STUB-006 | instant-interactives | idea | Interactive content app (gifts, quizzes, surveys) |
| STUB-010 | incremental-testing-workflow | improvement | Test as you build, not at the end |
| STUB-011 | stub-id-system | feature | Auto-incrementing STUB-ID system |
| STUB-012 | mcp-server-cleanup | refactor | Audit and remove unused MCP tools |
| STUB-024 | research-scout-agent | feature | Research assistant to scout tasks, explore feasibility, refine ideas |
| STUB-020 | terminal-settings-sync | feature | Scriptboard UI to configure Windows Terminal project profiles |
| STUB-025 | loveable-scrapper-engagements | feature | Integrate Loveable engagement features into NFL Scrapper app |
| STUB-026 | mcp-usage-tracker | feature | Track tool and slash command usage across MCP servers |
| STUB-033 | stub-tag-system | feature | Formalize tag system for stubs with standard vocabulary and dashboard filtering |
| STUB-035 | scrapper-league-hosting | feature | Host fantasy leagues with scores, stats, and history for Scrapper |
| STUB-036 | timestamp-enforcement | improvement | Require timestamps on all tool workflows and slash commands |
| STUB-037 | file-front-matter | improvement | Front matter directives for agents on important files (read-only, required-context, etc.) |
| STUB-047 | coderef-directory-rename | refactor | Rename coderef/working to coderef/work-order across all projects for clarity |
| STUB-048 | scriptboard-endpoints-test | test | Test Scriptboard orchestrator endpoints from WO-FILE-DISCOVERY-ENHANCEMENT-001 |
| STUB-050 | work-order-folder-rename | refactor | Rename coderef/working/{feature}/ to coderef/work-order/{feature}/ for clarity |
| STUB-051 | rename-execute-plan-to-align-plan | improvement | Rename /execute-plan to /align-plan for clarity (aligns plan with todo list) |
| STUB-052 | websocket-live-update-test | test | Test WebSocket real-time updates in Scriptboard dashboard |

---

## Key Paths

| Location | Purpose |
|----------|---------|
| `C:\Users\willh\Desktop\assistant` | This orchestrator assistant |
| `C:\Users\willh\Desktop\assistant\coderef\working\` | Stub storage |
| `C:\Users\willh\.mcp-servers\` | MCP servers home |
| `C:\Users\willh\Desktop\clipboard_compannion\next` | Scriptboard app |
| `C:\Users\willh\Desktop\app_documents` | Selector engine |
| `C:\Users\willh\Desktop\scrapper` | NFL stats scrapper |
| `C:\Users\willh\Desktop\latest-sim\gridiron-franchise` | Gridiron franchise sim |
| `C:\Users\willh\Desktop\projects\noted` | Noted app |
| `C:\Users\willh\Desktop\projects\coderef-system` | CodeRef system |
| `C:\Users\willh\Desktop\Business-Dash\latest-app` | Next multi-tenant app |

---

## Workflow

```
/stub "idea"           →  Creates STUB-XXX
/start-feature STUB-X  →  Promotes to WO-XXX, begins planning
Paste prompt           →  Delegate to embedded project agent
Agent executes         →  Updates plan.json, creates deliverables
```
