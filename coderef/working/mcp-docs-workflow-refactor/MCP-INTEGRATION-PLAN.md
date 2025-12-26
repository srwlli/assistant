# MCP Integration Plan

## Integration Scope

Integrate **git-mcp** and **claude-filesystem-mcp** with the 4 coderef servers:
- coderef-context
- coderef-workflow
- coderef-docs
- coderef-testing

---

## Integration Requirements by Server

### 1. coderef-context Integration

**What it needs from git-mcp:**
```typescript
// Track when analysis runs
await git.tagFeature(`coderef-context-analysis-${timestamp}`);

// Extract metadata about code age, activity
const commits = await git.queryWorkorderCommits(workorderId);
const contributors = await git.extractContributors(workorderId);

// Include in context output
context.metadata = {
  analyzed_at: timestamp,
  code_age: calculateAge(commits),
  active_contributors: contributors,
  last_modified: commits[0].date
};
```

**What it needs from claude-filesystem-mcp:**
```typescript
// Write generated context files
await filesystem.writeJson('coderef/context.json', codebaseContext);
await filesystem.writeJson('coderef/task-context.json', taskContext);

// Read existing standards
const standards = await filesystem.readJson('coderef/standards/UI-STANDARDS.md');

// Cache analysis results
await filesystem.writeJson('coderef/.analysis-cache.json', cache);
```

---

### 2. coderef-workflow Integration

**What it needs from git-mcp:**
```typescript
// Create workorder branch
await git.createWOBranch(`WO-FEATURE-XXX`);

// Track task assignments
await git.logWorkorder(workorderId, `Assigned to agent: @lloyd`);

// Validate completion
const diffs = await git.diffForbiddenFiles(workorderId);
if (diffs.length > 0) {
  throw new Error('Forbidden files were modified');
}

// Extract metrics for deliverables
const metrics = {
  lines_changed: await git.countLinesChanged(workorderId),
  commits: await git.countCommits(workorderId),
  contributors: await git.extractContributors(workorderId),
  time_elapsed: await git.calculateTimeElapsed(workorderId)
};

// Merge when complete
await git.mergeWOBranch(workorderId);

// Tag release
await git.tagFeature(`v${version}`);
```

**What it needs from claude-filesystem-mcp:**
```typescript
// Read requirements
const context = await filesystem.readJson('coderef/working/{feature}/context.json');
const analysis = await filesystem.readJson('coderef/working/{feature}/analysis.json');

// Write plan
await filesystem.writeJson('coderef/working/{feature}/plan.json', plan);

// Track execution
await filesystem.writeJson('coderef/working/{feature}/communication.json', {
  status: 'implementing',
  current_task: taskId,
  progress: 0.45,
  last_update: timestamp
});

// Generate handoff
await filesystem.writeJson('coderef/working/{feature}/claude.md', handoffPrompt);

// Update on completion
await filesystem.writeJson('coderef/working/{feature}/DELIVERABLES.md', deliverables);

// Archive when done
await filesystem.moveDirectory(
  'coderef/working/{feature}',
  'coderef/archived/{feature}'
);

// Update archive index
const archiveIndex = await filesystem.readJson('coderef/archived/index.json');
archiveIndex.features.push({feature_name, completed_at: timestamp});
await filesystem.writeJson('coderef/archived/index.json', archiveIndex);
```

---

### 3. coderef-docs Integration

**What it needs from git-mcp:**
```typescript
// Track documentation changes
await git.logWorkorder(workorderId, `Updated documentation`);

// Link docs to code versions
const codeVersion = await git.queryWorkorderCommits(workorderId);
docs.metadata.code_version = codeVersion[0].hash;

// Include changelog entries
const changes = await git.queryWorkorderCommits(workorderId);
docs.changelog = changes.map(c => ({
  commit: c.hash,
  message: c.message,
  author: c.author,
  date: c.date
}));
```

**What it needs from claude-filesystem-mcp:**
```typescript
// Write generated docs
await filesystem.writeJson('coderef/foundation-docs/README.md', readme);
await filesystem.writeJson('coderef/foundation-docs/ARCHITECTURE.md', architecture);
await filesystem.writeJson('coderef/foundation-docs/API.md', api);
await filesystem.writeJson('coderef/foundation-docs/SCHEMA.md', schema);

// Write standards
await filesystem.writeJson('coderef/standards/UI-STANDARDS.md', uiStandards);
await filesystem.writeJson('coderef/standards/BEHAVIOR-STANDARDS.md', behaviorStandards);
await filesystem.writeJson('coderef/standards/UX-PATTERNS.md', uxPatterns);

// Update changelog
const changelog = await filesystem.readJson('CHANGELOG.json');
changelog.push({version, changes, timestamp});
await filesystem.writeJson('CHANGELOG.json', changelog);
```

---

### 4. coderef-testing Integration

**What it needs from git-mcp:**
```typescript
// Get test patterns from commit history
const testCommits = await git.queryWorkorderCommits(workorderId);
const testPatterns = extractTestPatterns(testCommits);

// Run tests on specific commit
await git.checkoutCommit(testCommits[0].hash);

// Validate code after tests pass
const coverage = await runTests();
await git.logWorkorder(workorderId, `Tests: ${coverage.percentage}% coverage`);

// Only merge if tests pass
if (coverage.percentage < 80) {
  throw new Error('Insufficient test coverage');
}
```

**What it needs from claude-filesystem-mcp:**
```typescript
// Read test configuration
const testConfig = await filesystem.readJson('coderef/testing-config.json');

// Write test report
await filesystem.writeJson('coderef/test-results.json', {
  workorder_id: workorderId,
  coverage: coverage,
  results: testResults,
  timestamp: Date.now()
});

// Track test standards
await filesystem.writeJson('coderef/testing-standards.md', testStandards);

// Update DELIVERABLES with test metrics
const deliverables = await filesystem.readJson('coderef/working/{feature}/DELIVERABLES.md');
deliverables.test_coverage = coverage.percentage;
deliverables.test_status = 'passed';
await filesystem.writeJson('coderef/working/{feature}/DELIVERABLES.md', deliverables);
```

---

## Integration Architecture

### Dependency Graph

```
┌──────────────────────────────────────────────────────┐
│              coderef Dashboard                        │
│         (reads all files + git history)              │
└──────────────────────────────────────────────────────┘
         │           │           │           │
         ↓           ↓           ↓           ↓
    ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
    │coderef- │ │coderef-  │ │coderef-  │ │coderef-  │
    │context  │ │workflow  │ │docs      │ │testing   │
    └─────────┘ └──────────┘ └──────────┘ └──────────┘
         │           │           │           │
         └───────────┴───────────┴───────────┘
                     │           │
                     ↓           ↓
            ┌───────────────────────────┐
            │   git-mcp                 │
            │ (workorder tracking,      │
            │  metrics, branches)       │
            └───────────────────────────┘

            ┌───────────────────────────┐
            │ claude-filesystem-mcp     │
            │ (context.json, plan.json, │
            │  communication.json)      │
            └───────────────────────────┘
```

### File Structure

```
project/
├── coderef/
│   ├── context.json              (written by coderef-context)
│   ├── task-context.json         (written by coderef-context)
│   ├── .analysis-cache.json      (written by coderef-context)
│   ├── standards/
│   │   ├── UI-STANDARDS.md       (written by coderef-context)
│   │   ├── BEHAVIOR-STANDARDS.md (written by coderef-context)
│   │   └── UX-PATTERNS.md        (written by coderef-context)
│   ├── foundation-docs/
│   │   ├── README.md             (written by coderef-docs)
│   │   ├── ARCHITECTURE.md       (written by coderef-docs)
│   │   ├── API.md                (written by coderef-docs)
│   │   └── SCHEMA.md             (written by coderef-docs)
│   ├── test-results.json         (written by coderef-testing)
│   ├── testing-standards.md      (written by coderef-testing)
│   ├── testing-config.json       (read by coderef-testing)
│   ├── working/
│   │   └── {feature}/
│   │       ├── context.json      (created by orchestrator, read by agent)
│   │       ├── analysis.json     (created by coderef-context)
│   │       ├── plan.json         (written by coderef-workflow)
│   │       ├── communication.json (written by coderef-workflow)
│   │       ├── DELIVERABLES.md   (written by coderef-workflow, updated by git-mcp metrics)
│   │       └── claude.md         (written by coderef-workflow)
│   ├── archived/
│   │   ├── {completed-feature}/
│   │   │   └── (all of above moved here)
│   │   └── index.json            (maintained by coderef-workflow + claude-filesystem-mcp)
│   ├── workorder-log.txt         (appended by git-mcp)
│   └── .orchestrator-state.json  (metadata)
└── .git/
    └── (branches, commits, tags managed by git-mcp)
```

---

## Integration Checklist

### Phase 1: coderef-context Integration
- [ ] coderef-context calls git-mcp to get commit metadata
- [ ] coderef-context calls claude-filesystem-mcp to write context.json
- [ ] coderef-context calls claude-filesystem-mcp to read existing standards
- [ ] Test: `coderef-context analyze` writes to filesystem and references git

### Phase 2: coderef-workflow Integration
- [ ] coderef-workflow calls git-mcp to create WO branch
- [ ] coderef-workflow calls claude-filesystem-mcp to read context.json
- [ ] coderef-workflow calls claude-filesystem-mcp to write plan.json
- [ ] coderef-workflow calls claude-filesystem-mcp to write communication.json
- [ ] Test: `coderef-workflow create-plan` uses context and tracks in git

### Phase 3: coderef-docs Integration
- [ ] coderef-docs calls git-mcp to get code metadata
- [ ] coderef-docs calls claude-filesystem-mcp to write foundation docs
- [ ] coderef-docs calls claude-filesystem-mcp to write standards
- [ ] Test: `coderef-docs generate` links docs to code versions

### Phase 4: coderef-testing Integration
- [ ] coderef-testing calls git-mcp to extract test patterns
- [ ] coderef-testing calls claude-filesystem-mcp to read test config
- [ ] coderef-testing calls claude-filesystem-mcp to write test results
- [ ] Test: `coderef-testing validate` reports coverage + standards compliance

### Phase 5: End-to-End
- [ ] All 4 servers call git-mcp and claude-filesystem-mcp correctly
- [ ] Dashboard reads all filesystem outputs + git history
- [ ] Complete workflow: context → workflow → docs + testing → archive
- [ ] All metrics captured in DELIVERABLES.md

---

## Workorder Suggestion

**WO-MCP-INTEGRATION-LAYER-001**

**Scope:**
- Integrate git-mcp with all 4 coderef servers
- Integrate claude-filesystem-mcp with all 4 coderef servers
- Wire dashboard to read integrated data
- End-to-end testing

**Timeline:** 1-2 weeks (parallel with other workorders)

**Success Criteria:**
- All 4 servers successfully call git-mcp and claude-filesystem-mcp
- Dashboard displays real data from git + filesystem
- Complete workflow test end-to-end
