# Agent Investigation Report: coderef-context Tool Failures

**Date:** 2026-01-19
**Investigator:** Agent (coderef-context debugging session)
**Issue:** Two coderef-context MCP tools failing with Python type errors
**Status:** Root cause identified - Schema version mismatch

---

## Executive Summary

The coderef-context MCP server tools `coderef_complexity` and `coderef_query` are failing because they expect the **v1.0.0 schema** for `.coderef/index.json` and `.coderef/graph.json`, but the project is using the **v2.0.0 schema** with different data structures.

**Impact:** Complete failure of AST-based analysis tools (complexity scoring, relationship queries) for projects using v2.0.0 schema.

---

## Investigation Findings

### Issue 1: `coderef_complexity` - 'str' object has no attribute 'get'

#### The Error
```python
AttributeError: 'str' object has no attribute 'get'
```

#### Root Cause
The tool expects `.coderef/index.json` to be a **flat list of code elements**:

```json
// v1.0.0 schema (expected by server)
[
  {
    "id": "GameClient",
    "type": "class",
    "complexity": 15
  },
  {
    "id": "Tetris",
    "type": "class",
    "complexity": 20
  }
]
```

However, the project is using the **v2.0.0 schema**, where the file is a **dictionary** containing metadata at the top level and elements nested inside an `"elements"` key:

```json
// v2.0.0 schema (actual in project)
{
  "version": "2.0.0",
  "generatedAt": "2026-01-19T00:00:00Z",
  "metadata": {
    "project": "example",
    "language": "typescript"
  },
  "elements": [
    {
      "id": "GameClient",
      "type": "class",
      "complexity": 15
    },
    {
      "id": "Tetris",
      "type": "class",
      "complexity": 20
    }
  ]
}
```

#### What Happened
1. The server code tried to **"iterate over elements"** by doing:
   ```python
   for element in index_data:
       element.get('id')  # Expects element to be a dict
   ```

2. With the v2.0.0 schema, `index_data` is a **dictionary**, so iterating over it yields **keys** (strings like `"version"`, `"generatedAt"`, `"metadata"`, `"elements"`).

3. The code then tried to call `.get()` on these **string keys** instead of dictionaries, which caused the crash.

4. When analyzing `GameClient` or `Tetris`, the server never reached the actual elements because it was stuck iterating over metadata keys.

---

### Issue 2: `coderef_query` - 'list' object has no attribute 'items'

#### The Error
```python
AttributeError: 'list' object has no attribute 'items'
```

#### Root Cause
The tool expects the `"nodes"` in `.coderef/graph.json` to be a **dictionary** (mapped by ID):

```json
// v1.0.0 schema (expected by server)
{
  "nodes": {
    "GAMES_REGISTRY": {
      "id": "GAMES_REGISTRY",
      "type": "constant",
      "dependencies": []
    },
    "GameClient": {
      "id": "GameClient",
      "type": "class",
      "dependencies": ["GAMES_REGISTRY"]
    }
  },
  "edges": []
}
```

However, the project is using the **v2.0.0 schema**, where nodes are stored as a **list** of objects:

```json
// v2.0.0 schema (actual in project)
{
  "version": "2.0.0",
  "generatedAt": "2026-01-19T00:00:00Z",
  "nodes": [
    {
      "id": "GAMES_REGISTRY",
      "type": "constant",
      "dependencies": []
    },
    {
      "id": "GameClient",
      "type": "class",
      "dependencies": ["GAMES_REGISTRY"]
    }
  ],
  "edges": [
    {
      "from": "GameClient",
      "to": "GAMES_REGISTRY",
      "type": "depends-on"
    }
  ]
}
```

#### What Happened
1. The server code tried to **iterate over nodes as a dictionary**:
   ```python
   for node_id, node_data in graph_data['nodes'].items():
       # Process node
   ```

2. With the v2.0.0 schema, `graph_data['nodes']` is a **list**, not a dictionary.

3. Calling `.items()` on a list caused the crash.

4. When querying `GAMES_REGISTRY` relationships, the server couldn't process the nodes list.

---

## Schema Comparison

| Aspect | v1.0.0 Schema | v2.0.0 Schema |
|--------|---------------|---------------|
| **index.json structure** | Flat array of elements | Dictionary with metadata + elements array |
| **graph.json nodes** | Dictionary (keyed by ID) | Array of node objects |
| **graph.json edges** | Array (optional) | Array (required) |
| **Metadata** | None | version, generatedAt, metadata fields |
| **Server support** | ✅ Full support | ❌ Not supported |

---

## Impact Analysis

### Affected Tools
- ✅ `coderef_scan` - **Works** (generates v2.0.0 files)
- ❌ `coderef_complexity` - **Fails** (can't read v2.0.0 index.json)
- ❌ `coderef_query` - **Fails** (can't read v2.0.0 graph.json)
- ❌ `coderef_impact` - **Likely fails** (depends on graph.json)
- ❌ `coderef_patterns` - **Likely fails** (depends on index.json)
- ❌ `coderef_coverage` - **Unknown** (needs testing)

### Severity
**CRITICAL** - The scanning tool generates files that the analysis tools can't read. This creates a broken workflow where:
1. `coderef_scan` creates v2.0.0 files
2. All downstream analysis tools fail
3. Users lose access to complexity scoring, relationship queries, impact analysis, and pattern detection

---

## Recommended Solutions

### Option 1: Update Server to Support v2.0.0 Schema (Recommended)
**Effort:** Medium
**Impact:** High
**Compatibility:** Backward compatible if done correctly

**Changes needed:**
1. Update `coderef_complexity` to handle both schemas:
   ```python
   # Detect schema version
   if isinstance(index_data, dict) and 'version' in index_data:
       elements = index_data.get('elements', [])
   else:
       elements = index_data  # v1.0.0 flat array

   for element in elements:
       element.get('id')  # Now works for both schemas
   ```

2. Update `coderef_query` to handle both schemas:
   ```python
   # Detect schema version
   nodes_data = graph_data.get('nodes', [])
   if isinstance(nodes_data, list):
       # v2.0.0 - convert to dict for processing
       nodes = {node['id']: node for node in nodes_data}
   else:
       # v1.0.0 - already a dict
       nodes = nodes_data

   for node_id, node_data in nodes.items():
       # Process node
   ```

3. Add schema version detection utility:
   ```python
   def detect_schema_version(data):
       if isinstance(data, dict) and 'version' in data:
           return data['version']
       return '1.0.0'
   ```

### Option 2: Add Schema Migration Tool
**Effort:** Low
**Impact:** Medium
**Compatibility:** Workaround, not a fix

**Create a conversion tool:**
```python
def migrate_v2_to_v1(index_path, graph_path):
    # Read v2.0.0 files
    with open(index_path) as f:
        index_v2 = json.load(f)

    # Extract elements array
    index_v1 = index_v2.get('elements', [])

    # Write v1.0.0 file
    with open(index_path + '.v1', 'w') as f:
        json.dump(index_v1, f)
```

**Drawback:** Loses metadata, requires manual conversion

### Option 3: Revert coderef_scan to Generate v1.0.0
**Effort:** Low
**Impact:** Low (loses metadata benefits)
**Compatibility:** Fixes immediate issue but loses v2.0.0 features

---

## Next Steps

1. **Immediate:** Update coderef-context MCP server to support both schema versions
2. **Testing:** Add test cases for both v1.0.0 and v2.0.0 schemas
3. **Documentation:** Update schema documentation to clarify version support
4. **Migration:** Provide migration guide for projects using v1.0.0

---

## Files to Fix

### Primary Files
- `C:\Users\willh\.mcp-servers\coderef-context\src\tools\complexity.py` - Add schema detection and v2.0.0 support
- `C:\Users\willh\.mcp-servers\coderef-context\src\tools\query.py` - Add schema detection and v2.0.0 support

### Supporting Files
- `C:\Users\willh\.mcp-servers\coderef-context\src\analyzers\ast_analyzer.py` - Add schema version utility
- `C:\Users\willh\.mcp-servers\coderef-context\src\tools\impact.py` - Verify schema support
- `C:\Users\willh\.mcp-servers\coderef-context\src\tools\patterns.py` - Verify schema support

### Test Files
- Create test fixtures for both v1.0.0 and v2.0.0 schemas
- Add integration tests for schema detection
- Add regression tests for GameClient, Tetris, GAMES_REGISTRY

---

## Code Snippets for Fix

### complexity.py - Before
```python
def analyze_complexity(index_path, element_name):
    with open(index_path) as f:
        elements = json.load(f)

    for element in elements:  # ❌ Fails with v2.0.0 (iterates over dict keys)
        if element.get('id') == element_name:
            return element.get('complexity')
```

### complexity.py - After
```python
def analyze_complexity(index_path, element_name):
    with open(index_path) as f:
        data = json.load(f)

    # ✅ Schema detection
    if isinstance(data, dict) and 'version' in data:
        elements = data.get('elements', [])
    else:
        elements = data  # v1.0.0 flat array

    for element in elements:
        if element.get('id') == element_name:
            return element.get('complexity')
```

### query.py - Before
```python
def query_relationships(graph_path, target):
    with open(graph_path) as f:
        graph = json.load(f)

    for node_id, node_data in graph['nodes'].items():  # ❌ Fails with v2.0.0 (nodes is a list)
        if node_id == target:
            return node_data.get('dependencies', [])
```

### query.py - After
```python
def query_relationships(graph_path, target):
    with open(graph_path) as f:
        graph = json.load(f)

    # ✅ Schema detection
    nodes_data = graph.get('nodes', [])
    if isinstance(nodes_data, list):
        # v2.0.0 - convert to dict
        nodes = {node['id']: node for node in nodes_data}
    else:
        # v1.0.0 - already a dict
        nodes = nodes_data

    for node_id, node_data in nodes.items():
        if node_id == target:
            return node_data.get('dependencies', [])
```

---

## Testing Checklist

- [ ] Test `coderef_complexity` with v1.0.0 schema
- [ ] Test `coderef_complexity` with v2.0.0 schema
- [ ] Test `coderef_complexity` with GameClient component
- [ ] Test `coderef_complexity` with Tetris component
- [ ] Test `coderef_query` with v1.0.0 schema
- [ ] Test `coderef_query` with v2.0.0 schema
- [ ] Test `coderef_query` with GAMES_REGISTRY target
- [ ] Test `coderef_impact` with both schemas
- [ ] Test `coderef_patterns` with both schemas
- [ ] Add error handling for malformed schemas
- [ ] Add logging for schema version detection
- [ ] Document schema version support in README

---

## Conclusion

The root cause is clear: **Schema version mismatch between coderef_scan (generates v2.0.0) and analysis tools (expect v1.0.0).**

**Recommended fix:** Update all analysis tools to detect and support both schema versions. This preserves backward compatibility while enabling v2.0.0 metadata features.

**Priority:** CRITICAL - Fixes are needed to restore the AST-based analysis advantage that differentiates the coderef system from everything-claude-code.

---

**Related Files:**
- `stub.json` - Original stub capturing the bug report
- `C:\Users\willh\.mcp-servers\coderef-context\` - MCP server location
- `.coderef/index.json` - Project schema v2.0.0 (example)
- `.coderef/graph.json` - Project schema v2.0.0 (example)
