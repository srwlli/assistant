# MCP Tools & Commands Audit

## docs-mcp: Documentation Tools

| Command                  | Purpose                                              | Type      |
|--------------------------|------------------------------------------------------|-----------|
| generate-foundation-docs | Create README, ARCHITECTURE, API, COMPONENTS, SCHEMA | Generator |
| generate-individual-doc  | Single template generation                           | Generator |
| list-templates           | Show available templates                             | Query     |
| get-template             | Retrieve template content                            | Query     |
| establish-standards      | Extract UI/behavior/UX patterns                      | Generator |
| audit-codebase           | Compliance audit with violations                     | Auditor   |
| check-consistency        | Pre-commit standards gate                            | Validator |
| generate-quickref        | Universal quick reference guide                      | Generator |
| generate-user-guide      | User-facing documentation                            | Generator |
| generate-my-guide        | Tool inventory guide                                 | Generator |

---

## workorder-mcp: Planning & Execution

**Status:** Currently mixed in docs-mcp, needs separation ⚠️

| Command                      | Purpose                                   | Type       |
|------------------------------|-------------------------------------------|------------|
| gather-context               | Collect feature requirements              | Planner    |
| analyze-for-planning         | Auto-populate plan preparation            | Analyzer   |
| create-plan                  | Generate plan.json (10 sections)          | Planner    |
| validate-plan                | Quality score + issue detection           | Validator  |
| get-planning-template        | Show planning standard                    | Query      |
| execute-plan                 | Generate TodoWrite task list              | Executor   |
| update-task-status           | Agent marks task complete/in-progress     | Tracker    |
| track-agent-status           | Multi-agent coordination dashboard        | Tracker    |
| generate-deliverables        | Create DELIVERABLES.md template           | Generator  |
| update-deliverables          | Capture metrics from git                  | Updater    |
| generate-agent-communication | Multi-agent coordination protocol         | Generator  |
| generate-handoff-context     | Auto-populate claude.md for agents        | Generator  |
| assign-agent-task            | Assign workorder to specific agent        | Assigner   |
| verify-agent-completion      | Validate completion + git checks          | Verifier   |
| aggregate-agent-deliverables | Merge metrics across agents               | Aggregator |
| archive-feature              | Move to coderef/archived/                 | Archiver   |
| log-workorder                | Track WO-ID activities                    | Logger     |
| get-workorder-log            | Query workorder history                   | Query      |
| add-changelog-entry          | Create CHANGELOG.json entry               | Updater    |
| get-changelog                | Query changelog                           | Query      |
| update-changelog             | Auto-update with git analysis             | Updater    |
| update-docs                  | Update README/CLAUDE/CHANGELOG            | Updater    |
| audit-plans                  | Health check all plans in coderef/working | Auditor    |
| features-inventory           | List all features (working + archived)    | Query      |

---

## coderef-mcp: Code Reference Tools

| Command                 | Purpose                                 | Type      |
|-------------------------|-----------------------------------------|-----------|
| coderef-scan            | Scan directory for code elements        | Scanner   |
| coderef-query           | Find functions, classes, variables      | Query     |
| coderef-validate        | Validate CodeRef reference format       | Validator |
| coderef-batch-validate  | Parallel validation (5 workers)         | Validator |
| coderef-analyze         | Impact, complexity, coverage analysis   | Analyzer  |
| coderef-docs            | Generate documentation for elements     | Generator |
| coderef-audit           | Validation, coverage, performance audit | Auditor   |
| coderef-expert          | Expert guidance on code structure       | Expert    |
| coderef-foundation-docs | Deep extraction + ARCHITECTURE/SCHEMA   | Generator |

---

## coderef-context (PROPOSED)

**Status:** To be extracted from coderef-mcp

| Command              | Purpose                                      | Type      |
|----------------------|----------------------------------------------|-----------|
| scan-discover-standards | Analyze patterns, calculate confidence     | Scanner   |
| analyze-codebase-context | Deep extraction with violations           | Analyzer  |
| publish-standards    | Auto-publish to coderef-docs               | Publisher |
| query-codebase-json  | Query codebase-context.json                | Query     |

**Output:** `codebase-context.json` with:
- `discovered_standards` (JSON)
- `confidence_scores`
- `violations` (if comparing)

---

## coderef-docs (PROPOSED)

**Status:** To be extracted from docs-mcp

| Command                  | Purpose                                  | Type      |
|--------------------------|------------------------------------------|-----------|
| auto-generate-standards  | Create markdown from coderef-context    | Generator |
| auto-generate-foundation | Generate README, ARCHITECTURE, etc      | Generator |
| embed-standards-in-docs  | Embed discovered standards in markdown  | Embedder  |

**Output:**
- `UI-STANDARDS.md` (from coderef-context)
- `BEHAVIOR-STANDARDS.md` (from coderef-context)
- `UX-PATTERNS.md` (from coderef-context)
- `foundation-docs/` (README, ARCHITECTURE, etc)

---

## coderef-workflow (PROPOSED)

**Status:** To be extracted from docs-mcp

| Command                  | Purpose                              | Type     |
|--------------------------|--------------------------------------|----------|
| create-plan-with-standards | Embed standards in every task      | Planner  |
| validate-plan-against-standards | Ensure task compliance           | Validator |
| generate-task-with-standards | Auto-inject standards in task text | Generator |
| track-compliance         | Monitor agent compliance             | Tracker  |

**Features:**
- Auto-embed: "Follow these UI standards"
- Auto-embed: "Watch for these violations"
- Auto-embed: "Validate against these patterns"

---

## personas-mcp: Persona Management

| Command               | Purpose                            | Type        |
|-----------------------|------------------------------------|-------------|
| use-persona           | Activate expert persona            | Activator   |
| get-active-persona    | Show current persona               | Query       |
| clear-persona         | Deactivate persona                 | Deactivator |
| list-personas         | Show all available personas        | Query       |
| create-custom-persona | Build new persona via workflow     | Creator     |
| docs-expert           | Activate docs-expert persona       | Activator   |
| coderef-expert        | Activate coderef-expert persona    | Activator   |
| archer                | Orchestrator persona               | Activator   |
| ava                   | Frontend specialist persona        | Activator   |
| devon                 | Project setup specialist persona   | Activator   |
| taylor                | General purpose agent persona      | Activator   |
| lloyd                 | CLI checklist/task display persona | Activator   |
| marcus                | (Unknown - needs review)           | Activator   |
| quinn                 | (Unknown - needs review)           | Activator   |

---

## scriptboard-mcp: Scriptboard Tools

| Command           | Purpose                 | Type     |
|-------------------|-------------------------|----------|
| set-prompt        | Stage prompt for export | Stager   |
| clear-prompt      | Clear prompt            | Clearer  |
| add-attachment    | Attach code/logs        | Attacher |
| clear-attachments | Clear all attachments   | Clearer  |
| coderef-status    | Check CLI availability  | Status   |
| coderef-scan      | Local coderef scan      | Scanner  |
| coderef-query     | Local dependency query  | Query    |
| coderef-impact    | Local impact analysis   | Analyzer |

---

## Utility Commands

| Command         | Purpose                     | Type       |
|-----------------|-----------------------------|------------|
| stub            | Create stub feature         | Creator    |
| research-scout  | Research task automation    | Researcher |
| list-commands   | Show all commands           | Query      |
| list-tools      | Show all tools              | Query      |
| fix             | Quick fix handler           | Utility    |
| git-release     | Release automation          | Release    |
| prompt-workflow | Prompt composition workflow | Workflow   |

---

## Summary Stats

| Category        | Count | Status               |
|-----------------|-------|----------------------|
| docs-mcp        | 10    | Pure docs ✅          |
| workorder-mcp   | 24    | Mixed in docs-mcp ⚠️ |
| coderef-mcp     | 9     | Pure code analysis ✅ |
| personas-mcp    | 14    | Pure personas ✅      |
| scriptboard-mcp | 8     | Pure scriptboard ✅   |
| Utility         | 7     | Helpers              |
| TOTAL           | 72    | -                    |

---

## Key Insight

**Current Problem:** docs-mcp contains both:
- 10 pure documentation tools
- 24 planning/workorder/coordination tools

**Solution:** Extract workorder functionality into separate `coderef-workflow` server, which automatically receives standards from `coderef-context` → `coderef-docs` pipeline.
