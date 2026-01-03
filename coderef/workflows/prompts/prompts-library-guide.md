# Prompts Library Guide

**Location:** `coderef/workflows/prompts/`
**Purpose:** Centralized library of reusable prompts for various workflow tasks

---

## WHAT

**A curated collection of prompt templates for AI-assisted workflows across the coderef ecosystem**

### What It Contains
- Code review prompts
- Planning and analysis prompts
- Documentation generation prompts
- Agent coordination prompts
- Quality assurance prompts
- Improvement review prompts

### What It Provides
- Consistent prompt structure
- Reusable templates with variables
- Category-based organization
- Tag-based filtering
- Version-controlled prompts

### What It Produces
- Standardized LLM interactions
- Predictable output formats
- Improved prompt engineering
- Reduced prompt duplication

---

## HOW

### How Prompts Are Structured

**Prompt Schema:**
```
- key: unique identifier (kebab-case)
- name: Display name
- description: Purpose and use case
- template: Actual prompt text with {{variables}}
- category: Grouping (code-review, planning, documentation, etc.)
- tags: Metadata for filtering
- variables: List of required/optional variables
- expected_output: Format of LLM response
```

### How to Use Prompts

**Step 1: Browse Library**
- Navigate by category or search by tags
- Read description to find right prompt
- Check required variables

**Step 2: Prepare Variables**
- Gather values for {{placeholders}}
- Prepare attachments if needed
- Review constraints

**Step 3: Apply Prompt**
- Replace {{variables}} with actual values
- Add context/attachments
- Submit to LLM

**Step 4: Process Output**
- Parse expected_output format
- Validate against schema
- Save/archive results

### How to Add New Prompts

**Step 1: Define Prompt**
```json
{
  "key": "unique-prompt-key",
  "name": "Display Name",
  "description": "What this prompt does",
  "template": "Prompt text with {{variable}}",
  "category": "code-review",
  "tags": ["review", "quality"],
  "variables": {
    "required": ["variable"],
    "optional": ["optional_var"]
  },
  "expected_output": "format description"
}
```

**Step 2: Add to Library**
- Save to appropriate category folder
- Follow naming convention
- Update prompts registry

**Step 3: Document**
- Add usage example
- Note integration points
- Link related prompts

---

## WHY

### Why Centralized Prompts

**Problem:** Prompts scattered across conversations
- Duplication and inconsistency
- Hard to discover existing prompts
- No version control
- Difficult to improve iteratively

**Solution:** Centralized prompt library
- Single source of truth
- Easy discovery via categories/tags
- Version-controlled improvements
- Reusable across workflows

### Why Templates with Variables

**Flexibility:**
- One prompt, many use cases
- Customize without rewriting
- Maintain consistency while adapting

**Maintainability:**
- Update template, all uses benefit
- Clear separation of structure vs content
- Easy to test variations

**Documentation:**
- Variables document required inputs
- Expected outputs clarify usage
- Examples show substitution

### Why Category + Tag System

**Multiple Access Paths:**
- Browse by category (general grouping)
- Filter by tags (specific features)
- Search across both dimensions

**Scalability:**
- Add new categories as needed
- Tag prompts with multiple attributes
- Cross-category discovery

**Organization:**
- Logical grouping for humans
- Machine-searchable metadata
- Supports complex queries

---

## Prompt Categories

### Code Review
**Purpose:** Analyze code quality, patterns, and standards compliance

**Prompts:**
- `code-review-comprehensive` - Full codebase review
- `code-review-focused` - Specific file/module review
- `code-review-security` - Security vulnerability scan
- `code-review-performance` - Performance optimization suggestions

### Planning & Analysis
**Purpose:** Generate implementation plans and technical analysis

**Prompts:**
- `feature-planning` - Complete feature implementation plan
- `technical-analysis` - Analyze technical approach/architecture
- `risk-assessment` - Identify risks and mitigation strategies
- `effort-estimation` - Estimate complexity and time

### Documentation
**Purpose:** Generate or improve documentation

**Prompts:**
- `api-documentation` - Generate API docs from code
- `readme-generation` - Create comprehensive README
- `architecture-documentation` - Document system architecture
- `changelog-entry` - Generate changelog entries

### Agent Coordination
**Purpose:** Multi-agent workflow coordination

**Prompts:**
- `agent-review-assignment` - Assign review tasks to agents
- `agent-handoff` - Generate agent handoff prompts
- `communication-json-generation` - Create coordination files
- `status-aggregation` - Summarize multi-agent progress

### Quality Assurance
**Purpose:** Testing and validation prompts

**Prompts:**
- `test-generation` - Generate test cases
- `test-coverage-analysis` - Analyze test coverage gaps
- `validation-checklist` - Create validation checklists
- `acceptance-criteria` - Define acceptance criteria

### Improvement Review
**Purpose:** Ecosystem improvement and optimization

**Prompts:**
- `document-effectiveness-audit` - Review documentation usage
- `workflow-optimization` - Analyze and improve workflows
- `integration-testing` - Review integration points
- `standards-compliance` - Check standards adherence

---

## Tag Taxonomy

### Scope Tags
- `code` - Code-related prompts
- `docs` - Documentation prompts
- `workflow` - Process/workflow prompts
- `testing` - Testing/QA prompts
- `planning` - Planning/analysis prompts

### Function Tags
- `review` - Review and analysis
- `generation` - Content generation
- `validation` - Validation and checking
- `coordination` - Multi-agent coordination
- `optimization` - Improvement and optimization

### Output Tags
- `json` - Produces JSON output
- `markdown` - Produces Markdown output
- `checklist` - Produces checklist format
- `report` - Produces report format
- `communication` - Produces communication.json

### Domain Tags
- `coderef` - Coderef ecosystem specific
- `dashboard` - Dashboard integration
- `mcp` - MCP server related
- `agent` - Agent coordination
- `workorder` - Workorder management

---

## Prompt Template Format

### Basic Structure
```
[ROLE DEFINITION]
You are a {role} with expertise in {domain}.

[CONTEXT]
{context_description}

[TASK]
{task_description}

[INPUTS]
{{variable_1}}
{{variable_2}}

[CONSTRAINTS]
- Constraint 1
- Constraint 2

[EXPECTED OUTPUT]
{output_format_description}

[EXAMPLES]
{optional_examples}
```

### Variable Syntax
- Required: `{{variable_name}}`
- Optional: `{{variable_name?}}`
- Default: `{{variable_name:default_value}}`
- Multiple: `{{variable_name...}}`

### Output Format Specification
```json
"expected_output": {
  "format": "json|markdown|plaintext",
  "structure": {
    "field1": "description",
    "field2": "description"
  },
  "example": "sample output"
}
```

---

## Integration Points

### With Dashboard Prompting Workflow
- Dashboard reads prompts from this library
- PromptSelector component uses category/tag filters
- Export formats match expected_output specs
- Variables populated via UI forms

### With Improvement Workflow
- Agent review prompts use tag taxonomy
- Communication.json generation prompts
- Aggregation and reporting prompts
- Status tracking prompts

### With Workorder System
- Planning prompts generate plan.json
- Handoff prompts create agent instructions
- Validation prompts check deliverables
- Archive prompts finalize workorders

### With Foundation Docs
- Documentation generation prompts
- Architecture documentation updates
- API reference generation
- Standards documentation

---

## Usage Examples

### Example 1: Code Review
```
Prompt: code-review-focused
Variables:
  {{file_path}}: src/components/PromptingWorkflow.tsx
  {{review_focus}}: React hooks usage and state management
  {{standards}}: React best practices, TypeScript strict mode

Expected Output: JSON
{
  "issues": [...],
  "suggestions": [...],
  "compliance": {...}
}
```

### Example 2: Agent Review Assignment
```
Prompt: agent-review-assignment
Variables:
  {{review_scope}}: docs:foundation, docs:standards
  {{agents}}: coderef-context, coderef-workflow, coderef-docs
  {{task_name}}: document-effectiveness-audit

Expected Output: communication.json file
```

### Example 3: Feature Planning
```
Prompt: feature-planning
Variables:
  {{feature_name}}: coderef-prompting-workflows
  {{requirements}}: Standardize agent reviews, Tag taxonomy, Dashboard UI
  {{constraints}}: Must work with existing agents, JSON-based coordination

Expected Output: plan.json with 10 sections
```

---

## Best Practices

### Prompt Design
- Start with clear role definition
- Provide sufficient context
- Be specific about task requirements
- Define constraints explicitly
- Specify exact output format
- Include examples when helpful

### Variable Usage
- Keep variable names descriptive
- Document required vs optional
- Provide sensible defaults
- Validate variable values
- Use consistent naming conventions

### Testing
- Test with various input combinations
- Validate output formats
- Check edge cases
- Iterate based on results
- Version significant changes

### Maintenance
- Review prompts quarterly
- Update based on feedback
- Archive deprecated prompts
- Document changes in changelog
- Test after modifications

---

## Future Enhancements

### Planned Features
- Prompt versioning system
- A/B testing framework
- Output validation schemas
- Prompt composition (combine multiple prompts)
- Dynamic variable injection
- Context-aware suggestions
- Performance metrics tracking

### Planned Prompts
- `multi-agent-orchestration` - Coordinate complex multi-agent workflows
- `dependency-analysis` - Analyze and visualize dependencies
- `migration-planning` - Plan code/system migrations
- `refactoring-suggestions` - Suggest refactoring opportunities
- `knowledge-extraction` - Extract knowledge from codebases

### Integration Improvements
- Auto-discovery of prompts in dashboard
- Prompt recommendation engine
- Variable auto-population from context
- Real-time validation
- LLM API integration (direct execution)
