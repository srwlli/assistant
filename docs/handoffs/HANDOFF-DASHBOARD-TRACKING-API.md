# Handoff: Tracking API Implementation for Dashboard

**To:** Dashboard Agent (coderef-dashboard team)
**From:** Orchestrator
**Status:** Ready for Implementation
**Priority:** CRITICAL (blocks all dashboard features)
**Date:** 2025-12-26

---

## **Your Mission**

Implement the file system-based API layer that powers the dashboard's workorder and stub tracking system.

**Why This Matters:**
- Dashboard routes (`/coderef-assistant`, `/coderef-sources`) need live data
- You're building the **data foundation** everything else depends on
- This unblocks parallel work: you build API, UI team builds UI

---

## **What You're Building**

### **3 API Endpoints**

```
GET /api/stubs
  ↓ Returns: All stubs from assistant/coderef/working/

GET /api/workorders
  ↓ Returns: All workorders from all tracked projects

GET /api/workorders/:workorderId
  ↓ Returns: Complete workorder with all files + metadata
```

### **1 Configuration File**

```
C:\Users\willh\Desktop\assistant\projects.config.json
  ↓ Source of truth for all tracked projects
  ↓ Created by orchestrator, read by API
  ↓ Contains: paths, workorder directories, status
```

---

## **Projects You're Tracking**

These 6 projects/systems will be scanned for workorders:

| ID | Name | Type | Path | Workorders? |
|----|----|------|------|-------------|
| `mcp-coderef-context` | CodeRef Context MCP | System | `C:\Users\willh\.mcp-servers\coderef-context` | Yes |
| `mcp-coderef-workflow` | CodeRef Workflow MCP | System | `C:\Users\willh\.mcp-servers\coderef-workflow` | Yes |
| `mcp-coderef-docs` | CodeRef Docs MCP | System | `C:\Users\willh\.mcp-servers\coderef-docs` | Yes |
| `mcp-coderef-personas` | CodeRef Personas MCP | System | `C:\Users\willh\.mcp-servers\coderef-personas` | Yes |
| `mcp-servers` | MCP Servers Root | System | `C:\Users\willh\.mcp-servers` | Yes |
| `coderef-dashboard` | Dashboard (This Project) | App | `C:\Users\willh\Desktop\coderef-dashboard` | Yes |

### **Why These?**

- **4 Coderef MCP servers:** Where distributed work happens (agents create workorders)
- **MCP Servers root:** Umbrella for all MCP-related work
- **Dashboard:** Track your own workorders, plus `/coderef-assistant` and `/coderef-scout` routes will display all tracked workorders

---

## **Key Implementation Details**

### **How Workorder Discovery Works**

```
For each project:
  1. Go to {project_path}/coderef/workorder/
  2. List all folders
  3. Each folder = one workorder
  4. Read any files in the folder (optional):
     - communication.json
     - plan.json
     - DELIVERABLES.md
  5. Return aggregated list
```

**Important:** Files are optional. Folder existence = workorder exists.

### **API Behavior: Graceful Degradation**

**Missing communication.json?** → 200 OK, use folder stats
**Missing plan.json?** → 200 OK, tasks array empty
**Missing DELIVERABLES.md?** → 200 OK, deliverables empty
**Empty folder?** → 200 OK, all fields empty (agent just created it)
**Folder not found?** → 404 ONLY failure case

**Why?** Agents create folders immediately, add files as work progresses. No friction.

---

## **Implementation Path**

### **Step 1: Create projects.config.json**

Orchestrator will create this file before you start.
Located: `C:\Users\willh\Desktop\assistant\projects.config.json`

You'll read this in your API routes to know which projects to scan.

### **Step 2: Implement API Routes**

**File:** `packages/dashboard/src/app/api/stubs/route.ts`
```typescript
GET /api/stubs
- Read projects.config.json
- Scan assistant/coderef/working/
- Return StubListResponse
```

**File:** `packages/dashboard/src/app/api/workorders/route.ts`
```typescript
GET /api/workorders
- Read projects.config.json
- For each project, scan coderef/workorder/
- Return WorkorderListResponse
```

**File:** `packages/dashboard/src/app/api/workorders/[workorderId]/route.ts`
```typescript
GET /api/workorders/:workorderId
- Search all projects for workorder folder
- Read all files in folder
- Return WorkorderDetailResponse
```

### **Step 3: Define TypeScript Types**

See AGENT-HANDOFF-TRACKING-SYSTEM.md for complete type definitions:
- `StubObject`, `StubListResponse`
- `WorkorderObject`, `WorkorderListResponse`, `WorkorderDetailResponse`

### **Step 4: Add Utilities**

Create helper utilities:
- `lib/api/stubs.ts` - StubReader class
- `lib/api/workorders.ts` - WorkorderReader class
- `lib/api/projects.ts` - ProjectsConfig loader

### **Step 5: Error Handling**

Handle gracefully:
- Missing files (return partial data)
- Missing folders (return 404)
- Permission denied (return 403)
- Invalid JSON (return 500 with details)

### **Step 6: Testing**

21 test scenarios defined in AGENT-HANDOFF-TRACKING-SYSTEM.md:
- Core functionality (6 tests)
- Graceful degradation (7 tests)
- Error cases (4 tests)
- Edge cases (4 tests)

---

## **What Unblocks**

Once your API is working:

✅ **STUB-057 (coderef-assistant route)**
   - Can fetch GET /api/stubs
   - Can fetch GET /api/workorders
   - Display live workorder list in dashboard

✅ **STUB-059 (coderef-sources route)**
   - Can optionally fetch /api/stubs (for knowledge base)

✅ **Dashboard Widget Updates**
   - Show real-time workorder status
   - Track what's planned, what's implementing, what's complete

---

## **Success Criteria**

You're done when:

- [ ] All 3 API endpoints deployed and tested
- [ ] GET /api/stubs returns correct schema
- [ ] GET /api/workorders aggregates all 6 tracked projects
- [ ] GET /api/workorders/:id returns complete workorder
- [ ] Graceful degradation works (optional files handled correctly)
- [ ] Status inference logic works (file presence → status)
- [ ] Error responses match spec
- [ ] All 21 test scenarios pass
- [ ] Documentation in code (comments on complex logic)
- [ ] Ready to hand off to UI team

---

## **Reference Documents**

**Complete specs:**
- `AGENT-HANDOFF-TRACKING-SYSTEM.md` - Full implementation guide (415 lines)
- `ORCHESTRATOR-ROADMAP.md` - System architecture context
- `coderef/working/coderef-tracking-api-mvp/stub.json` - Detailed design spec

**Key sections:**
- Step 2: API Route Specifications (with examples)
- Step 3: TypeScript Type Definitions
- Step 4b: Graceful Degradation (optional files philosophy)
- Step 5: Testing (21 scenarios)

---

## **Questions?**

Refer to:
1. How do I discover workorders? → Step 4b: Graceful Degradation
2. What if files are missing? → Step 4b (scenario tables)
3. What are the response schemas? → Step 2: Implement API Routes
4. How do I handle errors? → Step 4: Error Handling
5. What should I test? → Step 5: Testing

---

## **Timeline**

**No hard deadlines.** Quality > Speed.

But roughly:
- API implementation: This week
- Integration with UI: Next week
- Full dashboard operational: By end of month

**You own the API completely.** No blockers. Ready to go when you are.

---

**Next:** Orchestrator creates projects.config.json, then you start implementation.
