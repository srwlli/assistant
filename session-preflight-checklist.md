# Session Pre-Flight Checklist

**Purpose:** Verify all projects are ready for multi-agent session launch
**When to Use:** BEFORE launching any multi-agent session
**Time Required:** 5-15 minutes per project

---

## Overview

Multi-agent sessions require **fresh coderef scans** and **foundation docs** for optimal performance. This checklist ensures agents have the context they need.

**Key Principle:** Orchestrator runs scans → Agents read results → Fast, accurate execution

---

## Pre-Flight Steps

### 1. Identify Participating Projects

List all projects that will have agents in this session:

```
Example:
☐ coderef-workflow (C:\Users\willh\.mcp-servers\coderef-workflow)
☐ coderef-docs (C:\Users\willh\.mcp-servers\coderef-docs)
☐ papertrail (C:\Users\willh\.mcp-servers\papertrail)
☐ coderef-testing (C:\Users\willh\.mcp-servers\coderef-testing)
```

### 2. Run Coderef Scan on Each Project

**For each project, run:**

```bash
# Use the coderef_scan MCP tool
coderef_scan(
  project_path="C:\\Users\\willh\\.mcp-servers\\{project-name}",
  languages=["ts", "tsx", "js", "jsx", "py"],
  use_ast=true
)
```

**Expected Output:**
- `.coderef/index.json` created in project directory
- Contains: functions, classes, components, imports, exports
- File size: typically 50KB - 500KB depending on project size

**Verification:**
```bash
# Check if index exists and is recent
ls C:\Users\willh\.mcp-servers\{project-name}\.coderef\index.json

# View file timestamp (should be within last 7 days)
```

### 3. Verify Foundation Docs Exist

**For each project, verify:**

```
☐ .coderef/context.md - High-level project overview (REQUIRED)
☐ ARCHITECTURE.md - Architecture patterns and decisions (optional)
☐ CLAUDE.md - AI agent context and workflows (REQUIRED)
☐ .coderef/index.json - Fresh coderef scan (REQUIRED)
```

**Missing Docs?**
- If `.coderef/context.md` missing → Generate with `coderef_context` tool
- If `CLAUDE.md` missing → Create from `CLAUDEMD-TEMPLATE.json`
- If `ARCHITECTURE.md` missing → Optional, but recommended for complex projects

### 4. Check Index Freshness

**Index Age Check:**
```bash
# If index is older than 7 days, re-run coderef_scan
# Recent code changes? Re-scan to capture latest structure
```

**When to Re-Scan:**
- Index older than 7 days
- Major code changes since last scan
- New files/modules added
- Refactoring completed

### 5. Create Session Files

**Session Structure:**
```
C:\Users\willh\.mcp-servers\coderef\sessions\{session-name}\
├── communication.json     ← Agent coordination
├── instructions.json      ← Agent instructions (MUST include session-requirements-template.json)
└── {subdirectories}       ← Additional context (testing/, etc.)
```

**Merge Requirements Template:**
- Include `session-requirements-template.json` in `instructions.json`
- Ensures agents use .coderef/ + coderef-context tools
- No exceptions - ALL sessions must include standard requirements

---

## Pre-Flight Checklist Template

Copy this checklist for each session:

```markdown
## Session: {session-name}
**Date:** {date}
**Participating Projects:** {list}

### Scans Complete
☐ Project 1: coderef_scan complete → .coderef/index.json verified
☐ Project 2: coderef_scan complete → .coderef/index.json verified
☐ Project 3: coderef_scan complete → .coderef/index.json verified
☐ Project 4: coderef_scan complete → .coderef/index.json verified

### Foundation Docs Verified
☐ Project 1: .coderef/context.md ✓ | ARCHITECTURE.md ✓/N/A | CLAUDE.md ✓
☐ Project 2: .coderef/context.md ✓ | ARCHITECTURE.md ✓/N/A | CLAUDE.md ✓
☐ Project 3: .coderef/context.md ✓ | ARCHITECTURE.md ✓/N/A | CLAUDE.md ✓
☐ Project 4: .coderef/context.md ✓ | ARCHITECTURE.md ✓/N/A | CLAUDE.md ✓

### Session Files Created
☐ communication.json created with agent list
☐ instructions.json created with session-requirements-template.json merged
☐ Subdirectories created (if needed)

### Ready to Launch
☐ All scans fresh (< 7 days old)
☐ All foundation docs present
☐ Session files include standard requirements
☐ Agent handoff prompts generated

**Status:** ✅ READY / ⚠️ ISSUES / ❌ NOT READY
```

---

## Common Issues & Solutions

### Issue: .coderef/index.json Missing
**Solution:**
```bash
coderef_scan(project_path="path/to/project", languages=["ts","tsx","js","jsx"])
```

### Issue: Foundation Docs Missing
**Solution:**
- `.coderef/context.md` → Run `coderef_context` tool
- `CLAUDE.md` → Copy from `CLAUDEMD-TEMPLATE.json` and customize
- `ARCHITECTURE.md` → Generate with `generate_foundation_docs` tool

### Issue: Index Stale (> 7 days old)
**Solution:**
- Re-run `coderef_scan` to refresh
- Takes 30-60 seconds per project

### Issue: Session Files Missing Requirements Template
**Solution:**
- Read `session-requirements-template.json`
- Merge into `instructions.json` under `context_requirements` section

---

## Quick Reference: coderef_scan Commands

### TypeScript/JavaScript Projects
```python
coderef_scan(
  project_path="C:\\Users\\willh\\.mcp-servers\\{project}",
  languages=["ts", "tsx", "js", "jsx"],
  use_ast=true
)
```

### Python Projects
```python
coderef_scan(
  project_path="C:\\Users\\willh\\.mcp-servers\\{project}",
  languages=["py"],
  use_ast=true
)

```

### Multi-Language Projects
```python
coderef_scan(
  project_path="C:\\Users\\willh\\.mcp-servers\\{project}",
  languages=["ts", "tsx", "js", "jsx", "py"],
  use_ast=true
)
```

---

## Session Launch Workflow

**Complete Pre-Flight → Launch Agents → Monitor Execution**

```
1. Pre-Flight Checklist (this document) → 5-15 min
   ↓
2. Generate Agent Handoff Prompts → 2-5 min
   ↓
3. Launch Agents (paste prompts into agent chats) → 1 min per agent
   ↓
4. Monitor communication.json for status updates → ongoing
   ↓
5. Verify completion and aggregate results → 10-30 min
```

---

## Notes

- **Frequency:** Run pre-flight before EVERY multi-agent session
- **Ownership:** Orchestrator (assistant) runs pre-flight, not project agents
- **Duration:** 5-15 minutes for 4-project session
- **Benefits:** Faster agent execution (30-60 min saved per agent), consistent quality, better traceability

**Last Updated:** 2026-01-10
**Template Version:** 1.0.0
