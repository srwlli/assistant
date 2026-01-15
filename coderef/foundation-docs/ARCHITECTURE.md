---
workorder_id: WO-FOUNDATION-DOCS-001
generated_by: coderef-docs v2.0.0
feature_id: foundation-documentation
doc_type: architecture
title: Assistant - Architecture Documentation
version: 2.0.0
status: APPROVED
---

# Architecture Documentation

**Project:** Assistant (Orchestrator CLI)
**Version:** 2.0.0
**Last Updated:** 2026-01-09

---

## System Overview

Assistant is a **delegation-first orchestrator** that coordinates work across multiple software projects without executing code directly in those projects. It follows the principle: **Identify, Delegate, Collect**.

### Core Innovation

**Problem:** Managing multi-project development with AI agents leads to context fragmentation and lost workorder tracking.

**Solution:** Centralized orchestrator that:
1. Captures ideas as stubs (STUB-XXX)
2. Promotes stubs to workorders (WO-XXX)
3. Delegates to project-specific agents via handoff protocol
4. Tracks progress via communication.json files
5. Aggregates results across all projects

---

## Architectural Patterns

### 1. Delegation Pattern (Core)

**Pattern:** Orchestrator never executes code in target projects

**Flow:**
```
User Idea
    ↓
Orchestrator captures (STUB-XXX)
    ↓
User approves promotion
    ↓
Orchestrator creates context.json + communication.json in target project
    ↓
Orchestrator generates handoff prompt
    ↓
User pastes prompt into project agent chat
    ↓
Project agent executes (has full project context)
    ↓
Agent updates communication.json
    ↓
Orchestrator reads status, updates centralized tracking
```

**Benefits:**
- Clear separation of concerns (orchestration vs. execution)
- Project agents have full codebase context
- No context fragmentation
- Conflict-free concurrent work across projects

---

### 2. File-Based API Pattern

**Pattern:** JSON files as data contracts between systems

**Data Files:**
- `workorders.json` - Centralized workorder tracking
- `projects.config.json` - Project registry
- `stub.json` - Idea capture
- `communication.json` - Inter-agent handoff protocol
- `plan.json` - Implementation plans
- `DELIVERABLES.md` - Completion metrics

**Advantages:**
- Version-controlled data (all changes in git)
- Human-readable and editable
- Language-agnostic (works with Python, JS, shell scripts)
- No database setup required
- Offline-first architecture

**Pattern Implementation:**
```javascript
// Read data
const data = JSON.parse(fs.readFileSync('data.json'));

// Modify
data.items.push(newItem);

// Write atomically
fs.writeFileSync('data.json', JSON.stringify(data, null, 2));
```

---

### 3. Two-Tier ID System

**Pattern:** Separate ID namespaces for ideas vs. active work

**Tier 1: Stub IDs (STUB-XXX)**
- Auto-incremented from `projects.md`
- Persistent (never reused)
- Tracked in orchestrator: `coderef/working/*/stub.json`
- Lifecycle: planning → ready → promoted/blocked/abandoned

**Tier 2: Workorder IDs (WO-FEATURE-XXX-###)**
- Format: `WO-{FEATURE}-{PROJECT}-{###}`
- Example: `WO-AUTH-DASHBOARD-001`
- Tracked in `workorders.json`
- Lifecycle: pending_plan → plan_submitted → approved → implementing → complete → verified → closed

**Relationship:**
```
STUB-057 (wo-tracking-widget)
    ↓ promotes to
WO-DASHBOARD-WIDGET-001
    └──> location: coderef-dashboard/coderef/workorder/wo-tracking-widget/
```

---

### 4. Communication Protocol (Handoff Pattern)

**Pattern:** Structured messaging between orchestrator and project agents

**File:** `communication.json`

**Protocol:**
```json
{
  "workorder_id": "WO-XXX",
  "status": "pending_plan",
  "handoff": {
    "orchestrator_to_agent": "Instructions here",
    "status": "pending_plan"
  },
  "communication_log": [
    {
      "timestamp": "2025-12-20T10:30:00Z",
      "from": "orchestrator",
      "message": "Workorder delegated",
      "phase": "planning"
    }
  ]
}
```

**Status Flow:**
1. **Planning Phase:** pending_plan → plan_submitted
2. **Approval Phase:** [changes_requested] → approved
3. **Implementation Phase:** implementing → complete
4. **Verification Phase:** verified → closed

**Rules:**
- Orchestrator writes initial handoff instructions
- Agent updates status after each phase
- Orchestrator reads (never modifies) agent's communication.json
- All updates logged in communication_log array

---

### 5. MCP Integration Architecture

**Pattern:** Tool-based APIs via Model Context Protocol servers

**6 MCP Servers:**

1. **coderef-context** - Code analysis (complexity, patterns, examples)
2. **coderef-workflow** - Implementation planning (gather_context, create_plan, execute_plan)
3. **coderef-docs** - Documentation generation (POWER framework docs, workorder logging)
4. **personas-mcp** - Persona activation system
5. **coderef-personas** - CodeRef Assistant persona (orchestrator-specific behavior)
6. **scriptboard-mcp** - Scriptboard UI integration

**Integration Pattern:**
```
Orchestrator
    ↓ uses
coderef-docs (log_workorder, generate_handoff_context)
coderef-personas (activate CodeRef Assistant)
    ↓ delegates to
Project Agent
    ↓ uses
coderef-workflow (create_plan, update_deliverables)
coderef-context (analyze complexity, get examples)
    ↓ reports back
Orchestrator (reads communication.json)
```

---

## System Layers

### Layer 1: Presentation

**Components:**
- `index.html` - Static HTML dashboard (workorders, stubs, stats)
- `web/index.html` - Electron app UI (file browser, project manager)
- CSS - Embedded styles (BEM-like naming, responsive grid layouts)

**Technologies:**
- Vanilla HTML/CSS/JS (no frontend framework)
- Material Icons for UI symbols
- CSS Grid + Flexbox for layouts
- Dark mode support (CSS variables)

**Data Binding:**
- File-based (reads workorders.json, projects.md)
- Static generation (no real-time updates in v2.0.0)

---

### Layer 2: Application Logic

**Components:**
- Slash Commands (`.claude/commands/`) - Workflow definitions
- Python Scripts (`*.py`) - Automation and validation
- `web/server.py` - HTTP API server for Electron app

**Key Scripts:**
- `/stub` - Capture idea workflow
- `/create-session` - Multi-agent session initialization
- `/archive-file` - File archival by project
- `validate-stubs.py` - Schema validation
- `infer-target-projects.py` - Auto-assign target projects

**Execution Model:**
- Slash commands execute in Claude agent context
- Python scripts run as CLI commands
- HTTP server runs as local development server (port 8080)

---

### Layer 3: Data

**File Structure:**
```
assistant/
├── projects.md                    # Project list + STUB-ID counter
├── workorders.json                # Centralized workorder tracking
├── projects.config.json           # Project registry
├── stub-schema.json               # Canonical stub validation schema
├── coderef/
│   ├── working/                   # Stub storage (orchestrator-owned)
│   │   └── {feature-name}/
│   │       └── stub.json
│   └── archived/                  # Completed features
└── index.html                     # Dashboard

Target Project Structure:
{project}/coderef/workorder/{feature-name}/
├── communication.json             # Handoff protocol (agent-owned)
├── context.json                   # Requirements (orchestrator-owned)
├── plan.json                      # Implementation plan (agent-created)
└── DELIVERABLES.md                # Completion metrics (agent-created)
```

**Data Ownership:**
- **Orchestrator owns:** stubs (coderef/working), workorders.json, context.json
- **Project agent owns:** communication.json, plan.json, DELIVERABLES.md
- **Shared read access:** Both can read each other's files

---

### Layer 4: Integration

**MCP Servers (External):**
- Located in `C:\Users\willh\.mcp-servers\{server-name}`
- Expose tools via MCP protocol
- Authenticated via Claude Desktop configuration
- Provide specialized capabilities (context analysis, workflow management, documentation generation)

**Projects (External):**
- Scrapper (`C:\Users\willh\Desktop\scrapper`)
- Gridiron (`C:\Users\willh\Desktop\latest-sim\gridiron-franchise`)
- CodeRef Dashboard (`C:\Users\willh\Desktop\coderef-dashboard`)
- Scriptboard (`C:\Users\willh\Desktop\clipboard_compannion\next`)
- Noted (`C:\Users\willh\Desktop\projects\noted`)
- Multi-Tenant (`C:\Users\willh\Desktop\Business-Dash\latest-app`)

**Communication:**
- Orchestrator reads project workorder folders
- Projects update their own communication.json files
- Orchestrator aggregates status into workorders.json

---

## Key Design Decisions

### 1. Why File-Based Instead of Database?

**Decision:** Use JSON files as primary data store

**Rationale:**
- Version control - All data changes tracked in git
- Human readable - Easy to inspect and debug
- No setup required - Works immediately without database installation
- Offline-first - No network dependency
- Simple backups - Just copy files
- Language-agnostic - Works with Python, JS, shell scripts

**Trade-offs:**
- ❌ No concurrent write safety (mitigated by single-writer pattern)
- ❌ No complex querying (mitigated by small dataset size)
- ✅ Simplicity and transparency win for orchestrator use case

---

### 2. Why Delegate Instead of Execute?

**Decision:** Orchestrator never executes code in target projects

**Rationale:**
- Project agents have full codebase context (orchestrator doesn't)
- Avoids context fragmentation across multiple agents
- Clear separation: orchestrator tracks, agents implement
- Prevents conflicts from concurrent execution
- Scales to unlimited projects without context limit issues

**Trade-offs:**
- ❌ Requires manual copy-paste of handoff prompts (automated in future)
- ✅ Zero conflicts, maximum context utilization

---

### 3. Why Two-Tier ID System?

**Decision:** Separate STUB-XXX and WO-XXX namespaces

**Rationale:**
- Stubs live for months before promotion (need persistent IDs)
- Workorders are time-bounded (weeks to complete)
- Stub IDs are simple incrementing numbers (STUB-001, STUB-002, ...)
- Workorder IDs include feature/project context (WO-AUTH-DASHBOARD-001)
- Allows tracking stub → workorder lineage

**Trade-offs:**
- ❌ Two ID systems to manage
- ✅ Clear lifecycle stages, better traceability

---

### 4. Why communication.json Instead of Centralized Log?

**Decision:** Each workorder has its own communication.json in target project

**Rationale:**
- Co-located with work (agent sees communication.json next to code)
- Project-owned (agent controls their status updates)
- Version-controlled with code (status history in git)
- Offline-capable (no central service required)

**Trade-offs:**
- ❌ Requires scanning multiple files for global status
- ✅ Better separation of concerns, version-controlled audit trail

---

## Security Considerations

### File Access Control

**Pattern:** Trust-based filesystem access

**Security Model:**
- Orchestrator has read-only access to target project files
- Project agents have write access to their own workorder folders
- No authentication/authorization layer (local development environment)

**Risks:**
- Malicious agent could modify orchestrator files (mitigated: single-user environment)
- No audit trail for file modifications (mitigated: git version control)

---

### Data Validation

**Pattern:** JSON Schema validation at write time

**Implementation:**
- `stub-schema.json` - Enforces stub structure
- `validate-stubs.py` - CLI validation script
- Pre-commit hooks (future: auto-validate before git commit)

**Validation Points:**
1. Stub creation (`/stub` command validates before writing)
2. Manual validation (`python validate-stubs.py`)
3. Dashboard display (filters invalid stubs)

---

## Performance Characteristics

### Scalability

**Current Scale (v2.0.0):**
- 82 stubs tracked
- 12 active projects
- 19 active workorders
- 6 completed workorders

**Expected Limits:**
- Stubs: 1000+ (STUB-001 to STUB-999 pattern)
- Projects: 50+ (file scan overhead minimal)
- Active workorders: 100+ (JSON parse/write overhead acceptable)

**Bottlenecks:**
- File I/O for workorder scanning (O(n) projects × O(m) workorders)
- Dashboard rendering (static HTML regeneration required)
- Stub validation (O(n) stubs × JSON schema validation)

**Future Optimizations:**
- Index files (pre-scanned workorder/stub metadata)
- Real-time dashboard updates (WebSocket integration)
- Incremental validation (only changed stubs)

---

### Latency

**Operation Times (estimated):**
- Stub creation (`/stub`): <1 second (file writes)
- Workorder promotion: <2 seconds (multi-file creation)
- Status check: <5 seconds (scan all communication.json files)
- Dashboard load: <1 second (static HTML)

---

## Deployment Architecture

### Development Environment

**Current Deployment (v2.0.0):**
- Local filesystem (`C:\Users\willh\Desktop\assistant`)
- Static HTML dashboard (`file:///` protocol)
- Python HTTP server for Electron app (port 8080, localhost-only)
- Manual slash command execution in Claude agent

**Requirements:**
- Node.js (for Electron app)
- Python 3.8+ (for automation scripts)
- Claude Desktop (for MCP server integration)
- Git (for version control)

---

### Production Considerations (Future)

**Potential Production Architecture:**
```
Web Dashboard (Next.js/React)
    ↓ HTTP
API Server (FastAPI or Express)
    ↓ File System
JSON Data Store (current structure)
    ↓ Git Sync
GitHub Repository (version control + collaboration)
```

**Challenges:**
- Multi-user collaboration (file locking, conflict resolution)
- Real-time updates (WebSocket or polling)
- Authentication/authorization (project-level access control)

---

## Extension Points

### 1. Custom Slash Commands

**Location:** `.claude/commands/{command-name}.md`

**Template:**
```markdown
# /my-command

Execute custom workflow...

Steps:
1. Read input from user
2. Process data
3. Write results
4. Confirm to user
```

**Usage:**
```bash
/my-command arg1 arg2
```

---

### 2. MCP Server Integration

**Pattern:** Add new tool-based APIs via MCP servers

**Steps:**
1. Create new MCP server in `C:\Users\willh\.mcp-servers\{name}`
2. Define tools in `src/index.ts` (TypeScript) or `server.py` (Python)
3. Add to Claude Desktop MCP configuration
4. Restart Claude Desktop
5. Invoke tools from orchestrator or project agents

**Example Tool:**
```typescript
server.tool("my_custom_tool", {
  description: "Does something useful",
  schema: { type: "object", properties: { input: { type: "string" } } }
}, async ({ input }) => {
  const result = process(input);
  return { content: [{ type: "text", text: result }] };
});
```

---

### 3. Python Automation Scripts

**Pattern:** Add new CLI scripts for automation

**Template:**
```python
#!/usr/bin/env python3
import json
from pathlib import Path

def main():
    # Read data
    data = json.loads(Path('data.json').read_text())

    # Process
    result = transform(data)

    # Write
    Path('output.json').write_text(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
```

---

## Monitoring & Observability

### Current State (v2.0.0)

**Logging:**
- Console output from Python scripts
- Agent conversation logs (Claude Desktop)
- Git commit history (audit trail)

**Metrics:**
- Dashboard stats (active WOs, completed WOs, stubs)
- Manual inspection of communication.json files

**Alerting:**
- None (manual monitoring only)

---

### Future Enhancements

**Potential Improvements:**
- Centralized logging (all script outputs to log file)
- Workorder status dashboard with real-time updates
- Slack/email notifications for status changes
- Grafana dashboards for metrics visualization
- Automated health checks (validate all communication.json files)

---

## Related Documentation

- **[API.md](./API.md)** - API endpoints and file-based APIs
- **[SCHEMA.md](./SCHEMA.md)** - Data schemas
- **[COMPONENTS.md](./COMPONENTS.md)** - UI and script components
- **[CLAUDE.md](../../CLAUDE.md)** - Full AI context documentation

---

**Document ID:** `assistant-architecture-v2.0.0`
**Last Generated:** 2026-01-09 via `/generate-docs`
