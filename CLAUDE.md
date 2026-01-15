# Assistant - AI Context Documentation

**Project:** Assistant (Orchestrator CLI)
**Version:** 2.0.0
**Status:** ✅ Production
**Created:** 2025-11-15
**Last Updated:** 2025-12-28

---

## Quick Summary

**Assistant** is a focused orchestrator CLI that coordinates work across multiple projects without executing code directly in those projects.

**Core Innovation:** Centralized workorder tracking with delegation-first architecture. Each target project has its own embedded agent with full context - Assistant identifies work, delegates to project agents, and aggregates results.

**Latest Update (v2.0.0):**
- ✅ Integrated with 6 MCP servers (coderef-context, coderef-workflow, coderef-docs, personas-mcp, coderef-personas, scriptboard-mcp)
- ✅ Added STUB-XXX and WO-XXX ID tracking system
- ✅ Implemented communication.json handoff protocol for project agents
- ✅ Built visual dashboard (index.html) for real-time workorder status

**Key Relationships:**
- **coderef-workflow** = Planning and execution tracking
- **coderef-docs** = Documentation generation and workorder logging
- **coderef-personas** = CodeRef Assistant persona activation
- **scriptboard-mcp** = UI bridge for Scriptboard integration
- **Target Projects** = Scrapper, Gridiron, CodeRef Dashboard, Noted, Multi-Tenant

Together they form a unified orchestration system where Assistant captures ideas as stubs, promotes them to workorders, delegates to project agents via handoff prompts, and tracks progress through communication.json files.

---

## Problem & Vision

### The Problem

Managing multiple software projects with AI agents leads to context fragmentation. Each project has its own embedded agent with full codebase context, but coordinating work across projects becomes chaotic. Ideas get lost, workorders aren't tracked, and there's no central visibility into what's happening where.

### The Solution

Assistant acts as a lightweight orchestrator that captures ideas, delegates work to project-specific agents, and aggregates results—without executing code in target projects. It maintains the separation of concerns: orchestrator sees the full arc across all projects, project agents execute with full local context.

### How It Works

1. User shares idea → Assistant captures as STUB-XXX
2. User ready to implement → Assistant promotes to WO-XXX, creates context.json + communication.json in target project
3. Assistant generates handoff prompt → User pastes into target project agent
4. Project agent executes, updates communication.json → Assistant tracks progress
5. Agent completes → Assistant verifies, updates centralized tracking, closes workorder

---

## Architecture

### Core Concepts

**1. Identify, Delegate, Collect**
Assistant NEVER executes code in other projects. Each project has its own embedded Lloyd agent with full context. Assistant's role:
- Capture ideas as STUB-XXX IDs
- Generate handoff prompts with WO-XXX IDs
- Track progress via communication.json
- Aggregate results across projects

**2. Stub vs Workorder Lifecycle**
```
Idea → STUB-XXX (captured in orchestrator)
       ↓
STUB promoted → WO-FEATURE-XXX (delegated to project agent)
                ↓
                context.json + communication.json created in target project
                ↓
                Agent executes, updates communication.json
                ↓
                Orchestrator verifies and closes workorder
```

**3. Two-Tier File System**
- **Orchestrator files** (coderef/working/) = Stubs only (ideas not yet delegated)
- **Target project files** (coderef/working/ or coderef/features/) = Active workorders with context.json + communication.json

### Data Flow
```
User Idea
  ↓
Assistant captures STUB-XXX
  ↓
projects.md updated (stub inventory)
  ↓
User promotes stub → WO-XXX
  ↓
Assistant creates files in TARGET PROJECT:
  - context.json (requirements)
  - communication.json (workflow tracking)
  ↓
Assistant generates handoff prompt
  ↓
User pastes prompt into project agent chat
  ↓
Project agent executes:
  - Runs /create-plan workflow
  - Updates communication.json (status: plan_submitted)
  - Implements features
  - Updates communication.json (status: complete)
  ↓
Assistant verifies:
  - Reads communication.json
  - Updates workorders.json (centralized tracking)
  - Updates index.html (dashboard)
  - Moves to completed_workorders
```

### Key Integration Points

- **Depends on:** coderef-workflow (planning), coderef-docs (logging), coderef-personas (orchestrator persona)
- **Used by:** Target projects (Scrapper, Gridiron, CodeRef Dashboard, Noted, Multi-Tenant)
- **Orchestrated via:** CodeRef Assistant persona, /stub command, handoff prompts

---

## Workflows Catalog

| Workflow | Purpose | Trigger |
|----------|---------|---------|
| `/stub [idea]` | Capture idea as STUB-XXX | User has new idea |
| Promote to Workorder | Convert STUB → WO-XXX, delegate to project | User ready to implement |
| Handoff Protocol | Generate prompt for project agent | Workorder created |
| Status Check | Read communication.json from active projects | User asks for updates |
| Verify Completion | Review deliverables, close workorder | Agent reports completion |
| Dashboard Update | Sync workorders.json and index.html | After any workorder change |
| Terminal Profile Mgmt | Add/update Windows Terminal profiles | New project added |

**Total:** 7 workflows across 3 categories (Capture, Delegation, Tracking)

---

## Core Workflows

### Stub Creation Workflow

When user has a new idea:
1. Create folder: `coderef/working/{feature-name}/`
2. Assign next STUB-XXX from projects.md
3. Create stub.json with metadata:
```json
{
  "stub_id": "STUB-057",
  "feature_name": "wo-tracking-widget",
  "created": "2025-12-20",
  "status": "planning",
  "target_project": "coderef-dashboard"
}
```
4. Validate and auto-fill stub using papertrail MCP tool:
   - Call `mcp__papertrail__validate_stub` with `auto_fill=True` and `save=True`
   - Tool auto-fills missing required fields (category, priority, description)
   - Returns validation results and updated stub
5. Update projects.md next STUB-ID counter
6. Confirm: "Stubbed: STUB-057: wo-tracking-widget"

### Workorder Handoff Protocol

**Location:** Files ALWAYS saved in TARGET PROJECT, not orchestrator.

When promoting stub to workorder:
1. Assign WO-FEATURE-XXX ID (preserves STUB-XXX for traceability)
2. Create in target project's `coderef/working/{feature-name}/` or `coderef/features/{feature-name}/`:
   - context.json (requirements, constraints, technical context)
   - communication.json (workflow status, tracking log)
3. Add to orchestrator's workorders.json (centralized tracking)
4. Generate handoff prompt:
```
NEW WORKORDER: WO-AUTH-001
Feature: authentication-system
Location: coderef/features/authentication-system/

Review:
1. context.json - requirements and constraints
2. communication.json - workflow instructions

Your Task:
1. Run /create-plan to generate implementation plan
2. Update communication.json:
   - Set handoff.status to "plan_submitted"
   - Add entry to communication_log with plan summary
3. Wait for approval before implementing

IMPORTANT: Update communication.json after EVERY phase change.
```
5. User pastes prompt into project agent chat

### Communication.json Status Flow

**Status Values:**
- `pending_plan` → Agent needs to submit plan
- `plan_submitted` → Awaiting orchestrator approval
- `changes_requested` → Orchestrator requested revisions
- `approved` → Ready to implement
- `implementing` → Agent executing plan
- `complete` → Agent finished (ran /update-deliverables + /archive-feature)
- `verified` → Orchestrator verified deliverables
- `closed` → Workorder complete

**4-Phase Workflow:**
```
Phase 1: Planning (agent)
  - Reviews context.json
  - Runs /create-plan
  - Updates communication.json → "plan_submitted"

Phase 2: Approval (orchestrator)
  - Reviews plan
  - Updates communication.json → "approved" or "changes_requested"

Phase 3: Implementation (agent)
  - Executes plan
  - Runs /update-deliverables (git metrics)
  - Runs /archive-feature
  - Updates communication.json → "complete"

Phase 4: Verification (orchestrator)
  - Reads communication.json (NEVER modifies files in target)
  - Updates workorders.json
  - Updates communication.json → "verified" → "closed"
```

### Terminal Profile Management

**File:** `terminal-profiles.md` - Master configuration for Windows Terminal quick-launch profiles

**Structure:** 18 Active Profiles organized in 3 groups:
- **Main Projects (10)** - Direct keyboard shortcuts (Ctrl+Shift+1 through Ctrl+Shift+9)
- **Coderef MCP Servers (6)** - Nested folder in new tab menu (🔌 system development)
- **Personas (2)** - Nested folder in new tab menu (🎭 specialized agent environments)

**To Add a New Profile:**

1. **Update terminal-profiles.md:**
   - Add entry to appropriate section (Main, Coderef, Personas)
   - Assign next ID number
   - Choose icon, color (from reference table at bottom)
   - Set directory path

2. **Update Windows Terminal settings.json:**
   - Location: `C:\Users\willh\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`
   - Generate new GUID: `[guid]::NewGuid()` in PowerShell
   - Add profile entry with: name, guid, icon, startingDirectory, tabColor, tabTitle
   - Add action entry: `User.open{ProfileName}`
   - Add keybinding (optional): if assigning keyboard shortcut

3. **Save & Reload:**
   - Close Windows Terminal
   - Edit settings.json
   - Reopen - auto-loads new profiles

4. **Update Documentation:**
   - Update total count in header: "## Current Profiles (X Active)"
   - Commit changes to git

**Current Unbound Shortcuts:** Ctrl+Shift+2, Ctrl+Shift+3, Ctrl+Shift+4, Ctrl+Shift+5, Ctrl+Shift+6, Ctrl+Shift+7, Ctrl+Shift+8, Ctrl+Shift+9, Ctrl+Shift+N

**Example Profile Entry:**
```json
{
  "guid": "{12345678-1234-1234-1234-123456789012}",
  "name": "CodeRef Dashboard",
  "icon": "🎨",
  "startingDirectory": "C:\\Users\\willh\\Desktop\\coderef-dashboard",
  "tabColor": "#FF5733",
  "tabTitle": "Dashboard"
}
```

---

## File Structure

```
assistant/
├── CLAUDE.md                                # This file - AI context
├── projects.md                              # Master project list + stub inventory
├── workorders.json                          # Centralized workorder tracking
├── index.html                               # Visual dashboard
├── terminal-profiles.md                     # Windows Terminal config reference
├── coderef/
│   └── working/
│       ├── feature-name-1/
│       │   └── stub.json                    # STUBS ONLY (ideas not delegated)
│       └── feature-name-2/
│           └── stub.json
└── README.md                                # User documentation

Target Project Structure (where work happens):
{project}/coderef/working/{feature-name}/
├── context.json                             # Requirements
├── communication.json                       # Workflow tracking
├── plan.json                                # Implementation plan (created by agent)
└── DELIVERABLES.md                          # Completion metrics (created by agent)
```

---

## Design Decisions

**1. Orchestrator Never Executes in Target Projects**
- ✅ Chosen approach: Read-only access to target projects, write only to orchestrator folder
- ❌ Rejected alternative: Orchestrator executing code directly in projects
- Reason: Target projects have embedded agents with full context. Orchestrator executing would bypass that context and risk conflicts. Delegation pattern keeps responsibilities clear.

**2. Two-Tier ID System (STUB-XXX → WO-XXX)**
- ✅ Chosen: STUB-XXX for ideas, WO-FEATURE-XXX for active work
- ❌ Rejected: Single unified ID system
- Reason: Stubs can live for months without promotion. Separating stub capture from workorder activation provides clear lifecycle stages and preserves traceability.

**3. communication.json for Handoff Tracking**
- ✅ Chosen: JSON file in target project with status enum
- ❌ Rejected: Centralized database, git commit messages, or manual reporting
- Reason: JSON is language-agnostic, version-controlled, and parseable by both humans and agents. Each project agent owns their communication.json, orchestrator only reads.

**4. File Location: Target Project vs Orchestrator**
- ✅ Chosen: orchestrator/coderef/working/ = stubs only, target/coderef/working/ = active workorders
- ❌ Rejected: All files in orchestrator folder
- Reason: Active work belongs with the project. Orchestrator coderef/working/ is for capture phase only. Once promoted, files live where the work happens.

**5. Centralized workorders.json + Distributed communication.json**
- ✅ Chosen: Orchestrator maintains workorders.json (aggregated view), each project has communication.json (detail)
- ❌ Rejected: Single source of truth in orchestrator only
- Reason: Orchestrator needs cross-project overview (workorders.json). Project agents need autonomy to update status (communication.json). Hybrid model balances visibility and ownership.

---

## Integration Guide

### With coderef-workflow
coderef-workflow provides planning tools used by project agents:
- `gather_context` - Agent captures requirements
- `create_plan` - Agent generates implementation plan
- `execute_plan` - Agent converts plan to TodoWrite task list
- `update_deliverables` - Agent records git metrics (LOC, commits, time)
- `archive_feature` - Agent moves completed work to coderef/archived/

Orchestrator delegates via handoff prompts that instruct agents to use these workflows.

### With coderef-docs
coderef-docs provides workorder logging:
- `log_workorder` - Orchestrator logs new WO-XXX to global workorder log
- `get_workorder_log` - Orchestrator queries workorder history
- `generate_handoff_context` - Auto-generates handoff prompts from plan.json

Orchestrator uses these tools to track cross-project history.

### With coderef-personas
coderef-personas provides CodeRef Assistant persona:
- Activates orchestrator-specific behavior (delegate, don't execute)
- Provides expertise in stub management, workorder tracking, handoff protocol
- Enforces read-only access to target projects

Orchestrator activates via `/coderef-assistant` slash command.

### With Target Projects (Scrapper, Gridiron, etc.)
Each project has:
- Embedded Lloyd agent with full project context
- coderef/working/ or coderef/features/ folder structure
- Ability to run coderef-workflow commands

Orchestrator creates context.json + communication.json in target project, generates handoff prompt, user pastes prompt into target agent chat.

### With MCP Servers Ecosystem

**6 Active MCP Servers:**

1. **coderef-context** (`C:\Users\willh\.mcp-servers\coderef-context`)
   - Code analysis and pattern detection
   - Complexity scoring and risk assessment
   - Task-specific context generation (effort, risk, examples, gotchas)
   - Used by: Project agents during implementation planning

2. **coderef-workflow** (`C:\Users\willh\.mcp-servers\coderef-workflow`)
   - Implementation planning (gather_context, create_plan, execute_plan)
   - Deliverables tracking (update_deliverables)
   - Feature archival (archive_feature)
   - Used by: Project agents for structured workflows

3. **coderef-docs** (`C:\Users\willh\.mcp-servers\coderef-docs`)
   - Workorder logging (log_workorder, get_workorder_log)
   - Handoff context generation (generate_handoff_context)
   - Documentation generation (foundation docs, standards)
   - Used by: Orchestrator for centralized tracking

4. **personas-mcp** (`C:\Users\willh\.mcp-servers\personas-mcp`)
   - Persona activation system
   - Expert role specialization
   - Used by: All agents for role-specific behavior

5. **coderef-personas** (`C:\Users\willh\.mcp-servers\coderef-personas`)
   - CodeRef Assistant persona definition
   - Orchestrator-specific behavior enforcement
   - Custom persona creation tools
   - Used by: Orchestrator via /coderef-assistant

6. **scriptboard-mcp** (`C:\Users\willh\.mcp-servers\scriptboard-mcp`)
   - Bridge to Scriptboard clipboard UI
   - Clipboard history management
   - Used by: Scriptboard project integration

**Integration Pattern:**
```
Orchestrator (uses coderef-docs + coderef-personas)
  ↓ delegates via handoff prompt
Project Agent (uses coderef-context + coderef-workflow + personas-mcp)
  ↓ executes and reports back
Orchestrator (reads results, updates central tracking)
```

### With Active Projects

**Connected Projects:**

| Project | Path | Git | Status |
|---------|------|-----|--------|
| Scriptboard | C:\Users\willh\Desktop\clipboard_compannion\next | [GitHub](https://github.com/user/scriptboard) | ✅ Active |
| Scrapper | C:\Users\willh\Desktop\scrapper | [GitHub](https://github.com/user/scrapper) | ✅ Active |
| Gridiron | C:\Users\willh\Desktop\latest-sim\gridiron-franchise | [GitHub](https://github.com/user/gridiron) | ✅ Active |
| CodeRef Dashboard | C:\Users\willh\Desktop\coderef-dashboard | [GitHub](https://github.com/user/coderef-dashboard) | 🚧 Building |
| Noted | C:\Users\willh\Desktop\projects\noted | [GitHub](https://github.com/user/noted) | ✅ Active |
| Multi-Tenant | C:\Users\willh\Desktop\Business-Dash\latest-app | [GitHub](https://github.com/user/multi-tenant) | ✅ Active |

**Active Workorder Locations:**
- Scrapper: `C:\Users\willh\Desktop\scrapper\coderef\working\`
- Gridiron: `C:\Users\willh\Desktop\latest-sim\gridiron-franchise\coderef\working\`
- CodeRef Dashboard: `C:\Users\willh\Desktop\coderef-dashboard\coderef\working\`

**Active Stubs (Strategic Planning):**

| STUB ID | Feature | Target Project | Status | Purpose |
|---------|---------|----------------|--------|---------|
| STUB-054 | persona-role-context-system | personas-mcp | Planning | Phased persona specialization (Phase 1: Widget Architect validation) |
| STUB-055 | personas-ecosystem-architecture | personas-mcp | Planning | Unified persona architecture across 5 agents with coderef ecosystem awareness |
| STUB-056 | known-issues-utility | coderef-workflow | Planning | Searchable bug fix registry for agent institutional knowledge |
| STUB-057 | wo-tracking-widget | coderef-dashboard | Planning | Orchestrator workorder tracking widget for dashboard UI |

---

## Essential Commands

### Development
```bash
# Activate orchestrator persona
/coderef-assistant

# Capture new idea as stub
/stub feature-name

# Check workorder status
Read workorders.json or check index.html dashboard
```

### Workorder Management
```bash
# Promote stub to workorder (manual process)
1. Assign WO-FEATURE-XXX ID
2. Create context.json in target project
3. Create communication.json in target project
4. Update orchestrator's workorders.json
5. Generate handoff prompt
```

### Slash Commands
```bash
/coderef-assistant     # Activate orchestrator persona
/stub [idea]           # Capture idea as STUB-XXX (future enhancement)
```

---

## Use Cases

### UC-1: User Has New Feature Idea
```
User: "I want to add a dashboard widget for tracking workorders"

Assistant (orchestrator):
Step 1: Create coderef/working/wo-tracking-widget/stub.json
Step 2: Assign STUB-057
Step 3: Update projects.md (Next STUB-ID → STUB-058)
Step 4: Confirm "Stubbed: STUB-057: wo-tracking-widget"
Step 5: Ask: "Target project? (coderef-dashboard)"
Step 6: Record target_project in stub.json

Result: Idea captured, tracked in projects.md, ready for promotion
```

### UC-2: User Promotes Stub to Workorder
```
User: "Let's implement STUB-057 in coderef-dashboard"

Assistant (orchestrator):
Step 1: Assign WO-DASHBOARD-WIDGET-001
Step 2: Create C:\Users\willh\Desktop\coderef-dashboard\coderef\working\wo-tracking-widget\context.json
  {
    "workorder_id": "WO-DASHBOARD-WIDGET-001",
    "stub_id": "STUB-057",
    "feature_name": "wo-tracking-widget",
    "requirements": ["Real-time workorder status", "Visual progress indicators"],
    "constraints": ["Must integrate with existing dashboard layout"]
  }
Step 3: Create communication.json in same folder
  {
    "workorder_id": "WO-DASHBOARD-WIDGET-001",
    "status": "pending_plan",
    "handoff": {
      "orchestrator_to_agent": "See handoff prompt below",
      "status": "pending_plan"
    }
  }
Step 4: Update orchestrator's workorders.json
Step 5: Generate handoff prompt (see Handoff Protocol section)
Step 6: User pastes prompt into coderef-dashboard agent chat

Result: Workorder delegated, agent receives structured context
```

---

## Recent Changes

### v2.0.0 - MCP Ecosystem Integration
- ✅ Integrated with 6 MCP servers (coderef-context, coderef-workflow, coderef-docs, personas-mcp, coderef-personas, scriptboard-mcp)
- ✅ Implemented STUB-XXX and WO-XXX ID tracking system
- ✅ Built communication.json handoff protocol for project agents
- ✅ Created visual dashboard (index.html) for workorder status
- ✅ Added CodeRef Assistant persona activation (/coderef-assistant)
- 🗑️ Deprecated direct code execution in target projects

### v1.0.0 - Initial Orchestrator Release
- ✅ Basic stub capture workflow
- ✅ projects.md tracking system
- ✅ Manual workorder delegation

---

## Next Steps / Roadmap

- ⏳ Automate stub promotion workflow (eliminate manual context.json creation)
- ⏳ Build /stub slash command for instant idea capture
- ⏳ Add real-time dashboard updates via websocket integration
- ⏳ Implement dependency tracking (WO-001 blocks WO-002)
- ⏳ Create automated handoff prompt generation from stub.json

---

## Resources

- **[projects.md](projects.md)** - Master project list and stub inventory
- **[workorders.json](workorders.json)** - Centralized workorder tracking
- **[index.html](index.html)** - Visual dashboard
- **[terminal-profiles.md](terminal-profiles.md)** - Windows Terminal configuration
- **[CLAUDEMD-TEMPLATE.json](C:\Users\willh\.mcp-servers\CLAUDEMD-TEMPLATE.json)** - Template used for this document

---

**Maintained by:** CodeRef Assistant (Orchestrator Persona)