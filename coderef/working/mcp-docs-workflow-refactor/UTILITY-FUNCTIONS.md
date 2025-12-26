# Utility Functions in the MCP Ecosystem

Utility functions are cross-cutting helpers that support the 4 core coderef servers and 2 infrastructure servers.

---

## Category 1: CLI/UX Utilities (7 Commands)

### 1. `/stub [idea]`
**Purpose:** Create a new stub (idea) for future work

**Usage:**
```bash
/stub "Add dark mode toggle to settings"
```

**Output:**
```
Stubbed: STUB-054: add-dark-mode-toggle

Created:
├── coderef/working/add-dark-mode-toggle/
│   └── stub.json
└── Updated projects.md (Next STUB-ID: STUB-055)
```

**Utility for:** Orchestrator capturing ideas before they're planned

---

### 2. `/research-scout [task]`
**Purpose:** Research-focused agent for exploring feasibility and refining ideas

**Usage:**
```bash
/research-scout "Is it feasible to integrate Stripe payments with our current stack?"
```

**Output:**
```
Research Report:
├── Feasibility: Yes (99% confidence)
├── Effort Estimate: 16-20 hours
├── Integration Points: 3
├── Recommended Approach: Use Stripe SDK + webhook validation
├── Risks: PCI compliance validation
└── Similar Projects Found: 2 in archive
```

**Utility for:** Agents validating ideas before committing to plans

---

### 3. `/list-commands`
**Purpose:** Show all available slash commands

**Usage:**
```bash
/list-commands
```

**Output:**
```
Core Commands:
├── /stub - Create stub
├── /create-plan - Generate implementation plan
├── /execute-plan - Break plan into tasks
└── /update-task-status - Mark task complete

coderef-context Commands:
├── analyze-codebase - Deep code analysis
├── generate-task-context - Task-specific context
└── discover-standards - Extract UI/behavior patterns

...
```

**Utility for:** Agents discovering available tools

---

### 4. `/list-tools`
**Purpose:** Show all available MCP tools (more detailed than commands)

**Usage:**
```bash
/list-tools
```

**Output:**
```
Tools by Category:
├── coderef-context (9 tools)
│   ├── analyze-codebase
│   ├── generate-task-context
│   └── ...
├── coderef-workflow (24 tools)
│   ├── create-plan
│   ├── execute-plan
│   └── ...
...
```

**Utility for:** Agents understanding tool inventory

---

### 5. `/fix [error]`
**Purpose:** Quick fix handler for common errors

**Usage:**
```bash
/fix "context.json not found"
```

**Output:**
```
Error: context.json not found

Suggestions:
1. Run /gather-context to create context.json
2. Check file path: coderef/working/{feature}/context.json
3. If migrating, check coderef/archived for backup

Applied Fix:
✅ Created template context.json
```

**Utility for:** Agents recovering from common mistakes

---

### 6. `/git-release [version]`
**Purpose:** Automate release workflow (versioning, tags, changelog)

**Usage:**
```bash
/git-release 1.2.0
```

**Process:**
```
1. Bump version in package.json → 1.2.0
2. Run tests (must pass)
3. Create git tag v1.2.0
4. Update CHANGELOG.md
5. Commit: "chore: release v1.2.0"
6. Ready to push
```

**Output:**
```
✅ Release prepared: v1.2.0
├── Version updated
├── Tests passed (98% coverage)
├── Tag created
├── Changelog updated
└── Ready to git push
```

**Utility for:** Orchestrator managing releases

---

### 7. `/prompt-workflow [task]`
**Purpose:** Build complex prompts for handoff to agents

**Usage:**
```bash
/prompt-workflow "Create comprehensive planning guide"
```

**Output:**
```
Prompt Building Interface:
├── Select template (feature, refactor, fix, research)
├── Add context (project, requirements)
├── Select audience (persona agent, human agent)
├── Generate prompt
└── Copy to clipboard

Generated Prompt:
[Full handoff prompt ready for agent...]
```

**Utility for:** Orchestrator creating delegation prompts

---

## Category 2: coderef-context Internal Utilities

### Analysis Utilities

```typescript
// File: coderef-context/src/context/utilities.ts

// 1. Complexity Calculator
export function calculateComplexity(
  relatedFiles: string[],
  relatedFunctions: number,
  hasExternalDeps: boolean
): "low" | "medium" | "high"

// 2. Confidence Scorer
export function scoreConfidence(
  analysisDepth: number,
  patternMatches: number,
  codebaseSize: "small" | "medium" | "large"
): number // 0-1

// 3. Edge Case Detector
export function detectEdgeCases(
  functionCode: string,
  relatedCode: string[]
): EdgeCase[]

// 4. Pattern Matcher
export function findPatterns(
  codebase: AST,
  searchTerms: string[]
): Pattern[]

// 5. Example Extractor
export function extractExamples(
  relatedFiles: string[],
  maxExamples: number
): CodeExample[]
```

**Usage in Phase 2 (Task-Specific Context):**

```typescript
const context = {
  complexity: calculateComplexity(files, funcCount, hasDeps),
  confidence: scoreConfidence(analysisDepth, matches, size),
  edge_cases: detectEdgeCases(code, relatedCode),
  patterns: findPatterns(ast, searchTerms),
  examples: extractExamples(files, 3)
};
```

---

## Category 3: coderef-workflow Internal Utilities

### Planning Utilities

```typescript
// File: coderef-workflow/src/planner/utilities.ts

// 1. Requirement Parser
export function parseRequirements(
  description: string
): Requirement[]

// 2. Task Sequencer
export function sequenceTasks(
  tasks: Task[],
  dependencies: Dependency[]
): SequencedTask[]

// 3. Risk Assessor
export function assessRisk(
  task: Task,
  context: TaskContext
): RiskAssessment

// 4. Effort Estimator
export function estimateEffort(
  complexity: string,
  taskSize: string,
  teamSize: number
): {min: hours, max: hours}

// 5. Workorder Generator
export function generateWorkorderId(
  category: string
): string // WO-CATEGORY-001
```

**Usage in create-plan:**

```typescript
const requirements = parseRequirements(featureDesc);
const tasks = sequenceTasks(requirementTasks, deps);
const woId = generateWorkorderId("AUTH-SYSTEM");

tasks.forEach(task => {
  const risk = assessRisk(task, taskContext);
  const effort = estimateEffort(
    task.complexity,
    "medium",
    teamSize
  );

  task.risk = risk;
  task.effort = effort;
});
```

---

## Category 4: coderef-docs Internal Utilities

### Documentation Utilities

```typescript
// File: coderef-docs/src/generators/utilities.ts

// 1. TOC Generator
export function generateTableOfContents(
  markdown: string
): TableOfContents

// 2. Cross-Referencer
export function findCrossReferences(
  doc: string,
  allDocs: string[]
): CrossReference[]

// 3. Code Snippet Versioner
export function trackSnippetVersion(
  snippet: CodeExample,
  gitCommit: string
): VersionedSnippet

// 4. Completeness Scorer
export function scoreCompleteness(
  doc: string,
  requiredSections: string[]
): {score: number, missing: string[]}

// 5. Freshness Checker
export function checkFreshness(
  doc: string,
  codebase: AST
): {stale: boolean, issues: string[]}
```

**Usage in generate-foundation-docs:**

```typescript
// Generate README
const toc = generateTableOfContents(readmeMarkdown);
const refs = findCrossReferences(readmeMarkdown, allDocs);
const score = scoreCompleteness(readmeMarkdown, REQUIRED_SECTIONS);

if (score.score < 80) {
  console.warn(`README incomplete: missing ${score.missing}`);
}

// Check if outdated
const freshness = checkFreshness(readmeMarkdown, codebase);
if (freshness.stale) {
  markForReview(freshness.issues);
}
```

---

## Category 5: coderef-testing Internal Utilities

### Testing Utilities

```typescript
// File: coderef-testing/src/validators/utilities.ts

// 1. Test Pattern Analyzer
export function analyzeTestPatterns(
  testFiles: string[]
): TestPattern[]

// 2. Coverage Calculator
export function calculateCoverage(
  testResults: TestResult[]
): {statements: %, branches: %, lines: %}

// 3. Standards Validator
export function validateAgainstStandards(
  code: string,
  standards: Standard[]
): Violation[]

// 4. Test Case Generator
export function generateTestCases(
  functionSignature: string,
  context: TaskContext
): TestCase[]

// 5. Failure Analyzer
export function analyzeFailure(
  failingTest: Test,
  code: string
): {cause: string, fix: string}
```

**Usage in coderef-testing validate:**

```typescript
const patterns = analyzeTestPatterns(testDir);
const coverage = calculateCoverage(results);
const violations = validateAgainstStandards(code, standards);
const generated = generateTestCases(funcSignature, context);

if (coverage.statements < 80) {
  const missing = generateTestCases(func, context);
  console.log(`Generate ${missing.length} more tests`);
}

failingTests.forEach(test => {
  const analysis = analyzeFailure(test, code);
  console.log(`Fix: ${analysis.fix}`);
});
```

---

## Category 6: git-mcp Utilities

### Git Operations

```typescript
// File: git-mcp/src/utilities.ts

// 1. Branch Manager
export async function createWOBranch(
  workorderId: string
): Promise<string> // WO-FEATURE-XXX

// 2. Metrics Extractor
export async function extractMetrics(
  workorderId: string
): Promise<{
  lines_added: number,
  lines_deleted: number,
  commits: number,
  contributors: string[],
  time_elapsed: seconds
}>

// 3. Commit Analyzer
export async function analyzeCommits(
  workorderId: string
): Promise<Commit[]>

// 4. Forbidden Files Validator
export async function validateForbiddenFiles(
  workorderId: string,
  forbiddenFiles: string[]
): Promise<{valid: boolean, violations: string[]}>

// 5. Merge Orchestrator
export async function mergeWOBranch(
  workorderId: string
): Promise<MergeResult>

// 6. Tag Manager
export async function tagFeature(
  tag: string,
  message: string
): Promise<void>

// 7. Workorder Logger
export async function logWorkorder(
  workorderId: string,
  message: string
): Promise<void> // Appends to workorder-log.txt
```

**Usage in coderef-workflow:**

```typescript
// Create branch
const branch = await gitMcp.createWOBranch(woId);
console.log(`Created branch: ${branch}`);

// Track work
await gitMcp.logWorkorder(woId, "Assigned to @lloyd");

// Validate completion
const valid = await gitMcp.validateForbiddenFiles(woId, [
  "package.json",
  "public/index.html"
]);

if (!valid.valid) {
  throw new Error(`Forbidden files modified: ${valid.violations}`);
}

// Extract metrics
const metrics = await gitMcp.extractMetrics(woId);
// metrics = {
//   lines_added: 342,
//   lines_deleted: 87,
//   commits: 12,
//   contributors: ["alice", "bob"],
//   time_elapsed: 86400
// }

// Update deliverables
deliverables.loc = metrics.lines_added;
deliverables.commits = metrics.commits;
deliverables.time_spent = formatDuration(metrics.time_elapsed);

// Merge when complete
const result = await gitMcp.mergeWOBranch(woId);

// Tag release
await gitMcp.tagFeature("v1.2.0", "Release 1.2.0");
```

---

## Category 7: claude-filesystem-mcp Utilities

### Filesystem Operations

```typescript
// File: claude-filesystem-mcp/src/utilities.ts

// 1. JSON Reader
export async function readJson(
  path: string
): Promise<any>

// 2. JSON Writer
export async function writeJson(
  path: string,
  data: any
): Promise<void>

// 3. Directory Manager
export async function createDirectory(
  path: string
): Promise<void>

export async function moveDirectory(
  from: string,
  to: string
): Promise<void>

export async function deleteDirectory(
  path: string
): Promise<void>

// 4. File Lister
export async function listFiles(
  directory: string
): Promise<string[]>

// 5. Markdown Writer
export async function writeMarkdown(
  path: string,
  content: string
): Promise<void>

// 6. Archive Manager
export async function archiveFeature(
  featureDir: string
): Promise<void> // Move to archived/, update index

// 7. Index Manager
export async function updateIndex(
  indexPath: string,
  entry: any
): Promise<void>
```

**Usage across all servers:**

```typescript
// coderef-context
const existingContext = await filesystem.readJson('coderef/context.json');
await filesystem.writeJson('coderef/context.json', newContext);

// coderef-workflow
const plan = await filesystem.readJson('coderef/working/{feature}/plan.json');
await filesystem.writeJson('coderef/working/{feature}/communication.json', status);

// coderef-docs
await filesystem.writeMarkdown('coderef/foundation-docs/README.md', content);

// When archiving
await filesystem.archiveFeature('coderef/working/feature-name');
await filesystem.updateIndex('coderef/archived/index.json', {
  feature_name: "feature-name",
  completed_at: timestamp
});
```

---

## Category 8: Coderef Dashboard Utilities

### UI/Widget Utilities

```typescript
// File: coderef-dashboard/src/utils/

// 1. Data Fetcher
export async function fetchWorkorderStatus(
  workorderId: string
): Promise<WorkorderStatus>

// 2. Progress Calculator
export function calculateProgress(
  completedTasks: number,
  totalTasks: number
): ProgressPercentage

// 3. Status Formatter
export function formatStatus(
  status: string
): HumanReadable // "implementing" → "In Progress"

// 4. Timestamp Formatter
export function formatTimestamp(
  iso: string
): HumanReadable // "2025-12-23T19:30:00Z" → "2 hours ago"

// 5. Widget Data Transformer
export function transformToWidgetData(
  communicationJson: any
): WidgetData

// 6. Real-time Updater
export function setupWebsocketListener(
  workorderId: string,
  callback: (data) => void
): void
```

**Usage in widgets:**

```typescript
// WorkorderStatus widget
const status = await fetchWorkorderStatus(woId);
const progress = calculateProgress(status.completed, status.total);
const formatted = formatStatus(status.current_status);
const time = formatTimestamp(status.last_update);

return {
  title: `${woId}: ${formatted}`,
  progress: `${progress}%`,
  lastUpdate: time,
  agent: status.assigned_to
};
```

---

## Summary Table

| Category | Count | Purpose |
|----------|-------|---------|
| CLI/UX Utilities | 7 | User interaction (stub, research, list, fix, release, prompt) |
| coderef-context Utilities | 5 | Code analysis helpers (complexity, confidence, patterns, examples) |
| coderef-workflow Utilities | 5 | Planning helpers (parse, sequence, assess, estimate, generate) |
| coderef-docs Utilities | 5 | Doc generation helpers (TOC, references, versioning, completeness, freshness) |
| coderef-testing Utilities | 5 | Test helpers (patterns, coverage, validation, generation, analysis) |
| git-mcp Utilities | 7 | Git operations (branch, metrics, commits, validation, merge, tag, log) |
| claude-filesystem-mcp Utilities | 7 | File operations (read, write, directory, list, markdown, archive, index) |
| Dashboard Utilities | 6 | UI helpers (fetch, progress, format, transform, websocket) |
| **TOTAL** | **47** | Cross-cutting support for all systems |

---

## How Agents Use Utilities

### Example: Agent implementing a feature

```typescript
// 1. Agent uses CLI utility to list available tools
/list-commands

// 2. Orchestrator uses /stub to create idea
/stub "Add payment processing"

// 3. Agent uses /prompt-workflow to get handoff
/prompt-workflow "Feature delegation"

// 4. coderef-context uses internal utilities (complexity, examples)
const context = {
  complexity: calculateComplexity(...),
  examples: extractExamples(...)
};

// 5. coderef-workflow uses utilities (sequencing, estimation)
const tasks = sequenceTasks(requirements, deps);
const effort = estimateEffort(complexity, size, team);

// 6. Agent implements, coderef-workflow uses git utilities
const metrics = await gitMpc.extractMetrics(woId);
const valid = await gitMcp.validateForbiddenFiles(woId, forbiddenFiles);

// 7. coderef-docs uses utilities (completeness, freshness)
const completeness = scoreCompleteness(doc, required);

// 8. Dashboard uses utilities (fetch, format)
const status = await fetchWorkorderStatus(woId);
const widget = transformToWidgetData(communicationJson);

// 9. When done, /git-release for versioning
/git-release 1.2.0

// 10. Archive with filesystem utility
await filesystem.archiveFeature(featurePath);
```

**Result:** Seamless workflow from idea to deployment, with utilities handling details at each step.
