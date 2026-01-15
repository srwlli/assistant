# Documentation Cleanup Plan

**Audit Date:** 2026-01-14
**Project Path:** C:\Users\willh\Desktop\assistant

---

## Executive Summary

- **Total Documentation Files Found:** 140
  - Markdown: 90 files
  - HTML: 17 files
  - Text: 33 files
- **Total Issues Detected:** 98
  - Schema Violations: 78
  - Staleness: 12
  - Redundancy: 8
  - Broken Links: 0

**Estimated Cleanup Time:** 2-3 hours

---

## Critical Findings

🔴 **High Impact Issues:**
1. **74/75 markdown files** in coderef/ missing YAML frontmatter (UDS compliance required)
2. **6 foundation docs** missing required frontmatter fields (workorder_id, generated_by, feature_id, doc_type)
3. **1 stub.json** has invalid status value: 'pending' (should be: planning, ready, blocked, promoted, abandoned)
4. **8 redundant summary/report files** in root directory (duplicate audit reports)
5. **12 HTML files** in coderef/user/ may be outdated (no git timestamps)
6. **Root directory cluttered** with 20+ temporary report files from previous audits

---

## Validation Summary

| Category | Checked | Valid | Issues |
|----------|---------|-------|--------|
| Markdown files | 90 | - | 74 missing frontmatter |
| HTML files | 17 | - | 12 potentially outdated |
| Text files | 33 | - | - |
| stub.json files | 52 | 51 | 1 invalid status |
| Foundation docs | 6 | 0 | 6 missing frontmatter |

---

## Priority Actions

### 🔴 High Priority (2 actions)

#### 1. UPDATE: Fix stub.json schema violation
- **File:** `coderef/working/agent-completion-workflow/stub.json`
- **Issue:** Invalid status value: 'pending'
- **Fix:** Change status from 'pending' to 'planning' (valid enum value)
- **Tool:** `mcp__papertrail__validate_stub`
- **Priority:** HIGH

#### 2. ADD_FRONTMATTER: Foundation docs missing required frontmatter
- **Files (6):**
  - `coderef/foundation-docs/README.md`
  - `coderef/foundation-docs/ARCHITECTURE.md`
  - `coderef/foundation-docs/API.md`
  - `coderef/foundation-docs/SCHEMA.md`
  - `coderef/foundation-docs/COMPONENTS.md`
  - `coderef/foundation-docs/CODEREF-EXPLORER-PAGE.md`
- **Reason:** Foundation docs require YAML frontmatter with workorder_id, generated_by, feature_id, doc_type
- **Template:** `foundation-doc-frontmatter-schema.json`
- **Example Frontmatter:**
  ```yaml
  ---
  workorder_id: WO-FOUNDATION-DOCS-001
  generated_by: coderef-docs v2.0.0
  feature_id: foundation-documentation
  doc_type: readme
  title: Assistant - Orchestrator CLI
  version: 2.0.0
  status: APPROVED
  ---
  ```
- **Priority:** HIGH

---

### 🟡 Medium Priority (4 actions)

#### 3. ARCHIVE: Historical audit reports
- **Files to archive (8):**
  - `ARCHIVAL_EXECUTION_SUMMARY.txt`
  - `ARCHIVAL_SUMMARY.md`
  - `ARCHIVE_SCRIPT_README.md`
  - `FINAL_REPORT.md`
  - `MIGRATION_COMPLETE_SUMMARY.md`
  - `STUB_AUDIT_REPORT.md`
  - `STUB_AUDIT_SUMMARY.txt`
  - `STUB_MIGRATION_REPORT.txt`
- **Destination:** `archive/audit-reports-2026-01-14/`
- **Reason:** Historical audit reports from previous cleanup operations, completed
- **Priority:** MEDIUM

#### 4. ARCHIVE: Planning documents from completed work
- **Files to archive (3):**
  - `CRITICAL_STUBS_TO_PROMOTE.md`
  - `AGENT-HANDOFF-TRACKING-SYSTEM.md`
  - `ROOT-ORGANIZATION.md`
- **Destination:** `archive/planning-docs-2026-01-14/`
- **Reason:** Planning documents from completed organizational work
- **Priority:** MEDIUM

#### 5. REVIEW_HTML: Verify HTML documentation relevance
- **Files to review (8):**
  - `coderef/user/coderef-commands.html`
  - `coderef/user/coderef-output-capabilities.html`
  - `coderef/user/coderef-scripts.html`
  - `coderef/user/coderef-setup.html`
  - `coderef/user/coderef-tools.html`
  - `coderef/user/coderef-workflows.html`
  - `coderef/user/index.html`
  - `coderef/user/page-template.html`
- **Reason:** HTML documentation files in coderef/user/ - verify if still relevant or should convert to Markdown
- **Recommendation:** Consider converting to Markdown in coderef/foundation-docs/ or archiving if outdated
- **Priority:** MEDIUM

#### 6. VALIDATE_STRUCTURE: Non-standard coderef directories
- **Issue:** coderef/ has unexpected directories
- **Found (7 non-standard directories):**
  - `coderef/documents/`
  - `coderef/features/`
  - `coderef/notes/`
  - `coderef/resource/`
  - `coderef/resources-sheets/`
  - `coderef/sessions/`
  - `coderef/workorder/`
- **Expected standard structure:**
  - `coderef/foundation-docs/`
  - `coderef/working/`
  - `coderef/archived/`
  - `coderef/standards/`
- **Recommendation:** Review non-standard directories and consolidate into standard structure
- **Priority:** MEDIUM

---

### 🟢 Low Priority (7 actions)

#### 7. MOVE: Portfolio assessment report
- **From:** `STATE-OF-THE-UNION.md`
- **To:** `coderef/reports/STATE-OF-THE-UNION-2026-01-14.md`
- **Reason:** Portfolio assessment report, move to reports directory with date
- **Priority:** LOW

#### 8. MOVE: Working context document
- **From:** `context.md`
- **To:** `coderef/working/context.md`
- **Reason:** Working context document, belongs in coderef structure
- **Priority:** LOW

#### 9. MOVE: Resource sheet systems context
- **From:** `resource-sheet-systems-context.md`
- **To:** `coderef/working/resource-sheet-systems-context.md`
- **Reason:** Working document, belongs in coderef structure
- **Priority:** LOW

#### 10. DELETE: Temporary file
- **File:** `claude.txt`
- **Reason:** Empty or minimal content file, likely temporary
- **Backup:** `archive/deleted-2026-01-14/`
- **Priority:** LOW

#### 11. DELETE: Personal note file
- **File:** `Jovi.txt`
- **Reason:** Personal note file, not project documentation
- **Backup:** `archive/deleted-2026-01-14/`
- **Priority:** LOW

#### 12. CONSOLIDATE: Merge README files in web/
- **Files to merge (2):**
  - `web/README.md`
  - `web/README-ELECTRON.md`
- **Merge into:** `web/README.md`
- **Reason:** Two README files in web/ directory, merge Electron instructions into main README
- **Priority:** LOW

#### 13. ADD_FRONTMATTER_BATCH: Working documents (Batch Operation)
- **Directory:** `coderef/working/`
- **Pattern:** `*.md`
- **Count:** 65 files
- **Reason:** Working documents missing YAML frontmatter for UDS compliance
- **Template:** `workorder-doc-frontmatter-schema.json`
- **Note:** Low priority - only required for formal workorder docs
- **Priority:** LOW

#### 14. ADD_FRONTMATTER_BATCH: Archived documents (Batch Operation)
- **Directory:** `coderef/archived/`
- **Pattern:** `*.md`
- **Count:** 9 files
- **Reason:** Archived documents missing YAML frontmatter
- **Template:** `workorder-doc-frontmatter-schema.json`
- **Note:** Low priority - archived content
- **Priority:** LOW

---

## Detailed Actions Checklist

### High Priority
- [ ] Fix stub.json schema violation (1 file)
- [ ] Add frontmatter to foundation docs (6 files)

### Medium Priority
- [ ] Archive audit reports (8 files)
- [ ] Archive planning docs (3 files)
- [ ] Review HTML documentation (8 files)
- [ ] Validate/consolidate coderef structure (7 directories)

### Low Priority
- [ ] Move reports and working docs (3 files)
- [ ] Delete temporary files (2 files)
- [ ] Consolidate web/ READMEs (2 files)
- [ ] Batch add frontmatter to working docs (65 files)
- [ ] Batch add frontmatter to archived docs (9 files)

**Total Actions:** 14

---

## Execution Strategy

### Phase 1: High Priority (Start Here)
1. Fix `agent-completion-workflow/stub.json` status field
2. Add frontmatter to 6 foundation docs

### Phase 2: Medium Priority (Clean Up Structure)
1. Archive old audit reports (cleans root directory)
2. Archive completed planning docs
3. Review HTML files for conversion/archival
4. Consolidate non-standard coderef directories

### Phase 3: Low Priority (Polish & Automation)
1. Move working docs to coderef structure
2. Delete temporary files
3. Consolidate web/ READMEs
4. Batch add frontmatter (can be automated)

---

## Execution Notes

**Backup Strategy:**
- Create `archive/deleted-2026-01-14/` before any deletions
- Create `archive/audit-reports-2026-01-14/` for old reports
- Create `archive/planning-docs-2026-01-14/` for completed planning

**Validation Tools Required:**
- `mcp__papertrail__validate_stub`
- `mcp__papertrail__validate_document`
- `mcp__papertrail__check_all_docs`

**Post-Cleanup Verification:**
- Re-run `check_all_docs` to verify schema violations fixed
- Run `validate_stub` on updated stub.json
- Check git status for uncommitted changes
- Update CLAUDE.md if coderef structure changes

---

## Recommendations

1. ✅ **Start with high priority:** Fix stub.json validation error and add frontmatter to foundation docs
2. 📦 **Archive old audit reports** to clean up root directory
3. 🏗️ **Review coderef/ directory structure** and consolidate non-standard folders
4. 🔄 **Consider converting HTML docs to Markdown** for consistency
5. ⚙️ **Low priority batch operations** can be automated with scripts

---

## Approval Required

**Review this plan and confirm:**
1. ✅ **Approve all actions** - Execute complete cleanup
2. ⚠️ **Approve with modifications** - Specify which actions to skip/modify
3. ❌ **Do not proceed** - Review needed

**Next Steps:** Awaiting user approval before executing cleanup operations.

---

**Generated by:** Documentation Cleanup & Validation workflow
**Validation Tools:** Papertrail MCP (stub, document, batch validation)
**Output Format:** Markdown (human-readable)
