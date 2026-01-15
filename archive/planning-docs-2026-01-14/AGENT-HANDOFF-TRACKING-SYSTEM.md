# Agent Handoff: Workorder & Stub Tracking System

**Target Agent:** Dashboard Team (coderef-dashboard)
**Workorder:** WO-TRACKING-SYSTEM-001
**Status:** Ready for Implementation
**Priority:** CRITICAL (blocks all dashboard features)
**Created:** 2025-12-26

---

## Mission

Implement a file system-based API layer that provides live access to workorders and stubs across all orchestrator projects. This is the **data foundation** for the assistant dashboard and knowledge base features.

**Why This Matters:**
- Dashboard needs real-time visibility of what's being worked on
- Stubs are stored in orchestrator (`assistant/coderef/working/`)
- Workorders are scattered across multiple projects (in `coderef/workorder/` folders)
- Without this API, the UI team can't display live data
- Agent-created workorders are autonomous (no orchestrator dependency)

---

## Your Responsibility

You own **STUB-060: coderef-tracking-api-mvp** implementation.

### What You Must Deliver

```
packages/dashboard/src/
├── app/
│   └── api/
│       ├── stubs/
│       │   └── route.ts              (GET /api/stubs)
│       └── workorders/
│           ├── route.ts              (GET /api/workorders)
│           └── [workorderId]/
│               └── route.ts          (GET /api/workorders/:id)
│
├── lib/
│   └── api/
│       ├── stubs.ts                  (StubReader utility)
│       ├── workorders.ts             (WorkorderReader utility)
│       └── projects.ts               (ProjectsConfig loader)
│
└── types/
    ├── stubs.ts                      (TypeScript interfaces)
    ├── workorders.ts                 (TypeScript interfaces)
    └── api.ts                        (Response schemas)
```

**Plus:** `C:\Users\willh\Desktop\assistant\projects.config.json` (single source of truth)

---

## Step 1: Create projects.config.json

**File Location:** `C:\Users\willh\Desktop\assistant\projects.config.json`

**Purpose:** Master registry of all projects and their locations

**Content:**
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
    "stubs_dir": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\working",
    "workorder_log": "C:\\Users\\willh\\Desktop\\assistant\\workorder-log.txt",
    "workorders_json": "C:\\Users\\willh\\Desktop\\assistant\\workorders.json"
  }
}
```

---

## Step 2: Implement API Routes

### GET /api/stubs

**Purpose:** Fetch all stubs from the orchestrator's backlog

**Implementation:**
1. Read from `projects.config.json` (get stubs_dir)
2. Scan `C:\Users\willh\Desktop\assistant\coderef\working\*/` (list folders)
3. For each folder, read `stub.json` if present
4. Return standardized response

**Response:**
```typescript
{
  success: true,
  data: {
    stubs: [
      {
        id: "coderef-tracking-api-mvp",
        feature_name: "coderef-tracking-api-mvp",
        title: "Workorder & Stub Tracking API - File System MVP",
        description: "Create Next.js API routes...",
        category: "feature",
        priority: "critical",
        status: "stub",
        created: "2025-12-26T11:00:00Z",
        updated: "2025-12-26T11:00:00Z",
        path: "C:\\Users\\willh\\Desktop\\assistant\\coderef\\working\\coderef-tracking-api-mvp\\stub.json"
      }
      // ... more stubs
    ],
    total: 42,
    location: "C:\\Users\\willh\\Desktop\\assistant\\coderef\\working"
  },
  timestamp: "2025-12-26T12:30:45Z"
}
```

---

### GET /api/workorders

**Purpose:** Fetch all active workorders from all projects

**Implementation:**
1. Read projects.config.json
2. For each project with has_workorders=true:
   - Scan `{project_path}/coderef/workorder/` (list folders)
   - If folder exists → workorder exists
   - Read any files in folder (communication.json, plan.json, DELIVERABLES.md)
3. Extract workorder metadata and status
4. Return aggregated list

**Response:**
```typescript
{
  success: true,
  data: {
    workorders: [
      {
        id: "WO-TRACKING-SYSTEM-001",
        project_id: "coderef-dashboard",
        project_name: "CodeRef Dashboard",
        feature_name: "coderef-tracking-api-mvp",
        status: "pending_plan",
        path: "C:\\Users\\willh\\Desktop\\coderef-dashboard\\coderef\\working\\coderef-tracking-api-mvp",
        files: {
          communication_json: { /* parsed */ },
          plan_json: { /* parsed, if exists */ },
          deliverables_md: "# Deliverables...",
        },
        created: "2025-12-26T11:00:00Z",
        updated: "2025-12-26T12:30:45Z",
        last_status_update: "2025-12-26T12:30:45Z"
      }
      // ... more workorders
    ],
    total: 15,
    by_project: {
      "scrapper": 3,
      "gridiron": 4,
      "coderef-dashboard": 8
    },
    by_status: {
      "pending_plan": 5,
      "in_progress": 4,
      "complete": 6
    }
  },
  timestamp: "2025-12-26T12:30:45Z"
}
```

---

### GET /api/workorders/:workorderId

**Purpose:** Fetch complete workorder with all files and status details

**Implementation:**
1. Parse workorderId from URL parameter
2. Search all projects: `{project_path}/coderef/workorder/{feature-name}/`
3. Read all files in the folder:
   - communication.json (if exists - workflow status, logs)
   - plan.json (if exists)
   - DELIVERABLES.md (if exists)
4. Return fully populated workorder object with all available files

**Response:**
```typescript
{
  success: true,
  data: {
    workorder: {
      id: "WO-TRACKING-SYSTEM-001",
      project_id: "coderef-dashboard",
      project_name: "CodeRef Dashboard",
      feature_name: "coderef-tracking-api-mvp",
      status: "pending_plan",
      path: "C:\\Users\\willh\\Desktop\\coderef-dashboard\\coderef\\working\\coderef-tracking-api-mvp",
      files: {
        communication_json: {
          workorder_id: "WO-TRACKING-SYSTEM-001",
          status: "pending_plan",
          created: "2025-12-26T11:00:00Z",
          instructions: "...",
          communication_log: [/* messages */]
        },
        plan_json: {
          title: "Tracking API Implementation",
          phases: [/* ... */],
          tasks: [/* ... */]
        },
        deliverables_md: "# Deliverables\n..."
      },
      created: "2025-12-26T11:00:00Z",
      updated: "2025-12-26T12:30:45Z",
      last_status_update: "2025-12-26T12:30:45Z"
    },
    tasks: [/* array from plan.json */],
    deliverables: [/* array from DELIVERABLES.md */],
    communication_log: [/* message history */]
  },
  timestamp: "2025-12-26T12:30:45Z"
}
```

---

## Step 3: Define TypeScript Types

Create comprehensive type definitions:

**`src/types/stubs.ts`:**
```typescript
export interface StubObject {
  id: string;
  feature_name: string;
  title: string;
  description: string;
  category: 'feature' | 'fix' | 'improvement' | 'idea' | 'refactor' | 'test';
  priority: 'low' | 'medium' | 'high' | 'critical';
  status: 'stub' | 'planned' | 'in_progress' | 'completed';
  created: string; // ISO 8601
  updated: string; // ISO 8601
  path: string;
}

export interface StubListResponse {
  success: boolean;
  data: {
    stubs: StubObject[];
    total: number;
    location: string;
  };
  timestamp: string;
}
```

**`src/types/workorders.ts`:**
```typescript
export interface WorkorderObject {
  id: string;
  project_id: string;
  project_name: string;
  feature_name: string;
  status: 'pending_plan' | 'plan_submitted' | 'changes_requested' |
          'approved' | 'implementing' | 'complete' | 'verified' | 'closed';
  path: string;
  files: {
    communication_json: any;
    plan_json?: any;
    deliverables_md?: string;
  };
  created: string;
  updated: string;
  last_status_update: string;
}

export interface WorkorderListResponse {
  success: boolean;
  data: {
    workorders: WorkorderObject[];
    total: number;
    by_project: Record<string, number>;
    by_status: Record<string, number>;
  };
  timestamp: string;
}

export interface WorkorderDetailResponse {
  success: boolean;
  data: {
    workorder: WorkorderObject;
    tasks: Task[];
    deliverables: Deliverable[];
    communication_log: LogEntry[];
  };
  timestamp: string;
}
```

---

## Step 4: Error Handling

Handle these scenarios gracefully:

- **projects.config.json missing:** Return 500 with clear message
- **project path inaccessible:** Return 404 with project details
- **workorder folder not found:** Return 404 with searched locations
- **Invalid JSON files in folder:** Return 500 with parsing error details
- **File permission denied:** Return 403 with path info
- **Empty workorder folder (no files):** Return 200 with empty files object

All errors should follow this format:
```typescript
{
  success: false,
  error: {
    code: string; // e.g., "WORKORDER_NOT_FOUND"
    message: string;
    details?: object;
  },
  timestamp: string;
}
```

---

## Step 4b: Graceful Degradation

**API Behavior: Optional Files Philosophy**

All files are optional. The API discovers workorders based on **folder existence**, not file presence. This enables agents to create workorders immediately and add files as work progresses.

### **Behavior by Scenario**

**Missing communication.json:**
- ✓ Return 200 (workorder exists)
- Use folder stats for timestamps (creation time, last modified)
- Status: null or inferred from other files
- Impact: Low (status is informational, not critical)

```typescript
{
  success: true,
  data: {
    workorder: {
      id: "feature-name",  // derived from folder name
      status: null,        // no communication.json = no explicit status
      created: "2025-12-26T11:00:00Z",  // from folder.birthtimeMs
      updated: "2025-12-26T11:00:00Z",  // from folder.mtimeMs
      files: {
        communication_json: null,
        plan_json: null,
        deliverables_md: null
      }
    }
  }
}
```

**Missing plan.json:**
- ✓ Return 200 (workorder exists)
- Tasks array is empty
- Status inference: no plan.json = "pending" (not planned yet)
- Impact: Low (just means planning hasn't started)

**Missing DELIVERABLES.md:**
- ✓ Return 200 (workorder exists)
- Deliverables array is empty
- Status inference: has plan.json but no DELIVERABLES.md = "planned" (planning done, not implementing yet)
- Impact: Low (deliverables tracked separately from status)

**Empty workorder folder (no files at all):**
- ✓ Return 200 (workorder exists) — **Key decision**
- All file fields are null/empty
- Use folder stats for all metadata
- Status: "pending" (just created)
- Impact: None (valid intermediate state while agent prepares)

```typescript
{
  success: true,
  data: {
    workorder: {
      id: "new-feature",
      status: "pending",
      path: "{project}/coderef/workorder/new-feature",
      files: {},  // all empty
      created: "2025-12-26T11:00:00Z",
      updated: "2025-12-26T11:00:00Z"
    },
    tasks: [],
    deliverables: [],
    communication_log: []
  }
}
```

**Workorder folder not found:**
- ✗ Return 404 (workorder doesn't exist)
- This is the only failure case for workorders
- Error: `{ code: "WORKORDER_NOT_FOUND", ... }`

### **Status Inference Logic**

When communication.json missing, infer status from file presence:

```
No files → "pending"
Has plan.json → "planned"
Has plan.json + DELIVERABLES.md → "implementing"
Has all files + communication.json marked complete → "complete"
```

### **Timestamp Fallback Strategy**

When JSON files don't have timestamps, use file system stats:

```typescript
timestamps = {
  created: folder.birthtimeMs,      // folder creation time
  updated: folder.mtimeMs,          // folder last modification
  last_status_update: folder.mtimeMs // same as updated (no better source)
}
```

### **Why This Matters**

This design enables **agent autonomy without friction:**

1. Agent creates `coderef/workorder/{feature}/` → API discovers it immediately (200)
2. Agent adds `plan.json` → API shows "planned" status
3. Agent adds `DELIVERABLES.md` → API shows "implementing" status
4. Agent updates `communication.json` → Full details available

**No registration step. No orchestrator coordination. Just folder creation triggers discovery.**

---

## Step 5: Testing

### **Core Functionality**
- [ ] GET /api/stubs returns all stubs from assistant/coderef/working/ folders
- [ ] GET /api/workorders scans all projects' coderef/workorder/ folders
- [ ] GET /api/workorders/:id returns complete workorder with all files found in folder
- [ ] All responses match defined TypeScript types
- [ ] Error responses are consistent and descriptive
- [ ] Large workorder lists load efficiently

### **Graceful Degradation (Optional Files)**
- [ ] Folder scan discovers workorders even without communication.json
- [ ] Missing communication.json → status: null, use folder stats for timestamps
- [ ] Missing plan.json → tasks array empty, infer "pending" status
- [ ] Missing DELIVERABLES.md → deliverables array empty, infer "planned" status
- [ ] Completely empty workorder folder → Return 200 with all fields empty
- [ ] Empty folder gets timestamps from fs.stat() (birthtimeMs, mtimeMs)
- [ ] Status inference logic works correctly (file presence → status)

### **Error Cases**
- [ ] Workorder folder not found → Return 404 with WORKORDER_NOT_FOUND
- [ ] Invalid JSON in files → Return 500 with JSON_PARSE_ERROR details
- [ ] Permission denied on folder → Return 403
- [ ] projects.config.json missing → Return 500

### **Edge Cases**
- [ ] Multiple agents create workorder folders simultaneously (race condition handling)
- [ ] Workorder folder disappears mid-scan (ENOENT handling)
- [ ] Very large workorder with many files in folder
- [ ] Folder with only hidden files (should be treated as "has files")

---

## Dependencies on This Work

Once you deliver these APIs, the team can immediately start:

- **STUB-057:** coderef-assistant route (will consume these APIs)
- **STUB-059:** coderef-sources route (will use GET /api/stubs, potentially)

---

## Success Criteria

You're done when:

1. ✓ projects.config.json created and readable
2. ✓ GET /api/stubs endpoint responds with 200 + correct schema
3. ✓ GET /api/workorders endpoint responds with 200 + aggregates all projects
4. ✓ GET /api/workorders/:id endpoint responds with 200 + full workorder details
5. ✓ All error cases handled with consistent error format
6. ✓ All responses match TypeScript types
7. ✓ Tested with curl/Postman to verify responses
8. ✓ Documentation in code (comments on complex logic)
9. ✓ Ready for frontend team to wire up UI

---

## Files to Review

- [ORCHESTRATOR-ROADMAP.md](./ORCHESTRATOR-ROADMAP.md) - Full system architecture
- [STUB-060](./coderef/working/coderef-tracking-api-mvp/stub.json) - Detailed specifications
- [CLAUDE.md](./CLAUDE.md) - Orchestrator principles & workflow

---

## Questions?

Refer to:
1. projects.config.json structure (Step 1 above)
2. Response schema examples (Steps 2 above)
3. Full stub.json for edge cases
4. ORCHESTRATOR-ROADMAP.md for system context

**Remember:** This is the **foundation** everything else depends on. Quality > Speed.
