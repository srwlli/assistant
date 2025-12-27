# MCP Refactor - Architecture Layers

## Clear Separation of Concerns

```
Layer 5: coderef-personas
└── "How should agents behave?"

Layer 4: coderef-workflow
└── "How should work be orchestrated?"

Layer 3: coderef-context
└── "What exists in the code and what matters?"

Layer 2: coderef-docs
└── "What should humans/agents read as reference?"

Layer 1: Code
└── The actual implementation
```

---

## No Overlap

| System           | Owns                                                                         | Doesn't Own                                             |
|------------------|------------------------------------------------------------------------------|---------------------------------------------------------|
| coderef-context  | Code analysis, pattern discovery, complexity scoring, task-specific insights | Documentation writing, orchestration, agent behavior    |
| coderef-docs     | Foundation docs (README, ARCHITECTURE, API, SCHEMA), standards publishing    | Code analysis, task planning, agent behavior            |
| coderef-workflow | Orchestrating flows, embedding context, progress tracking                    | Code analysis, documentation generation, agent behavior |
| coderef-personas | Agent specialized behaviors, tool usage patterns                             | Everything else                                         |

---

## Data Flow (Clean)

```
Code
  ↓
coderef-context analyzes
  ├→ codebase-context.json (general)
  └→ task-context.json (task-specific)
  ↓
coderef-docs generates foundation docs
  ├→ README.md
  ├→ ARCHITECTURE.md
  ├→ API.md
  ├→ SCHEMA.md
  └→ STANDARDS.md
  ↓
coderef-workflow orchestrates
  ├→ Uses both contexts
  ├→ Embeds in task description
  └→ Agents implement
  ↓
coderef-personas
  └→ Specialized agent execution
```
