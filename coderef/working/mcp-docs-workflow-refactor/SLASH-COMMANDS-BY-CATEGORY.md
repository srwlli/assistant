# Slash Commands by Category

## docs-mcp Commands (10 pure doc tools)

- generate-foundation-docs - Create README, ARCHITECTURE, API, COMPONENTS, SCHEMA
- generate-individual-doc - Single template
- list-templates - Show available templates
- get-template - Retrieve template content
- establish-standards - Extract UI/behavior/UX patterns
- audit-codebase - Compliance audit
- check-consistency - Pre-commit standards gate
- generate-quickref - Universal quick reference
- generate-user-guide - User-facing docs
- generate-my-guide - Tool inventory

---

## workorder-mcp Commands (24 planning/execution tools - mixed in docs-mcp)

- gather-context - Feature requirements
- analyze-for-planning - Project analysis
- create-plan - Generate plan.json
- create-workorder - Full workflow (context → analysis → plan)
- validate-plan - Quality scoring
- execute-plan - Generate TodoWrite tasks
- update-task-status - Agent progress tracking
- track-agent-status - Multi-agent dashboard
- generate-deliverables - DELIVERABLES.md template
- update-deliverables - Capture metrics
- archive-feature - Move to archived/
- log-workorder - Track WO-IDs
- get-workorder-log - Query history
- add-changelog-entry - Create entry
- update-changelog - Auto-update
- update-docs - README/CLAUDE/CHANGELOG sync
- audit-plans - Health check all plans
- features-inventory - List all features
- Plus: agent communication, handoff, assignment, verification, aggregation

---

## coderef-mcp Commands (9 code analysis)

- coderef-scan - Scan for code elements
- coderef-query - Find functions/classes/variables
- coderef-validate - Validate references
- coderef-batch-validate - Bulk validation
- coderef-analyze - Impact/complexity/coverage
- coderef-docs - Generate docs for elements
- coderef-audit - Validation/coverage/performance audit
- coderef-expert - Expert guidance
- coderef-foundation-docs - Deep ARCHITECTURE/SCHEMA extraction

---

## personas-mcp Commands (14 persona tools)

- use-persona - Activate persona
- get-active-persona - Show current
- clear-persona - Deactivate
- list-personas - Show all
- create-custom-persona - Build new persona
- Plus 9 specific personas: archer, ava, devon, taylor, lloyd, docs-expert, coderef-expert, marcus, quinn

---

## scriptboard-mcp Commands (8 scriptboard tools)

- set-prompt - Stage prompt
- clear-prompt - Clear
- add-attachment - Attach files
- clear-attachments - Clear all
- coderef-status - Check CLI
- coderef-scan - Local scan
- coderef-query - Local query
- coderef-impact - Local impact

---

## Utility Commands (7 helpers)

- stub - Create stub
- research-scout - Research automation
- list-commands - Show all commands
- list-tools - Show all tools
- fix - Quick fix
- git-release - Release automation
- prompt-workflow - Prompt composition
