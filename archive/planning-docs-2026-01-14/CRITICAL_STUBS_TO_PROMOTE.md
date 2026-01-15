# Critical Stubs Ready for Workorder Promotion

**Summary:** These 7 stubs have comprehensive specifications and high/critical priority. They are ready to be promoted to WO-* workorders with context.json and communication.json files.

---

## 1. STUB-053: MCP Docs Workflow Refactor

**Status:** planning
**Priority:** high
**Target Project:** docs-mcp
**Location:** C:\Users\willh\Desktop\assistant\coderef\working\mcp-docs-workflow-refactor\

**Description:**
Refactor docs-mcp to separate concerns: standards discovery (coderef-context), documentation generation (coderef-docs), and workflow embedding (coderef-workflow). Creates 4 focused MCP systems under unified coderef brand.

**Why Promote Now:**
- Already in "planning" status (halfway to implementation)
- Extensive scope document with 5 phases defined
- Multiple active workorders already in progress related to this
- High impact on ecosystem architecture

**Recommendation:**
Promote to **WO-MCP-DOCS-REFACTOR-001** immediately. Assign to coderef-workflow agent.

---

## 2. STUB-055: Personas Ecosystem Architecture

**Status:** stub
**Priority:** high
**Target Project:** coderef-docs
**Location:** C:\Users\willh\Desktop\assistant\coderef\working\personas-ecosystem-architecture\

**Description:**
Define unified persona system where all personas are aware of coderef ecosystem. Resolve architectural questions about persona file structure, context inheritance, versioning, and external knowledge references.

**Current State Analysis Included:**
- Detailed assessment of each persona (CodeRef Assistant, Lloyd, Ava, Taylor, Devon)
- 3 design options evaluated
- Recommended hybrid approach outlined
- Specific updates needed documented per persona

**Why Promote Now:**
- Extensive architectural analysis complete
- Clear design options with pros/cons
- Immediate next steps defined
- Blocking point for STUB-054 (Widget Architect specialization)

**Recommendation:**
Promote to **WO-PERSONAS-ECOSYSTEM-ARCH-001**. Assign to personas-mcp agent.

---

## 3. STUB-056: Known Issues Utility

**Status:** stub
**Priority:** high
**Target Project:** coderef-dashboard
**Location:** C:\Users\willh\Desktop\assistant\coderef\working\known-issues-utility\

**Description:**
Agent-logged bug fixes and context library. Creates searchable database where agents log issues, fixes, and prevention tips. Future agents can query before debugging, eliminating repeated problem-solving.

**Complete Specification Includes:**
- Scope of what gets logged
- Access patterns and queries
- Workflow diagram
- Technical considerations (storage, format, integration)
- Example entry (KI-001: Python not found)
- Success criteria

**Why Promote Now:**
- End-to-end specification complete
- Clear use case and benefits identified
- Detailed JSON schema provided
- High value for agent productivity and knowledge transfer

**Recommendation:**
Promote to **WO-KNOWN-ISSUES-UTILITY-001**. This is institutional knowledge infrastructure.

---

## 4. STUB-062: Realtime Sync System

**Status:** stub
**Priority:** high
**Target Project:** coderef-dashboard
**Location:** C:\Users\willh\Desktop\assistant\coderef\working\realtime-sync-system\

**Description:**
Real-time workorder/stub sync with Server-Sent Events (SSE), IndexedDB caching, and Broadcast Channel API for multi-tab synchronization. Monitors coderef/workorder/ directory changes and broadcasts to all connected clients.

**4-Phase Implementation Plan:**
1. Workorder/Stub Tracking Foundation
2. Backend File Watcher & SSE
3. Multi-Tab & Real-Time UI
4. Offline & Conflict Resolution

**Why Promote Now:**
- Detailed implementation phases with specific tasks
- Architecture diagram provided
- Technology stack defined (no frameworks)
- Complexity/effort estimated
- Data flow documented

**Recommendation:**
Promote to **WO-REALTIME-SYNC-SYSTEM-001**. This transforms dashboard from static to live. Large effort (3-4 weeks) but well-defined.

---

## 5. STUB-007: MCP SaaS Platform (Lloyd.ai)

**Status:** stub
**Priority:** high
**Target Project:** coderef-dashboard
**Location:** C:\Users\willh\.mcp-servers\coderef\working\mcp-saas-platform\

**Description:**
Lloyd.ai - AI-native development workflow platform built on MCP. Full SaaS with project dashboards, workorder tracking, multi-agent coordination, and team collaboration.

**Maturity Level:** Detailed spec exists
**Has SPEC.md:** Yes (at C:\Users\willh\.mcp-servers\coderef\working\mcp-saas-platform\SPEC.md)

**Tech Stack Defined:**
- Frontend: Next.js 14 + shadcn/ui + Tailwind
- Backend: FastAPI (Python)
- Database: PostgreSQL (Supabase)
- Auth: Clerk
- AI: Claude API
- MCP: docs-mcp, coderef-mcp, personas-mcp

**MVP Timeline:** 12 weeks
**Pricing Tiers:** Free, Pro ($29/user), Team ($79/user), Enterprise

**Why Promote Now:**
- Complete specification exists
- Strategic product initiative
- Addresses real market need
- Clear phasing and timeline

**Recommendation:**
Promote to **WO-MCP-SAAS-PLATFORM-001** or wait for strategic alignment decision. This is a major initiative - may require separate approval process.

---

## 6. STUB-027: Orchestrator MCP

**Status:** stub
**Priority:** high
**Target Project:** assistant
**Location:** C:\Users\willh\Desktop\assistant\coderef\working\orchestrator-mcp\

**Description:**
MCP server providing orchestrator workflows as tools + assistant persona. Centralizes workorder management, delegation, and tracking. Includes 12 defined tools for stub/workorder operations.

**12 Tools Defined:**
1. create_stub - Capture ideas with auto-incrementing STUB-ID
2. delegate_workorder - Create communication.json in target project
3. check_workorder_status - Poll project status
4. update_tracking - Sync workorders.json and index.html
5. list_active_workorders - List all active work
6. generate_handoff_prompt - Generate delegation prompt
7. request_features_doc - Request features inventory
8. collect_features_docs - Aggregate all features
9. create_context - Create context.json
10. pass_context - Transfer context between projects
11. bridge_projects - Coordinate multi-project work
12. broadcast_prompt - Batch delegation to multiple agents

**Persona Included:** Orchestrator-assistant with clear do/don't principles

**Workflows Documented:**
- Context orchestration workflow
- Cross-project coordination
- Status tracking

**Why Promote Now:**
- Complete tool specifications
- Clear persona definition with principles
- Ready for MCP server implementation
- Foundational infrastructure

**Recommendation:**
Promote to **WO-ORCHESTRATOR-MCP-001** immediately. This is infrastructure that enables other workorders.

---

## 7. STUB-028: Plan Audit Workflow

**Status:** stub
**Priority:** high
**Target Project:** scriptboard
**Location:** C:\Users\willh\Desktop\assistant\coderef\working\plan-audit-workflow\

**Description:**
Audit workflow to scan all project coderef folders, index plan.json files, extract status/progress, and surface stale or active plans. Uses Scriptboard file indexer for discovery.

**Current Discovery Results Included:**
- Total plans found: 118
- Archived plans: 89
- Active plans: 29
- Projects scanned: 7 with detailed breakdown

**Projects with Plans:**
- Scriptboard: 23 archived, 5 working
- Scrapper: 1 archived, 5 working
- Gridiron: 31 archived, 4 working
- Noted: 3 archived, 0 working
- App-documents: 0 archived, 2 working
- CodeRef-system: 31 archived, 5 working
- Multi-tenant: 0 archived, 8 working

**Workflow Defined:**
1. Orchestrator triggers audit
2. Scriptboard file indexer scans folders
3. Indexes plan.json with metadata extraction
4. Aggregates into audit report
5. Surfaces stale/blocked/active plans
6. Orchestrator reviews and takes action

**Why Promote Now:**
- Existing data inventory already completed (118 plans found)
- Clear workflow documented
- Integration points defined
- High value for visibility and maintenance

**Recommendation:**
Promote to **WO-PLAN-AUDIT-WORKFLOW-001**. This provides critical visibility into distributed project work.

---

## Promotion Checklist

For each stub being promoted, follow these steps:

### 1. Create Workorder Directory
```
{target_project}/coderef/working/{feature-name}/
```

### 2. Create context.json
Document requirements, constraints, and technical context:
```json
{
  "workorder_id": "WO-XXX-001",
  "stub_id": "STUB-XXX",
  "feature_name": "feature-name",
  "requirements": ["req1", "req2"],
  "constraints": ["constraint1"],
  "technical_context": {}
}
```

### 3. Create communication.json
Track workflow status:
```json
{
  "workorder_id": "WO-XXX-001",
  "status": "pending_plan",
  "handoff": {
    "orchestrator_to_agent": "[handoff prompt]",
    "status": "pending_plan"
  },
  "communication_log": []
}
```

### 4. Update orchestrator workorders.json
Add entry tracking the workorder across all projects.

### 5. Generate Handoff Prompt
Create structured prompt for project agent with:
- Workorder ID and location
- Context and requirements
- Next steps (e.g., "Run /create-plan")
- Expected deliverables

### 6. User Pastes Prompt into Project Agent
Project agent executes, updates communication.json, implements feature.

---

## Promotion Timeline Recommendation

**Week 1 (Immediate):**
- Promote STUB-027 (Orchestrator MCP) - Foundational infrastructure
- Promote STUB-053 (MCP Docs Refactor) - Already in planning

**Week 2:**
- Promote STUB-056 (Known Issues Utility) - High value, self-contained
- Promote STUB-028 (Plan Audit) - Quick data visibility win

**Week 3:**
- Promote STUB-055 (Personas Ecosystem) - Architecture work, medium complexity
- Promote STUB-062 (Realtime Sync) - Large effort, needs planning

**Deferred (Strategic Decision Needed):**
- STUB-007 (MCP SaaS Platform) - Requires business alignment, product strategy

---

## Summary

These 7 stubs represent significant architecture improvements and feature additions:

| STUB | Feature | Effort | Impact | Status |
|------|---------|--------|--------|--------|
| STUB-027 | Orchestrator MCP | Medium | Foundation | Ready |
| STUB-053 | MCP Docs Refactor | Large | Architecture | In Planning |
| STUB-056 | Known Issues Utility | Medium | Knowledge | Ready |
| STUB-028 | Plan Audit | Medium | Visibility | Ready |
| STUB-055 | Personas Ecosystem | Medium | Architecture | Ready |
| STUB-062 | Realtime Sync | Large | UX/Dashboard | Ready |
| STUB-007 | MCP SaaS Platform | Very Large | Product | Ready (strategic gate) |

**Total estimated effort:** ~20-24 weeks (spread across 7 workorders)

**Next step:** Present this promotion slate to stakeholders for prioritization and approval.

---

**Report Generated:** 2026-01-13
**Source:** Comprehensive audit of 99 stubs in C:\Users\willh\Desktop\assistant\coderef\working\
