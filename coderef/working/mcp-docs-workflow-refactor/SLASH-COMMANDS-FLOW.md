# Slash Commands: Flow & Sequence

| Command                   | Flow Steps | Output | Status |
|---------------------------|---------|--------|--------|
| /create-workorder | 1. Get feature name<br>2. Gather context (Q&A)<br>3. Generate foundation docs<br>4. Analyze project<br>5. Create plan<br>6. Multi-agent decision<br>7. Validate plan (auto-fix loop, max 3)<br>8. Output summary<br>9. Commit & push | context.json<br>analysis.json<br>plan.json<br>DELIVERABLES.md<br>communication.json (if multi-agent) | ✅ Complete |
| /create-plan | 1. Load context.json (assumes exists)<br>2. Load analysis.json (assumes exists)<br>3. Synthesize with template<br>4. Generate plan.json<br>5. Validate<br>6. Commit & push | plan.json<br>DELIVERABLES.md | ✅ Complete |
| /execute-plan | 1. Read plan.json<br>2. Extract tasks from section 5 & 9<br>3. Convert to TodoWrite format<br>4. Generate task list display | TodoWrite list<br>execution-log.json | ✅ Complete |
| /gather-context | 1. Interactive Q&A (goal, description)<br>2. Multi-select requirements<br>3. Gather out-of-scope items<br>4. Gather constraints<br>5. Save context.json | context.json | ✅ Complete |
| /analyze-for-planning | 1. Scan foundation docs<br>2. Scan coding standards<br>3. Find reference components<br>4. Identify patterns<br>5. Detect tech stack<br>6. Identify gaps/risks<br>7. Save analysis.json | analysis.json | ✅ Complete |
| /validate-plan | 1. Load plan.json<br>2. Validate against schema<br>3. Check for issues (critical/major/minor)<br>4. Score 0-100<br>5. Output report | Validation report<br>Score | ✅ Complete |
| /update-task-status | 1. Read plan.json<br>2. Find task by ID<br>3. Update status (pending/in_progress/completed/blocked)<br>4. Add timestamp & notes<br>5. Write plan.json | Updated plan.json | ✅ Complete |
| /update-deliverables | 1. Query git history (feature-related commits)<br>2. Count LOC (added/deleted)<br>3. Sum commits<br>4. Calculate time (first → last)<br>5. Merge contributors<br>6. Update DELIVERABLES.md | Updated DELIVERABLES.md | ✅ Complete |
| /archive-feature | 1. Check DELIVERABLES.md status<br>2. Prompt if incomplete<br>3. Move folder to archived/<br>4. Update archive index | Folder moved<br>index.json updated | ✅ Complete |
| /log-workorder | 1. Create WO-ID entry<br>2. Append to workorder-log.txt<br>3. Include timestamp | Line added to log | ✅ Complete |
| /update-docs | 1. Read plan.json<br>2. Extract version, changes<br>3. Update README.md version<br>4. Update CLAUDE.md history<br>5. Update CHANGELOG.json | README.md<br>CLAUDE.md<br>CHANGELOG.json | ✅ Complete |
| /establish-standards | 1. Scan codebase<br>2. Extract UI patterns<br>3. Extract behavior patterns<br>4. Extract UX patterns<br>5. Generate 4 markdown files | UI-STANDARDS.md<br>BEHAVIOR-STANDARDS.md<br>UX-PATTERNS.md | ✅ Complete |
| /audit-codebase | 1. Load standards from coderef/standards/<br>2. Scan all source files<br>3. Detect violations<br>4. Score compliance<br>5. Generate report | Audit report<br>Violations list | ✅ Complete |
| /check-consistency | 1. Auto-detect git changes<br>2. Scan only modified files<br>3. Check against standards<br>4. Report violations<br>5. Return exit code | Consistency report<br>Pass/fail status | ✅ Complete |
| /assign-agent-task | 1. Read plan.json<br>2. Read communication.json<br>3. Select phase/task<br>4. Assign to agent (1-10)<br>5. Update communication.json | Updated communication.json | ✅ Complete |
| /verify-agent-completion | 1. Read communication.json<br>2. Check git diff<br>3. Verify forbidden files unchanged<br>4. Validate success criteria<br>5. Update agent status | Agent marked VERIFIED | ✅ Complete |
| /track-agent-status | 1. Read all communication.json files<br>2. Extract agent statuses<br>3. Calculate progress %<br>4. Display dashboard | Status dashboard | ✅ Complete |
| /coderef-foundation-docs | 1. Deep extract existing ARCHITECTURE.md<br>2. Deep extract SCHEMA.md<br>3. Auto-detect API endpoints<br>4. Auto-detect database schema<br>5. Analyze git activity<br>6. Generate COMPONENTS.md (UI only) | ARCHITECTURE.md<br>SCHEMA.md<br>COMPONENTS.md<br>project-context.json | ✅ Complete |
| /generate-foundation-docs | 1. Generate README.md<br>2. Generate ARCHITECTURE.md<br>3. Generate API.md<br>4. Generate COMPONENTS.md<br>5. Generate SCHEMA.md | 5 markdown files | ✅ Complete |
| /audit-plans | 1. Scan coderef/working/<br>2. Validate all plan.json files<br>3. Check for stale plans<br>4. Extract progress status<br>5. Health score 0-100 | Plan health report | ✅ Complete |

---

## Key Observations

### Phase 1: Context (Gathering)

- `/gather-context` - Manual Q&A for requirements
- **Output:** context.json

### Phase 2: Planning (Strategy)

- `/create-workorder` - Full orchestration (context → analysis → plan → validate)
- `/create-plan` - Just the plan (assumes context/analysis exist)
- `/analyze-for-planning` - Auto-populate prep section
- `/coderef-foundation-docs` - Generate foundation docs
- `/validate-plan` - Quality gate
- **Output:** plan.json, DELIVERABLES.md, analysis.json

### Phase 3: Execution (Implementation)

- `/execute-plan` - Generate TodoWrite task list
- `/update-task-status` - Agent marks task complete
- `/track-agent-status` - Monitor progress
- `/update-deliverables` - Capture git metrics
- `/update-docs` - Update changelog/version
- `/archive-feature` - Move to archived/
- **Output:** Code + metrics + changelog

---

## Command Distribution by Phase

**Phase 1 (Gathering):** 1 command
- gather-context

**Phase 2 (Planning):** 6 commands
- create-workorder (full orchestrator)
- create-plan
- analyze-for-planning
- coderef-foundation-docs
- validate-plan
- establish-standards (prep step)

**Phase 3 (Execution):** 8 commands
- execute-plan
- update-task-status
- track-agent-status
- update-deliverables
- update-docs
- archive-feature
- log-workorder
- verify-agent-completion

**Utilities:** 5 commands
- audit-codebase
- check-consistency
- assign-agent-task
- audit-plans
- generate-foundation-docs

---

## Separation Insight

**Currently in docs-mcp:**
- Phase 1: 1 command (gather-context)
- Phase 2: 6 commands (create-workorder, create-plan, analyze-for-planning, etc)
- Phase 3: 8 commands (execute-plan, update-task-status, etc)
- Utilities: 5 commands (audit-*, check-*, etc)

**Should be in coderef-workflow:**
- All of Phase 2 (planning orchestration)
- All of Phase 3 (execution tracking)
- All Phase 3 utilities (assign, verify, track)

**Should stay in docs-mcp:**
- Phase 1 (context gathering)
- Foundation docs generation
- Standards establishment
- Audit/compliance commands
