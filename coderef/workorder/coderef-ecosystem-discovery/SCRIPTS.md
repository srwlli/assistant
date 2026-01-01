# Ecosystem Discovery Scripts Documentation

**Workorder:** WO-CODEREF-ECOSYSTEM-DISCOVERY-001
**Location:** `coderef/workorder/coderef-ecosystem-discovery/scripts/`
**Purpose:** Automated analysis scripts that process `.coderef/` data from all 7 MCP servers to generate discovery documents for v1→v2 refactor planning.

---

## Scripts Inventory

### 1. generate_dependencies.py

**Purpose:** Generate cross-server import dependency matrix
**Input:** `.coderef/index.json` from all 7 servers
**Output:** `DEPENDENCIES.md`
**Runtime:** ~5-10 seconds

**What it does:**
- Loads `index.json` from each server's `.coderef/` directory
- Extracts all import statements from code elements
- Identifies cross-server imports (e.g., coderef-workflow importing from coderef-context)
- Builds dependency matrix showing which servers depend on which
- Detects circular dependencies (A imports B, B imports A)

**Key functions:**
- `load_index(server_path)` - Loads index.json file
- `extract_imports(elements)` - Extracts import statements from elements
- `build_dependency_matrix()` - Creates server-to-server dependency map
- `generate_markdown(matrix)` - Formats output as markdown table

**Output format:**
```markdown
## Import Matrix
| From Server | To Server | Import Statements |
|-------------|-----------|-------------------|
| coderef-workflow | coderef-context | `coderef_context.analyze`, ... |

## Circular Dependencies
⚠️ **coderef-workflow ↔ coderef-docs** (circular)
```

**Servers scanned:**
1. coderef-context
2. coderef-docs
3. coderef-personas
4. coderef-workflow
5. coderef-testing
6. papertrail
7. archived/coderef-mcp

**Usage:**
```bash
cd C:\Users\willh\Desktop\assistant\coderef\workorder\coderef-ecosystem-discovery\scripts
python generate_dependencies.py
```

**Error handling:**
- Skips servers without `.coderef/index.json` with warning
- Continues processing even if one server fails
- Validates JSON structure before parsing

---

### 2. generate_shared_code.py

**Purpose:** Identify duplicated code across servers
**Input:** `.coderef/index.json` from all 7 servers
**Output:** `SHARED-CODE.md`
**Status:** Created (awaiting verification)

**What it does:**
- TBD: Extract function/class names from all servers
- TBD: Compare names to find duplicates (18+ generators mentioned)
- TBD: Group duplicates by similarity and purpose

---

## Script Architecture

### Common Patterns

All scripts follow this structure:
1. **Import dependencies** (json, pathlib, collections)
2. **Define server paths** (MCP_ROOT = `C:/Users/willh/.mcp-servers`)
3. **Load data functions** (read `.coderef/index.json` files)
4. **Analysis functions** (process data, find patterns)
5. **Markdown generation** (format output as markdown tables)
6. **Output to workorder folder** (save alongside plan.json)

### File Paths

**Server locations:**
```
C:\Users\willh\.mcp-servers\
├── coderef-context\.coderef\index.json
├── coderef-docs\.coderef\index.json
├── coderef-personas\.coderef\index.json
├── coderef-workflow\.coderef\index.json
├── coderef-testing\.coderef\index.json
├── papertrail\.coderef\index.json
└── archived\coderef-mcp\.coderef\index.json
```

**Output location:**
```
C:\Users\willh\Desktop\assistant\coderef\workorder\coderef-ecosystem-discovery\
├── DEPENDENCIES.md
├── SHARED-CODE.md
├── ECOSYSTEM-ARCHITECTURE.mmd
├── REFACTOR-TARGETS.md
└── PATTERNS-ANALYSIS.md
```

---

## Data Sources

### .coderef/index.json Structure

Each server's `index.json` contains code elements with:
- `name` - Element name (function, class, hook)
- `type` - Element type (function, class, component)
- `file` - Source file path
- `line` - Line number
- `imports` - Array of import statements
- `exports` - Array of exported items
- `complexity` - Cyclomatic complexity score

**Example element:**
```json
{
  "name": "coderef_scan",
  "type": "function",
  "file": "src/index.ts",
  "line": 45,
  "imports": ["fs", "path", "coderef-context"],
  "complexity": 12
}
```

---

## Execution Order

Scripts should run in this order:
1. **generate_dependencies.py** - Identifies cross-server relationships
2. **generate_shared_code.py** - Finds duplicate implementations
3. **generate_ecosystem_diagram.py** - Visualizes architecture
4. **generate_refactor_targets.py** - Highlights complexity hotspots
5. **generate_patterns_analysis.py** - Detects inconsistencies
6. **copy_graph_exports.py** - Copies full graph data

**Total runtime:** < 30 minutes (constraint from context.json)

---

## Maintenance

**Adding new servers:**
1. Update `SERVERS` array in each script
2. Ensure server has `.coderef/index.json` generated
3. Re-run all scripts to update analysis

**Debugging:**
- Scripts print progress messages (⚠️ warnings, ✅ success)
- Check console output for skipped servers
- Verify `.coderef/index.json` exists before running

**Validation:**
- All output files should be valid markdown
- Tables should have consistent column alignment
- Cross-references between documents should be accurate

---

**Last Updated:** 2026-01-01
**Maintained by:** WO-CODEREF-ECOSYSTEM-DISCOVERY-001
