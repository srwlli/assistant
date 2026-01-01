# Shared Code Analysis

Functions, classes, and components that appear in multiple servers.

**Total duplicates found:** 3

## Duplicate Inventory

| Name | Type | Locations | Recommendation |
|------|------|-----------|----------------|
| `run_all_tests` | function | `archived/coderef-mcp:C:/Users/willh/.mcp-servers/coderef-mcp/tests/integration/test_nl_query.py:337`<br>`archived/coderef-mcp:C:/Users/willh/.mcp-servers/coderef-mcp/tests/integration/test_prompts.py:239`<br>`archived/coderef-mcp:C:/Users/willh/.mcp-servers/coderef-mcp/tests/integration/test_resources.py:186` | 🟡 Consider consolidation |
| `ErrorResponse` | class/component | `archived/coderef-mcp:C:/Users/willh/.mcp-servers/coderef-mcp/coderef/models.py:331`<br>`archived/coderef-mcp:C:/Users/willh/.mcp-servers/coderef-mcp/error_responses.py:8` | 🟢 Acceptable duplication |
| `TestErrorHandling` | class/component | `archived/coderef-mcp:C:/Users/willh/.mcp-servers/coderef-mcp/tests/integration/test_mcp_server.py:229`<br>`archived/coderef-mcp:C:/Users/willh/.mcp-servers/coderef-mcp/tests/unit/test_query_tools.py:355` | 🟢 Acceptable duplication |

## Consolidation Recommendations

### High Priority (4+ duplicates)

None

### Shared Library Candidates

Consider creating `coderef-shared` package for:
- Common generators (planning, docs, analysis)
- Utility functions (path handling, JSON parsing)
- Shared data models (plan structure, metadata)