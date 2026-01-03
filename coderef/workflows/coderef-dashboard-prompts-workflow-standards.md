# CodeRef Dashboard - Prompting Workflow Standards

**Version:** 1.0.0
**Route:** `/prompts`

---

## WHAT

**A workflow builder UI for constructing prompts with attachments and exporting for LLM use**

### What It Does
- Lets users select predefined prompts
- Attach files/documents as context
- Export complete workflows in multiple formats (JSON, Markdown)
- Save LLM responses for session tracking

### What It Requires
- Prompt selection (from library)
- At least 1 attachment
- Browser environment (Next.js dashboard)

### What It Produces
- `workflow_{name}_{timestamp}.json` - Structured workflow data
- `workflow_{name}_{timestamp}.md` - Human-readable format
- `session_{timestamp}.json` - Complete session with LLM result

---

## HOW

### How It Works (5 Steps)

1. **Select Prompt** - Choose from predefined library (`prompts.ts`)
2. **Add Attachments** - Upload files via file picker
3. **Review Metadata** - Automatic summary display
4. **Export** - Copy to clipboard or save file
5. **Paste Result** - Optional LLM response capture

### How State Is Managed
- **WorkflowContext** - React Context API
- **State Shape:** `{ selectedPrompt, attachments[], finalResult }`
- **Actions:** `setSelectedPrompt`, `addAttachments`, `removeAttachment`, `setFinalResult`

### How Validation Works
- **Rule:** `selectedPrompt && attachments.length > 0`
- **Effect:** Export buttons disabled until validation passes
- **Feedback:** Warning message displays when incomplete

### How To Extend

**Add New Prompt:**
1. Open `src/components/PromptingWorkflow/utils/prompts.ts`
2. Add object: `{ key, name, description, template, category, tags }`
3. Prompt appears in selector automatically

**Add New Export Format:**
1. Create formatter function in `utils/exportFormatter.ts`
2. Add handler to `PromptingWorkflow.tsx`
3. Add button to `ExportMenu` component

**Integrate Agent Review:**
1. Create "agent-review" category prompts
2. Add communication.json template format
3. Extend export to support structured agent data

---

## WHY

### Why This Exists

**Problem:** Manual prompt construction is time-consuming and error-prone
- Users forget to include necessary context
- Inconsistent prompt formats across teams
- No easy way to share/reuse workflows
- LLM responses get lost without tracking

**Solution:** Standardized workflow builder
- Predefined prompts ensure consistency
- Attachments guarantee context inclusion
- Multiple export formats for different use cases
- Session saves preserve complete workflows

### Why This Architecture

**React Context + Composition:**
- Centralized state without prop drilling
- Reusable components across dashboard
- Easy to extend with new features

**File-Based Exports:**
- No database required (lightweight)
- Version-controllable (git-friendly)
- Portable across systems
- Human-readable formats

**Validation-First:**
- Prevents incomplete workflows
- Clear user feedback
- Reduces errors downstream

### Why These Formats

**JSON Export:**
- Machine-readable for automation
- Structured data for parsing
- API integration ready

**Markdown Export:**
- Human-readable documentation
- Easy to review/share
- Git-friendly diffs

**Session Save:**
- Complete audit trail
- Reproducible workflows
- Training data for LLM fine-tuning

---

## Architecture

- **Framework:** Next.js App Router (client-side)
- **State:** React Context API (`WorkflowContext`)
- **Styling:** Tailwind CSS (industrial/cyberpunk theme)
- **Pattern:** Component composition with context

---

## Components

### PromptSelector
- Dropdown/list for selecting prompts
- Props: `prompts[]`, `selectedPromptKey`, `onSelectPrompt`

### AttachmentManager
- File picker + attachment list
- Actions: Add, Remove, Clear All
- Props: `attachments[]`, `onAddAttachments`, `onRemoveAttachment`, `onClearAll`

### WorkflowMeta
- Read-only workflow summary
- Shows: Prompt name, attachment count, metadata

### ExportMenu
- Action buttons: Copy JSON, Export JSON, Export Markdown
- Disabled until validation passes

### PasteFinalResultModal
- Modal for pasting LLM response
- Optional session save after result captured

---

## Data Structures

### Prompt
```
- key: unique identifier
- name: display name
- description: purpose
- template: prompt text
- category: code-review | planning | documentation | analysis
- tags: metadata tags
```

### Attachment
```
- id: unique ID
- name: file name
- path: file path
- type: mime type
- size: bytes
- content: file content (optional)
```

### Workflow State
```
- selectedPrompt: Prompt | null
- attachments: Attachment[]
- finalResult: string | null
```

---

## Export Formats

### JSON
- Filename: `workflow_{promptName}_{timestamp}.json`
- Contains: prompt, attachments, finalResult, metadata

### Markdown
- Filename: `workflow_{promptName}_{timestamp}.md`
- Sections: Prompt text, attachment list, final result

### Session
- Filename: `session_{timestamp}.json`
- Complete workflow save for later retrieval

---

## How to Extend

### Add New Prompt
**File:** `src/components/PromptingWorkflow/utils/prompts.ts`

Add to prompts array:
```typescript
{
  key: "unique-key",
  name: "Display Name",
  description: "What it does",
  template: "Prompt text with {{placeholders}}",
  category: "code-review",
  tags: ["tag1", "tag2"]
}
```

### Add New Export Format
1. Add handler to `PromptingWorkflow.tsx` (e.g., `handleExportYAML`)
2. Add button to `ExportMenu` component
3. Create formatter in `utils/exportFormatter.ts`

### Integrate with Agent Review System
- Create "agent-review" prompt category
- Add communication.json template format
- Extend Attachment type for structured data
- Add agent status tracking hooks

---

## Use Cases

### Code Review
1. Select "Code Review" prompt
2. Attach source files
3. Export as JSON → send to LLM
4. Paste response back
5. Save session

### Planning
1. Select "Implementation Planning" prompt
2. Attach requirements, code samples
3. Export as Markdown
4. Use with LLM
5. Save final plan

### Agent Review
1. Select "Agent Review" prompt (with tags: docs:foundation, code:patterns)
2. Attach communication.json template
3. Export for agent consumption
4. Agent fills analysis fields
5. Paste completed communication.json
6. Save for orchestrator aggregation

---

## Key Files

- **Page:** `src/app/prompts/page.tsx`
- **Main Component:** `src/components/PromptingWorkflow/components/PromptingWorkflow.tsx`
- **Prompts Library:** `src/components/PromptingWorkflow/utils/prompts.ts`
- **Export Formatters:** `src/components/PromptingWorkflow/utils/exportFormatter.ts`
- **Context:** `src/contexts/WorkflowContext.tsx`

---

## Styling

- **Theme:** Industrial/cyberpunk
- **Custom Classes:** `ind-panel`, `ind-border`, `ind-accent`, `ind-text-muted`
- **Accents:** 4px decorative corners on panels
- **Typography:** Uppercase headers, monospace technical content

---

## Limitations

- File saves use browser download fallback (not true file system access)
- No auto-save (user-initiated session saves only)
- Large attachments loaded into memory

---

## Future Enhancements

- Auto-save to localStorage
- Workflow templates (save/load custom combos)
- Direct LLM API integration
- Real-time collaboration
- Version history
- Attachment preview/editor
- Prompt variable replacement UI
- Integration with coderef-workflow MCP tools
