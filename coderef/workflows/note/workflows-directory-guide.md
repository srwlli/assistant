# Workflows Directory Guide

**Location:** `coderef/workflows/`
**Purpose:** Centralized reference for workflow processes, tools, and standards

---

## WHAT

**A knowledge base for workflow definitions, technical standards, and process documentation**

### What It Contains
- Workflow process definitions (.md + .json pairs)
- Tool/feature technical standards
- Human-readable guides (.md)
- Machine-readable schemas (.json)

### What It's For
- AI agents needing technical context
- Humans learning workflow processes
- Reference during implementation
- Standardization across ecosystem

### What It Produces
- Consistent workflow patterns
- Reusable process templates
- Clear technical specifications
- Shared understanding across teams

---

## HOW

### How Files Are Organized

**Paired Documentation Pattern:**
- `{name}.md` - Human-readable (WHAT/HOW/WHY format)
- `{name}.json` - Machine-readable (complete schema)

**Example:**
```
workflows/
├── coderef-improvement-workflow-process.md
├── coderef-improvement-workflow-process.json
├── coderef-dashboard-prompts-workflow-standards.md
└── coderef-dashboard-prompts-workflow-standards.json
```

### How to Use This Directory

**For Humans:**
1. Read `.md` files for quick understanding
2. Use WHAT/HOW/WHY structure to navigate
3. Reference examples and use cases
4. Follow step-by-step instructions

**For AI Agents:**
1. Read `.json` files for complete schema
2. Parse structured data programmatically
3. Generate implementations from templates
4. Validate against defined schemas

### How to Add New Workflows

**Step 1: Create Markdown Guide**
- Use WHAT/HOW/WHY structure
- Keep it brief, list-based, precise
- Include use cases and examples
- Add clear extension points

**Step 2: Create JSON Schema**
- Define complete data structures
- Include all technical details
- Add validation rules
- Document agent instructions

**Step 3: Name Consistently**
- Use kebab-case
- Match .md and .json names
- Be descriptive but concise

---

## WHY

### Why This Directory Exists

**Problem:** Workflow knowledge scattered across conversations
- No single source of truth
- Inconsistent process documentation
- Hard to onboard new agents
- Duplicate effort recreating workflows

**Solution:** Centralized workflow repository
- Single location for all workflows
- Paired human/AI documentation
- Version-controlled knowledge base
- Reusable across projects

### Why Paired .md + .json

**Different Audiences:**
- Humans need context and narrative
- AI agents need structured data
- Both need same information, different formats

**Complementary Strengths:**
- .md for understanding (why and context)
- .json for implementation (what and how)
- Together: complete picture

**Maintainability:**
- Update both when workflow changes
- Keep them in sync
- Single source of truth per workflow

### Why in coderef/

**Ecosystem Integration:**
- Part of coderef documentation system
- Alongside foundation docs and standards
- Discoverable via coderef tools
- Version-controlled with ecosystem

**Standardization:**
- Follows coderef conventions
- Compatible with coderef-docs tools
- Integrates with dashboard
- Supports multi-agent workflows

---

## Current Workflows

### coderef-improvement-workflow-process
**Purpose:** Standardized process for ecosystem improvements through agent review

**Key Features:**
- Tag-based review scoping (40+ tags)
- Multi-agent coordination via communication.json
- Structured analysis + freeform comments
- 5-phase workflow (define → generate → review → track → aggregate)

**Use Cases:**
- Document effectiveness audits
- Code quality reviews
- Workflow optimization
- Integration testing
- Standards compliance checks

### coderef-dashboard-prompts-workflow-standards
**Purpose:** Technical reference for dashboard prompting workflow system

**Key Features:**
- React Context + composition architecture
- 5-step workflow (select → attach → review → export → save)
- Multiple export formats (JSON, Markdown, Session)
- Extension points for new prompts/formats

**Use Cases:**
- Code review workflows
- Planning workflows
- Agent review workflows
- Custom prompt creation

---

## Naming Conventions

### File Names
- Format: `{workflow-name}.md` / `{workflow-name}.json`
- Use kebab-case
- Be descriptive
- Keep concise

**Examples:**
- ✅ `coderef-improvement-workflow-process.md`
- ✅ `agent-coordination-handoff.json`
- ❌ `workflow1.md` (not descriptive)
- ❌ `CodeRefProcess.md` (not kebab-case)

### Workflow Names
- Start with domain/scope
- End with type (workflow, process, standards, guide)
- Include version if needed

**Examples:**
- `coderef-improvement-workflow-process`
- `dashboard-prompts-workflow-standards`
- `agent-handoff-protocol-v2`

---

## File Structure Templates

### Markdown (.md) Template

```markdown
# {Workflow Name}

**Version:** X.Y.Z
**Purpose:** Brief description

---

## WHAT
- What it does
- What it requires
- What it produces

## HOW
- How it works (steps)
- How to use it
- How to extend it

## WHY
- Why it exists (problem/solution)
- Why this approach
- Why these choices

---

[Additional sections as needed]
```

### JSON (.json) Template

```json
{
  "workflow_name": "workflow-name",
  "version": "X.Y.Z",
  "purpose": "Brief description",
  "workflow_definition": {},
  "data_structures": {},
  "use_cases": [],
  "agent_instructions": {},
  "validation_rules": {},
  "future_enhancements": []
}
```

---

## Best Practices

### Documentation
- Keep .md concise (aim for <500 lines)
- Use examples liberally
- Include use cases
- Add clear next steps

### Schema
- Define all required fields
- Include validation rules
- Document expected formats
- Provide examples

### Maintenance
- Update both files together
- Version changes appropriately
- Test with actual workflows
- Archive deprecated versions

### Discovery
- Reference workflows in other docs
- Link from CLAUDE.md when relevant
- Include in foundation docs
- Add to dashboard if applicable

---

## Integration Points

### With Foundation Docs
- Workflows referenced in ARCHITECTURE.md
- Process flows documented in foundation docs
- Standards enforcement via workflows

### With Dashboard
- Workflow creation UI reads from schemas
- Status tracking uses communication.json format
- Export formats follow standards

### With Agents
- Agents read .json for implementation
- Personas reference workflows
- Coordination via defined protocols

### With Workorders
- Workflows create workorder artifacts
- Communication.json tracks execution
- Standards validate deliverables

---

## Future Additions

**Planned Workflows:**
- `agent-handoff-protocol` - Standardized agent-to-agent handoff
- `workorder-lifecycle` - Complete workorder workflow
- `documentation-generation` - Auto-doc workflows
- `testing-coordination` - Multi-agent test workflows
- `release-process` - Version/release workflows

**Templates:**
- Workflow creation wizard
- Communication.json generator
- Analysis structure builder
- Tag taxonomy extension guide
