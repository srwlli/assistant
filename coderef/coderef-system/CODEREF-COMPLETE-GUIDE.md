# CodeRef System - The Complete Guide

**Document Type:** User Guide
**Version:** 1.1.0
**Status:** Living Document
**Created:** 2025-12-30
**Last Updated:** 2025-12-30
**Workorder:** WO-CODEREF-GUIDE-001
**Feature:** coderef-system-documentation

---

## What is CodeRef?

CodeRef is an **AI-powered code intelligence system** that scans, maps, and analyzes your entire codebase to answer questions like:

- "What will break if I change this function?"
- "How is feature X connected to feature Y?"
- "Where is this code being used?"
- "Which parts of my code have no tests?"
- "What's the complexity of this module?"

Think of it as **X-ray vision for your code**. Instead of manually searching files or guessing dependencies, CodeRef builds a complete map of your codebase and lets you query it instantly.

---

## Why CodeRef Exists

### The Problem

Managing large codebases with AI agents leads to:
- **Context fragmentation** - Agents can't see the full dependency graph
- **Risky refactoring** - No way to know what breaks when you change code
- **Slow discovery** - Manual grep/search to find connections
- **Missing tests** - No visibility into untested code
- **Hidden complexity** - Hard to identify technical debt

### The Solution

CodeRef provides:
- ✅ **Complete code inventory** - Every function, class, method mapped
- ✅ **Dependency graph** - Visual maps of how code connects
- ✅ **Impact analysis** - See what breaks before you break it
- ✅ **Complexity scoring** - Identify technical debt hotspots
- ✅ **Test coverage gaps** - Find untested code automatically
- ✅ **AI-native queries** - Ask questions in plain English

---

## How CodeRef Works

### The 3-Step Process

**1. Scan** - CodeRef reads your entire codebase and builds an index

```bash
# What happens during a scan:
- Finds all Python (.py), TypeScript (.ts), JavaScript (.js) files
- Parses each file using AST (Abstract Syntax Tree) - 99% accuracy
- Extracts every function, class, method, export
- Records exact location (file path, line number)
- Maps relationships (what calls what, what imports what)
```

**Example Output:**
```
✅ Successfully scanned the project
  - 116,233 code elements discovered
  - Functions: 45,782
  - Classes: 12,441
  - Methods: 58,010
  - Files analyzed: 3,847
```

**2. Index** - Creates a searchable database of code relationships

```json
{
  "element": "generate_plan",
  "type": "function",
  "file": "coderef-workflow/server.py",
  "line": 245,
  "calls": ["validate_context", "create_tasks", "save_plan"],
  "called_by": ["main_handler", "api_endpoint"],
  "complexity": 12,
  "test_coverage": true
}
```

**3. Query** - Answer questions about your code instantly

```bash
# Example queries:
coderef query --type calls --target generate_plan
# Shows: What does generate_plan() call?

coderef query --type calls-me --target generate_plan
# Shows: What calls generate_plan()?

coderef impact --element generate_plan
# Shows: What breaks if we change this?
```

---

## What the Scan Captures

### For Every Code Element:

| Data Point | Description | Example |
|------------|-------------|---------|
| **Name** | Function/class name | `generate_plan` |
| **Type** | Element type | `function`, `class`, `method` |
| **File Path** | Exact location | `coderef-workflow/server.py` |
| **Line Number** | Where defined | `245` |
| **Export Status** | Public or private | `exported`, `private` |
| **Dependencies** | What it calls | `[validate_context, save_plan]` |
| **Dependents** | What calls it | `[main_handler, api_endpoint]` |
| **Complexity** | Cyclomatic complexity | `12` (moderate) |
| **Test Coverage** | Has tests or not | `true`, `false` |

### Real Example from Your Scan:

```python
# File: coderef-docs/server.py:245
def generate_plan(context: dict) -> Plan:
    """Creates implementation plan from context"""
    # CodeRef knows:
    # - This function is at line 245
    # - It's exported (public API)
    # - It calls: validate_context, create_tasks, save_plan
    # - It's called by: main_handler, api_endpoint
    # - Complexity score: 12
    # - Has test coverage: Yes
```

---

## What You Can Do With CodeRef

### 1. Impact Analysis - "What breaks if I change this?"

**Before CodeRef:**
```
User: "Can I rename generate_plan()?"
Developer: "Let me search... grep... check imports... maybe?"
*30 minutes later, still unsure*
```

**With CodeRef:**
```bash
coderef impact --element generate_plan

# Result (in 2 seconds):
Impact Analysis: generate_plan
  Direct Callers: 2 files
    - coderef-workflow/handlers/main.py:87
    - coderef-workflow/api/endpoints.py:145

  Transitive Impact: 12 files affected
    - server.py → handlers → api → database

  Risk Score: Medium (12 dependencies)
  Recommendation: ✅ Safe to rename with automated refactoring
```

### 2. Dependency Mapping - "How is this connected?"

**Query: "What's the path from user input to database?"**

```bash
coderef query --type path --source user_input --target save_to_db

# Result: Visual call chain
user_input (api.py:12)
  → validate_request (validators.py:45)
    → process_data (handlers.py:89)
      → transform_model (models.py:156)
        → save_to_db (database.py:234)
```

### 3. Test Coverage Gaps - "What needs tests?"

```bash
coderef coverage --format detailed

# Result:
Test Coverage Report:
  Overall: 67% coverage

  Untested Functions (23):
    ❌ coderef-workflow/utils.py:generate_workorder_id
    ❌ coderef-docs/handlers.py:archive_feature
    ❌ coderef-context/analysis.py:calculate_complexity

  Low Coverage (<50%):
    ⚠️ coderef-workflow/planning.py - 23% covered
```

### 4. Complexity Scoring - "Where's the technical debt?"

```bash
coderef complexity --element generate_plan

# Result:
Complexity Analysis: generate_plan
  Cyclomatic Complexity: 12
  Lines of Code: 87
  Number of Branches: 8
  Max Nesting Depth: 4

  Rating: ⚠️ Moderate Complexity
  Recommendation: Consider refactoring if adding more logic
```

### 5. Pattern Detection - "What patterns exist?"

```bash
coderef patterns --project-path C:/Users/willh/Desktop/assistant

# Result:
Common Patterns Detected:
  - Error Handling: try/except with logging (89 instances)
  - Decorators: @mcp_tool wrapper (47 instances)
  - Validators: Pydantic models (34 instances)

  Inconsistencies Found:
    ⚠️ 12 functions use print() instead of logger
    ⚠️ 5 files missing type hints
```

---

## Real-World Use Cases

### Use Case 1: Safe Refactoring

**Scenario:** You want to rename `generate_plan()` to `create_implementation_plan()`

**Without CodeRef:**
1. Search for "generate_plan" manually
2. Hope you found all occurrences
3. Rename and pray tests pass
4. Debug production errors you missed

**With CodeRef:**
```bash
# Step 1: Check impact
coderef impact --element generate_plan
# Shows: 2 direct callers, 12 transitive dependencies

# Step 2: Safe to proceed
# Rename knowing exactly what needs updating

# Step 3: Verify
coderef query --type calls --target create_implementation_plan
# Confirms: No references to old name remain
```

### Use Case 2: Understanding Legacy Code

**Scenario:** New developer joins team, needs to understand auth flow

**Without CodeRef:**
1. Read docs (probably outdated)
2. Grep for "auth" (hundreds of results)
3. Trace code manually (hours of work)
4. Still missing edge cases

**With CodeRef:**
```bash
# Step 1: Find entry point
coderef query --pattern "authenticate.*"
# Shows: authenticate_user is main entry

# Step 2: Trace flow
coderef query --type calls --target authenticate_user --depth 3
# Visual dependency tree shows entire auth flow

# Step 3: See usage
coderef query --type calls-me --target authenticate_user
# Shows: Where auth is used across codebase
```

### Use Case 3: Finding Orphaned Code

**Scenario:** Cleanup codebase, remove unused code

**Without CodeRef:**
1. Guess which functions are unused
2. Comment out and hope nothing breaks
3. Wait for production errors

**With CodeRef:**
```bash
coderef query --type calls-me --target old_legacy_function

# Result:
No callers found for old_legacy_function
  ✅ Safe to delete
  Last modified: 2023-05-12
  Recommendation: Archive to git history
```

---

## Your CodeRef Ecosystem

### Current Scan Results

From your latest scan:
- **116,233 code elements discovered**
- **3,847 files analyzed**
- **7 active MCP servers** mapped

### Active MCP Servers in Your Project:

| Server | Size | Purpose |
|--------|------|---------|
| **coderef-context** | 595 KB | Code intelligence & dependency analysis |
| **coderef-docs** | 102 MB | Documentation generation (largest) |
| **coderef-personas** | 11 MB | Expert agent system |
| **coderef-testing** | 1.6 MB | Test automation |
| **coderef-workflow** | 7.4 MB | Planning & orchestration |
| **papertrail** | 501 KB | Workorder logging system |
| **mcp-workflows** | 108 KB | Workflow definitions |

### Scanned Languages:

- **Python** (.py) - Primary language
- **TypeScript** (.ts) - Frontend/tooling
- **JavaScript** (.js) - Legacy support

---

## Next Steps: Discovering Features Together

This guide is a **living document**. As we explore CodeRef together, we'll discover and document:

### Features to Explore:

- **Visual Dependency Diagrams** - Generate Mermaid/Graphviz charts
- **Drift Detection** - Find code that changed since last scan
- **Custom Patterns** - Define your own code patterns to find
- **Cross-Project Analysis** - Compare patterns across multiple projects
- **AI-Powered Suggestions** - Let CodeRef recommend refactorings

### How to Use This Guide:

1. **Read** - Understand what CodeRef can do
2. **Experiment** - Try queries on your codebase
3. **Discover** - Find new use cases we haven't documented
4. **Contribute** - Add your discoveries to this guide

---

## Quick Reference: Common Queries

### Dependency Queries

```bash
# What does X call?
coderef query --type calls --target function_name

# What calls X?
coderef query --type calls-me --target function_name

# What does X import?
coderef query --type imports --target module_name

# What imports X?
coderef query --type imports-me --target module_name

# Show dependency path
coderef query --type path --source A --target B
```

### Impact Analysis

```bash
# Check impact of changing element
coderef impact --element function_name

# Check impact of deleting element
coderef impact --element function_name --operation delete

# Check impact of refactoring element
coderef impact --element function_name --operation refactor
```

### Code Quality

```bash
# Get complexity score
coderef complexity --element function_name

# Find patterns
coderef patterns --project-path /path/to/project

# Check test coverage
coderef coverage --format summary

# Check test coverage (detailed)
coderef coverage --format detailed
```

### Visualization

```bash
# Generate dependency diagram
coderef diagram --project-path /path/to/project

# Generate call graph
coderef diagram --type calls --depth 2

# Generate import graph
coderef diagram --type imports --format mermaid
```

---

## Best Practices

### When to Scan

- **Before major refactoring** - Know what you're changing
- **After pulling changes** - Stay synced with team
- **Before releases** - Verify test coverage
- **Weekly** - Detect drift early

### Scan Optimization

**Include** only source code:
```bash
# Create .coderefignore
.venv/
node_modules/
__pycache__/
*.pyc
build/
dist/
```

**Focus** on specific directories:
```bash
# Scan only your server code
coderef scan --path C:/Users/willh/.mcp-servers/coderef-workflow
```

### Query Tips

- **Start broad** - Use `calls-me` to see usage
- **Then narrow** - Add `--depth 1` for direct dependencies only
- **Visualize** - Use `diagram` for complex relationships
- **Save results** - Export to JSON for later analysis

---

## Troubleshooting

### "Scan takes too long"

**Problem:** Scanning large projects with node_modules/venv
**Solution:** Add exclusions to `.coderefignore`

### "Can't find element"

**Problem:** Query returns no results
**Solution:** Check exact name/spelling, scan may be stale

### "Too many results"

**Problem:** Query returns hundreds of dependencies
**Solution:** Reduce `--depth` or use `--max-results 10`

---

## File Storage & Output System

### Automatic File Storage (.coderef Directory)

CodeRef uses a `.coderef/` directory for persistent storage:

```
.coderef/
├── config.json          # Project configuration
├── index.json           # Code element index
├── graph.json           # Dependency graph (cached)
├── reports/             # Auto-saved analysis reports
│   ├── drift-2025-*.json
│   ├── impact-2025-*.json
│   └── breaking-2025-*.json
└── cache/               # Temporary cache (gitignored)
```

**Key Features:**
- ✅ Auto-initialization on first use
- ✅ Persistent caching of dependency graphs
- ✅ Timestamped report storage
- ✅ Gitignore support for cache directory

### Commands with --output File Saving

15 commands support `--output <file>` or `-o <file>`:

| Command | Output Formats | Default | Example |
|---------|---------------|---------|---------|
| drift | JSON, summary | stdout | `--output drift-report.json` |
| validate | table, JSON, summary | stdout | `--output validation.json` |
| query | table, JSON, tree | stdout | `--output query-results.json` |
| coverage | table, JSON, summary | stdout | `--output coverage-report.json` |
| impact | table, JSON, tree | stdout | `--output impact-analysis.json` |
| update-ref | text report | stdout | `--output stale-refs.txt` |
| format-ref | text report | stdout | `--output format-report.txt` |
| diagram | mermaid, graphviz | stdout | `--output deps.mmd` |
| breaking | JSON, table | stdout | `--output breaking-changes.json` |
| complexity | table, JSON, summary | stdout | `--output complexity-metrics.json` |
| patterns | table, JSON | stdout | `--output patterns-report.json` |
| context | markdown, JSON | ./coderef-context/ | `--output ./docs/` |
| export | mermaid, dot, jsonld, json | stdout | `--output graph.json` |

### Export Command - Multiple Formats

The `export` command provides 4 serialization formats:

```bash
# Mermaid diagram (for documentation)
coderef export --format mermaid --output deps.mmd

# GraphViz DOT (for high-quality visualization)
coderef export --format dot --output deps.dot

# JSON-LD (for semantic web/knowledge graphs)
coderef export --format jsonld --output codebase.jsonld

# JSON (standard structured format)
coderef export --format json --output graph.json
```

**Features:**
- Loads cached graph from `.coderef/graph.json` by default
- `--scan` flag forces fresh analysis
- `--wrap` wraps Mermaid in markdown code fence
- Supports node/edge label control
- Max nodes limit configurable

### Context Command - Comprehensive Documentation

Generates complete codebase context in 2 formats:

```bash
# Generate both markdown and JSON
coderef context ./src --output ./docs

# Creates:
# - CONTEXT.md (human-readable documentation)
# - context.json (machine-readable structured data)
```

**What Gets Documented:**
- Total files, elements, entry points
- Critical functions (high complexity/impact)
- Code patterns and examples
- Edge cases and complexity metrics
- Dependency relationships
- Test coverage information

**Output Formats:**
- `markdown` - Human-readable docs
- `json` - Structured data for agents
- `both` (default) - Both formats

### Tag Command - Code Annotation

Injects CodeRef2 tags directly into source files:

```bash
# Preview changes
coderef tag ./src --dry-run

# Apply tags to directory
coderef tag ./src --force --verbose

# Tag single file
coderef tag ./src/auth.ts
```

**Output:**
- Modifies source files in-place
- Adds comments like `// @Fn/path#element:line`
- Supports multiple languages (configurable comment syntax)
- Dry-run mode for safety

### Scan Command - Element Discovery

```bash
# JSON output (default)
coderef scan ./src --json > elements.json

# Table output
coderef scan ./src
```

**Output:** Array of discovered elements with:
- Element type (function, class, method, etc.)
- Name, file path, line number
- Export status
- Metadata

### Auto-Save Configuration

In `.coderef/config.json`:

```json
{
  "output": {
    "autoSave": true,
    "format": "json"
  }
}
```

**When autoSave: true:**
- Reports automatically saved to `.coderef/reports/`
- Timestamped filenames prevent overwrites
- Dependency graph cached to `.coderef/graph.json`

### Watch Command - Continuous Monitoring

```bash
coderef watch ./src
```

**Output:**
- Continuous re-analysis on file changes
- Real-time console updates
- Auto-saves to `.coderef/` when configured

### Format Support Summary

| Format | Commands | Use Case |
|--------|----------|----------|
| JSON | All commands | Machine-readable, agent integration |
| Table | query, coverage, impact, complexity, patterns | Human-readable CLI output |
| Markdown | context | Documentation generation |
| Mermaid | export, diagram | Visual diagrams in docs |
| GraphViz DOT | export, diagram | High-quality graph rendering |
| JSON-LD | export | Semantic web, knowledge graphs |
| Tree | query, impact | Hierarchical relationship visualization |

### Key Saving Features

1. **Persistent Graph Cache** - Avoids re-analysis (saves seconds to minutes)
2. **Timestamped Reports** - History tracking in `.coderef/reports/`
3. **Gitignore Integration** - Cache excluded, reports optionally committed
4. **Multiple Output Formats** - Choose format based on use case
5. **Stdout/File Flexibility** - Pipe to tools or save to files
6. **Directory Output** - Context command creates organized doc folders

### System Capabilities Summary

- ✅ 15/19 commands support `--output` file saving
- ✅ 4 export formats (JSON, Mermaid, DOT, JSON-LD)
- ✅ Automatic persistence via `.coderef/` directory
- ✅ Multiple presentation formats (table, JSON, tree, markdown)
- ✅ Direct code annotation via `tag` command
- ✅ Comprehensive documentation via `context` command
- ✅ Graph caching for performance
- ✅ Report history with timestamps

---

## Resources

- **[CLAUDE.md](../CLAUDE.md)** - Assistant project context
- **[projects.md](../projects.md)** - Master project list
- **[workorders.json](../workorders.json)** - Active workorders

---

## Contributing to This Guide

As you discover new CodeRef features or use cases:

1. **Document it** - Add to this guide
2. **Share examples** - Include real queries from your work
3. **Update best practices** - What worked? What didn't?
4. **Version it** - Increment version number, update "Last Updated"

---

**Version History:**

- **v1.1.0** (2025-12-30) - File storage and output system
  - Added comprehensive file storage documentation (.coderef directory structure)
  - Documented all 15 commands with --output support
  - Included export formats (JSON, Mermaid, DOT, JSON-LD)
  - Added context, tag, and watch command details
  - Documented auto-save configuration and caching system

- **v1.0.0** (2025-12-30) - Initial guide creation
  - Documented scan capabilities
  - Added query examples
  - Included real-world use cases
  - Set foundation for feature discovery

---

**Maintained by:** CodeRef Assistant
**Attribution:** 🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
