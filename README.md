# Assistant - Orchestrator CLI

**Version:** 2.0.0
**Status:** ✅ Production
**Principle:** Identify, Delegate, Collect

---

## Overview

**Assistant** is a lightweight orchestrator CLI that coordinates work across multiple software projects without executing code directly in those projects. It maintains centralized tracking of ideas (stubs) and workorders while delegating implementation to project-specific AI agents with full codebase context.

### Core Innovation

Each project has its own embedded agent with complete project context. Assistant orchestrates at a higher level:
1. Captures ideas as **STUB-XXX** (centralized in orchestrator)
2. Promotes ready ideas to **WO-XXX** workorders (delegated to projects)
3. Tracks progress via **communication.json** handoff protocol
4. Aggregates results across all projects in one dashboard

**Result:** Zero context fragmentation, maximum agent effectiveness, complete visibility.

---

## Quick Start

### Prerequisites

- **Python 3.8+** (for automation scripts)
- **Node.js 18+** (for Electron app, optional)
- **Claude Desktop** (for MCP server integration)
- **Git** (for version control)

### Installation

```bash
# Clone repository
git clone https://github.com/your-username/assistant.git
cd assistant

# Verify structure
ls -la
# Expected: CLAUDE.md, projects.md, workorders.json, index.html, coderef/

# Open dashboard
open index.html  # macOS
start index.html  # Windows
xdg-open index.html  # Linux
```

### First Steps

1. **Review Dashboard** - Open `index.html` to see current stubs and workorders
2. **Capture an Idea** - Run `/stub my-feature-idea` to create STUB-082
3. **Validate Stubs** - Run `python validate-stubs.py` to check schema compliance
4. **Explore Projects** - Check `projects.md` for all tracked projects

---

## Key Concepts

### Stubs (Ideas)

**What:** Captured ideas before implementation

**Location:** `coderef/working/{feature-name}/stub.json`

**Lifecycle:**
```
planning → ready → promoted (to workorder)
              ↓
           blocked / abandoned
```

**Example:**
```json
{
  "stub_id": "STUB-057",
  "feature_name": "wo-tracking-widget",
  "description": "Dashboard widget for workorder tracking",
  "category": "feature",
  "priority": "high",
  "status": "planning",
  "created": "2025-12-20",
  "target_project": "coderef-dashboard"
}
```

**Commands:**
- `/stub [idea]` - Capture new idea
- `python validate-stubs.py` - Validate all stubs

---

### Workorders (Active Work)

**What:** Promoted stubs delegated to project agents

**Location (centralized):** `workorders.json`
**Location (project):** `{project}/coderef/workorder/{feature-name}/communication.json`

**Lifecycle:**
```
pending_plan → plan_submitted → approved → implementing → complete → verified → closed
```

**Example:**
```json
{
  "workorder_id": "WO-DASHBOARD-WIDGET-001",
  "stub_id": "STUB-057",
  "feature_name": "wo-tracking-widget",
  "target_project": "coderef-dashboard",
  "status": "pending_plan",
  "next_action": "Agent: Run /create-plan workflow"
}
```

**Status Check:**
```bash
# Read workorders.json to see all active/completed workorders
cat workorders.json | jq '.active_workorders[] | {id, status, next_action}'
```

---

### Communication Protocol

**What:** Handoff mechanism between orchestrator and project agents

**File:** `{project}/coderef/workorder/{feature-name}/communication.json`

**Phases:**
1. **Planning** - Agent creates plan, updates status to `plan_submitted`
2. **Approval** - Orchestrator reviews, sets status to `approved` or `changes_requested`
3. **Implementation** - Agent executes, updates to `implementing` → `complete`
4. **Verification** - Orchestrator verifies, closes workorder

**Example Handoff:**
```json
{
  "workorder_id": "WO-AUTH-001",
  "status": "plan_submitted",
  "handoff": {
    "orchestrator_to_agent": "Review context.json and run /create-plan",
    "status": "plan_submitted"
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

---

## Workflows

### Capture Idea Workflow

**Command:** `/stub [feature-name]`

**Steps:**
1. Run `/stub wo-tracking-widget`
2. Assistant creates `coderef/working/wo-tracking-widget/stub.json`
3. Assistant assigns next STUB-ID (e.g., STUB-057)
4. Assistant updates `projects.md` counter (Next STUB-ID: STUB-058)
5. Confirm: "Stubbed: STUB-057: wo-tracking-widget"

---

### Promote Stub to Workorder Workflow

**Process:** (Manual in v2.0.0, automating in v2.1.0)

1. **Identify Ready Stub** - Check dashboard or `projects.md`
2. **Assign Workorder ID** - Format: `WO-FEATURE-PROJECT-###`
3. **Create Files in Target Project:**
   ```bash
   # Example: coderef-dashboard
   mkdir -p {target-project}/coderef/workorder/wo-tracking-widget
   ```
4. **Generate context.json:**
   ```json
   {
     "workorder_id": "WO-DASHBOARD-WIDGET-001",
     "stub_id": "STUB-057",
     "requirements": ["Real-time status", "Visual indicators"],
     "constraints": ["Must integrate with existing dashboard"]
   }
   ```
5. **Generate communication.json:**
   ```json
   {
     "workorder_id": "WO-DASHBOARD-WIDGET-001",
     "status": "pending_plan",
     "handoff": {
       "orchestrator_to_agent": "Review context.json and run /create-plan",
       "status": "pending_plan"
     }
   }
   ```
6. **Update workorders.json** - Add to `active_workorders` array
7. **Generate Handoff Prompt** - Provide to user for project agent
8. **User Pastes Prompt** - Into target project agent chat

---

### Check Workorder Status Workflow

**Steps:**
1. Open `workorders.json`
2. Filter by project or status:
   ```bash
   # All coderef-dashboard workorders
   cat workorders.json | jq '.active_workorders[] | select(.target_project=="coderef-dashboard")'

   # All pending plan workorders
   cat workorders.json | jq '.active_workorders[] | select(.status=="pending_plan")'
   ```
3. Check specific project's communication.json:
   ```bash
   cat {project}/coderef/workorder/{feature}/communication.json
   ```
4. Review dashboard at `index.html`

---

## File Structure

```
assistant/
├── README.md                          # This file
├── CLAUDE.md                          # Full AI context documentation
├── projects.md                        # Project list + STUB-ID counter
├── workorders.json                    # Centralized workorder tracking
├── projects.config.json               # Project registry
├── stub-schema.json                   # Canonical stub validation schema
├── index.html                         # Visual dashboard
├── terminal-profiles.md               # Windows Terminal profiles
├── .claude/
│   └── commands/                      # Slash command definitions
│       ├── stub.md
│       ├── create-session.md
│       └── archive-file.md
├── coderef/
│   ├── foundation-docs/               # Generated documentation
│   │   ├── API.md
│   │   ├── SCHEMA.md
│   │   ├── COMPONENTS.md
│   │   ├── ARCHITECTURE.md
│   │   └── README.md
│   ├── working/                       # Stub storage
│   │   └── {feature-name}/
│   │       └── stub.json
│   └── archived/                      # Completed features
├── web/                               # Electron app (CodeRef Explorer)
│   ├── index.html
│   ├── server.py                      # Python HTTP server
│   └── package.json
├── scripts/
│   ├── validate-stubs.py
│   ├── infer-target-projects.py
│   └── create-coderef-structure.py
└── tools/                             # Python automation utilities
```

---

## Commands Reference

### Slash Commands (Claude Agent)

| Command | Description | Example |
|---------|-------------|---------|
| `/stub [idea]` | Capture new idea as STUB-XXX | `/stub wo-tracking-widget` |
| `/create-session` | Initialize multi-agent session | `/create-session` |
| `/archive-file` | Archive file by project | `/archive-file old-doc.md` |
| `/generate-docs` | Generate foundation documentation | `/generate-docs` |

### Python Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `validate-stubs.py` | Validate all stub.json against schema | `python validate-stubs.py` |
| `infer-target-projects.py` | Auto-assign target_project to stubs | `python infer-target-projects.py` |
| `assign-unknown-targets.py` | Assign projects to stubs missing target | `python assign-unknown-targets.py` |

### Electron App (Optional)

```bash
cd web
npm install
npm start  # Launch CodeRef Explorer desktop app
```

---

## Configuration

### projects.config.json

**Purpose:** Central registry of all tracked projects

**Structure:**
```json
{
  "version": "1.0.0",
  "projects": [
    {
      "id": "coderef-dashboard",
      "name": "CodeRef Dashboard",
      "type": "application",
      "path": "C:\\Users\\willh\\Desktop\\coderef-dashboard",
      "has_workorders": true,
      "workorder_dir": "coderef/workorder",
      "status": "active"
    }
  ],
  "centralized": {
    "stubs_dir": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\working"
  }
}
```

**Adding a Project:**
1. Add entry to `projects` array
2. Set `has_workorders: true` if project accepts delegated work
3. Specify `workorder_dir` (usually `coderef/workorder`)
4. Update orchestrator's tracking

---

## MCP Server Integration

Assistant integrates with 6 MCP servers for enhanced capabilities:

| Server | Purpose | Tools Provided |
|--------|---------|----------------|
| **coderef-context** | Code analysis | Pattern detection, complexity scoring, examples |
| **coderef-workflow** | Implementation planning | gather_context, create_plan, execute_plan |
| **coderef-docs** | Documentation generation | POWER framework docs, workorder logging |
| **personas-mcp** | Persona activation | Expert role specialization |
| **coderef-personas** | CodeRef Assistant persona | Orchestrator-specific behavior |
| **scriptboard-mcp** | Scriptboard UI bridge | Clipboard history, UI integration |

**Usage Example:**
```
Orchestrator uses coderef-docs tools:
- log_workorder(workorder_id, details)
- generate_handoff_context(plan.json path)

Project Agent uses coderef-workflow tools:
- create_plan(feature_name, requirements)
- update_deliverables(git_metrics)
```

---

## Active Projects

| Project | Path | Status | Workorders |
|---------|------|--------|------------|
| Scriptboard | `C:\Users\willh\Desktop\clipboard_compannion\next` | ✅ Active | 3 active |
| Scrapper | `C:\Users\willh\Desktop\scrapper` | ✅ Active | 1 active |
| Gridiron | `C:\Users\willh\Desktop\latest-sim\gridiron-franchise` | ✅ Active | 2 active |
| CodeRef Dashboard | `C:\Users\willh\Desktop\coderef-dashboard` | 🚧 Building | 4 active |
| Noted | `C:\Users\willh\Desktop\projects\noted` | ✅ Active | 1 active |
| Multi-Tenant | `C:\Users\willh\Desktop\Business-Dash\latest-app` | ✅ Active | 1 active |

**Current Stats (v2.0.0):**
- **82 Stubs** tracked
- **19 Active Workorders** across 6 projects
- **6 Completed Workorders** verified and archived

---

## Development

### Prerequisites

- Python 3.8+ (scripts and validation)
- Node.js 18+ (optional, for Electron app)
- Claude Desktop (MCP server integration)
- Git (version control)

### Local Setup

```bash
# Clone repository
git clone https://github.com/your-username/assistant.git
cd assistant

# Validate stubs
python validate-stubs.py

# Open dashboard
open index.html

# (Optional) Run Electron app
cd web
npm install
npm start
```

### Adding a Stub

```bash
# Via slash command
/stub my-new-feature

# Manually
mkdir -p coderef/working/my-new-feature
cat > coderef/working/my-new-feature/stub.json << EOF
{
  "stub_id": "STUB-082",
  "feature_name": "my-new-feature",
  "description": "Description of my feature idea",
  "category": "feature",
  "priority": "medium",
  "status": "planning",
  "created": "2026-01-09"
}
EOF

# Update projects.md next STUB-ID counter
# Next STUB-ID: STUB-083
```

### Running Validation

```bash
# Validate all stubs against schema
python validate-stubs.py

# Output:
# ✓ STUB-001: scriptboard-assistant-integration
# ✓ STUB-002: tool-inventory-workflow
# ...
# 82 stubs validated, 0 error(s) found
```

---

## Documentation

### Foundation Docs

- **[API.md](coderef/foundation-docs/API.md)** - File-based APIs, HTTP endpoints, slash commands
- **[SCHEMA.md](coderef/foundation-docs/SCHEMA.md)** - Data schemas (stub, workorder, communication, project config)
- **[COMPONENTS.md](coderef/foundation-docs/COMPONENTS.md)** - UI components, Python scripts, workflows
- **[ARCHITECTURE.md](coderef/foundation-docs/ARCHITECTURE.md)** - System architecture, design decisions, patterns

### AI Context

- **[CLAUDE.md](CLAUDE.md)** - Complete AI context documentation for CodeRef Assistant persona

### Project Tracking

- **[projects.md](projects.md)** - Master project list and stub inventory
- **[workorders.json](workorders.json)** - Live workorder tracking
- **[terminal-profiles.md](terminal-profiles.md)** - Windows Terminal configuration

---

## Troubleshooting

### Stub Validation Errors

**Error:** `Missing required field: category`

**Solution:**
```bash
# Add missing field to stub.json
{
  "stub_id": "STUB-057",
  "category": "feature",  # Add this
  ...
}
```

---

### Workorder Not Showing in Dashboard

**Check:**
1. Is it in `workorders.json` active_workorders array?
2. Does `index.html` need regeneration? (Currently static)
3. Is communication.json in correct location?

**Solution:**
```bash
# Verify entry in workorders.json
cat workorders.json | jq '.active_workorders[] | select(.workorder_id=="WO-XXX")'

# Check communication.json exists
ls {project}/coderef/workorder/{feature}/communication.json
```

---

### Python Script Errors

**Error:** `ModuleNotFoundError: No module named 'jsonschema'`

**Solution:**
```bash
pip install jsonschema
```

---

## Roadmap

### v2.1.0 (Next Release)
- ⏳ Automate stub promotion workflow
- ⏳ Build `/stub` slash command with auto-ID assignment
- ⏳ Real-time dashboard updates (WebSocket integration)
- ⏳ Automated handoff prompt generation

### v3.0.0 (Future)
- ⏳ Dependency tracking (WO-001 blocks WO-002)
- ⏳ Multi-user collaboration support
- ⏳ Web-based dashboard (replace static HTML)
- ⏳ Scriptboard UI integration (primary visual interface)

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Validate stubs (`python validate-stubs.py`)
5. Commit your changes (`git commit -am 'Add my feature'`)
6. Push to the branch (`git push origin feature/my-feature`)
7. Create a Pull Request

---

## License

MIT License - see LICENSE file for details

---

## Support

- **Issues:** [GitHub Issues](https://github.com/your-username/assistant/issues)
- **Discussions:** [GitHub Discussions](https://github.com/your-username/assistant/discussions)
- **Documentation:** [Foundation Docs](coderef/foundation-docs/)

---

## Acknowledgments

**Built with:**
- Claude Desktop & MCP Protocol
- Python 3.8+
- Electron (for desktop app)
- Vanilla HTML/CSS/JS (dashboard)

**Powered by:**
- coderef-context MCP server
- coderef-workflow MCP server
- coderef-docs MCP server
- coderef-personas MCP server

---

**Version:** 2.0.0
**Last Updated:** 2026-01-09
**Maintained by:** CodeRef Assistant (Orchestrator Persona)
