# Orchestrator System Roadmap

> **Last Updated:** 2025-12-26
> **Phase:** Implementation Planning (Phase 3)
> **Status:** Ready for Agent Delegation

---

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   CODEREF ORCHESTRATOR                      │
│          C:\Users\willh\Desktop\assistant\                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─ projects.config.json ──────────────────────────────┐  │
│  │  Source of truth: all projects, paths, status       │  │
│  └────────────────────────────────────────────────────┘  │
│           │                                               │
│           ▼                                               │
│  ┌─────────────────────────────────────────────────────┐  │
│  │   GET /api/stubs                                    │  │
│  │   └─ Reads: coderef/working/*/stub.json            │  │
│  │                                                      │  │
│  │   GET /api/workorders                               │  │
│  │   └─ Reads: All projects + workorder-log.txt        │  │
│  │                                                      │  │
│  │   GET /api/workorders/:id                           │  │
│  │   └─ Reads: Full workorder + all files              │  │
│  └─────────────────────────────────────────────────────┘  │
│           │                                               │
│           ▼                                               │
│  ┌─────────────────────────────────────────────────────┐  │
│  │      JSON Response Schemas (Contracts)              │  │
│  │   ✓ StubObject, StubListResponse                    │  │
│  │   ✓ WorkorderObject, WorkorderListResponse          │  │
│  │   ✓ WorkorderDetailResponse                         │  │
│  └─────────────────────────────────────────────────────┘  │
│           │                                               │
└───────────┼───────────────────────────────────────────────┘
            │
            ├─────────────────────┬──────────────────────┐
            │                     │                      │
            ▼                     ▼                      ▼
      ┌─────────────┐      ┌─────────────┐     ┌──────────────┐
      │ Dashboard   │      │ Dashboard   │     │ Integration  │
      │ Route:      │      │ Route:      │     │ into MCP     │
      │ /coderef-   │      │ /coderef-   │     │ Servers      │
      │ assistant   │      │ sources     │     │              │
      │             │      │             │     │              │
      │ (STUB-057)  │      │ (STUB-059)  │     │ (STUB-058)   │
      └─────────────┘      └─────────────┘     └──────────────┘
```

---

## Critical Path: Implementation Sequence

### Phase 1: Data Layer (BLOCKING)
**STUB-060: coderef-tracking-api-mvp** ← **START HERE**

Required before UI routes can function.

**Deliverables:**
1. ✓ Design complete (in stub.json)
2. □ Create `projects.config.json` with all project definitions
3. □ Implement GET /api/stubs route handler
4. □ Implement GET /api/workorders route handler
5. □ Implement GET /api/workorders/:workorderId route handler
6. □ Define TypeScript types for all response schemas
7. □ Add error handling and validation

**Data Sources:**
- Stubs: `C:\Users\willh\Desktop\assistant\coderef\working\*/` (folder scan + stub.json)
- Workorders: Distributed across projects in `coderef/workorder\*/` (folder scan)
- Projects registry: NEW `projects.config.json` to be created

**Dependencies:**
- None (self-contained MVP)

**Future Dependency:** All UI routes depend on this

---

### Phase 2: Dashboard UI Routes (depends on Phase 1)

#### A. STUB-057: coderef-assistant-route
**Purpose:** AI Assistant dashboard showing workorders, stubs, and documentation

**Requires:**
- Phase 1 complete (API endpoints functioning)
- Consumes: GET /api/stubs, GET /api/workorders

**Components:**
- Sidebar: Workorders | Stubs | Documentation tabs
- Content: Document viewer (reuse documentation-site pattern)
- Data source: API responses

**Status:** Specification complete, awaiting Phase 1

---

#### B. STUB-059: coderef-sources-route
**Purpose:** Knowledge base for team resources (internal/external, searchable)

**Requires:**
- Phase 1 complete (optional - can hard-code initially)
- Optional API integration: GET /api/sources (future enhancement)

**Features:**
- Search + filtering
- Categories: Standards, Guides, Documentation, Frameworks, Libraries
- Favorites/bookmarking
- Metadata display

**Status:** Specification complete, awaiting Phase 1

---

### Phase 3: Standards Integration (parallel with Phase 2)

#### STUB-058: mcp-doc-standards-integration
**Purpose:** Integrate UDS templates into MCP servers (headers/footers with workorder tracking)

**Affects:**
- coderef-docs MCP server
- coderef-workflow MCP server
- coderef-context MCP server
- coderef-personas MCP server

**Enhancements:**
- Add workorder_id, generated_by, feature_id to headers
- Add next_review_date, workorder_reference to footers
- Validation linter for compliance

**Status:** Design complete, independent from Phase 1

---

### Phase 4: Validation & Testing

#### STUB-061: stub-location-test
**Purpose:** Validate stub centralization workflow

**Validates:** All stubs save to `C:\Users\willh\Desktop\assistant\coderef\working\` regardless of project origin

**Status:** Test specification defined

---

### Phase 5: Refactoring (parallel track)

#### STUB-062: align-plan-command-refactor
**Purpose:** Align /create-plan workflow with plan.json standard structure

**Ensures:** Consistent plan format across all MCP servers

**Status:** Refactoring specification defined

---

## Project Registry: projects.config.json

**Location:** `C:\Users\willh\Desktop\assistant\projects.config.json`

**Structure:**
```json
{
  "projects": [
    {
      "id": "scrapper",
      "name": "Scrapper Project",
      "path": "C:\\Users\\willh\\Desktop\\scrapper",
      "has_workorders": true,
      "workorder_dir": "coderef/workorder",
      "status": "active",
      "description": "Web scraping tool"
    },
    {
      "id": "gridiron",
      "name": "Gridiron Franchise Simulator",
      "path": "C:\\Users\\willh\\Desktop\\latest-sim\\gridiron-franchise",
      "has_workorders": true,
      "workorder_dir": "coderef/workorder",
      "status": "active",
      "description": "Sports franchise simulation"
    },
    {
      "id": "coderef-dashboard",
      "name": "CodeRef Dashboard",
      "path": "C:\\Users\\willh\\Desktop\\coderef-dashboard",
      "has_workorders": true,
      "workorder_dir": "coderef/workorder",
      "status": "active",
      "description": "Multi-agent orchestration dashboard"
    },
    {
      "id": "documentation-site",
      "name": "Documentation Site",
      "path": "C:\\Users\\willh\\Desktop\\assistant\\documentation-site",
      "has_workorders": false,
      "status": "active",
      "description": "Markdown documentation viewer"
    }
  ],
  "centralized": {
    "stubs_dir": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\working"
  }
}
```

---

## API Contracts

### GET /api/stubs
**Response Schema:**
```typescript
{
  success: boolean;
  data: {
    stubs: StubObject[];
    total: number;
    location: string;
  };
  timestamp: ISO8601;
}
```

### GET /api/workorders
**Response Schema:**
```typescript
{
  success: boolean;
  data: {
    workorders: WorkorderObject[];
    total: number;
    by_project: { [projectId]: count };
    by_status: { [status]: count };
  };
  timestamp: ISO8601;
}
```

### GET /api/workorders/:workorderId
**Response Schema:**
```typescript
{
  success: boolean;
  data: {
    workorder: WorkorderObject;
    tasks: Task[];
    deliverables: Deliverable[];
    communication_log: LogEntry[];
  };
  timestamp: ISO8601;
}
```

---

## Completed Work (Committed)

✓ **STUB-057:** coderef-assistant-route specification (105 lines)
✓ **STUB-058:** mcp-doc-standards-integration specification (105 lines)
✓ **STUB-059:** coderef-sources-route specification (175 lines)
✓ **STUB-060:** coderef-tracking-api-mvp specification (280+ lines)
✓ **STUB-061:** stub-location-test specification
✓ **STUB-062:** align-plan-command-refactor specification
✓ **projects.md:** Updated with tracking

---

## Next Steps

1. **Delegate STUB-060** → Agent in coderef-dashboard
   - Create projects.config.json
   - Implement API routes
   - Define TypeScript schemas
   - Add error handling

2. **Monitor Phase 1 Completion**
   - Verify all API endpoints respond correctly
   - Verify response schemas match contracts
   - Test error cases

3. **Delegate STUB-057** → Agent in coderef-dashboard (after Phase 1)
   - Implement /coderef-assistant route
   - Wire up API consumption
   - Add sidebar navigation

4. **Parallel: Delegate STUB-058** → MCP Server Maintainers
   - Integrate UDS templates
   - Update header/footer generation
   - Create validation linter

5. **Run STUB-061** → Test suite
   - Validate stub centralization workflow
   - Confirm location consistency

---

## System Benefits

- **Unified Data Access:** Single API for all workorders/stubs
- **Scalable Architecture:** File system MVP → backend migration path
- **Frontend Independence:** UI routes consume via standard schemas
- **Real-Time Ready:** API design supports WebSocket upgrades
- **Distributed Teams:** Orchestrator aggregates from multiple projects
- **Traceability:** Full audit trail via communication.json + workorder logs

---

## Success Criteria

- [ ] All API endpoints deployed and tested
- [ ] Dashboard /coderef-assistant route displays live workorders
- [ ] Dashboard /coderef-sources route displays knowledge base
- [ ] UDS standards integrated into all MCP server outputs
- [ ] Stub centralization validated (STUB-061)
- [ ] Plan workflow standardized (STUB-062)
- [ ] Team can track workorder progress in real-time via dashboard
