# Tool Inventory Workflow - Brain Dump

> Session: 2025-12-16
> Status: Capturing ideas

---

## Core Insight

**This assistant = Orchestrator, NOT executor**

Each project already has an embedded Lloyd with the best context. This tool:
- **Identifies** projects/tools
- **Delegates** to embedded agents
- **Collects** formatted results
- **Aggregates** into inventory

---

## Architecture

```
This Assistant (Orchestrator)
       │
       ├── Scans for projects
       ├── Identifies which have embedded Lloyd
       ├── Sends prompt via communication.json pattern
       │
       ▼
Project-Embedded Lloyd (Executor)
       │
       ├── Has full project context
       ├── Generates features.md (or structured output)
       ├── Returns formatted result
       │
       ▼
This Assistant (Aggregator)
       │
       ├── Collects all results
       ├── Builds master inventory
       └── Surfaces in Scriptboard
```

---

## Existing Patterns to Use

- `/agentic-workflow` - multi-agent coordination
- `communication.json` - agent communication protocol
- Embedded Lloyd - project-specific context

---

## Workflow Steps (Draft)

1. **Discover** - Scan for projects with embedded agents
2. **Prompt** - Send structured request to each Lloyd
   - "Generate a features.md for this project"
   - "What can this tool do?"
   - Standard format/schema
3. **Collect** - Receive formatted responses
4. **Aggregate** - Build master inventory index
5. **Surface** - Display in Scriptboard dashboard

---

## Open Questions

- [ ] Where do embedded Lloyds live? (CLAUDE.md? .claude folder?)
- [ ] What's the communication.json schema?
- [ ] How does delegation actually work? (spawn agent? file-based?)
- [ ] What's the standard output format for features?

---

## Related Stubs

- `scriptboard-assistant-integration` - where inventory lives visually
- `reorganize-gits-projects` - may surface projects to inventory

---

## Raw Ideas (Unprocessed)

- This assistant specializes in orchestration, not execution
- Each tool knows itself best
- Leverage existing agent infrastructure
- Don't duplicate context - delegate to where context lives
- Scriptboard = visual home for aggregated data
