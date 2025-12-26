# CodeRef Index - All Projects

> Generated: 2025-12-17
> Source: Orchestrator scan of all project coderef folders

---

## Summary

| Project | Working | Archived | Has Foundation | Has Standards | Has Orchestration |
|---------|---------|----------|----------------|---------------|-------------------|
| scriptboard | 8 | 31 | Yes | Yes | Yes |
| scrapper | 8 | 2 | Yes | No | Yes |
| gridiron | 3 | 34 | Yes | No | Yes |
| noted | 1 | 2 | Yes | Yes | Yes |
| app-documents | 2 | 0 | Yes | No | Yes |
| coderef-system | 5 | 40 | Yes | Yes | Yes |
| multi-tenant | 8 | 0 | Yes | No | Yes |

**Totals:** 35 working features, 109 archived features

---

## Scriptboard

**Path:** `C:\Users\willh\Desktop\clipboard_compannion\next\coderef`

**Structure:**
```
coderef/
├── archived/          (31 completed features)
├── context/
├── docs/
├── feature/
├── features/
├── foundation-docs/
├── orchestration.json
├── standards/
└── working/           (8 active features)
```

**Working Features:**
| Feature | Description |
|---------|-------------|
| electron-updater | Electron auto-update |
| file-explorer-tree-picker | File tree component |
| generate-features-inventory | Features.md generation |
| lovable-scraper-themes | Theme integration |
| orchestrator-dashboard | **WO-ORCHESTRATOR-DASHBOARD-001** |
| promptbox | Prompt UI component |
| scraper-engagement-sections | Engagement UI |
| scriptboard-prompting-workflow | Main workflow |

---

## Scrapper

**Path:** `C:\Users\willh\Desktop\scrapper\coderef`

**Structure:**
```
coderef/
├── archived/          (2 completed features)
├── foundation-docs/
├── inventory/
├── orchestration.json
└── working/           (8 active features)
```

**Working Features:**
| Feature | Description |
|---------|-------------|
| admin-dashboard | Admin UI |
| enhanced-activity-metadata | Activity tracking |
| game-details-ui-components | Game detail UI |
| historical-backfill | Data backfill |
| mobile-dropdown-fix | Mobile fix |
| scraper-reliability-fixes | Reliability |
| v2-scraper-ui | V2 UI redesign |
| video-links | Video integration |

---

## Gridiron

**Path:** `C:\Users\willh\Desktop\latest-sim\gridiron-franchise\coderef`

**Structure:**
```
coderef/
├── archived/          (34 completed features)
├── changelog/
├── context-experts/
├── experts/
├── foundation-docs/
├── inventory/
├── orchestration.json
├── workorder-log.txt
└── working/           (3 active features)
```

**Working Features:**
| Feature | Description |
|---------|-------------|
| page-content | **WO-PAGE-CONTENT-001** - Dashboard page audit |
| stub-pages | Stub pages |
| testing-critical-files | Test coverage |

---

## Noted

**Path:** `C:\Users\willh\Desktop\projects\noted\coderef`

**Structure:**
```
coderef/
├── archived/          (2 completed features)
├── foundation-docs/
├── future/
├── orchestration.json
├── standards/
└── working/           (1 active feature)
```

**Working Features:**
| Feature | Description |
|---------|-------------|
| folder-filter-sort | Folder filtering |

---

## App-Documents

**Path:** `C:\Users\willh\Desktop\app_documents\coderef`

**Structure:**
```
coderef/
├── foundation-docs/
├── orchestration.json
└── working/           (2 active features)
```

**Working Features:**
| Feature | Description |
|---------|-------------|
| football-insight-engine | Insight engine |
| selector-engine | Core selector |

**Note:** Also has `working/optimization/` at root level with completed **WO-INSIGHT-OPTIMIZATION-001**

---

## CodeRef-System

**Path:** `C:\Users\willh\Desktop\projects\coderef-system\coderef`

**Structure:**
```
coderef/
├── archived/          (40 completed features)
├── changelog/
├── foundation-docs/
├── future/
├── IMPROVEMENTS.md
├── inventory/
├── orchestration.json
├── reviews/
├── standards/
└── working/           (5 active features)
```

**Working Features:**
| Feature | Description |
|---------|-------------|
| ast-element-scanner | AST scanning |
| coderef-expert-rag-update | RAG updates |
| fix-all | Bug fixes |
| mcp-rag-integration | MCP RAG |
| root-cleanup | Cleanup |

---

## Multi-Tenant

**Path:** `C:\Users\willh\Desktop\Business-Dash\latest-app\coderef`

**Structure:**
```
coderef/
├── ARCHITECTURE-GUIDE.md
├── foundation-docs/
├── orchestration.json
└── working/           (8 active features)
```

**Working Features:**
| Feature | Description |
|---------|-------------|
| bugfixes | Bug fixes |
| multi-tenant-widgets | Widgets |
| simplify-base | Simplification |
| state-management | State |
| tenant-switcher | Tenant switching |
| testing | Tests |
| ui-components | UI components |
| widget-integrations | Widget integration |

---

## Common Folders

| Folder | Purpose | Projects With |
|--------|---------|---------------|
| `working/` | Active features in progress | All 7 |
| `archived/` | Completed features | 5 of 7 |
| `foundation-docs/` | ARCHITECTURE, SCHEMA, etc. | All 7 |
| `standards/` | UI/UX patterns | 3 of 7 |
| `orchestration.json` | Orchestrator tracking | All 7 |
| `inventory/` | API/DB/Config inventories | 3 of 7 |
| `changelog/` | Version history | 2 of 7 |

---

## Key Files

| File | Purpose | Location |
|------|---------|----------|
| `orchestration.json` | Orchestrator audit/tracking | All project roots |
| `communication.json` | Workorder handoff | `working/{feature}/` |
| `plan.json` | Implementation plan | `working/{feature}/` |
| `context.json` | Feature requirements | `working/{feature}/` |
| `DELIVERABLES.md` | Task checklist | `working/{feature}/` |

---

## Active Workorders by Project

| Project | WO-ID | Feature | Status |
|---------|-------|---------|--------|
| scriptboard | WO-ORCHESTRATOR-DASHBOARD-001 | orchestrator-dashboard | pending_plan |
| scriptboard | WO-TERMINAL-SETTINGS-SYNC-001 | terminal-settings-sync | pending_plan |
| scriptboard | WO-TOOL-INVENTORY-001 | tool-inventory-workflow | approved |
| gridiron | WO-PAGE-CONTENT-001 | page-content | pending_audit |
| app-documents | WO-INSIGHT-OPTIMIZATION-001 | insight-engine-optimization | complete |
