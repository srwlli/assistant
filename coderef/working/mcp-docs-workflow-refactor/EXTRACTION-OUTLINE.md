# Extraction & Integration Outline

## Part 1: What Gets Extracted (24 Tools from docs-mcp)

```
docs-mcp (currently 34 tools)
├── 10 pure docs tools → STAY in coderef-docs
│   ├── generate-foundation-docs
│   ├── generate-individual-doc
│   ├── establish-standards
│   ├── audit-codebase
│   ├── check-consistency
│   ├── generate-quickref
│   ├── generate-user-guide
│   ├── generate-my-guide
│   ├── list-templates
│   └── get-template
│
└── 24 workorder tools → MOVE to coderef-workflow
    ├── Planning (gather-context, analyze-for-planning, create-plan, validate-plan)
    ├── Execution (execute-plan, update-task-status, track-agent-status)
    ├── Coordination (generate-agent-communication, assign-agent-task, verify-agent-completion)
    ├── Tracking (generate-deliverables, update-deliverables, log-workorder, get-workorder-log)
    ├── Changelog (add-changelog-entry, get-changelog, update-changelog, update-docs)
    ├── Auditing (audit-plans, features-inventory, archive-feature)
    └── Handoff (generate-handoff-context, aggregate-agent-deliverables)
```

---

## Part 2: New Structure After Extraction

```
C:\Users\willh\Desktop\MCLVI\

├── coderef-context/
│   ├── src/
│   │   ├── cli.ts
│   │   ├── context/
│   │   ├── analysis/
│   │   ├── formatters/
│   │   └── commands/
│   └── package.json
│
├── coderef-workflow/  (NEW - extracted from docs-mcp)
│   ├── src/
│   │   ├── cli.ts
│   │   ├── planner/
│   │   │   ├── plan-generator.ts
│   │   │   ├── context-gatherer.ts
│   │   │   └── plan-validator.ts
│   │   ├── executor/
│   │   │   ├── executor.ts
│   │   │   └── task-tracker.ts
│   │   ├── coordinator/
│   │   │   ├── agent-communicator.ts
│   │   │   ├── agent-assigner.ts
│   │   │   └── completion-verifier.ts
│   │   ├── tracking/
│   │   │   ├── workorder-logger.ts
│   │   │   ├── deliverables-tracker.ts
│   │   │   └── changelog-manager.ts
│   │   ├── formatters/
│   │   │   └── handoff-generator.ts
│   │   ├── types/
│   │   │   └── workflow-types.ts
│   │   └── commands/
│   │       ├── create-plan.ts
│   │       ├── execute-plan.ts
│   │       ├── track-status.ts
│   │       └── ... (20 more command handlers)
│   └── package.json
│
├── coderef-docs/ (STAYS - docs-mcp simplified)
│   ├── src/
│   │   ├── cli.ts
│   │   ├── generators/
│   │   ├── standards/
│   │   ├── audit/
│   │   └── commands/
│   └── package.json
│
└── coderef-testing/ (NEW - to build)
    ├── src/
    │   ├── cli.ts
    │   ├── generators/
    │   ├── validators/
    │   └── commands/
    └── package.json
```

---

## Part 3: Integration into coderef-context

**The key insight:** coderef-context doesn't absorb workflow. Instead:

```
coderef-context (PURE CODE ANALYSIS)
├── Scans code
├── Analyzes dependencies
├── Generates context.json
├── Generates task-context.json
└── Outputs structured context
    ↓ feeds into

coderef-workflow (ORCHESTRATION)
├── Receives context from coderef-context
├── Uses context to generate plans
├── Assigns tasks to agents
├── Tracks progress
└── Orchestrates execution
    ↓ references standards from

coderef-docs (DOCUMENTATION)
├── Generates README, ARCHITECTURE
├── Publishes auto-discovered standards
└── Provides reference material
    ↓ validates with

coderef-testing (TEST VALIDATION)
├── Extracts test patterns from code
├── Generates test cases
├── Validates code quality
└── Reports coverage
```

They're separate, not nested. coderef-context stays focused on analysis.

---

## Part 4: Data Flow (How They Talk)

```
Agent creates workorder
  ↓
coderef-workflow: gather-context
  (collects feature requirements)
  ↓
coderef-context: analyze-for-planning
  (scans codebase, returns context)
  ↓
coderef-workflow: create-plan
  (uses context from coderef-context to plan)
  ↓
coderef-workflow: execute-plan
  (breaks into tasks)
  ↓
Each task contains:
  - Context from coderef-context
  - Standards from coderef-docs
  - Test patterns from coderef-testing
  ↓
Agents implement
  ↓
coderef-testing: validate
  (tests code)
  ↓
coderef-workflow: track-status
  (marks complete)
  ↓
coderef-docs: update-changelog
  (records what changed)
```

---

## Part 5: File Mapping (What Moves Where)

### FROM docs-mcp → TO coderef-workflow

```
docs-mcp/src/mcp/tools/          coderef-workflow/src/commands/
├── gather-context.ts            ├── gather-context.ts
├── analyze-project.ts           ├── analyze-for-planning.ts
├── create-plan.ts               ├── create-plan.ts
├── validate-plan.ts             ├── validate-plan.ts
├── execute-plan.ts              ├── execute-plan.ts
├── update-task-status.ts        ├── update-task-status.ts
├── track-agent-status.ts        ├── track-agent-status.ts
├── generate-communication.ts    ├── generate-agent-communication.ts
├── assign-agent-task.ts         ├── assign-agent-task.ts
├── verify-agent-completion.ts   ├── verify-agent-completion.ts
├── generate-deliverables.ts     ├── generate-deliverables.ts
├── update-deliverables.ts       ├── update-deliverables.ts
├── generate-handoff-context.ts  ├── generate-handoff-context.ts
├── log-workorder.ts             ├── log-workorder.ts
├── get-workorder-log.ts         ├── get-workorder-log.ts
├── add-changelog-entry.ts       ├── add-changelog-entry.ts
├── get-changelog.ts             ├── get-changelog.ts
├── update-changelog.ts          ├── update-changelog.ts
├── update-docs.ts               ├── update-docs.ts
├── audit-plans.ts               ├── audit-plans.ts
├── features-inventory.ts        ├── features-inventory.ts
├── archive-feature.ts           ├── archive-feature.ts
├── aggregate-deliverables.ts    ├── aggregate-deliverables.ts
├── get-planning-template.ts     └── get-planning-template.ts
└── generate-handoff-context.ts
```

### STAY IN docs-mcp → coderef-docs

```
coderef-docs/src/commands/
├── generate-foundation-docs.ts
├── generate-individual-doc.ts
├── establish-standards.ts
├── audit-codebase.ts
├── check-consistency.ts
├── generate-quickref.ts
├── generate-user-guide.ts
├── generate-my-guide.ts
├── list-templates.ts
└── get-template.ts
```

---

## Part 6: How coderef-context Integrates with coderef-workflow

### coderef-context API (exported functions)

```typescript
// coderef-context/src/index.ts (new exports for workflow)

export {
  // General context
  generateCodebaseContext,

  // Task-specific context
  generateTaskContext,

  // Analysis
  analyzeForPlanning,
  extractComplexity,
  extractGotchas,
  extractTestPatterns,
  extractCodeExamples,

  // Utilities
  discoverStandards,
  analyzeImpact,
  queryCode
}
```

### coderef-workflow uses these

```typescript
// coderef-workflow/src/planner/plan-generator.ts

import {
  generateTaskContext,
  analyzeForPlanning,
  discoverStandards
} from '@coderef/context';

async function createPlan(feature: FeatureDescription) {
  // Step 1: Analyze codebase
  const analysis = await analyzeForPlanning(sourceDir);

  // Step 2: Discover standards from code
  const standards = await discoverStandards(sourceDir);

  // Step 3: For each planned task, generate task-specific context
  const tasks = feature.requirements.map(async (requirement) => {
    const taskContext = await generateTaskContext(
      sourceDir,
      requirement.description
    );

    return {
      requirement,
      context: taskContext,
      standards: standards
    };
  });

  // Step 4: Generate plan.json
  return generatePlanJson(tasks, analysis);
}
```

---

## Part 7: coderef-context Enhancements (Six Phases)

Phase 1-6 all happen in `coderef-context/src/context/`

- **Phase 1:** complexity-scorer.ts
- **Phase 2:** task-context-generator.ts
- **Phase 3:** edge-case-detector.ts
- **Phase 4:** test-pattern-analyzer.ts
- **Phase 5:** example-extractor.ts
- **Phase 6:** agentic-formatter.ts

Each exports functions that coderef-workflow calls

```typescript
// Example: Phase 2 (Task-Specific Context)
export async function generateTaskContext(
  sourceDir: string,
  taskDescription: string
): Promise<TaskContextJson> {
  // Find related code
  const relatedFunctions = await findRelatedCode(taskDescription);

  // Calculate complexity
  const complexity = await scoreComplexity(relatedFunctions);

  // Assess risk
  const risk = await assessRisk(relatedFunctions);

  // Extract examples
  const examples = await extractExamples(relatedFunctions);

  // Detect gotchas
  const gotchas = await detectGotchas(relatedFunctions);

  return {
    task: taskDescription,
    related_functions: relatedFunctions,
    complexity_estimate: complexity,
    risk_level: risk,
    examples: examples,
    gotchas: gotchas,
    confidence: 0.92
  };
}
```

---

## Part 8: Integration Points (Concrete)

### When workflow calls context:

```
coderef-workflow/src/commands/create-plan.ts
  ↓
calls: analyzeForPlanning() from coderef-context
  ↓
returns: analysis.json (what exists in codebase)
  ↓
uses to: inform plan.json structure
```

```
coderef-workflow/src/commands/execute-plan.ts
  ↓
for each task:
  calls: generateTaskContext() from coderef-context
  ↓
  returns: task-context.json (effort, risk, examples)
  ↓
  embeds in: task description
  ↓
  agents read and implement
```

---

## Part 9: Build Sequence

### Week 1: Extraction
- **Day 1-2:** Set up coderef-workflow package
- **Day 3-4:** Move 24 tools from docs-mcp to coderef-workflow
- **Day 5:** Test imports/exports, fix dependencies

### Week 2: Enhancement
- **Day 1:** Phase 1 (complexity-scorer) in coderef-context
- **Day 2:** Phase 2 (task-context-generator) in coderef-context
- **Day 3:** Phase 3 (edge-case-detector) in coderef-context
- **Day 4:** Phase 4 (test-pattern-analyzer) in coderef-context
- **Day 5:** Phase 5 (example-extractor) in coderef-context

### Week 3: Integration
- **Day 1:** Phase 6 (agentic-formatter) in coderef-context
- **Day 2-3:** Wire coderef-workflow to call coderef-context APIs
- **Day 4-5:** Test end-to-end (create plan → execute → embed context)

---

## Summary

**coderef-context stays pure analysis:**
- Scans code
- Analyzes patterns
- Generates context.json, task-context.json
- Outputs agentic-formatted JSON

**coderef-workflow uses that context:**
- Calls coderef-context functions
- Receives analysis + context
- Creates plans embedding the context
- Orchestrates execution

They're separate tools that talk via function calls, not nested.
