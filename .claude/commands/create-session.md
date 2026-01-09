# Create Multi-Agent Session

**Task:** Create a new multi-agent session following the agentic communication pattern.

**Pattern:** Sessions use one consolidated instructions.json file:
1. **communication.json** - Agent roster and progress tracking
2. **instructions.json** - Single document with ALL instructions (orchestrator + agents)
3. **README.md** - User-facing documentation explaining the session

---

## Step 1: Gather Session Details

Ask the user for:
1. **Session name** (kebab-case, e.g., "document-effectiveness")
2. **Workorder ID** (e.g., "WO-DOCUMENT-EFFECTIVENESS-001")
3. **Task description** (what agents will do)
4. **Output format** (JSON, markdown, etc.)
5. **Which agents participate** (default: all 9 agents, or specific subset)

---

## Step 2: Create Session Directory

Create: `C:\Users\willh\.mcp-servers\coderef\sessions\{session-name}\`

---

## Step 3: Create communication.json

```json
{
  "workorder_id": "WO-{CATEGORY}-{ID}",
  "feature_name": "{session-name}",
  "created": "{YYYY-MM-DD}",
  "status": "not_started",
  "description": "{Brief description of what agents will do}",
  "instructions_file": "C:\\Users\\willh\\.mcp-servers\\coderef\\sessions\\{session-name}\\instructions.json",

  "orchestrator": {
    "agent_id": "coderef",
    "agent_path": "C:\\Users\\willh\\.mcp-servers\\coderef",
    "role": "{Specific role for this session}",
    "output_file": "C:\\Users\\willh\\.mcp-servers\\coderef\\sessions\\{session-name}\\orchestrator-output.{ext}",
    "status": "not_started",
    "notes": ""
  },

  "agents": [
    {
      "agent_id": "{agent-name}",
      "agent_path": "{agent-path}",
      "role": "{Agent-specific role}",
      "output_file": "C:\\Users\\willh\\.mcp-servers\\coderef\\sessions\\{session-name}\\{agent-name}-output.{ext}",
      "status": "not_started",
      "notes": ""
    }
  ],

  "aggregation": {
    "total_agents": {count},
    "completed": 0,
    "pending": 0,
    "not_started": {count}
  }
}
```

---

## Step 4: Create instructions.json

**One consolidated document with sections for orchestrator AND agents:**

```json
{
  "workorder_id": "WO-{CATEGORY}-{ID}",
  "task": "{Clear task name}",
  "description": "{What agents need to do}",

  "orchestrator_instructions": {
    "role": "{What orchestrator does in this session}",
    "steps": {
      "step_1": "READ {what}",
      "step_2": "ANALYZE {what}",
      "step_3": "SYNTHESIZE {what}"
    }
  },

  "agent_instructions": {
    "role": "{What agents do in this session}",
    "steps": {
      "step_1": "READ {what}",
      "step_2": "ANALYZE {what}",
      "step_3": "CREATE output at path in communication.json"
    }
  },

  "output_format": "{json|markdown|text}",

  "output_template": "{Expected structure - show example}",

  "quality_standards": {
    "completeness": "{What makes output complete}",
    "accuracy": "{What makes output accurate}",
    "format": "{Required format rules}"
  }
}
```

---

## Step 5: Create README.md (User Documentation)

**IMPORTANT:** Create user-facing documentation in the session directory.

Create: `C:\Users\willh\.mcp-servers\coderef\sessions\{session-name}\README.md`

```markdown
# {Session Name}

**Workorder ID:** WO-{CATEGORY}-{ID}
**Created:** {YYYY-MM-DD}
**Status:** Not Started

---

## Purpose

{1-2 sentence description of what this session accomplishes}

---

## Agents Involved

| Agent | Role | Output |
|-------|------|--------|
| orchestrator | {role} | orchestrator-output.{ext} |
| {agent-1} | {role} | {agent-1}-output.{ext} |
| {agent-2} | {role} | {agent-2}-output.{ext} |

---

## How It Works

1. **Agents read** communication.json to find their assigned task
2. **Agents follow** instructions.json for step-by-step guidance
3. **Agents create** output files at their designated paths
4. **Orchestrator aggregates** all agent outputs into final synthesis

---

## Files

- **communication.json** - Agent roster, status tracking, output paths
- **instructions.json** - Consolidated instructions for orchestrator + agents
- **README.md** - This file (user documentation)
- **orchestrator-output.{ext}** - Orchestrator's aggregated output
- **{agent}-output.{ext}** - Individual agent outputs

---

## Execution Steps

### For Agents:

1. Navigate to your agent path
2. Open communication.json
3. Find your entry in the `agents[]` array
4. Read instructions.json → follow `agent_instructions` section
5. Execute your task
6. Create output at your `output_file` path
7. Update your `status` in communication.json: "not_started" → "complete"

### For Orchestrator:

1. Wait for all agents to complete
2. Read all agent output files
3. Follow `orchestrator_instructions` in instructions.json
4. Create aggregated output at `orchestrator.output_file` path
5. Update `orchestrator.status` in communication.json

---

## Current Status

**Not Started** - Agents have not begun execution yet.

Check communication.json for real-time progress tracking.

---

**Session Directory:** `C:\Users\willh\.mcp-servers\coderef\sessions\{session-name}\`
```

---

## Step 6: Log and Track

1. **Add to workorder-log.txt** using mcp__coderef-workflow__log_workorder:
```
WO-{CATEGORY}-{ID} | coderef-ecosystem | {description} | {timestamp}
```

2. **Add to SESSION-INDEX.md** under Active Sessions

---

## Step 7: Confirm with User

Show user:
- Session directory path
- communication.json path (agent roster)
- instructions.json path (one file with orchestrator + agent instructions)
- README.md path (user documentation)
- Expected outputs (orchestrator + N agent output files)

---

## Example Usage

**User:** "Create session for agents to audit code complexity"

**Assistant creates:**
- `sessions/code-complexity-audit/communication.json` (agent roster)
- `sessions/code-complexity-audit/instructions.json` (orchestrator + agent instructions)
- `sessions/code-complexity-audit/README.md` (user documentation)
- Logs WO-CODE-COMPLEXITY-AUDIT-001
- Updates SESSION-INDEX.md

**Result:** Agents read communication.json and instructions.json, follow steps, and create outputs. Users read README.md to understand the session.

---

## Agent Roster (Default 9 Agents)

When user doesn't specify agents, include all 9:

1. **coderef-assistant** - `C:\Users\willh\Desktop\assistant`
2. **coderef-context** - `C:\Users\willh\.mcp-servers\coderef-context`
3. **coderef-workflow** - `C:\Users\willh\.mcp-servers\coderef-workflow`
4. **coderef-docs** - `C:\Users\willh\.mcp-servers\coderef-docs`
5. **coderef-personas** - `C:\Users\willh\.mcp-servers\coderef-personas`
6. **coderef-testing** - `C:\Users\willh\.mcp-servers\coderef-testing`
7. **papertrail** - `C:\Users\willh\.mcp-servers\papertrail`
8. **coderef-system** - `C:\Users\willh\Desktop\projects\coderef-system`
9. **coderef-dashboard** - `C:\Users\willh\Desktop\coderef-dashboard`

---

## Pattern Reference

**Session Directory Structure:**
```
sessions/{session-name}/
├── communication.json          # Agent roster and progress tracking
├── instructions.json           # Orchestrator + agent instructions (consolidated)
├── README.md                   # User documentation (this file)
├── orchestrator-output.{ext}   # Orchestrator synthesis output
├── agent-1-output.{ext}        # Agent 1 output
├── agent-2-output.{ext}        # Agent 2 output
└── ...
```

---

**Key Improvements:**

1. **README.md added** - User-facing documentation explains session to humans
2. **One instructions.json** - Orchestrator and agents share single file with separate sections
3. **Clear role separation** - `orchestrator_instructions` vs `agent_instructions`
4. **Simplified file structure** - Three core files (communication, instructions, README)
