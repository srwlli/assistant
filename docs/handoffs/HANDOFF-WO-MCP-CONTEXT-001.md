# WO-MCP-CONTEXT-001: Deep-Dive Analysis - Coderef-Context Server

**Workorder:** WO-MCP-CONTEXT-001
**Session:** MCP-Server-Capabilities-Deep-Dive
**Phase:** 1 (Individual Analysis)
**Agent:** Context Analysis Agent
**Location:** `C:\Users\willh\.mcp-servers\coderef-context\`

---

## Your Task

You are the subject matter expert for the coderef-context MCP server. Conduct a comprehensive deep-dive analysis of your server's current capabilities, limitations, and architectural role within the ecosystem.

---

## What to Analyze

1. **All Tools/Functions:**
   - Name, parameters, return types
   - What each tool does (purpose)
   - Known limitations or constraints
   - Performance characteristics (speed, accuracy)

2. **Capabilities:**
   - What does this server do exceptionally well?
   - What are its core strengths?
   - What problems does it solve?

3. **Limitations:**
   - What can't it do?
   - Where does it fail or struggle?
   - What edge cases break it?

4. **Gaps:**
   - What features should exist but don't?
   - What's blocking full potential?
   - What would unlock new use cases?

5. **Dependencies:**
   - Does this server depend on other servers?
   - Which servers depend on this one?
   - Are these dependencies explicit or implicit?

6. **Performance Profile:**
   - Speed: fast/medium/slow
   - Scalability: how does it handle large inputs?
   - Accuracy: how reliable are the results?

---

## Output Format

Update `C:\Users\willh\Desktop\assistant\session-mcp-capabilities.json`

In the `servers.coderef-context` section, add:

```json
{
  "tools": [
    {
      "name": "tool_name",
      "parameters": ["param1", "param2"],
      "purpose": "what it does",
      "limitation": "known constraints"
    }
  ],
  "capabilities": ["list", "of", "strengths"],
  "limitations": ["list", "of", "constraints"],
  "gaps": ["missing", "features"],
  "dependencies_on": ["server_x", "server_y"],
  "provides_to": ["server_a", "server_b"],
  "performance_profile": {
    "speed": "fast/medium/slow",
    "scalability": "description",
    "accuracy": "high/medium/low"
  },
  "notes": "any additional insights"
}
```

---

## Completion Checklist

- [ ] Read all tools in this server
- [ ] Document each tool with name, params, purpose, limitation
- [ ] Identify 3+ capabilities
- [ ] Identify 3+ limitations
- [ ] Identify 2+ gaps
- [ ] List dependencies (both directions)
- [ ] Document performance profile
- [ ] Update session-mcp-capabilities.json
- [ ] Set `analysis_complete` to `true`
- [ ] Set `agent_status` to `complete`

---

## Reference Files

- **Communication:** `C:\Users\willh\.mcp-servers\coderef-context\communication.json`
- **Shared Doc:** `C:\Users\willh\Desktop\assistant\session-mcp-capabilities.json`
- **Session Status:** Check shared doc for other agents' progress

---

## Next Phase (After All Agents Complete)

Once all 4 agents (context, workflow, docs, personas) complete Phase 1:
- Phase 2: Cross-server sync (analyze overlaps, gaps, dependencies)
- Phase 3: Aggregate roadmap (priorities, improvements, next actions)

**You will be recalled for Phase 2 to review other agents' findings.**
