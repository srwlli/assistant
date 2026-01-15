# MCP Configuration Investigation Report
**STUB-046: mcp-config-investigation**
**Generated:** 2025-12-19
**By:** Archer (Orchestrator)

---

## Executive Summary

**Problem:** scriptboard-mcp exists but is NOT loaded in Claude Code sessions
**Root Cause:** scriptboard-mcp is NOT registered in the active MCP configuration
**Solution:** Add scriptboard-mcp to `C:\Users\willh\.claude.json` under the `.mcp-servers` project scope

---

## 1. Official MCP Configuration Standards

### Configuration File Locations (Per Official Docs)

| Scope | Windows Path | Purpose |
|-------|--------------|---------|
| **User-level** | `%USERPROFILE%\.claude.json` | Global settings (all projects) |
| **Project-level** | `{project}\.mcp.json` | Team-shared (committed to git) |
| **Project settings** | `{project}\.claude\settings.local.json` | Personal overrides (gitignored) |
| **Enterprise** | `C:\Program Files\ClaudeCode\managed-mcp.json` | IT-managed (read-only) |

### Configuration Schema (Official)

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio|http|sse",
      "command": "/path/to/executable",
      "args": ["arg1", "arg2"],
      "env": {
        "KEY": "value"
      }
    }
  }
}
```

### Loading Precedence (Official)

1. **Enterprise** (highest) - IT-managed, cannot override
2. **Project** - `.mcp.json` in repo root
3. **User** (lowest) - `~/.claude.json` in home directory

---

## 2. Your Actual Configuration (Found)

### Primary Config File

**Location:** `C:\Users\willh\.claude.json`
**Size:** 28,300 tokens (very large - contains per-project settings)
**Structure:** Project-scoped configurations

### Active MCP Servers Configuration

**Path in .claude.json:**
`C:\Users\willh\.mcp-servers` → `mcpServers` object

**Current Registration (3 servers):**

```json
{
  "C:\\Users\\willh\\.mcp-servers": {
    "mcpServers": {
      "docs-mcp": {
        "type": "stdio",
        "command": "python",
        "args": ["C:/Users/willh/.mcp-servers/docs-mcp/server.py"],
        "env": {}
      },
      "personas-mcp": {
        "type": "stdio",
        "command": "python",
        "args": ["C:/Users/willh/.mcp-servers/personas-mcp/server.py"],
        "env": {}
      },
      "coderef-mcp": {
        "type": "stdio",
        "command": "python",
        "args": ["C:/Users/willh/.mcp-servers/coderef-mcp/server.py"],
        "env": {
          "CODEREF_CLI_PATH": "C:/Users/willh/Desktop/projects/coderef-system/packages/cli"
        }
      }
    }
  }
}
```

### Missing Server

**scriptboard-mcp:**
- ✅ Exists at: `C:\Users\willh\.mcp-servers\scriptboard-mcp\server.py`
- ✅ Has 8 tools defined
- ❌ NOT in `.claude.json` config
- ❌ NOT showing in `ListMcpResourcesTool`

---

## 3. Comparison: Official vs Your Setup

### Configuration Location

| Official Standard | Your Actual Setup | Match? |
|-------------------|-------------------|--------|
| `~/.claude.json` for global | `C:\Users\willh\.claude.json` | ✅ Yes |
| Project scope at `.mcp-servers` | `C:\Users\willh\.mcp-servers` key | ✅ Yes |
| `mcpServers` object | `mcpServers` object | ✅ Yes |

### Server Registration Format

| Field | Official | Your Setup | Match? |
|-------|----------|------------|--------|
| `type` | `"stdio"` for local | `"stdio"` | ✅ Yes |
| `command` | Full path or `python` | `"python"` | ✅ Yes |
| `args` | Array with script path | `["C:/Users/.../server.py"]` | ✅ Yes |
| `env` | Object (optional) | `{}` or specific vars | ✅ Yes |

**Path Format:** Forward slashes (`C:/Users/...`) - ✅ Correct (Windows accepts both)

---

## 4. Current MCP Server Inventory

### Registered and Working (3)

| Server | Location | Tools | Status |
|--------|----------|-------|--------|
| **docs-mcp** | `C:\Users\willh\.mcp-servers\docs-mcp\server.py` | 40+ | ✅ Loaded |
| **personas-mcp** | `C:\Users\willh\.mcp-servers\personas-mcp\server.py` | 8 | ✅ Loaded |
| **coderef-mcp** | `C:\Users\willh\.mcp-servers\coderef-mcp\server.py` | 7 | ✅ Loaded |

### Not Registered (1)

| Server | Location | Tools | Status |
|--------|----------|-------|--------|
| **scriptboard-mcp** | `C:\Users\willh\.mcp-servers\scriptboard-mcp\server.py` | 8 | ❌ NOT in config |

---

## 5. scriptboard-mcp Details

### Server Location

```
C:\Users\willh\.mcp-servers\scriptboard-mcp\
├── server.py           (MCP server entry point)
├── http_client.py      (Scriptboard HTTP client)
├── pyproject.toml      (Dependencies)
├── plan.json           (Feature plan)
└── tests/              (Test suite)
```

### Available Tools (8)

**Prompt Management:**
1. `mcp__scriptboard__set_prompt` - Set prompt text in Scriptboard
2. `mcp__scriptboard__clear_prompt` - Clear current prompt
3. `mcp__scriptboard__add_attachment` - Add file/code attachments
4. `mcp__scriptboard__clear_attachments` - Clear all attachments

**CodeRef Integration:**
5. `mcp__scriptboard__coderef_status` - Check CodeRef CLI availability
6. `mcp__scriptboard__coderef_scan` - Scan directory for code elements
7. `mcp__scriptboard__coderef_query` - Query dependencies/usages
8. `mcp__scriptboard__coderef_impact` - Analyze impact of changes

### Server Implementation

**Transport:** stdio (Python subprocess)
**Framework:** `mcp.server.Server`
**Communication:** stdin/stdout
**HTTP Backend:** Connects to Scriptboard app via `http_client.py`

---

## 6. Other MCP Config Files Found

### Cursor (IDE)

```
C:\Users\willh\.cursor\mcp.json
```

**Registered:**
- docs-mcp
- personas-mcp

### VS Code

```
C:\Users\willh\AppData\Roaming\Code\User\mcp.json
```

**Registered:**
- hello-mcp (demo server)

### Windsurf (IDE)

```
C:\Users\willh\.windsurf\mcp.json
C:\Users\willh\AppData\Roaming\Windsurf\User\mcp.json
```

**Note:** These are separate IDE configs, NOT used by Claude Code

---

## 7. The Fix: Add scriptboard-mcp

### Location to Edit

**File:** `C:\Users\willh\.claude.json`
**Section:** `"C:\\Users\\willh\\.mcp-servers"` → `"mcpServers"`

### Required Addition

Add this to the `mcpServers` object (alongside docs-mcp, personas-mcp, coderef-mcp):

```json
"scriptboard-mcp": {
  "type": "stdio",
  "command": "python",
  "args": ["C:/Users/willh/.mcp-servers/scriptboard-mcp/server.py"],
  "env": {}
}
```

### Full Context (After Fix)

```json
{
  "C:\\Users\\willh\\.mcp-servers": {
    "mcpServers": {
      "docs-mcp": {
        "type": "stdio",
        "command": "python",
        "args": ["C:/Users/willh/.mcp-servers/docs-mcp/server.py"],
        "env": {}
      },
      "personas-mcp": {
        "type": "stdio",
        "command": "python",
        "args": ["C:/Users/willh/.mcp-servers/personas-mcp/server.py"],
        "env": {}
      },
      "coderef-mcp": {
        "type": "stdio",
        "command": "python",
        "args": ["C:/Users/willh/.mcp-servers/coderef-mcp/server.py"],
        "env": {
          "CODEREF_CLI_PATH": "C:/Users/willh/Desktop/projects/coderef-system/packages/cli"
        }
      },
      "scriptboard-mcp": {
        "type": "stdio",
        "command": "python",
        "args": ["C:/Users/willh/.mcp-servers/scriptboard-mcp/server.py"],
        "env": {}
      }
    }
  }
}
```

---

## 8. Validation Steps

### Before Making Changes

```bash
# 1. Test scriptboard-mcp runs manually
python C:\Users\willh\.mcp-servers\scriptboard-mcp\server.py

# 2. Verify Python dependencies
pip list | findstr mcp

# 3. Current server count
# Expected: 3 servers (docs-mcp, personas-mcp, coderef-mcp)
```

### After Adding scriptboard-mcp

```bash
# 1. Restart Claude Code session (close and reopen)

# 2. Verify 4 servers loaded
# Run: ListMcpResourcesTool
# Expected: docs-mcp, coderef-mcp, personas-mcp, scriptboard-mcp

# 3. Test a scriptboard-mcp tool
# Try: mcp__scriptboard__coderef_status
# Expected: Returns CLI status

# 4. Check tool palette
# Look for: mcp__scriptboard__* tools (8 total)
```

### Success Criteria

- [ ] `.claude.json` updated with scriptboard-mcp entry
- [ ] Claude Code session restarted
- [ ] `ListMcpResourcesTool` returns 4 servers (not 3)
- [ ] `mcp__scriptboard__coderef_status` tool is callable
- [ ] All 8 scriptboard-mcp tools appear in tool palette
- [ ] No error messages in Claude Code logs

---

## 9. Why This Happened

### Root Cause

**scriptboard-mcp was created but never registered** in `.claude.json`

**Timeline:**
1. ✅ scriptboard-mcp server developed
2. ✅ 8 tools implemented
3. ✅ Server tested manually
4. ❌ **NEVER added to .claude.json config**
5. ❌ Claude Code never knew to load it

### Similar Servers (Working)

**docs-mcp, personas-mcp, coderef-mcp:**
- ✅ Created
- ✅ Implemented
- ✅ **Registered in .claude.json**
- ✅ Loaded by Claude Code

---

## 10. Related Issues

### STUB-001: scriptboard-assistant-integration

**Blocked by this issue:**
> "Make Scriptboard the primary visual UI for this CLI assistant"

**Requires:**
- ✅ scriptboard-mcp loaded (this fix)
- ⬜ Integration workflow between orchestrator and Scriptboard
- ⬜ Handoff prompts exported to Scriptboard UI

### Future Enhancements

1. **Auto-discovery:** Scan `.mcp-servers/` and auto-register valid servers
2. **Config validation:** Tool to verify all servers in directory are registered
3. **MCP server template:** Scaffold new servers with auto-registration

---

## 11. Configuration Best Practices

### From Official Docs

1. **Use project scope** for team MCP servers (`.mcp.json` in repo)
2. **Use user scope** for personal tools (`~/.claude.json`)
3. **Use forward slashes** in paths (Windows accepts both)
4. **Test manually first** before adding to config
5. **Restart Claude Code** after config changes

### Your Setup (Recommended)

**Keep using:**
- ✅ `.claude.json` for MCP server registration
- ✅ Project scope: `C:\Users\willh\.mcp-servers`
- ✅ stdio transport for local Python servers
- ✅ Forward slash paths (`C:/Users/...`)

**Add scriptboard-mcp** to existing pattern

---

## 12. Action Items

### Immediate (Fix STUB-046)

1. [ ] Edit `C:\Users\willh\.claude.json`
2. [ ] Add scriptboard-mcp to `mcpServers` object
3. [ ] Save file
4. [ ] Restart Claude Code session
5. [ ] Verify with `ListMcpResourcesTool`
6. [ ] Test `mcp__scriptboard__coderef_status`

### Follow-up (STUB-001)

1. [ ] Test all 8 scriptboard-mcp tools
2. [ ] Create integration workflow docs
3. [ ] Update CLAUDE.md with scriptboard-mcp usage
4. [ ] Promote STUB-001 to workorder

---

## 13. References

### Official Documentation

- **MCP Guide:** https://code.claude.com/docs/en/mcp.md
- **Settings Reference:** https://code.claude.com/docs/en/settings.md
- **Setup/Installation:** https://code.claude.com/docs/en/setup.md

### Files Investigated

| File | Purpose | Status |
|------|---------|--------|
| `C:\Users\willh\.claude.json` | Active MCP config | ✅ Found |
| `C:\Users\willh\.mcp-servers\scriptboard-mcp\server.py` | Server entry point | ✅ Exists |
| `C:\Users\willh\.cursor\mcp.json` | Cursor IDE config | ℹ️ Separate |
| `C:\Users\willh\AppData\Roaming\Code\User\mcp.json` | VS Code config | ℹ️ Separate |

### Search Results

Searched for MCP config files:
- Found 10+ config files across different IDEs
- Identified active config: `C:\Users\willh\.claude.json`
- Confirmed 3 servers registered, 1 missing

---

## Conclusion

**Problem:** scriptboard-mcp not loading
**Cause:** Not registered in `.claude.json`
**Solution:** Add 5-line JSON object to `mcpServers`
**Effort:** < 5 minutes
**Impact:** Unlocks 8 tools + STUB-001 integration

**Your configuration follows official standards.** The only issue is a missing server registration. Once added, scriptboard-mcp will load automatically on next session start.

---

**Report Complete.**
**Status:** STUB-046 investigation complete, ready for implementation.
**Next:** Apply fix and validate.
