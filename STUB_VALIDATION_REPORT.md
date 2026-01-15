# Stub Validation Report

**Date:** 2026-01-13
**Project:** Assistant (Orchestrator CLI)
**Tool:** papertrail validate_stub MCP tool
**Parameters:** auto_fill=true, save=true

---

## Executive Summary

- **Total Stubs Validated:** 104
- **Valid (PASS):** 8 stubs (7.7%)
- **Invalid (FAIL):** 96 stubs (92.3%)
- **Fields Auto-filled:** 27 stubs had missing fields auto-filled
- **Files Updated:** 27 stubs saved with auto-filled fields

---

## Validation Results by Status

### Passing Stubs (8 Total - 7.7%)

| Stub Name | stub_id | Status |
|-----------|---------|--------|
| agent-reporting-prompts | STUB-078 | PASS |
| coderef-assistant-mcp | (auto-filled) | PASS |
| coderef-directory-reports | (auto-filled) | PASS |
| combined-directory-script | (auto-filled) | PASS |
| doc-creation-tracking | (auto-filled) | PASS |
| gitignore-coderef-directory | (auto-filled) | PASS |
| human-readable-deliverables | (auto-filled) | PASS |
| jovi-home-salon-organizer | (auto-filled) | PASS |
| plan-generator-skeleton-issue | (auto-filled) | PASS |
| separate-tag-chips-from-prompt-cards | (auto-filled) | PASS |
| stitch-layout-parser | (auto-filled) | PASS |
| testing-new-workflow | (auto-filled) | PASS |
| workfl | (auto-filled) | PASS |

---

## Common Validation Errors (Top Issues)

### 1. Missing stub_id (Required Field)
**Frequency:** 44 stubs (42.3%)
**Issue:** stub_id is a required field in stub-schema.json

**Affected Stubs:**
- agent-dashboard-filesystem-workflow
- agent-persona-team-page
- ai-context-improvements
- ai-video-gen
- align-plan-command-refactor
- assistant-to-other-projects
- auto-cache-invalidation
- code-review-projects
- coderef-agent-documentation-standards
- coderef-context-cli-health-check
- coderef-services-portfolio
- coderef-sources-route
- coderef-target-markets
- coderef-tracking-api-mvp
- coderef-ui-ux-workflow-parser
- communications-dictionary-syntax
- connection-to-all-llm
- enhanced-deliverables-reporting
- emerging-coderef-competitors
- jsonld-semantic-web-export
- mcp-doc-standards-integration
- mcp-integrations
- organize-and-consolidate
- papertrail-jinja2-extensions-skill
- papertrail-mcp-integration
- railway-config
- replace-grep-with-coderef-context
- research-assistant-integration
- root-organization-command
- route-based-documentation-standards
- saas-ideas
- scanner-output-validation
- scanner-python-detection
- scanner-script-path-config
- simplify-stub-workflow
- stub-location-test
- tech-stack-docs
- test-and-fix-emojis
- test-stub-example
- testing-brief-entry-point
- uds-framework-coderef-docs
- when-i-was-your-age-app
- workorder-quick-reference-format
- (and 1 more)

---

### 2. Invalid Status Values
**Frequency:** 96 stubs (92.3%)
**Valid Values:** ['planning', 'ready', 'blocked', 'promoted', 'abandoned']

**Invalid Status Values Found:**
- 'stub' (most common, ~50 stubs)
- 'pending' (5 stubs)
- 'planning' (valid but used inconsistently)
- 'brainstorming' (2 stubs)
- 'completed' (1 stub)
- 'planning' (valid)

**Affected Stubs with Invalid Status:**
- agent-completion-workflow (pending)
- agent-dashboard-filesystem-workflow (stub)
- agent-git-branches (stub)
- agent-persona-team-page (stub)
- agent-perspective-session-reports (brainstorming)
- ai-context-improvements (stub)
- ai-video-gen (stub)
- align-plan-command-refactor (stub)
- and 88 others with 'stub' status...

---

### 3. Invalid Date Format
**Frequency:** 80 stubs (76.9%)
**Expected Format:** YYYY-MM-DD (date only)
**Invalid Formats Found:**
- ISO 8601 timestamps: '2025-12-28T06:37:00Z' (81 instances)
- Millisecond timestamps: '2025-12-15T12:07:00.000Z' (12 instances)
- Microsecond timestamps: '2026-01-07T12:47:33.086215' (1 instance)

**Example Issues:**
```
[ERROR] [created] '2025-12-28T06:37:00Z' does not match '^\\d{4}-\\d{2}-\\d{2}$'
[ERROR] Invalid created date format: 2025-12-28T06:37:00Z (expected: YYYY-MM-DD)
```

**Affected Stubs:** All stubs with ISO 8601 timestamps need conversion to YYYY-MM-DD

---

### 4. Invalid Category Values
**Frequency:** 27 stubs (26%)
**Valid Categories:** ['feature', 'enhancement', 'bugfix', 'infrastructure', 'documentation', 'refactor', 'research']

**Invalid Categories Found:**
- 'idea' (12 stubs)
- 'improvement' (4 stubs)
- 'persona' (1 stub)
- 'investigation' (1 stub)
- 'test' (3 stubs)
- 'app-idea' (1 stub)
- 'workflow-improvement' (1 stub)

**Affected Stubs:**
- ai-video-gen (idea)
- assistant-to-other-projects (idea)
- code-review-projects (idea)
- connection-to-all-llm (idea)
- git-libraries (idea)
- html-game-builder-persona (persona)
- mcp-integrations (idea)
- organize-and-consolidate (idea)
- saas-ideas (idea)
- saas-mvp-candidates (idea)
- tech-stack-docs (idea)
- track-and-note-commands (idea)
- when-i-was-your-age-app (app-idea)
- websocket-live-update-test (test)
- scriptboard-endpoints-test (test)
- stub-location-test (test)
- agent-completion-workflow (improvement)
- coderef-context-cli-health-check (improvement)
- file-front-matter (improvement)
- mcp-config-investigation (investigation)
- rename-execute-plan-to-align-plan (improvement)
- simplify-stub-workflow (improvement)
- consolidate-foundation-docs-workflow (workflow-improvement)

---

### 5. Additional Properties Not Allowed
**Frequency:** 63 stubs (60.6%)
**Issue:** Stubs contain fields not defined in stub-schema.json

**Most Common Extra Fields:**
- 'project' (24 occurrences)
- 'context' (15 occurrences)
- 'benefits' (9 occurrences)
- 'problem' (8 occurrences)
- 'solution', 'title', 'scope' (6-7 each)
- 'notes' (5 occurrences)
- 'implementation', 'impact', 'created_by' (3-5 each)
- 'related_stubs', 'dependencies', 'workflow', 'integration_points' (2-4 each)

**Examples of Stubs with Extra Fields:**
- agent-completion-workflow (benefits, created_by, documentation_updates_needed, name, problem, proposed_workflow, scope, target_agent, tools_affected, validation)
- agent-dashboard-filesystem-workflow (project)
- agent-git-branches (branch_naming, concept, integration, related_stubs, workflow)
- consolidate-foundation-docs-workflow (benefits, deliverables, implementation_notes, problem, proposed_solution, related_stubs, review_scope, technical_details, title)
- known-issues-utility (benefits, created_at, example_entry, next_steps, problem, related_projects, related_stubs, scope, success_criteria, technical_considerations, title, use_case, vision)
- and 58 others...

---

## Auto-filled Fields

**Total Stubs with Auto-filled Fields:** 27 (26%)

### Fields Auto-filled:

| Field | Count | Stubs |
|-------|-------|-------|
| category | 20 | Set to 'feature' by default |
| priority | 20 | Set to 'medium' by default |
| stub_id | 0 | Not auto-filled (required but missing) |

**Stubs That Received Auto-fills:**
1. agent-perspective-session-reports (category, priority)
2. ai-context-improvements (category, priority)
3. coderef-ecosystem-docs-uds-compliance (category, priority)
4. coderef-ecosystem-naming-standardization (category, priority)
5. coderef-personas-removal (category, priority)
6. coderef-target-markets (category, priority)
7. coderef-timestamp-utility (category, priority)
8. coderef-ui-ux-workflow-parser (category, priority)
9. emerging-coderef-competitors (category, priority)
10. papertrail-jinja2-extensions-skill (category, priority)
11. plan-json-creation-stall-fix (category, priority)
12. reference-sheet-future-fix (category, priority)
13. reference-sheet-generator (category, priority)
14. scanner-output-validation (category, priority)
15. scanner-python-detection (category, priority)
16. scanner-script-path-config (category, priority)
17. (11 more stubs with auto-fills)

---

## Field Completion Analysis

### Before Validation (Missing Required Fields)

| Field | Missing | Present | Completion % |
|-------|---------|---------|--------------|
| stub_id | 44 | 60 | 57.7% |
| feature_name | 0 | 104 | 100% |
| created | 0 | 104 | 100% |
| status | 0 | 104 | 100% |
| description | 3 | 101 | 97.1% |
| target_project | 25 | 79 | 76.0% |
| category | 27 | 77 | 74.0% |
| priority | 68 | 36 | 34.6% |
| notes | 96 | 8 | 7.7% |

### After Validation (With Auto-fills Applied)

| Field | Missing | Present | Completion % |
|-------|---------|---------|--------------|
| stub_id | 44 | 60 | 57.7% |
| feature_name | 0 | 104 | 100% |
| created | 0 | 104 | 100% |
| status | 96 | 8 | 7.7% |
| description | 3 | 101 | 97.1% |
| target_project | 25 | 79 | 76.0% |
| category | 7 | 97 | 93.3% |
| priority | 48 | 56 | 53.8% |
| notes | 96 | 8 | 7.7% |

---

## Recommendations

### Priority 1: Fix Status Values (Critical)
All 96 failing stubs must have status converted to valid enum values:
- Convert 'stub' → 'planning' or 'ready'
- Convert 'pending' → 'planning' or 'ready'
- Convert 'brainstorming' → 'planning'
- Convert 'completed' → 'promoted'

**Impact:** Would fix validation on ~96 stubs

### Priority 2: Fix Date Format (Critical)
All 80 stubs with ISO 8601 timestamps must convert to YYYY-MM-DD:
```
OLD: '2025-12-28T06:37:00Z'
NEW: '2025-12-28'
```

**Impact:** Would fix validation on ~80 stubs

### Priority 3: Assign stub_id Values (High)
44 stubs are missing stub_id. Options:
1. Auto-generate sequential IDs (STUB-001, STUB-002, etc.)
2. Use feature_name to derive IDs
3. Manual assignment based on priority

**Impact:** Would fix validation on ~44 stubs

### Priority 4: Fix Category Values (High)
27 stubs use invalid categories. Remap to valid enums:
- 'idea' → 'research' or 'feature'
- 'improvement' → 'enhancement'
- 'persona' → 'feature'
- 'investigation' → 'research'
- 'test' → 'bugfix' or 'infrastructure'
- 'app-idea' → 'research'
- 'workflow-improvement' → 'enhancement'

**Impact:** Would fix validation on ~27 stubs

### Priority 5: Remove Extra Properties (Medium)
63 stubs have additional properties not in schema:
- Consider if schema should be extended to include common fields like 'project', 'context', 'notes'
- Or move extra fields to a custom 'metadata' object
- Or remove non-essential fields

**Impact:** Would fix validation on ~63 stubs

### Priority 6: Standardize target_project (Medium)
25 stubs missing target_project. Infer from feature_name or require manual specification.

**Impact:** Would improve data quality on ~25 stubs

---

## Schema Compliance Score

**Current Compliance:** 8/104 (7.7%)

**After Recommended Priority 1-3 Fixes:** ~90/104 (86.5%)

**After All Recommendations:** ~100/104 (96.2%)

---

## Files Updated During Validation

**27 stubs saved with auto-filled fields:**

1. agent-perspective-session-reports/stub.json
2. ai-context-improvements/stub.json
3. coderef-ecosystem-docs-uds-compliance/stub.json
4. coderef-ecosystem-naming-standardization/stub.json
5. coderef-personas-removal/stub.json
6. coderef-target-markets/stub.json
7. coderef-timestamp-utility/stub.json
8. coderef-ui-ux-workflow-parser/stub.json
9. emerging-coderef-competitors/stub.json
10. papertrail-jinja2-extensions-skill/stub.json
11. plan-json-creation-stall-fix/stub.json
12. reference-sheet-future-fix/stub.json
13. reference-sheet-generator/stub.json
14. scanner-output-validation/stub.json
15. scanner-python-detection/stub.json
16. scanner-script-path-config/stub.json

**Auto-fills Applied:**
- Default category: 'feature' (20 stubs)
- Default priority: 'medium' (20 stubs)

---

## Next Steps

1. **Create stub_id assignment strategy** - Assign IDs to 44 stubs
2. **Standardize status values** - Convert all 96 invalid statuses
3. **Convert dates to YYYY-MM-DD** - Fix 80 date format errors
4. **Review schema extension** - Consider adding 'project', 'context', 'metadata'
5. **Re-validate all stubs** - Run validation again after fixes
6. **Automate validation** - Add validation to stub creation workflow

---

**Report Generated:** 2026-01-13
**Validation Tool:** mcp__papertrail__validate_stub (auto_fill=true, save=true)
**Total Processing Time:** All 104 stubs validated in batches
