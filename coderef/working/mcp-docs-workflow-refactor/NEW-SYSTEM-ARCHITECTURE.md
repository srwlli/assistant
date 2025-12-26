# New MCP System Architecture

## 6 Focused MCP Servers (Unified Ecosystem)

### Core Systems (4 coderef servers)

```
┌─────────────────────────────────────────────────────────────┐
│                    coderef Dashboard                         │
│            (modular-widget-system-pwa-electron)              │
│              PWA + Electron Widget Interface                 │
└──────┬────────────┬────────────┬──────────────┬──────────┬──┘
       │            │            │              │          │
       ↓            ↓            ↓              ↓          ↓
  ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐
  │ coderef-│ │ coderef- │ │ coderef- │ │ coderef- │ │  git-  │
  │context  │ │workflow  │ │  docs    │ │  testing │ │  mcp   │
  └─────────┘ └──────────┘ └──────────┘ └──────────┘ └────────┘
      │            │            │              │          │
      │            │            │              │          │
      └─────────────┴────────────┴──────────────┴──────────┘
                        │
                        ↓
            ┌────────────────────────┐
            │ claude-filesystem-mcp  │
            └────────────────────────┘
```

---

## Server Definitions

### 1. coderef-context
**Purpose:** Code analysis, pattern discovery, complexity scoring

**Outputs:**
- `codebase-context.json` - General code analysis
- `task-context.json` - Task-specific context with effort/risk/gotchas
- Standards discovery (auto-detect UI/behavior/UX patterns)
- Confidence scores on all outputs

**Phases (6):**
1. Complexity scoring
2. Task-specific context generation
3. Edge case detection
4. Test pattern analysis
5. Code example extraction
6. Agentic output formatting

**Status:** WO-CODEREF-CONTEXT-ENHANCEMENT-001 (in progress)

---

### 2. coderef-workflow
**Purpose:** Planning, orchestration, execution tracking, coordination

**Extracted from docs-mcp (24 tools):**
- Planning: gather-context, analyze-for-planning, create-plan, validate-plan
- Execution: execute-plan, update-task-status, track-agent-status
- Coordination: generate-agent-communication, assign-agent-task, verify-agent-completion
- Tracking: generate-deliverables, update-deliverables, log-workorder, get-workorder-log
- Changelog: add-changelog-entry, get-changelog, update-changelog, update-docs
- Auditing: audit-plans, features-inventory, archive-feature
- Handoff: generate-handoff-context, aggregate-agent-deliverables

**Status:** WO-MCP-DOC-WORKFLOW-REFACTOR-001 (in progress)

---

### 3. coderef-docs
**Purpose:** Documentation generation, standards publishing, reference materials

**Stays in docs-mcp (10 pure doc tools):**
- generate-foundation-docs
- generate-individual-doc
- establish-standards
- audit-codebase
- check-consistency
- generate-quickref
- generate-user-guide
- generate-my-guide
- list-templates
- get-template

**Enhancements:**
- Auto-generated table of contents
- Cross-references between docs
- Code snippet versioning
- Documentation completeness scoring
- Out-of-date detection
- Relationship visualization

**Status:** Part of WO-MCP-DOC-WORKFLOW-REFACTOR-001

---

### 4. coderef-testing
**Purpose:** Test validation, coverage analysis, quality assurance

**To be built:**
- Extract test patterns from code
- Generate test cases
- Validate code quality
- Report coverage
- Standards compliance validation

**Status:** Planned (coderef-testing)

---

### 5. git-mcp
**Purpose:** Git operations, workorder tracking, metrics extraction

**Commands:**
- git-log-workorder: Append WO-ID to log
- git-query-workorder-commits: Find commits for WO
- git-create-wo-branch: Create WO-FEATURE-XXX branch
- git-merge-wo-branch: Orchestrator merges
- git-tag-feature: Tag release boundary
- git-count-lines-changed: Extract LOC metrics
- git-count-commits: Commit count
- git-extract-contributors: Find authors
- git-calculate-time-elapsed: Track elapsed time
- git-diff-forbidden-files: Validation

**Status:** ✅ Available (existing)

---

### 6. claude-filesystem-mcp
**Purpose:** Filesystem operations, file tracking, context management

**Operations:**
- Read/write context.json files
- Read/write plan.json files
- Read/write communication.json files
- Manage coderef/working/ and coderef/archived/
- Directory traversal and indexing
- File metadata management

**Status:** ✅ Available (existing)

---

## Access Layers

### Layer 1: Persona Agents
**Who:** Expert personas (archer, ava, devon, taylor, lloyd, docs-expert, coderef-expert, marcus, quinn)

**How they access:**
```typescript
// Persona agent code
import { usePersona } from '@coderef/personas';
import { generateTaskContext } from '@coderef/context';
import { createPlan } from '@coderef/workflow';

// Use context to plan
const context = await generateTaskContext(sourceDir, task);
const plan = await createPlan(features, context);

// Execute with tracking
await executePlan(plan);
```

**Tools available:** All MCP tools through unified CLI

---

### Layer 2: Human AI Agents
**Who:** Claude instances in project codebases with embedded agents

**How they access:**
```typescript
// Agent in project (has full context)
const context = await coderefContext.analyze(projectDir);
const plan = await coderefWorkflow.createPlan(requirements, context);
const tasks = await coderefWorkflow.executePlan(plan);

// Agents implement tasks
for (const task of tasks) {
  // Task contains:
  // - context from coderef-context
  // - standards from coderef-docs
  // - test strategy from coderef-testing
  implementTask(task);
}

// Track completion
await coderefWorkflow.updateTaskStatus(task.id, "completed");
```

**Tools available:** All MCP tools + project-specific context

---

### Layer 3: coderef Dashboard
**Who:** Human operators, orchestrator, dashboard widgets

**How they access:**
```
Dashboard UI
├── Workorder Status Widget
│   ├── WO-ID
│   ├── Progress bar
│   ├── Agent assignments
│   └── Last update
├── Agent Progress Widget
│   ├── Current task
│   ├── Time spent
│   └── Blockers
├── Task Tracking Widget
│   ├── Open tasks
│   ├── In-progress
│   └── Completed
├── Standards Compliance Widget
│   ├── UI standards
│   ├── Behavior patterns
│   └── Violations
└── Changelog Widget
    ├── Recent changes
    ├── Contributors
    └── Metrics
```

**Data sources:**
- communication.json (workorder status)
- plan.json (task breakdown)
- git history (metrics)
- DELIVERABLES.md (completion stats)

---

## Data Flow (Complete System)

```
Orchestrator (archer)
  ↓ creates workorder
  ↓
coderef-workflow: gather-context
  (collects requirements)
  ↓
coderef-context: analyze-for-planning
  (scans codebase, returns context)
  ↓
coderef-workflow: create-plan
  (uses context to generate plan.json)
  ↓
dashboard: displays plan progress
  ↓
coderef-workflow: execute-plan
  (breaks into tasks, embeds context)
  ↓
agents (personas or human AI): implement
  - Read context (coderef-context)
  - Follow standards (coderef-docs)
  - Run tests (coderef-testing)
  - Commit code (git-mcp)
  - Update status (coderef-workflow)
  ↓
dashboard: live updates show progress
  ↓
coderef-workflow: verify-agent-completion
  (git-mcp validates forbidden files)
  ↓
coderef-docs: update-changelog
  (records what changed)
  ↓
coderef-testing: validate
  (ensures code quality)
  ↓
coderef-workflow: archive-feature
  (move to coderef/archived/)
  ↓
dashboard: shows completion
```

---

## Integration Points (How They Talk)

### coderef-context → coderef-workflow
**Interface:** Function imports
```typescript
import {
  generateTaskContext,
  analyzeForPlanning,
  discoverStandards
} from '@coderef/context';
```

### coderef-workflow → coderef-docs
**Interface:** File reads
```typescript
// Workflow reads standards from coderef-docs output
const standards = fs.readFileSync('coderef/standards/UI-STANDARDS.md');
// Embeds in task description
```

### All servers → git-mcp
**Interface:** Tool calls
```typescript
// Any server can call git operations
await gitMcp.createWOBranch(workorderId);
await gitMcp.countLinesChanged(workorderId);
```

### All servers → claude-filesystem-mcp
**Interface:** File operations
```typescript
// All servers use filesystem operations
await filesystem.readJson('coderef/working/{feature}/plan.json');
await filesystem.writeJson('coderef/working/{feature}/context.json', data);
```

### All servers → coderef Dashboard
**Interface:** Real-time WebSocket
```typescript
// Dashboard subscribes to communication.json changes
ws.on('workorder.updated', (data) => {
  updateWidget(data);
});
```

---

## Deployment Architecture

```
├── coderef-context/
│   ├── src/
│   ├── package.json
│   └── MCP server (exports functions)
│
├── coderef-workflow/
│   ├── src/
│   ├── package.json
│   └── MCP server (calls coderef-context)
│
├── coderef-docs/
│   ├── src/
│   ├── package.json
│   └── MCP server (generates markdown)
│
├── coderef-testing/
│   ├── src/
│   ├── package.json
│   └── MCP server (validates code)
│
├── git-mcp/
│   ├── src/
│   ├── package.json
│   └── MCP server (git operations)
│
├── claude-filesystem-mcp/
│   ├── src/
│   ├── package.json
│   └── MCP server (file operations)
│
└── coderef-dashboard/
    ├── src/
    ├── package.json
    └── Next.js + Electron app
        ├── PWA (web)
        ├── Electron (desktop)
        └── Widget system
```

---

## Current Status

### Agents Already Working On:

1. **WO-MCP-DOC-WORKFLOW-REFACTOR-001** (docs-mcp agent)
   - Extracting 24 tools to coderef-workflow
   - Simplifying docs-mcp to 10 pure doc tools

2. **WO-CODEREF-CONTEXT-ENHANCEMENT-001** (coderef-system agent)
   - Building Phases 1-6 in coderef-context
   - Generating context.json and task-context.json

3. **WO-MODULAR-WIDGET-SYSTEM-PWA-ELECTRON-001** (scriptboard agent)
   - Building widget system
   - Connecting to live workorder data

### Next Phase:
- git-mcp integration (parallel)
- claude-filesystem-mcp integration (parallel)
- Dashboard consumption of all 4 coderef + 2 utility servers
- End-to-end test of unified system

---

## Key Innovation

**Not a monolithic system.**

Each server is:
- ✅ Independently deployable
- ✅ Focused on one concern
- ✅ Talks via clean APIs (function imports or file I/O)
- ✅ Accessible to both persona agents and human AI agents
- ✅ Visualized in unified dashboard

**Result:** Agents (personas or humans) have access to all tools they need, through multiple access points (CLI, imports, dashboard).
