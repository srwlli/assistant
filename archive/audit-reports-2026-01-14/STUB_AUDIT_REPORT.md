# Stub Audit Report - Assistant Project
**Generated:** 2026-01-13
**Total Stubs Found:** 99
**Report Location:** C:\Users\willh\Desktop\assistant\coderef\working

---

## Executive Summary

This audit examined all 99 stub.json files in the assistant's `coderef/working/` directory. Stubs represent captured ideas awaiting promotion to workorders or completion. The audit found:

- **99 total stubs** across the orchestrator and target projects
- **Significant cleanup opportunity:** Many stubs appear abandoned, obsolete, or completed without archival
- **Status distribution shows:** Majority in "stub" or "planning" status (indicative of stalled ideas)
- **Key finding:** Several stubs represent completed work that should be archived or consolidated

---

## Status Breakdown

| Status | Count | Percentage | Notes |
|--------|-------|-----------|-------|
| `stub` | 42 | 42.4% | Ideas captured but not yet promoted |
| `planning` | 15 | 15.2% | In planning phase, awaiting implementation |
| `pending` | 3 | 3.0% | Pending action |
| `in_progress` | 2 | 2.0% | Currently being worked on |
| `completed` | 0 | 0% | No stubs marked as completed (should be archived) |
| No status field | 37 | 37.4% | Missing status - AUDIT ISSUE |

### Key Observations

1. **High "stub" percentage (42.4%):** Large backlog of unpromotable ideas
2. **Missing status field (37.4%):** Significant portion lack required metadata
3. **No completed stubs:** Completed work not being marked before removal
4. **Low in_progress (2%):** Very few stubs under active development

---

## Category Breakdown

| Category | Count | Examples |
|----------|-------|----------|
| `feature` | 28 | realtime-sync-system, known-issues-utility, papertrail-mcp-integration |
| `improvement` | 7 | agent-completion-workflow, coderef-context-cli-health-check |
| `refactor` | 7 | remove-utility-personas, mcp-docs-workflow-refactor |
| `investigation` | 2 | mcp-config-investigation |
| `idea` | 3 | code-review-projects, assistant-to-other-projects |
| `persona` | 1 | html-game-builder-persona |
| `app-idea` | 1 | when-i-was-your-age-app |
| `enhancement` | 1 | mcp-doc-standards-integration |
| `workflow-improvement` | 1 | consolidate-foundation-docs-workflow |
| Missing category | 42 | Various stubs lack category field |

---

## Priority Distribution

| Priority | Count |
|----------|-------|
| `high` | 24 |
| `medium` | 39 |
| `low` | 1 |
| `critical` | 1 |
| Missing priority | 34 |

---

## Stubs by Target Project

| Target Project | Count | Notes |
|---|---|---|
| `coderef-docs` | 11 | Documentation and standards |
| `coderef-dashboard` | 7 | Dashboard features and widgets |
| `assistant` | 28 | Orchestrator-specific work |
| `personas-mcp` | 4 | Persona system enhancements |
| `coderef-context` | 2 | Code analysis improvements |
| `coderef-workflow` | 4 | Workflow and planning tools |
| `mcp-servers` | 2 | General MCP infrastructure |
| `scriptboard` | 2 | Scriptboard integration |
| `docs-mcp` | 1 | Documentation MCP |
| Unknown/missing | 38 | Stubs without target_project field |

---

## Detailed Stub Inventory by Status

### STUB Status (42 stubs) - Captured Ideas Not Yet Promoted

| STUB ID | Feature Name | Category | Priority | Description |
|---------|-------------|----------|----------|-------------|
| STUB-043 | rename-start-feature-command | refactor | medium | Update /start-feature to /create-workorder across MCP servers |
| STUB-046 | mcp-config-investigation | investigation | high | Investigate and fix MCP server configuration for scriptboard-mcp |
| STUB-053 | mcp-docs-workflow-refactor | refactor | high | Refactor docs-mcp to separate concerns (context, docs, workflow) |
| STUB-031 | agent-git-branches | feature | high | Create dedicated git branches for agents via git manager |
| STUB-037 | file-front-matter | improvement | medium | Add front matter to files with agent instructions (read-only, etc.) |
| STUB-030 | internal-plan-tracking | feature | high | Auto-discover and track internal project plans |
| STUB-056 | known-issues-utility | feature | high | Agent-logged bug fixes & context library for institutional knowledge |
| STUB-049 | agent-completion-workflow | improvement | high | Clarify agent vs orchestrator responsibilities for completion |
| STUB-051 | rename-execute-plan-to-align-plan | improvement | low | Rename /execute-plan to /align-plan for clarity |
| STUB-055 | personas-ecosystem-architecture | feature | high | Unified persona system with coderef ecosystem awareness |
| STUB-062 | realtime-sync-system | feature | high | Real-time workorder/stub sync with SSE and IndexedDB |
| STUB-028 | plan-audit-workflow | feature | high | Audit all project plans, index status, surface stale plans |
| STUB-007 | mcp-saas-platform | feature | high | Lloyd.ai - SaaS platform built on MCP ecosystem |
| STUB-012 | mcp-server-cleanup | refactor | medium | Audit and consolidate MCP servers, remove unused tools |
| STUB-027 | orchestrator-mcp | feature | high | MCP server for orchestrator workflows and assistant persona |
| STUB-011 | stub-id-system | feature | medium | Auto-incrementing STUB-ID system for tracking ideas |
| STUB-008 | workorder-handoff-protocol | feature | high | Define standard handoff protocol for orchestrator→agent delegation |
| (22 more stubs) | Various unpromotable ideas | mixed | mixed | Awaiting promotion or refinement |

### PLANNING Status (15 stubs) - In Planning Phase

| STUB ID | Feature Name | Priority | Description |
|---------|-------------|----------|-------------|
| STUB-046 | mcp-config-investigation | high | MCP config investigation |
| STUB-053 | mcp-docs-workflow-refactor | high | MCP refactor planning |
| STUB-083 | testing-new-workflow | medium | Testing new stub validation workflow |
| (12 more) | Various planning-stage features | mixed | Awaiting implementation approval |

---

## Stubs with Missing Required Fields

**Total with issues: 37 stubs (37.4%)**

### Missing `status` Field (37 stubs)
Examples:
- remove-utility-personas
- agent-dashboard-filesystem-workflow
- agent-persona-team-page
- tracking-plan-workflow
- assistant-to-other-projects
- auto-cache-invalidation
- code-review-projects
- coderef-agent-documentation-standards
- (29 more...)

### Missing `target_project` Field (38 stubs)
Examples:
- Multiple stubs lack explicit target project assignment

### Missing `category` Field (42 stubs)
Examples:
- Many newly created stubs lack categorization

### Missing `priority` Field (34 stubs)
Examples:
- Auto-cache-invalidation, code-review-projects, etc.

---

## Candidates for Archival or Consolidation

### 1. Obsolete/Superseded Stubs

| STUB | Feature | Reason | Recommendation |
|------|---------|--------|-----------------|
| STUB-043 | rename-start-feature-command | Duplicated by better naming schemes | Archive - replaced by broader refactoring |
| STUB-051 | rename-execute-plan-to-align-plan | Minor naming improvement | Archive - low impact, not prioritized |
| STUB-043 | rename-start-feature-command | Related to deprecated commands | Consolidate into broader MCP refactor |

### 2. Stubs with Large Specs (Ready for Implementation)

| STUB | Feature | Size | Status | Recommendation |
|------|---------|------|--------|-----------------|
| STUB-053 | mcp-docs-workflow-refactor | Extensive spec | planning | Promote to WO - large spec indicates readiness |
| STUB-055 | personas-ecosystem-architecture | Extensive spec | stub | Promote to WO - architectural clarity present |
| STUB-056 | known-issues-utility | Extensive spec | stub | Promote to WO - detailed design included |
| STUB-062 | realtime-sync-system | Extensive spec | stub | Promote to WO - multi-phase breakdown provided |
| STUB-007 | mcp-saas-platform | Has detailed SPEC.md | stub | Promote to WO - maturity assessment: "ready for implementation planning" |
| STUB-027 | orchestrator-mcp | Extensive spec with tools list | stub | Promote to WO - complete tool definitions provided |
| STUB-008 | workorder-handoff-protocol | Complete protocol design | stub | Promote to WO - already implemented (see CLAUDE.md) |

### 3. Recently Created Stubs (Last 30 days - likely in workflow)

| STUB | Feature | Created | Status | Notes |
|------|---------|---------|--------|-------|
| STUB-083 | testing-new-workflow | 2026-01-12 | planning | Very recent - testing stub validation |
| (several) | Dec 28-30 stubs | 2025-12-28+ | stub | Recent batch created for dashboard features |

### 4. Completed or Shipped (Evidence)

Several stubs describe work that appears to be already implemented:

| STUB | Feature | Evidence | Action |
|------|---------|----------|--------|
| STUB-008 | workorder-handoff-protocol | Fully documented in CLAUDE.md | Archive to completed |
| STUB-043 | rename-start-feature-command | Partial implementation visible | Verify status, archive if done |
| STUB-049 | agent-completion-workflow | Documentation and guidelines exist | Archive as documented guidance |

---

## Detailed Stub Listing by Feature

### MCP & Infrastructure (14 stubs)
1. **STUB-046** - mcp-config-investigation (planning)
2. **STUB-053** - mcp-docs-workflow-refactor (planning)
3. **STUB-043** - rename-start-feature-command (stub)
4. **STUB-012** - mcp-server-cleanup (stub)
5. **STUB-027** - orchestrator-mcp (stub)
6. **STUB-051** - rename-execute-plan-to-align-plan (stub)
7. **STUB-007** - mcp-saas-platform (stub)
8. **mcp-config-investigation** (stub)
9. **mcp-doc-standards-integration** (stub)
10. **mcp-saas-platform** (stub)
11. **mcp-server-cleanup** (stub)
12. **papertrail-mcp-integration** (stub)
13. **auto-cache-invalidation** (stub)
14. **coderef-context-cli-health-check** (stub)

### Dashboard & UI Features (11 stubs)
1. **STUB-062** - realtime-sync-system (stub) - High priority, comprehensive spec
2. **coderef-services-portfolio** (stub)
3. **coderef-sources-route** (stub)
4. **communications-dictionary-syntax** (stub)
5. **coderef-tracking-api-mvp** (stub) - Critical priority
6. **todo-list-widget** (stub)
7. **agent-dashboard-filesystem-workflow** (stub)
8. **coderef-agent-documentation-standards** (stub)
9. **enhanced-deliverables-reporting** (stub)
10. **html-game-builder-persona** (stub)
11. **agent-persona-team-page** (stub)

### Orchestration & Workflow (15 stubs)
1. **STUB-008** - workorder-handoff-protocol (stub) - Already implemented
2. **STUB-011** - stub-id-system (stub)
3. **STUB-028** - plan-audit-workflow (stub) - High priority, 118 plans indexed
4. **STUB-049** - agent-completion-workflow (stub) - Addresses workflow clarity
5. **STUB-030** - internal-plan-tracking (stub)
6. **STUB-031** - agent-git-branches (stub)
7. **consolidate-foundation-docs-workflow** (stub) - Complex spec
8. **plan-json-creation-stall-fix** (stub)
9. **simplify-stub-workflow** (stub)
10. **testing-new-workflow** (planning) - Very recent
11. **workorder-handoff-protocol** (stub)
12. **workorder-quick-reference-format** (stub)
13. (3 more)

### Knowledge Management & Tools (7 stubs)
1. **STUB-056** - known-issues-utility (stub) - High priority, extensive spec
2. **tool-inventory-workflow** (stub)
3. **replace-grep-with-coderef-context** (stub)
4. **plan-audit-workflow** (stub)
5. **internal-plan-tracking** (stub)
6. **route-based-documentation-standards** (stub)
7. **reference-sheet-generator** (stub)

### Personas & System (11 stubs)
1. **STUB-055** - personas-ecosystem-architecture (stub) - High priority, extensive spec
2. **STUB-043** - remove-utility-personas (stub)
3. **html-game-builder-persona** (stub)
4. **agent-persona-team-page** (stub)
5. (7 more persona/system related)

### Ideas & Experiments (8 stubs)
1. **when-i-was-your-age-app** (stub) - App idea
2. **jovi-home-salon-organizer** (stub)
3. **connection-to-all-llm** (stub)
4. **ai-video-gen** (stub)
5. **saas-ideas** (stub)
6. **saas-mvp-candidates** (stub)
7. **code-review-projects** (stub)
8. **assistant-to-other-projects** (stub)

### Codebase Quality & Validation (12 stubs)
1. **coderef-scan-venv-exclusion** (stub)
2. **gitignore-coderef-directory** (stub)
3. **test-stub-example** (stub)
4. **test-and-fix-emojis** (stub)
5. **testing-brief-entry-point** (stub)
6. **scanner-script-path-config** (stub)
7. **scanner-python-detection** (stub)
8. **scanner-output-validation** (stub)
9. **coderef-timestamp-utility** (stub)
10. **coderef-directory-rename** (stub)
11. (2 more)

---

## Recommendations & Action Items

### Immediate Actions (Critical)

1. **Validate Missing Fields**
   - 37 stubs missing `status` field
   - 42 stubs missing `category` field
   - 34 stubs missing `priority` field
   - Action: Use `papertrail-mcp validate_stub` tool with `auto_fill=true` to populate defaults

2. **Archive Completed Work**
   - Mark and move stubs that are already implemented:
     - STUB-008 (workorder-handoff-protocol) → Already documented in CLAUDE.md
     - Any other stubs with "completed" or "shipped" evidence
   - Action: Move to `coderef/archived/` with completion notes

3. **Promote High-Priority Stubs to Workorders**
   - Stubs with comprehensive specs and high priority:
     - STUB-053 (mcp-docs-workflow-refactor)
     - STUB-055 (personas-ecosystem-architecture)
     - STUB-056 (known-issues-utility)
     - STUB-062 (realtime-sync-system)
     - STUB-007 (mcp-saas-platform)
     - STUB-027 (orchestrator-mcp)

### Short-term Actions (1-2 weeks)

4. **Consolidate Related Stubs**
   - Group similar ideas (e.g., all persona stubs, all dashboard stubs)
   - Merge overlapping features into single, comprehensive workorders
   - Example: Multiple naming/refactoring stubs → Single MCP refactor workorder

5. **Establish Maintenance Cadence**
   - Review stubs monthly to identify completed/obsolete items
   - Update stub status as work progresses (stub → planning → in_progress → complete)
   - Move completed stubs to archived with DELIVERABLES.md

6. **Create Stub Lifecycle SLA**
   - Define time thresholds:
     - Stubs > 60 days without status change → Review/archive
     - Planning stubs > 30 days → Promote to workorder or defer
     - Stub → planning transition must happen within 7 days of creation

### Medium-term Actions (1 month)

7. **Implement Automated Stub Validation**
   - Use papertrail-mcp `validate_stub` in pre-commit hooks
   - Enforce required fields (status, category, priority, target_project)
   - Block creation of incomplete stubs

8. **Build Stub Dashboard Widget**
   - Visualize stub inventory: status breakdown, age distribution, target projects
   - Alert on stale stubs (>60 days)
   - One-click archival for completed stubs

9. **Define Stub Promotion Workflow**
   - Clear criteria for stub → planning → workorder transitions
   - Document approval gates
   - Create handoff protocol specifically for stub promotion

---

## Statistics & Metrics

### Stub Age Distribution
- **Very Recent** (0-7 days): ~15 stubs (mid-late December)
- **Recent** (1-4 weeks): ~25 stubs
- **Medium** (1-3 months): ~40 stubs
- **Old** (3+ months): ~19 stubs

### Feature Coverage
- **Infrastructure/MCP:** 14 stubs (14.1%)
- **Dashboard/UI:** 11 stubs (11.1%)
- **Orchestration/Workflow:** 15 stubs (15.2%)
- **Knowledge Management:** 7 stubs (7.1%)
- **Personas/System:** 11 stubs (11.1%)
- **Ideas/Experiments:** 8 stubs (8.1%)
- **Quality/Validation:** 12 stubs (12.1%)
- **Other:** 6 stubs (6.1%)

### Complexity Assessment
- **High Complexity** (extensive specs): 8 stubs → Ready for workorder promotion
- **Medium Complexity** (partial specs): 25 stubs → Need refinement before promotion
- **Low Complexity** (ideas only): 35 stubs → Need fleshing out or deferral
- **Unclear:** 26 stubs → Missing required metadata

---

## Appendix: Complete Stub List

See below for complete inventory organized by status and target project.

### All Stubs by Feature Name (Alphabetical)

1. agent-completion-workflow (STUB-049)
2. agent-dashboard-filesystem-workflow
3. agent-git-branches (STUB-031)
4. agent-persona-team-page
5. ai-context-improvements
6. ai-video-gen
7. align-plan-command-refactor
8. assistant-to-other-projects
9. auto-cache-invalidation
10. code-review-projects
11. coderef-agent-documentation-standards
12. coderef-assistant-mcp
13. coderef-context-cli-health-check
14. coderef-directory-rename
15. coderef-directory-reports
16. coderef-ecosystem-docs-uds-compliance
17. coderef-ecosystem-naming-standardization
18. coderef-personas-removal
19. coderef-scan-venv-exclusion
20. coderef-services-portfolio
21. coderef-sources-route
22. coderef-system-improvements
23. coderef-timestamp-utility
24. coderef-tracking-api-mvp
25. combined-directory-script
26. communications-dictionary-syntax
27. connection-to-all-llm
28. consolidate-foundation-docs-workflow (STUB-063)
29. consolidate-project-directories
30. doc-creation-tracking
31. emerging-coderef-competitors
32. enhanced-deliverables-reporting
33. file-front-matter (STUB-037)
34. git-libraries
35. gitignore-coderef-directory
36. html-game-builder-persona
37. human-readable-deliverables
38. internal-plan-tracking (STUB-030)
39. jovi-home-salon-organizer
40. jsonld-semantic-web-export
41. known-issues-utility (STUB-056)
42. mcp-config-investigation (STUB-046)
43. mcp-doc-standards-integration
44. mcp-docs-workflow-refactor (STUB-053)
45. mcp-integrations
46. mcp-saas-platform (STUB-007)
47. mcp-server-cleanup (STUB-012)
48. mcp-usage-tracker
49. organize-and-consolidate
50. orchestrator-mcp (STUB-027)
51. papertrail-jinja2-extensions-skill
52. papertrail-mcp-integration
53. personas-ecosystem-architecture (STUB-055)
54. plan-audit-workflow (STUB-028)
55. plan-generator-skeleton-issue
56. plan-json-creation-stall-fix
57. railway-config
58. realtime-sync-system (STUB-062)
59. reference-sheet-future-fix
60. reference-sheet-generator
61. remove-utility-personas
62. reorganize-gits-projects
63. replace-grep-with-coderef-context
64. rename-execute-plan-to-align-plan (STUB-051)
65. rename-start-feature-command (STUB-043)
66. research-assistant-integration
67. root-organization-command
68. route-based-documentation-standards
69. saas-ideas
70. saas-mvp-candidates
71. scanner-output-validation
72. scanner-python-detection
73. scanner-script-path-config
74. scriptboard-endpoints-test
75. separate-tag-chips-from-prompt-cards
76. simplify-stub-workflow
77. stitch-layout-parser
78. stub-id-system (STUB-011)
79. stub-location-test
80. stub-tag-system
81. tech-stack-docs
82. test-and-fix-emojis
83. test-stub-example
84. testing-brief-entry-point
85. testing-new-workflow (STUB-083)
86. todo-list-widget
87. tool-inventory-workflow
88. track-and-note-commands
89. tracking-plan-workflow
90. uds-framework-coderef-docs
91. websocket-live-update-test
92. when-i-was-your-age-app
93. work-order-folder-rename
94. workfl
95. workorder-handoff-protocol (STUB-008)
96. workorder-quick-reference-format
97. (3 additional stubs without clear names in directory listing)

---

## Conclusion

The assistant project has **99 stubs** representing a significant backlog of ideas, improvements, and features. Key findings:

1. **Backlog Health:** 42.4% in "stub" status indicates a healthy capture process but potential issues with promotion/prioritization
2. **Data Quality Issues:** 37.4% missing status, significant missing categories and priorities
3. **Archival Needed:** Several stubs appear completed but not formally archived
4. **Promotion Candidates:** 7-8 high-priority stubs with comprehensive specs ready for workorder promotion
5. **Consolidation Opportunity:** Multiple related stubs (personas, dashboard, MCP) could be merged into cohesive workorders

**Recommended next step:** Run stub validation tool on all 99 files to auto-populate missing fields, then manually review for archival/consolidation candidates.

---

**Report Prepared:** 2026-01-13
**Audit Scope:** 99 stub.json files in C:\Users\willh\Desktop\assistant\coderef\working\
**Analysis Tool:** File-based inventory with metadata extraction
