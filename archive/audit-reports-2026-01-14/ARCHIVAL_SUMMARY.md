# Stub Archival Summary

**Date:** 2026-01-13  
**Total Stubs Archived:** 36  
**Remaining Active Stubs:** 62  
**Overall Reduction:** 37% of stub inventory archived  

---

## Archival Results

| Category | Count | Stubs |
|----------|-------|-------|
| **TEST/EXAMPLE** | 7 | Validation workflow testing stubs |
| **COMPLETED** | 1 | Finished work (coderef-timestamp-utility) |
| **OBSOLETE_NAME** | 1 | Clearly deprecated (remove-utility-personas) |
| **DUPLICATE** | 5 | Redundant implementations in same functional area |
| **INFRA_UTILITY_LOW** | 7 | Low-priority infrastructure/utility items |
| **LOW_PRIORITY_OLD** | 15 | Medium-priority items created before 2025-12-20 |

**Total:** 36 stubs archived

---

## Archive Location

- **Source:** `C:\Users\willh\Desktop\assistant\coderef\working\`
- **Destination:** `C:\Users\willh\Desktop\assistant\coderef\archived\`
- **Report:** `C:\Users\willh\Desktop\assistant\coderef\ARCHIVAL_REPORT.txt`

---

## Archival Criteria

### 1. TEST/EXAMPLE (7 stubs)
Validation stubs for workflow testing. Include names like "test", "example", "testing".
- scriptboard-endpoints-test
- stub-location-test
- test-and-fix-emojis
- test-stub-example
- testing-brief-entry-point
- testing-new-workflow
- websocket-live-update-test

### 2. COMPLETED (1 stub)
Work marked as complete/done.
- coderef-timestamp-utility (status: completed)

### 3. OBSOLETE_NAME (1 stub)
Names indicating deprecated/removed work.
- remove-utility-personas

### 4. DUPLICATE (5 stubs)
Similar features in same functional area - kept best version, archived redundant.
- consolidate-foundation-docs-workflow (kept mcp-docs-workflow-refactor)
- rename-execute-plan-to-align-plan (kept as-is, renamed implementation planned)
- scanner-output-validation, scanner-python-detection, scanner-script-path-config (scanner consolidation)

### 5. INFRA_UTILITY_LOW (7 stubs)
Low/medium priority infrastructure tasks created before 2025-01-06.
- consolidate-project-directories
- gitignore-coderef-directory
- mcp-server-cleanup
- rename-start-feature-command
- reorganize-gits-projects
- separate-tag-chips-from-prompt-cards
- work-order-folder-rename

### 6. LOW_PRIORITY_OLD (15 stubs)
Medium-priority backlog items created before 2025-12-20.
- ai-video-gen
- assistant-to-other-projects
- code-review-projects
- connection-to-all-llm
- file-front-matter
- git-libraries
- mcp-integrations
- mcp-usage-tracker
- organize-and-consolidate
- railway-config
- saas-ideas
- stub-id-system
- stub-tag-system
- tech-stack-docs
- track-and-note-commands

---

## Impact

**Before Archival:**
- 98 total stubs in `/working/`
- Mix of high/medium/low priority
- Test scaffolding mixed with active work

**After Archival:**
- 62 active stubs remaining
- Focused on high-priority, recent work
- Cleaner backlog for prioritization

---

## Archive Strategy Notes

**Conservative Approach:**
- Only archived clear candidates (test, completed, obsolete)
- Kept all CRITICAL and HIGH priority stubs active
- Kept recent stubs (less than 1 week old) even if medium priority
- Preserved cross-project coordination stubs (orchestrator-related)

**Reversibility:**
- All archived stubs can be recovered from `coderef/archived/`
- Git history preserved
- No data loss

---

## Script Details

**Script:** `archive-stubs.py`  
**Location:** `C:\Users\willh\Desktop\assistant\archive-stubs.py`  
**Function:** Identifies and moves stubs based on archival criteria

**Identification Criteria (in order):**
1. Test/Example keywords
2. Completed status
3. Obsolete naming patterns
4. Duplicate functional areas
5. Vague exploration/brainstorm stubs
6. Low-priority infrastructure stubs
7. Low-priority + old stubs

**Output:** 
- Console log with before/after counts
- Detailed archival report (ARCHIVAL_REPORT.txt)
- Moved all 36 candidate stubs to archived folder

---

## Next Steps

1. Review remaining 62 active stubs for prioritization
2. Consider updating projects.md to reflect new stub count
3. Consider archival process automation (monthly cleanup)
4. Monitor for test/example stubs going forward - archive immediately

