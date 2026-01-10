---
name: coderef-scanner
description: Analyzes codebase structure using .coderef/index.json and .coderef/graph.json from dashboard's coderef-core integration. Reports on functions, classes, components, dependencies, complexity, and architecture patterns. NO CLI tools - uses pre-generated coderef data only.
allowed-tools: Read, Grep, Glob
model: haiku
context: fork
---

# CodeRef Scanner Skill

Analyzes codebases using pre-generated coderef data from the dashboard's coderef-core integration.

## Core Principle

**DO NOT use CLI tools** - No `coderef scan`, `coderef analyze`, or any command-line executables.

**DO use dashboard integration** - Read from `.coderef/index.json` and `.coderef/graph.json` directly.

---

## Workflow

### 1. Check for CodeRef Data

```bash
# Verify index exists
Read: .coderef/index.json

# Verify graph exists (optional)
Read: .coderef/graph.json
```

**If files don't exist:** Inform user that coderef data needs to be generated via dashboard first.

### 2. Parse Index Data

Read `.coderef/index.json` and extract:

**Functions:**
- Name, file location, line number
- Parameters and return type
- Complexity score (if available)

**Classes:**
- Name, file location, line number
- Methods and properties
- Inheritance relationships

**Components:** (for UI frameworks)
- Component name and type
- Props and state
- File location

**Files:**
- File paths
- Language/type
- Size and line count

### 3. Parse Dependency Graph (if available)

Read `.coderef/graph.json` and extract:

**Dependencies:**
- Module imports/exports
- Function call relationships
- Class inheritance trees
- Component hierarchies

**Metrics:**
- Cyclomatic complexity
- Dependency depth
- Coupling scores
- Dead code detection

### 4. Generate Analysis Report

Provide structured analysis in requested format:

**Summary Stats:**
```
Total Functions: X
Total Classes: Y
Total Components: Z
Files Scanned: N
Languages: [list]
```

**Hot Spots:**
- Most complex files (by complexity score)
- Most connected modules (by dependencies)
- Largest files (by LOC)
- Deeply nested functions

**Architecture Patterns:**
- Detected design patterns
- Layering violations
- Circular dependencies
- Code smells

---

## Supported Queries

Auto-triggers on these user requests:

**Code Inventory:**
- "How many functions/classes/components are in this project?"
- "List all API endpoints"
- "Show me all React components"
- "What files are in the src/ directory?"

**Complexity Analysis:**
- "Which files are most complex?"
- "Find the most complicated functions"
- "Show cyclomatic complexity"
- "Identify refactoring candidates"

**Dependency Analysis:**
- "What depends on this module?"
- "Show module dependencies"
- "Find circular dependencies"
- "Identify tightly coupled code"

**Architecture Review:**
- "Describe the project structure"
- "What's the architecture pattern?"
- "Find layering violations"
- "Show component hierarchy"

---

## Output Formats

### JSON Format
```json
{
  "summary": {
    "functions": 1523,
    "classes": 342,
    "components": 89,
    "files": 456
  },
  "hot_spots": [
    {
      "file": "src/utils/processor.ts",
      "complexity": 45,
      "functions": 23,
      "lines": 892
    }
  ],
  "dependencies": {
    "circular": ["moduleA -> moduleB -> moduleA"],
    "depth": {"max": 8, "avg": 3.2}
  }
}
```

### Markdown Format
```markdown
# Codebase Analysis Report

## Summary
- **Functions:** 1,523
- **Classes:** 342
- **Components:** 89
- **Files:** 456

## Hot Spots
1. `src/utils/processor.ts` (complexity: 45)
2. `src/services/api.ts` (complexity: 38)

## Recommendations
- Refactor processor.ts (too complex)
- Break up large classes
```

### Table Format
```
| File                      | Functions | Complexity | LOC  |
|---------------------------|-----------|------------|------|
| src/utils/processor.ts    | 23        | 45         | 892  |
| src/services/api.ts       | 18        | 38         | 654  |
```

---

## Index Schema Reference

### .coderef/index.json Structure

```json
{
  "version": "1.0.0",
  "generated": "2025-01-09T12:00:00Z",
  "project": {
    "name": "project-name",
    "path": "/absolute/path"
  },
  "functions": [
    {
      "name": "functionName",
      "file": "src/utils/helper.ts",
      "line": 42,
      "params": ["arg1", "arg2"],
      "return": "string",
      "complexity": 5,
      "type": "function"
    }
  ],
  "classes": [
    {
      "name": "ClassName",
      "file": "src/models/User.ts",
      "line": 10,
      "methods": ["constructor", "save", "delete"],
      "properties": ["id", "name", "email"],
      "extends": "BaseModel"
    }
  ],
  "components": [
    {
      "name": "UserCard",
      "file": "src/components/UserCard.tsx",
      "line": 8,
      "props": ["user", "onEdit"],
      "state": ["isEditing"],
      "type": "react"
    }
  ],
  "files": [
    {
      "path": "src/index.ts",
      "language": "typescript",
      "lines": 150,
      "size": 4096
    }
  ]
}
```

### .coderef/graph.json Structure

```json
{
  "version": "1.0.0",
  "nodes": [
    {
      "id": "src/utils/helper.ts",
      "type": "module",
      "exports": ["helperFunction", "HelperClass"]
    }
  ],
  "edges": [
    {
      "from": "src/index.ts",
      "to": "src/utils/helper.ts",
      "type": "import",
      "symbols": ["helperFunction"]
    }
  ],
  "metrics": {
    "complexity": {
      "src/utils/helper.ts": 12,
      "src/index.ts": 8
    },
    "coupling": {
      "src/utils/helper.ts": 5
    }
  }
}
```

---

## Example Usage

### Example 1: Quick Stats

**User:** "How many functions are in this project?"

**Skill Response:**
```
Reading .coderef/index.json...

Found 1,523 functions across 456 files:
- TypeScript: 1,234 functions
- JavaScript: 289 functions

Top 3 files by function count:
1. src/utils/processor.ts (23 functions)
2. src/services/api.ts (18 functions)
3. src/models/User.ts (15 functions)
```

### Example 2: Complexity Analysis

**User:** "Which files are most complex?"

**Skill Response:**
```
Reading .coderef/index.json and .coderef/graph.json...

Top 5 Most Complex Files:

1. src/utils/processor.ts
   - Complexity: 45
   - Functions: 23
   - Recommendation: Split into smaller modules

2. src/services/api.ts
   - Complexity: 38
   - Functions: 18
   - Recommendation: Extract request handlers

3. src/components/Dashboard.tsx
   - Complexity: 32
   - Functions: 12
   - Recommendation: Break into smaller components
```

### Example 3: Dependency Analysis

**User:** "Show circular dependencies"

**Skill Response:**
```
Reading .coderef/graph.json...

Found 2 circular dependencies:

1. src/models/User.ts → src/services/auth.ts → src/models/User.ts
   - Recommendation: Extract shared types to separate file

2. src/utils/validator.ts → src/utils/formatter.ts → src/utils/validator.ts
   - Recommendation: Create utils/index.ts for shared utilities
```

---

## Error Handling

### Missing Index File

**Error:** `.coderef/index.json` not found

**Response:**
```
CodeRef data not found. Please generate index via dashboard first:

1. Open coderef-dashboard
2. Navigate to project
3. Click "Scan Codebase"
4. Wait for indexing to complete
5. Retry analysis

Do NOT use CLI tools like `coderef scan` - use the dashboard.
```

### Invalid Index Format

**Error:** Malformed JSON or missing required fields

**Response:**
```
Invalid .coderef/index.json format.

Expected structure:
{
  "version": "1.0.0",
  "functions": [...],
  "classes": [...],
  "files": [...]
}

Please regenerate index via dashboard.
```

### Empty Index

**Error:** Index exists but contains no data

**Response:**
```
CodeRef index is empty (0 functions, 0 classes).

Possible causes:
- Project has no code files
- Unsupported language
- Indexing incomplete

Try rescanning via dashboard.
```

---

## Performance Characteristics

**Speed:** Very fast (haiku model + read-only operations)

**Scalability:**
- Small projects (<100 files): <1 second
- Medium projects (100-1000 files): 1-3 seconds
- Large projects (1000+ files): 3-5 seconds

**Memory:** Minimal (only reads necessary JSON data)

---

## Limitations

❌ **Cannot:**
- Scan codebases (use dashboard to generate .coderef/ data)
- Execute CLI tools
- Modify code or files
- Generate new .coderef/index.json

✅ **Can:**
- Read existing .coderef/index.json
- Parse and analyze structure
- Generate reports and recommendations
- Identify patterns and issues

---

## Integration with Dashboard

This skill complements the coderef-dashboard by providing CLI-based analysis of dashboard-generated data:

**Dashboard Role:**
- Scan codebase → generate .coderef/index.json
- Visualize in web UI
- Trigger scans on code changes

**Skill Role:**
- Analyze pre-generated data
- Answer specific queries
- Generate text-based reports
- Provide recommendations

**Workflow:**
```
1. Dashboard scans codebase → .coderef/index.json
2. User asks question in Claude
3. Skill reads .coderef/index.json
4. Skill generates answer
```

---

## Best Practices

✅ **DO:**
- Always check if .coderef/index.json exists first
- Provide clear error messages if data missing
- Use haiku model for speed
- Return concise summaries by default
- Offer detailed breakdown on request

❌ **DON'T:**
- Run CLI commands (coderef scan, analyze, etc.)
- Modify .coderef/ files
- Make assumptions about missing data
- Return entire index (too large)

---

## Troubleshooting

**Q: Skill says index not found but file exists**
A: Check file path - should be `.coderef/index.json` in project root

**Q: Analysis seems outdated**
A: Regenerate index via dashboard (codebase changed since last scan)

**Q: Skill is slow**
A: Index may be very large (>10MB) - use specific queries instead of "analyze everything"

**Q: Wrong language/framework detected**
A: Check index.json format - may need dashboard update

---

## See Also

- [SKILLS-GUIDE.md](../../../coderef-docs/SKILLS-GUIDE.md) - Complete skills documentation
- [API.md](../../../coderef/foundation-docs/API.md) - Dashboard API documentation
- [ARCHITECTURE.md](../../../coderef/foundation-docs/ARCHITECTURE.md) - System architecture

---

**Skill Version:** 1.0.0
**Last Updated:** 2026-01-09
**Maintained by:** CodeRef Assistant
