# Create Resource Sheet - Unified MCP Tool Integration

## Purpose
Generate an authoritative, refactor-safe technical documentation resource sheet for a specific code element using the coderef-docs MCP tool with 60-80% auto-fill from dependency graph analysis.

## Usage
```
/create-resource-sheet <target> [element-type]

Required:
  target        Path to code file or element name (e.g., AuthService.ts, Button.tsx)

Optional:
  element-type  Override auto-detection (e.g., stateful-container, api-client, custom-hook)
                If omitted, element type is auto-detected from code characteristics

Examples:
/create-resource-sheet src/auth/AuthService.ts
/create-resource-sheet components/Button.tsx design-system
/create-resource-sheet hooks/useLocalStorage.ts custom-hook
```

## Agent Instructions

**IMPORTANT:** You MUST use the `generate_resource_sheet` MCP tool instead of generating documentation manually.

### Step 1: Call the MCP Tool

Use the `mcp__coderef-docs__generate_resource_sheet` tool with these parameters:

```typescript
{
  project_path: string,        // Current project root (auto-detected)
  element_name: string,         // Target file/element from user input
  mode: "reverse-engineer",     // Default mode for existing code
  element_type?: string,        // Optional: pass through if user specified
  output_path?: string          // Optional: custom output directory
}
```

### Step 2: Handle the Response

**IMPORTANT:** The MCP tool automatically saves all 3 output formats:
1. **Markdown** → `coderef/reference-sheets/{element_name}/{element_name}.md`
2. **JSON Schema** → `coderef/reference-sheets/{element_name}/{element_name}.schema.json`
3. **JSDoc** → `coderef/reference-sheets/{element_name}/{element_name}.jsdoc.txt`

The tool response includes:
- `outputs.markdown` - Path to saved markdown file
- `outputs.schema` - Path to saved schema file
- `outputs.jsdoc` - Path to saved JSDoc file
- `auto_fill_rate` - Percentage of auto-filled content
- `warnings` - Any issues detected

**Inform the user where all 3 files were saved** and provide the auto-fill percentage.

### Step 3: Quality Validation

The MCP tool automatically runs 4-gate validation:
- **Gate 1:** Structural validation (header, summary, required sections)
- **Gate 2:** Content quality (no placeholders, writing standards)
- **Gate 3:** Element-specific validation (type requirements met)
- **Gate 4:** Auto-fill threshold (>= 60% completion)

If validation fails, the tool provides specific issues to address. Review and apply fixes if needed.

### Example Invocation

```
User: /create-resource-sheet src/auth/AuthService.ts

Agent:
I'll generate a resource sheet for AuthService using the unified MCP tool.

[Calls mcp__coderef-docs__generate_resource_sheet with:
  project_path: "C:/path/to/project",
  element_name: "AuthService",
  mode: "reverse-engineer"
]

[Tool generates and auto-saves all 3 formats with 68% auto-fill rate]

✅ Resource sheet generated with 68% auto-fill rate!

All 3 formats saved to:
1. 📄 Markdown: coderef/reference-sheets/authservice/authservice.md
2. 📋 JSON Schema: coderef/reference-sheets/authservice/authservice.schema.json
3. 💬 JSDoc: coderef/reference-sheets/authservice/authservice.jsdoc.txt

The markdown file contains the full documentation. The schema provides
type contracts for validation, and the JSDoc file has inline comment
suggestions you can copy into your source code.
```

## Migration Note

This command was upgraded from a template-based system to an MCP tool integration on 2026-01-03 (WO-RESOURCE-SHEET-CONSOLIDATION-001). The MCP tool provides:
- ✅ **60-80% auto-fill** from dependency graph analysis
- ✅ **20 element type** specializations
- ✅ **4-gate validation** pipeline
- ✅ **3 output formats:** Markdown + JSON Schema + JSDoc
- ✅ **150-300x speedup** vs manual documentation

**Reference:** For element type catalog and detailed documentation, see `.claude/commands/resource-sheet-catalog.md`

---

**Note:** This command was fully migrated to MCP tool integration on 2026-01-03. The old manual template has been removed. All documentation generation now happens via the `mcp__coderef-docs__generate_resource_sheet` tool with 60-80% auto-fill.
