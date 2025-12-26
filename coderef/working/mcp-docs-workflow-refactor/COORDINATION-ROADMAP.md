# 3-Project Coordination Roadmap

## All Workorders (4 Active + 1 Planned)

### Active (In Progress)



### 1. mcp-doc-workflow-refactor (STUB-053)
**Project:** docs-mcp
**Location:** `C:\Users\willh\.mcp-servers\docs-mcp\coderef\working\mcp-doc-workflow-refactor`
**Status:** In Progress

**Scope:** Extract 24 workflow tools from docs-mcp → new coderef-workflow server

**Deliverables:**
- ✅ Strategic planning documents (9 files in STUB-053)
- New coderef-workflow MCP server (24 tools)
- Updated docs-mcp (simplified to 10 pure doc tools)

---

### 2. context-generation (coderef-context-enhancement)
**Project:** coderef-system
**Location:** `C:\Users\willh\Desktop\projects\coderef-system\coderef\working\context-generation`
**Status:** In Progress

**Scope:** Build coderef-context Phases 1-6

**Phases:**
1. Complexity scoring
2. Task-specific context generation
3. Edge case detection
4. Test pattern analysis
5. Code example extraction
6. Agentic output formatting

**Deliverables:**
- codebase-context.json (general analysis)
- task-context.json (per-task with effort/risk/gotchas)
- Standards discovery (auto-extract UI/behavior/UX patterns)

---

### 3. modular-widget-system-pwa-electron
**Project:** scriptboard
**Location:** `C:\Users\willh\Desktop\clipboard_compannion\next\coderef\working\modular-widget-system-pwa-electron`
**Status:** In Progress

**Scope:** New widget-based dashboard (PWA + Electron)

**Architecture:**
- Modular widget system
- Real-time updates via WebSocket
- Displays orchestrator data (workorder status, agent progress)
- Support for both web (PWA) and desktop (Electron)

**Widget Types:**
- Workorder status widget
- Agent progress widget
- Task tracking widget
- Standards compliance widget
- Changelog widget

### Planned (Next Phase)

#### 4. mcp-integration-layer
**Workorder:** WO-MCP-INTEGRATION-LAYER-001
**Scope:** Integrate git-mcp and claude-filesystem-mcp with all 4 coderef servers + dashboard
**Timeline:** 1-2 weeks (can run in parallel with Phase 3)
**Dependencies:** All 4 coderef servers must be functional

---

## Coordination Flow

```
Timeline →

Week 1-2: Phase 1 (PARALLEL START)
├── coderef-context: Phase 1 (complexity-scorer)
├── coderef-workflow: Extract 24 tools from docs-mcp
└── scriptboard: Design widget architecture

Week 3-4: Phase 2 (context-generation)
├── coderef-context: Phases 2-4 (task context, edge cases, test patterns)
├── coderef-workflow: Wire imports from coderef-context
└── scriptboard: Build core widgets (status, progress)

Week 5: Phase 3 (integration)
├── coderef-context: Phases 5-6 (examples, agentic formatting)
├── coderef-workflow: Test end-to-end planning with context
└── scriptboard: Integrate with coderef-workflow data

Week 5-6: Phase 4 (PARALLEL) - MCP Integration Layer
├── Wire git-mcp into all 4 coderef servers
├── Wire claude-filesystem-mcp into all 4 coderef servers
├── Test filesystem operations (read/write context, plan, communication files)
└── Test git operations (branch creation, metrics extraction, merging)

Week 6-7: Phase 5 (launch)
├── coderef-workflow: Production-ready
├── scriptboard: Live dashboard reading integrated git + filesystem data
├── All MCP servers: Connected and operational
└── All systems: Unified orchestration platform with complete audit trail
```

---

## Data Flow Between Projects

```
┌─────────────────────┐
│  coderef-context    │
│  (context-gen)      │
└──────────┬──────────┘
           │ outputs
           │ context.json
           │ task-context.json
           ↓
┌─────────────────────┐
│  coderef-workflow   │
│  (mcp-doc-refactor) │
└──────────┬──────────┘
           │ creates
           │ plan.json
           │ communication.json
           │ task descriptions
           ↓
┌──────────────────────────────┐
│     scriptboard             │
│ (modular-widget-system)     │
└──────────────────────────────┘
    Displays:
    - Workorder status
    - Agent progress
    - Task completion
    - Compliance (standards)
    - Changes (changelog)
```

---

## Integration Points

### coderef-context → coderef-workflow

**What coderef-context provides:**
```typescript
interface TaskContext {
  task: string;
  related_functions: string[];
  complexity_estimate: string;  // "low" | "medium" | "high"
  risk_level: string;           // "low" | "medium" | "high"
  examples: CodeExample[];
  gotchas: string[];
  confidence: number;           // 0-1
}
```

**How coderef-workflow uses it:**
```typescript
// In create-plan.ts
const taskContext = await generateTaskContext(sourceDir, requirement);

// Embed in plan.json
task.effort_estimate = taskContext.complexity_estimate;
task.risk_assessment = taskContext.risk_level;
task.examples = taskContext.examples;
task.gotchas = taskContext.gotchas;

// Embed in task description for agent
taskDescription = `
Task: ${requirement}

Complexity: ${taskContext.complexity_estimate}
Risk: ${taskContext.risk_level}

Examples:
${taskContext.examples.map(e => e.code).join('\n')}

Watch out for:
${taskContext.gotchas.join('\n')}
`;
```

---

### coderef-workflow → scriptboard

**What coderef-workflow provides:**
```typescript
interface WorkorderStatus {
  workorder_id: string;
  status: "pending" | "planning" | "implementing" | "complete";
  current_task: string;
  progress_percent: number;
  last_update: timestamp;
  agent_assignments: AgentAssignment[];
}
```

**How scriptboard displays it:**
```
Widget: Workorder Status
├── Title: WO-FEATURE-XXX
├── Status bar: ████░░░░░░ 40%
├── Current task: "Implement authentication"
├── Agent: @lloyd
├── Last update: 2 minutes ago
└── Actions: [View Details] [Message Agent]
```

---

## Success Criteria

### For coderef-context (Week 5)
- ✅ Phases 1-6 complete
- ✅ context.json accurate (confidence > 0.85)
- ✅ task-context.json contains all fields
- ✅ Exports clean API for coderef-workflow

### For coderef-workflow (Week 5)
- ✅ 24 tools extracted and working
- ✅ Imports coderef-context successfully
- ✅ create-plan embeds context in every task
- ✅ execute-plan breaks tasks with context

### For scriptboard (Week 5)
- ✅ Widget system working
- ✅ Connects to real workorder data
- ✅ Real-time updates via WebSocket
- ✅ Displays at least 3 widget types

### Overall (Week 6)
- ✅ End-to-end test: orchestrator → coderef-workflow → agents → scriptboard
- ✅ Live dashboard showing real workorder execution
- ✅ All 3 systems decoupled and independently deployable

---

## Dependencies

```
coderef-context (must finish first)
  ↓ (API)
coderef-workflow (depends on context API)
  ↓ (data)
scriptboard (displays workflow data)
```

**Parallel work possible:**
- coderef-context Phases 1-4 can run while coderef-workflow extraction happens
- scriptboard widget design can happen in parallel
- Integration tests start in Week 4

---

## Handoff Points

### From coderef-context to coderef-workflow
**Week 4 Handoff:**
- ✅ context-generation/plan.json shows Phases 1-3 complete
- ✅ API exports finalized in coderef-context/src/index.ts
- ✅ Sample context.json and task-context.json files
- coderef-workflow can start integration

### From coderef-workflow to scriptboard
**Week 5 Handoff:**
- ✅ mcp-doc-workflow-refactor/plan.json shows extraction complete
- ✅ coderef-workflow deployed and tested
- ✅ Sample communication.json from real run
- scriptboard can start consuming real data

---

## Related Files in STUB-053

1. **EXTRACTION-OUTLINE.md** - How 24 tools move to coderef-workflow
2. **SLASH-COMMANDS-FLOW.md** - Flow of workflow commands (3 phases)
3. **ARCHITECTURE-LAYERS.md** - 5-layer architecture (coderef-context at Layer 3)
4. **CONTEXT-TOOLS-COMPARISON.md** - How coderef-context compares to alternatives
5. **GIT-MCP-FILESYSTEM-TRACKING.md** - How git-mcp + filesystem track execution
6. **DOCS-IMPROVEMENTS.md** - Features for coderef-docs (parallel concern)
7. **COORDINATION-ROADMAP.md** - This file (project alignment)
