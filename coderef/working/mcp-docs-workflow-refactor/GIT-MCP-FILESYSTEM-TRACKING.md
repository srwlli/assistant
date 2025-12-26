# Git MCP & Filesystem Tracking

## Git MCP: Local Tracking (Workorder Phases & Metrics)

Git MCP manages tracking that lives in **git history and local filesystem**:

### What Git MCP Tracks

| Item | Tracked By | Storage | Purpose |
|------|-----------|---------|---------|
| Workorder phases | Git commits + branch metadata | Git history | Track WO progression (pending → plan_submitted → approved → implementing → complete → verified) |
| Metrics (LOC, commits, time) | Git log queries | Git history | Calculate deliverables (lines changed, commit count, elapsed time) |
| Agent branches | Git branch names | Git refs | One branch per agent/workorder (WO-FEATURE-XXX) |
| Merge decisions | Git commit messages | Git history | Orchestrator manages merges (not agents) |
| Task completion timestamps | Git commit timestamps | Git history | Track when tasks completed |
| Contributors | Git author metadata | Git history | Identify who worked on what |
| Code changes | Git diff | Git history | Validate forbidden files unchanged |
| Feature tags | Git tags | Git refs | Mark feature release boundaries |

---

## Filesystem Tracking (Project Context Files)

Filesystems track **structured metadata and context**:

### What Filesystem Tracks

| Location | File | Purpose | Owner |
|----------|------|---------|-------|
| `coderef/working/{feature}/` | context.json | Feature requirements, constraints | Orchestrator writes, Agent reads |
| `coderef/working/{feature}/` | communication.json | Workorder status, workflow log | Agent updates, Orchestrator reads |
| `coderef/working/{feature}/` | plan.json | Implementation plan (10 sections) | Agent writes, Orchestrator reviews |
| `coderef/working/{feature}/` | DELIVERABLES.md | Metrics template + actual metrics | Agent updates after /update-deliverables |
| `coderef/archived/{feature}/` | * (all above) | Archived after completion | Moved by /archive-feature |
| `coderef/standards/` | UI-STANDARDS.md | Discovered UI patterns | coderef-context writes, coderef-docs reads |
| `coderef/standards/` | BEHAVIOR-STANDARDS.md | Discovered behavior patterns | coderef-context writes, coderef-docs reads |
| `coderef/standards/` | UX-PATTERNS.md | Discovered UX patterns | coderef-context writes, coderef-docs reads |
| `coderef/foundation-docs/` | README.md, ARCHITECTURE.md, etc | Generated reference docs | coderef-docs writes |
| `coderef/` | workorders.json | Centralized WO tracking (orchestrator) | Orchestrator writes/reads |
| `coderef/` | workorder-log.txt | Historical log of all WOs | Git MCP appends |

---

## Git MCP Commands (Proposed)

### Phase Tracking

| Command | Purpose | Output |
|---------|---------|--------|
| git-log-workorder | Append WO-ID entry to git log | workorder-log.txt |
| git-query-workorder-commits | Find commits for WO-ID | List of commits |
| git-create-wo-branch | Create branch WO-FEATURE-XXX | New branch |
| git-merge-wo-branch | Orchestrator merges WO branch | Merged commits |
| git-tag-feature | Tag release boundary | Git tag |

### Metrics Extraction

| Command | Purpose | Output |
|---------|---------|--------|
| git-count-lines-changed | LOC (added/deleted) for feature | +XXX/-YYY lines |
| git-count-commits | Commit count for feature | N commits |
| git-extract-contributors | Find all authors on feature | [Author1, Author2, ...] |
| git-calculate-time-elapsed | First commit → last commit | HH:MM:SS |
| git-get-commit-timestamps | Extract all commit times | [timestamp1, timestamp2, ...] |

### Validation

| Command | Purpose | Output |
|---------|---------|--------|
| git-diff-forbidden-files | Check if read-only files changed | Pass/fail |
| git-verify-branch-clean | Ensure no uncommitted changes | Pass/fail |
| git-check-merge-conflicts | Pre-merge conflict detection | Conflicts list |

---

## Data Flow: Git + Filesystem

```
Workorder Created
  ↓
Filesystem: Write context.json, communication.json
  ↓
Agent Creates Branch: WO-FEATURE-XXX
  ↓
Git: Track branch creation
  ↓
Agent Works & Commits
  ↓
Git: Track commits, authors, LOC
  ↓
Agent Completes & Updates DELIVERABLES.md
  ↓
Git MCP: Extract metrics from git history
  ↓
Agent Archives Feature
  ↓
Filesystem: Move to coderef/archived/
Git: Tag release boundary
  ↓
Orchestrator Verifies
  ↓
Git MCP: Validate commit history
  ↓
Workorder Closed
  ↓
Git MCP: Log to workorder-log.txt
```

---

## Ownership Matrix

| System | Owns Git | Owns Filesystem |
|--------|----------|-----------------|
| **git-mcp** (proposed) | ✅ Branch management, commit tracking, merge decisions, metrics extraction, validation | ❌ No filesystem writes |
| **coderef-workflow** | ❌ No direct git access | ✅ Creates/updates communication.json, context.json, reads plan.json |
| **coderef-context** | ❌ No git access | ✅ Writes coderef/standards/ markdown files |
| **coderef-docs** | ❌ No git access | ✅ Writes coderef/foundation-docs/ markdown files |
| **coderef-personas** | ❌ No git access | ❌ No filesystem writes (read-only context) |

---

## Git MCP Integration Points

### With coderef-workflow
- Get feature branch: `git-query-workorder-commits WO-FEATURE-XXX`
- Get metrics for DELIVERABLES: `git-count-lines-changed`, `git-count-commits`, etc
- Validate completion: `git-diff-forbidden-files`

### With Orchestrator
- Create WO branch: `git-create-wo-branch WO-FEATURE-XXX`
- Merge WO branch: `git-merge-wo-branch WO-FEATURE-XXX`
- Tag release: `git-tag-feature {version}`
- Log WO: `git-log-workorder WO-FEATURE-XXX`

### With Agent
- Agent commits on their assigned branch (automatic via git workflow)
- Agent calls `/update-deliverables` which uses git-mcp tools
