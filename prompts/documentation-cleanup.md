# MISSION: Documentation Cleanup & Validation

You are conducting a comprehensive cleanup of project documentation to eliminate redundancy, validate against schemas, and ensure coderef structure compliance.

## Your Task

Scan the project for all documentation files (.md, .html, .txt) and coderef structure files, validate them against Papertrail schemas, detect issues (redundancy, staleness, schema violations), and generate an actionable cleanup plan.

---

## Pre-loaded Validation Tools

You have access to Papertrail MCP tools for schema validation:

### Papertrail MCP Tools
```javascript
// Validate stub.json files
mcp__papertrail__validate_stub({
  file_path: "absolute/path/to/stub.json",
  auto_fill: true,  // Auto-fill missing required fields
  save: false       // Set true to save auto-filled version
})

// Validate resource sheets (-RESOURCE-SHEET.md files)
mcp__papertrail__validate_resource_sheet({
  file_path: "absolute/path/to/resource-sheet.md"
})

// Validate any UDS document (auto-detects type)
mcp__papertrail__validate_document({
  file_path: "absolute/path/to/document.md"
})

// Batch validate all docs in directory
mcp__papertrail__check_all_docs({
  directory: "absolute/path/to/directory",
  pattern: "**/*.md"  // Optional glob pattern
})

// Batch validate all resource sheets
mcp__papertrail__check_all_resource_sheets({
  directory: "absolute/path/to/directory"
})
```

---

## Analysis Process

### Phase 1: Discovery & Inventory

#### A. Find All Documentation Files

Run these commands to locate all documentation:

```bash
# Find all Markdown files (exclude node_modules, .venv)
find . -name "*.md" -not -path "*/node_modules/*" -not -path "*/.venv/*" -not -path "*/dist/*" -not -path "*/build/*"

# Find all HTML files
find . -name "*.html" -not -path "*/node_modules/*" -not -path "*/.venv/*" -not -path "*/dist/*"

# Find all text documentation
find . -name "*.txt" -o -name "NOTES*" -o -name "TODO*" -not -path "*/node_modules/*"
```

**Output:** List all found files with:
- Absolute path
- File size (bytes)
- Last modified date
- File type (markdown/html/text)

#### B. Map CodeRef Structure

Check if project follows standard coderef structure:

```
Official CodeRef Structure (from coderef-core/setup-coderef-dir):

.coderef/ (Hidden, Technical)
├── reports/
│   └── complexity/          # Complexity analysis reports
├── diagrams/                # Dependency diagrams (Mermaid, Graphviz)
└── exports/                 # Exported data (JSON-LD, etc.)

coderef/ (Visible, Workflow)
├── workorder/               # Active workorders (shared across all coderef projects)
│   └── {feature-name}/
│       ├── stub.json        # Required
│       ├── plan.json        # Optional (if promoted)
│       ├── context.json     # Optional (if promoted)
│       ├── communication.json  # Optional (if multi-agent)
│       └── DELIVERABLES.md  # Optional (if complete)
├── archived/                # Completed/cancelled features
├── standards/               # UI/UX/behavior standards
├── foundation-docs/         # Generated docs (README, ARCHITECTURE, API, SCHEMA, COMPONENTS)
├── documents/               # General documentation
├── resource/                # Resource sheets
├── user/                    # User-facing documentation
├── notes/                   # Working notes
├── sessions/                # Multi-agent session files
└── reports/                 # Project assessment and analysis reports

Note: The `working/` directory is project-specific (e.g., Assistant orchestrator)
and should not be confused with the shared `workorder/` directory.
```

**Validation Checks:**

1. ✅ `.coderef/` directory exists (hidden, technical)
2. ✅ `coderef/` directory exists (visible, workflow)
3. ✅ `coderef/workorder/` exists
4. ✅ `coderef/archived/` exists
5. ✅ `coderef/standards/` exists
6. ✅ `coderef/foundation-docs/` exists
7. ✅ `coderef/documents/` exists
8. ✅ `coderef/resource/` exists
9. ✅ `coderef/user/` exists
10. ✅ `coderef/notes/` exists
11. ✅ `coderef/sessions/` exists
12. ✅ `coderef/reports/` exists
13. ⚠️ Non-standard directories (e.g., `features/`, `resources-sheets/`, `working/` if not project-specific)
14. ⚠️ Workorder folders in `workorder/` missing stub.json
15. ⚠️ Completed workorders (status: complete in stub.json) still in `workorder/` (should be archived)

---

### Phase 2: Schema Validation

#### A. Validate stub.json Files

For each `coderef/workorder/{feature}/stub.json`:

Note: If project has `coderef/working/` (project-specific like Assistant), validate those stubs too.

```javascript
mcp__papertrail__validate_stub({
  file_path: "C:/path/to/stub.json",
  auto_fill: true,
  save: false  // Preview mode first
})
```

**Check for:**
- Required fields: stub_id, feature_name, description, category, priority, status, created
- Valid stub_id pattern: `STUB-\d{3}` (e.g., STUB-001)
- Valid feature_name: kebab-case, matches folder name
- Valid status: planning, ready, blocked, promoted, abandoned
- Valid category: feature, enhancement, bugfix, infrastructure, documentation, refactor, research
- Valid priority: low, medium, high, critical

#### B. Validate plan.json Files

For each `coderef/workorder/{feature}/plan.json`:

```javascript
mcp__papertrail__validate_document({
  file_path: "C:/path/to/plan.json"
})
```

**Check for:**
- 10-section UPS (Universal Planning Structure) format
- Required sections: 0_preparation through 9_implementation_checklist
- Valid workorder_id pattern: `WO-[A-Z0-9-]+-\d{3}` (e.g., WO-AUTH-001)
- META_DOCUMENTATION section complete
- Valid task IDs and phase structure

#### C. Validate Foundation Documents

For each file in `coderef/foundation-docs/`:

```javascript
mcp__papertrail__validate_document({
  file_path: "C:/path/to/README.md"
})
```

**Check YAML frontmatter for:**
- workorder_id (required)
- generated_by (required, must be "coderef-docs")
- feature_id (required)
- doc_type (required: readme, architecture, api, schema, components)
- title, version, status (optional)
- required_sections matching doc_type

#### D. Validate Resource Sheets

For files ending with `-RESOURCE-SHEET.md`:

```javascript
mcp__papertrail__validate_resource_sheet({
  file_path: "C:/path/to/Component-RESOURCE-SHEET.md"
})
```

**Check for:**
- Filename ends with `-RESOURCE-SHEET.md`
- snake_case frontmatter (not camelCase)
- Required fields: subject, parent_project, category
- Recommended sections present
- Valid naming conventions

#### E. Batch Validation

Run batch checks on entire directories:

```javascript
// Validate all docs in coderef/
mcp__papertrail__check_all_docs({
  directory: "C:/path/to/project/coderef",
  pattern: "**/*.md"
})

// Validate all resource sheets
mcp__papertrail__check_all_resource_sheets({
  directory: "C:/path/to/project/coderef"
})
```

---

### Phase 3: Detect Issues

#### A. Redundancy Detection

**1. Duplicate READMEs:**

Check for multiple README files:
- `README.md`
- `readme.md` (case variant)
- `README.txt`
- `docs/README.md`
- `coderef/foundation-docs/README.md`

**Rule:** Keep `coderef/foundation-docs/README.md` (generated) or root `README.md` (if no coderef). Archive others.

**2. Overlapping Content:**

Compare similar files for text similarity:
- `ARCHITECTURE.md` vs `architecture.html`
- `GETTING-STARTED.md` vs `docs/setup.html`
- `API.md` vs `api-docs.html`

**Detection Method:**
- Read both files
- Calculate text similarity (ignore whitespace, case)
- Flag if >70% similar content

**Rule:** Prefer Markdown in coderef/foundation-docs/, archive HTML versions.

**3. Multiple Index Files:**

Check for:
- `index.html`
- `INDEX.html` (case variant)
- `docs/index.html`

**Rule:** Keep primary index (usually root), archive others with date suffix.

#### B. Freshness Issues

**1. Outdated HTML Documentation:**

Scan HTML files for indicators of staleness:
- `<meta name="generator" content="FrontPage">` (ancient tool, pre-2006)
- `<meta name="generator" content="Dreamweaver">` (old tool)
- jQuery version < 2.0 when project uses React/Vue
- Copyright dates >3 years old (e.g., "© 2020" in 2026)
- References to removed dependencies

**2. Stale Markdown:**

Check for:
- Last modified >6 months ago
- Contains "Coming Soon", "WIP", "TODO", "In Progress" sections >90 days old
- References dependencies no longer in package.json or requirements.txt
- Links to removed files

**3. Broken Links:**

Validate all links:
- **Internal links:** `[text](./path/to/file.md)` - Check if target exists
- **Anchor links:** `[text](#section-heading)` - Check if heading exists in target
- **External links:** `[text](https://example.com)` - Optional: HTTP HEAD request for 404s

#### C. CodeRef Structure Issues

**1. Invalid JSON Files:**

Check for:
- Malformed JSON (syntax errors)
- Missing required fields (per schemas)
- Invalid field values (wrong types, out-of-range)

**2. Orphaned Files:**

Detect incomplete workorders:
- `coderef/working/feature-x/` has stub.json but no plan.json (if status: promoted)
- `coderef/working/feature-x/` has plan.json but no DELIVERABLES.md (if plan status: complete)

**3. Misplaced Files:**

Check for:
- Workorders with status "complete" or "abandoned" still in `coderef/working/` (should be in archived/)
- Files in coderef root that don't belong (only index.json, graph.json, PROJECT-STATE-ASSESSMENT.md allowed)

**4. Naming Violations:**

Check for:
- Folder names not using kebab-case (e.g., `MyFeature` should be `my-feature`)
- Files with spaces in names (e.g., `my file.md` should be `my-file.md`)
- Resource sheets not ending with `-RESOURCE-SHEET.md`

---

### Phase 4: Generate Cleanup Plan

Output: **`docs-cleanup-plan.md`** (Markdown format for easy human review)

```markdown
# Documentation Cleanup Plan

**Audit Date:** 2026-01-14
**Project Path:** C:/path/to/project

---

## Executive Summary

- **Total Documentation Files Found:** 47
- **Total Issues Detected:** 23
  - Redundancy: 8
  - Staleness: 7
  - Broken Links: 3
  - Schema Violations: 5

**Estimated Cleanup Time:** 2-3 hours

---

## Validation Summary

| Category | Checked | Valid | Invalid |
|----------|---------|-------|---------|
| stub.json files | 12 | 9 | 3 |
| plan.json files | 8 | 7 | 1 |
| Foundation docs | 5 | 5 | 0 |
| Resource sheets | 3 | 2 | 1 |

---

## Priority Actions

### 🔴 High Priority (5 actions)

#### 1. UPDATE: Fix stub.json schema violations
- **File:** `coderef/working/auth-system/stub.json`
- **Issue:** Missing required field: category
- **Fix:** Run `validate_stub` with auto_fill=true, save=true
- **Tool:** `mcp__papertrail__validate_stub`

#### 2. VALIDATE_AND_FIX: Fix plan.json issues
- **File:** `coderef/working/auth-system/plan.json`
- **Issues:**
  - Missing section: 2_risk_assessment
  - Invalid workorder_id: 'WO-001' (should be 'WO-AUTH-SYSTEM-001')
- **Validation Score:** 65/100
- **Tool:** `mcp__papertrail__validate_document`

#### 3. RENAME: Fix folder naming violation
- **From:** `coderef/working/My Feature/stub.json`
- **To:** `coderef/working/my-feature/stub.json`
- **Reason:** Folder name must be kebab-case
- **Note:** Update feature_name field in stub.json

---

### 🟡 Medium Priority (3 actions)

#### 4. MOVE: Archive completed workorder
- **From:** `coderef/working/completed-feature/`
- **To:** `coderef/archived/completed-feature/`
- **Reason:** Workorder status: complete (from stub.json)

#### 5. FIX_LINKS: Repair broken links in README
- **File:** `README.md`
- **Broken Links:**
  - Line 45: `./docs/missing.md` → Target file does not exist
    - **Suggestion:** Remove or update to `./coderef/foundation-docs/API.md`
  - Line 78: `https://dead-site.com` → External link returns 404
    - **Suggestion:** Remove or replace with archive.org link

#### 6. MERGE: Consolidate scattered API docs
- **Files to merge:**
  - `docs/api.md`
  - `API-GUIDE.md`
- **Merge into:** `coderef/foundation-docs/API.md`
- **Reason:** Consolidate scattered API docs into foundation docs
- **Backup:** `coderef/archived/_merged_docs_2026-01-14/`

---

### 🟢 Low Priority (2 actions)

#### 7. ARCHIVE: Historical reference document
- **File:** `docs/v1-migration.html`
- **To:** `docs/archive/2023-v1-migration.html`
- **Reason:** Historical reference, v1 deprecated in 2023
- **Add Archive Note:** Yes

#### 8. DELETE: Duplicate README
- **File:** `old-readme.txt`
- **Reason:** Duplicate of README.md, last modified 2 years ago
- **Backup:** None (duplicate content)

---

## Detailed Actions Checklist

- [ ] **HIGH**: Fix stub.json schema violations (3 files)
- [ ] **HIGH**: Fix plan.json validation errors (1 file)
- [ ] **HIGH**: Rename folders to kebab-case (1 folder)
- [ ] **MED**: Move completed workorders to archived/ (3 folders)
- [ ] **MED**: Fix broken links in documentation (2 files)
- [ ] **MED**: Merge duplicate API documentation (2 files)
- [ ] **LOW**: Archive historical documentation (4 files)
- [ ] **LOW**: Delete duplicate files (2 files)

---

## Execution Notes

**Backup Strategy:**
- Create `coderef/archived/_backups_2026-01-14/` before any deletions
- Merged files backed up to `coderef/archived/_merged_docs_2026-01-14/`

**Validation Tools Required:**
- `mcp__papertrail__validate_stub`
- `mcp__papertrail__validate_document`
- `mcp__papertrail__check_all_docs`

**Post-Cleanup Verification:**
- Re-run `check_all_docs` to verify all schema violations fixed
- Check git status for uncommitted changes
- Update CLAUDE.md if structure changes

---

## Approval Required

**Review this plan and confirm:**
1. ✅ Approve all actions
2. ⚠️ Approve with modifications (specify which)
3. ❌ Do not proceed

**Next Steps:** Awaiting user approval before executing cleanup.
```

---

### Phase 5: Execute Cleanup (With Approval)

**IMPORTANT:** Do NOT execute changes automatically. Show the cleanup plan to the user first.

**Workflow:**
1. Generate `docs-cleanup-plan.md` (Markdown format)
2. Display summary to user:
   ```
   Found 47 documentation files
   Detected 23 issues:
   - 8 redundancies
   - 7 stale documents
   - 3 broken links
   - 5 schema violations

   Proposed actions:
   - DELETE: 2 files
   - MERGE: 3 file groups
   - ARCHIVE: 4 files
   - UPDATE: 5 files
   - MOVE: 3 folders
   - FIX_LINKS: 2 files
   - RENAME: 1 folder
   - VALIDATE_AND_FIX: 3 files
   ```
3. Ask: "Review `docs-cleanup-plan.md`. Approve execution? (yes/no)"
4. Wait for user approval
5. Execute approved actions with progress updates
6. Create backup before destructive operations
7. Generate completion report

---

## Analysis Guidelines

1. **Non-destructive first:** Always propose changes before executing
2. **Backup before delete:** Create `docs/archive/` or `coderef/archived/_backups_YYYY-MM-DD/` before deleting
3. **Preserve history:** When merging, add note showing source files and merge date
4. **Use validation tools:** Always run Papertrail MCP validation before flagging schema issues
5. **Evidence-based:** Every issue must reference specific file location, line number, or validation output
6. **Prioritize safety:** When uncertain, ARCHIVE instead of DELETE
7. **Update references:** When moving/renaming files, check for broken links in other docs
8. **Log all changes:** Record every action in cleanup execution log

---

## Project Directory

**Project to analyze:** The current working directory (where this prompt is being executed)

The agent should automatically detect the project path and analyze it without requiring explicit path specification.

---

## Output Files

1. **`docs-cleanup-plan.md`** - Detailed cleanup plan in Markdown format (generated in Phase 4)
2. **`docs-cleanup-execution-log.md`** - Log of executed actions (generated in Phase 5)
3. **Updated files** - Files fixed via validation tools (with backups)
4. **Archived files** - Moved to `coderef/archived/_backups_YYYY-MM-DD/`

---

## Critical Reminders

**BEFORE YOU BEGIN:**

1. ✅ **Run batch validation first** - Use `check_all_docs` and `check_all_resource_sheets` for overview
2. ✅ **Use Papertrail MCP tools** - Don't manually validate schemas, use provided tools
3. ✅ **Check coderef structure** - Verify standard folder structure before flagging issues
4. ✅ **Calculate text similarity** - For redundancy detection, actually read and compare files
5. ✅ **Generate plan before acting** - NEVER delete/move files without user approval
6. ✅ **Preserve history** - Archive, don't delete (unless explicitly approved)
7. ✅ **Update cross-references** - When moving/renaming, update links in other files

---

**Begin analysis and generate docs-cleanup-plan.md in Markdown format. Wait for user approval before executing any changes.**
