# Orchestrator Root - File Organization Guide

**Date:** December 27, 2025
**Status:** Cleaned and organized

---

## Directory Structure

```
assistant/
├── web/                          # Project Manager Site (NEW)
│   ├── src/
│   │   ├── css/main.css         # Industrial design system
│   │   ├── components/          # Reusable components
│   │   ├── js/                  # Utilities and logic
│   │   └── pages/               # HTML pages
│   ├── COMPONENT-STRUCTURE.md   # Design documentation
│   └── index.html               # Dashboard entry point
│
├── coderef/                      # CodeRef Ecosystem
│   ├── workorder/               # Active workorders (by feature)
│   │   └── coderef-explorer-endpoints/
│   ├── working/                 # Stubs (ideas not yet delegated)
│   │   └── papertrail-mcp-integration/
│   └── archived/                # Completed features
│
├── docs/                         # DOCUMENTATION (Organized)
│   ├── handoffs/                # Agent handoff briefs
│   │   ├── HANDOFF-DASHBOARD-TRACKING-API.md
│   │   ├── HANDOFF-WO-*.md      # Individual workorder handoffs
│   │   └── AGENT-HANDOFF-TRACKING-SYSTEM.md
│   └── roadmaps/                # Planning & roadmaps
│       ├── ORCHESTRATOR-ROADMAP.md
│       ├── PHASE-3-ROADMAP-SYNTHESIS.md
│       └── SESSION-SUMMARY-2025-12-26.md
│
├── tools/                        # UTILITIES
│   └── terminal-profile-manager.html  # Terminal config UI
│
├── archive/                      # HISTORICAL
│   ├── Screenshot*.png           # UI mockups from earlier sessions
│   └── documents.html            # Earlier documentation site
│
├── CLAUDE.md                     # MASTER: Assistant configuration & behavior
├── projects.md                   # MASTER: Active projects registry
├── projects.config.json          # MASTER: Dashboard API projects config
├── README.md                     # Quick start
├── TRACKING.md                   # Agent synthesis findings & priorities
├── CODEREF-EXPLORER-ENDPOINTS.md # Technical specification (API endpoints)
├── workorders.json               # DEPRECATED: Use communication.json instead
└── session-mcp-capabilities.json # REFERENCE: Complete MCP analysis from agents
```

---

## Root-Level Files Explained

### 🔵 MASTER CONFIGURATION FILES
These are the **source of truth** for the orchestrator:

- **CLAUDE.md**
  - Role: Orchestrator behavior definition
  - Contains: Workflow protocols, delegation patterns, file structure rules
  - Update: When orchestration process changes
  - Reference: Core operating instructions

- **projects.md**
  - Role: Master registry of all active projects
  - Contains: Project paths, git links, deployment URLs, stub counter
  - Update: When adding new projects or stubs
  - Reference: Single source of truth for project list

- **projects.config.json**
  - Role: API registry for dashboard tracking
  - Contains: Project paths, workorder directories, enabled status
  - Update: When adding projects to dashboard tracking
  - Reference: Used by tracking API to discover workorders

### 📊 TRACKING & REPORTING

- **TRACKING.md**
  - Agent synthesis findings from Phase 2 analysis
  - Critical blockers, high-value gaps, roadmap priorities
  - **Reference:** For understanding system status and next priorities

- **session-mcp-capabilities.json**
  - Complete MCP server analysis (coderef-context, coderef-workflow, coderef-docs, coderef-personas)
  - 49 tools documented with limitations and opportunities
  - Phase 3 roadmap synthesis
  - **Reference:** For understanding MCP ecosystem capabilities

### 📋 DOCUMENTATION

- **CODEREF-EXPLORER-ENDPOINTS.md**
  - Complete technical specification for coderef folder explorer
  - 7 API endpoints with request/response schemas
  - Multi-project registry system
  - **For:** Dashboard agent implementing the tracking API

- **README.md**
  - Quick start guide
  - **For:** Developers new to the project

### 🗂️ ORGANIZED SUBDIRECTORIES

#### `/docs/handoffs/`
All agent handoff briefs organized by workorder:
- `HANDOFF-DASHBOARD-TRACKING-API.md` - Brief for dashboard agent
- `HANDOFF-WO-MCP-*.md` - Individual MCP server handoffs
- `HANDOFF-WO-*.md` - Feature-specific handoffs
- `AGENT-HANDOFF-TRACKING-SYSTEM.md` - Complete tracking system guide

**Purpose:** Each file can be copied to project agent for context

#### `/docs/roadmaps/`
Strategic planning documents:
- `ORCHESTRATOR-ROADMAP.md` - System architecture overview
- `PHASE-3-ROADMAP-SYNTHESIS.md` - 12-week implementation roadmap
- `SESSION-SUMMARY-2025-12-26.md` - Previous session work summary

**Purpose:** Strategic context and planning reference

#### `/tools/`
Utility applications:
- `terminal-profile-manager.html` - UI for managing Windows Terminal profiles

**Purpose:** Standalone tools for orchestrator use

#### `/archive/`
Historical files (not needed daily):
- Screenshots from earlier UI design sessions
- Previous documentation sites
- Old indexes and references

**Purpose:** Reference only, not active

#### `/web/`
**New Project Manager Site**
- Industrial design system (CSS)
- Component structure documentation
- Working dashboard example
- Ready for incremental development

**Purpose:** Frontend for project management dashboard (will migrate to coderef-dashboard)

#### `/coderef/`
**CodeRef Ecosystem**
- `/workorder/` - Active feature workorders
- `/working/` - Stubs (ideas not yet delegated)
- `/archived/` - Completed features

**Purpose:** Feature tracking and workorder management

---

## Cleanup Summary

**What was cleaned up:**
- ✅ Organized 32 root files into 6 directories
- ✅ Grouped handoffs (11 files) → `/docs/handoffs/`
- ✅ Grouped roadmaps (3 files) → `/docs/roadmaps/`
- ✅ Moved tools → `/tools/`
- ✅ Moved historical assets → `/archive/`
- ✅ Left 7 master files in root (active daily use)

**What stayed in root:**
- CLAUDE.md (behavior definition)
- projects.md (project registry)
- projects.config.json (API config)
- README.md (quick start)
- TRACKING.md (status & priorities)
- CODEREF-EXPLORER-ENDPOINTS.md (technical spec)
- session-mcp-capabilities.json (reference data)

---

## Root File Maintenance

### When to use each file:

**Daily:**
- `CLAUDE.md` - Refer to orchestration protocols
- `projects.md` - Check active projects, next STUB-ID

**Weekly:**
- `TRACKING.md` - Review system status
- `projects.config.json` - Update if adding projects to tracking API

**For Agent Handoffs:**
- Copy appropriate file from `/docs/handoffs/`
- Paste into project agent chat

**For Planning:**
- Reference `/docs/roadmaps/` for strategic context
- PHASE-3-ROADMAP-SYNTHESIS.md for 12-week plan

**Deprecated Files:**
- `workorders.json` - **No longer used.** Use communication.json from projects instead
- Files in `/archive/` - Reference only

---

## Best Practices

1. **Keep root minimal** - Only files accessed daily
2. **Use subdirectories** for organization - `/docs/`, `/tools/`, `/archive/`
3. **Update CLAUDE.md** when orchestration process changes
4. **Update projects.md** when adding projects or stubs
5. **Reference TRACKING.md** for priorities and blockers
6. **Archive completed work** - Move to `/archive/` when no longer active

---

## Quick Reference

**What's the current status?**
→ Read: TRACKING.md

**What projects are we working on?**
→ Read: projects.md

**How does the orchestrator work?**
→ Read: CLAUDE.md

**What should the dashboard agent build?**
→ Read: docs/handoffs/HANDOFF-DASHBOARD-TRACKING-API.md

**What's the 12-week roadmap?**
→ Read: docs/roadmaps/PHASE-3-ROADMAP-SYNTHESIS.md

**Are there any blockers or risks?**
→ Read: TRACKING.md (Critical Blockers section)

