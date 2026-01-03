# Complete CodeRef Output Capabilities

## 11 MCP Tools (from coderef-context server)

1. **scan** - Discover all code elements
   - Output: JSON array of functions, classes, components, hooks
   - Saves to: `.coderef/index.json` (4MB for coderef-docs)
   - Example: 116,233 elements discovered

2. **query** - Query relationships
   - Types: calls, calls-me, imports, imports-me, depends-on, depends-on-me
   - Output: JSON dependency graph
   - Saves to: `.coderef/graph.json` (6.2MB for coderef-docs)

3. **impact** - Analyze change impact
   - Output: JSON with affected files, risk level, ripple effects
   - Saves to: `.coderef/reports/impact-{element}.json`

4. **complexity** - Calculate metrics
   - Output: JSON with LOC, cyclomatic complexity, dependencies, test coverage %
   - Saves to: `.coderef/reports/complexity-{element}.json`

5. **patterns** - Discover code patterns
   - Output: JSON array of patterns, anti-patterns, untested areas
   - Saves to: `.coderef/reports/patterns.json`

6. **coverage** - Test coverage analysis
   - Output: JSON with overall coverage %, file-by-file breakdown
   - Saves to: `.coderef/reports/coverage.json`

7. **context** - Comprehensive codebase context
   - Output: Markdown/JSON full project overview
   - Saves to: `.coderef/context.md` or `.coderef/context.json`
   - Includes: Architecture, components, dependencies, patterns

8. **validate** - Validate CodeRef2 references
   - Output: JSON with valid/invalid reference counts
   - Saves to: `.coderef/reports/validation.json`

9. **drift** - Detect index drift
   - Output: JSON diff between cached index and current code
   - Saves to: `.coderef/reports/drift.json`

10. **diagram** - Generate dependency diagrams
    - Output: Mermaid or Graphviz format
    - Saves to: `.coderef/diagrams/dependencies.mmd` or `.dot`

11. **tag** - Add CodeRef2 tags to source files
    - Output: Text report of tagged elements
    - Modifies: Source files directly (adds @Fn, @Cl, @Cp tags)

---

## What Gets Saved (.coderef/ Directory Structure)

```
.coderef/
├── index.json              # All code elements (functions, classes, etc.)
├── graph.json              # Dependency relationships
├── context.json            # Comprehensive project context
├── context.md              # Human-readable overview
├── reports/
│   ├── impact-*.json       # Impact analysis results
│   ├── complexity-*.json   # Complexity metrics
│   ├── patterns.json       # Pattern discovery
│   ├── coverage.json       # Test coverage
│   ├── validation.json     # Reference validation
│   └── drift.json          # Index drift detection
└── diagrams/
    ├── dependencies.mmd    # Mermaid diagram
    ├── dependencies.dot    # Graphviz diagram
    └── calls.mmd           # Call graph diagram
```

---

## Export Formats Available

1. **JSON** - Machine-readable structured data (all tools)
2. **Markdown** - Human-readable documentation (context tool)
3. **Mermaid** - Visual diagrams for documentation (diagram tool)
4. **GraphViz (.dot)** - Visual diagrams for analysis tools (diagram tool)
5. **JSON-LD** - Semantic linked data format (context tool with --format json-ld)

---

## 15 CLI Commands with --output Support

1. `coderef scan --output .coderef/index.json`
2. `coderef query --output .coderef/graph.json`
3. `coderef impact --output .coderef/reports/impact.json`
4. `coderef complexity --output .coderef/reports/complexity.json`
5. `coderef patterns --output .coderef/reports/patterns.json`
6. `coderef coverage --output .coderef/reports/coverage.json`
7. `coderef context --output .coderef/context.json`
8. `coderef validate --output .coderef/reports/validation.json`
9. `coderef drift --output .coderef/reports/drift.json`
10. `coderef diagram --output .coderef/diagrams/dependencies.mmd`
11. `coderef tag --output .coderef/reports/tagging.txt`
12-15. (Additional commands with output support)

---

## Current Reality Check

**What we actually have saved:**
```
coderef-docs/.coderef/
├── index.json     # 4MB - 116,233 elements ✅
└── graph.json     # 6.2MB - relationships ✅

coderef-context/.coderef/    # Empty ❌
coderef-workflow/.coderef/   # Empty ❌
coderef-personas/.coderef/   # Empty ❌
coderef-testing/.coderef/    # Empty ❌
```

**The Gap:** Only 2 of 15+ possible output files exist, and only for 1 of 5 servers.

---

## Maximum Potential Output (If We Use Everything)

For each of the 5 servers, we could have:

```
coderef/{server-name}/
├── index.json              # Code inventory
├── graph.json              # Dependencies
├── context.json            # Full overview
├── context.md              # Human-readable
├── reports/
│   ├── patterns.json       # Common patterns
│   ├── coverage.json       # Test coverage
│   ├── complexity/         # Per-element complexity
│   ├── impact/             # Per-element impact
│   ├── validation.json     # Reference validation
│   └── drift.json          # Code changes detection
└── diagrams/
    ├── dependencies.mmd    # Architecture diagram
    ├── calls.mmd          # Call graph
    └── imports.mmd        # Import graph
```

**Total potential:** ~15 files per server × 5 servers = 75 organized output files

**Currently we have:** 2 files (index.json + graph.json for coderef-docs only)

**Utilization rate:** 2.6% 😱

---

## The Question

How do we organize and use this intelligently?
