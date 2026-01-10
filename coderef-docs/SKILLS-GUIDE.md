# Claude Skills Integration Guide

**Project:** Assistant (Orchestrator CLI)
**Version:** 2.0.0
**Last Updated:** 2026-01-09
**Official Sources:** Anthropic Claude Skills Documentation

---

## Official Claude Skills Integration Guide

Based on official sources from Anthropic, here's the proper way to integrate skills into your core package:

---

## 1. Skill File Structure (Required)

Every skill must follow this structure:

```
your-skill-name/
└── SKILL.md          # Required main file
```

**For complex skills with progressive disclosure:**

```
your-skill-name/
├── SKILL.md          # Overview (keep under 500 lines)
├── REFERENCE.md      # Detailed documentation
├── EXAMPLES.md       # Usage examples
└── scripts/
    └── helper.py     # Supporting scripts
```

---

## 2. SKILL.md Format (Required)

```markdown
---
name: your-skill-name
description: What this skill does and when to use it (be specific!)
allowed-tools: Read, Grep, Glob    # Optional: restrict tools
model: haiku                       # Optional: specify model
context: fork                      # Optional: isolated execution
user-invocable: true              # Optional: show in slash menu
---

# Skill Instructions

Your markdown instructions here...

[Link to REFERENCE.md for details](./REFERENCE.md)
```

### Critical Metadata Rules

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | ✅ Yes | Lowercase, hyphens/numbers only, max 64 chars, no XML tags |
| `description` | ✅ Yes | Max 1024 chars, **be specific** (drives auto-discovery) |
| `allowed-tools` | ❌ No | Restricts Claude's tool access during skill execution |
| `model` | ❌ No | `sonnet`, `opus`, or `haiku` |
| `context` | ❌ No | Set to `fork` for isolated sub-agent |
| `user-invocable` | ❌ No | `true` (default) = shows in slash menu |

---

## 3. Distribution Methods

### Option A: Project-Local Skills (Recommended for Core Package)

**Location:** `.claude/skills/your-skill-name/`

**Advantages:**
- Version controlled with project
- Team-wide availability
- Easy to package with npm/pip

**Setup:**
```bash
# In your core package
mkdir -p .claude/skills/coderef-analyzer
cat > .claude/skills/coderef-analyzer/SKILL.md << 'EOF'
---
name: coderef-analyzer
description: Analyzes codebase using coderef-core dashboard integration (no CLI tools)
allowed-tools: Read, Grep
---

# CodeRef Analyzer Skill

Uses dashboard's built-in coderef-core to analyze code...
EOF
```

### Option B: Personal Skills (User-Wide)

**Location:** `~/.claude/skills/your-skill-name/`

**Advantages:**
- Available across all projects
- Personal customization

### Option C: Plugin Distribution (Marketplace)

**Location:** `.claude-plugin/` directory structure

**For Claude Code Plugin Marketplace:**
```
your-package/
├── .claude-plugin/
│   └── plugin.json         # Plugin metadata
└── skills/
    └── your-skill/
        └── SKILL.md
```

**plugin.json example:**
```json
{
  "name": "your-plugin",
  "version": "1.0.0",
  "description": "Plugin with bundled skills",
  "skills": [
    {
      "path": "skills/your-skill",
      "name": "your-skill"
    }
  ]
}
```

---

## 4. API Integration (For Programmatic Use)

### Custom Skills via API

**Step 1: Upload Skill Files**
```bash
curl https://api.anthropic.com/v1/skills \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "file=@skills/your-skill/SKILL.md;type=text/markdown"
```

**Response:**
```json
{
  "id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "custom",
  "created_at": "2025-01-09T12:00:00Z"
}
```

**Step 2: Use in Messages API**
```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    tools=[
        {"type": "code_execution_20250825"}
    ],
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest"
            }
        ]
    },
    messages=[{"role": "user", "content": "Analyze the codebase"}]
)
```

---

## 5. Recommended Approach for Core Package

**For integrating a skill into your core package (dashboard), here's the best practice:**

### Structure
```
coderef-dashboard/
├── .claude/
│   └── skills/
│       └── coderef-core-analyzer/
│           ├── SKILL.md              # Main skill
│           ├── REFERENCE.md          # Detailed docs
│           └── scripts/
│               └── analyze.py        # Helper scripts
├── package.json                      # Include .claude/ in files
└── README.md
```

### package.json (if npm package)
```json
{
  "name": "@your-org/coderef-dashboard",
  "files": [
    "dist",
    ".claude"
  ]
}
```

### Example SKILL.md for CodeRef Integration
```markdown
---
name: coderef-core-analyzer
description: Analyzes codebase structure using dashboard's built-in coderef-core integration. No CLI tools. Reads from .coderef/index.json and .coderef/graph.json directly.
allowed-tools: Read, Grep, Glob
context: fork
---

# CodeRef Core Analyzer

**DO NOT use CLI tools** (no `coderef scan`, `coderef analyze`)

**USE dashboard's coderef-core integration:**
- Read `.coderef/index.json` for code index
- Read `.coderef/graph.json` for dependency graph
- Use dashboard API for queries

## Workflow

1. Read `.coderef/index.json`
2. Parse functions, classes, components
3. Generate analysis report
4. Return structured data

[See detailed reference](./REFERENCE.md)
```

---

## 6. Key Best Practices

✅ **DO:**
- Keep `SKILL.md` under 500 lines (use linked files for details)
- Write specific descriptions (enables auto-discovery)
- Use `allowed-tools` to restrict capabilities
- Version control skills with your project (`.claude/skills/`)
- Include skills in package distribution

❌ **DON'T:**
- Use vague descriptions ("Helps with documents")
- Exceed 8MB total size for uploaded skills
- Use uppercase or special characters in skill names
- Include sensitive data in skill files

---

## 7. Advanced Features

### Tool Restrictions

Limit which tools Claude can use during skill execution:

```yaml
---
name: safe-analyzer
description: Analyzes code without modifying files
allowed-tools:
  - Read
  - Grep
  - Glob
---
```

**Bash Tool Restrictions:**
```yaml
allowed-tools:
  - Bash(python:*)    # Allow only python commands
  - Bash(npm:*)       # Allow only npm commands
```

### Hooks and Lifecycle Control

Execute commands before/after tool use:

```yaml
---
name: security-scanner
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/security-check.sh $TOOL_INPUT"
          once: true
---
```

**Hook Parameters:**
- `matcher` - Tool name to intercept
- `once: true` - Execute only once per session
- `command` - Shell command to run (receives `$TOOL_INPUT`)

### Visibility Controls

**Hide from slash menu (programmatic use only):**
```yaml
---
name: internal-helper
user-invocable: false
---
```

**Allow manual invocation only (block auto-discovery):**
```yaml
---
name: manual-tool
disable-model-invocation: true
---
```

### Isolated Execution

Run skill in isolated sub-agent context:

```yaml
---
name: experimental-analyzer
context: fork
---
```

**Benefits:**
- Separate conversation context
- Isolated tool state
- Clean environment for complex workflows

---

## 8. Progressive Disclosure Pattern

For complex skills, split content across multiple files:

**SKILL.md** (Overview - 200 lines)
```markdown
---
name: pdf-processor
description: Comprehensive PDF processing (forms, extraction, generation)
---

# PDF Processor

Quick start guide...

For detailed instructions: [FORMS.md](./FORMS.md)
For API reference: [REFERENCE.md](./REFERENCE.md)
```

**FORMS.md** (Detailed Instructions - 500 lines)
```markdown
# PDF Form Processing

Detailed step-by-step instructions...
```

**REFERENCE.md** (API Documentation - 1000+ lines)
```markdown
# PDF API Reference

Complete API documentation...
```

**Benefits:**
- Faster skill loading (Claude only reads what's needed)
- Better organization
- Easier maintenance

---

## 9. Testing Your Skill

### Manual Testing

1. **Create skill:**
   ```bash
   mkdir -p .claude/skills/test-skill
   cat > .claude/skills/test-skill/SKILL.md << 'EOF'
   ---
   name: test-skill
   description: Test skill for validation
   ---
   # Test Skill
   This is a test.
   EOF
   ```

2. **Verify loading:**
   - Skills load automatically on creation
   - Check Claude Code UI for skill appearance
   - Try invoking: `/test-skill` or let Claude auto-discover

3. **Test tool restrictions:**
   ```yaml
   allowed-tools: Read
   ```
   - Verify Claude cannot use Write, Bash, etc.

### Common Issues

**Skill Not Triggering:**
- ❌ Bad: "Helps with documents"
- ✅ Good: "Fills PDF forms, extracts text, generates reports from PDF files"

**Files Not Loading:**
- Check exact filename: `SKILL.md` (case-sensitive)
- Verify YAML syntax (spaces, not tabs)
- Ensure frontmatter between `---` markers

**Scripts Not Executing:**
- Make executable: `chmod +x script.py`
- Use Unix paths: `scripts/helper.py` not `scripts\helper.py`

---

## 10. Distribution Checklist

### For Project-Local Skills (`.claude/skills/`)

- [ ] Create `.claude/skills/{skill-name}/` directory
- [ ] Add `SKILL.md` with required frontmatter
- [ ] Test skill loads automatically
- [ ] Add to version control (git)
- [ ] Include in package files (npm: `package.json`, pip: `MANIFEST.in`)
- [ ] Document in project README

### For Personal Skills (`~/.claude/skills/`)

- [ ] Create `~/.claude/skills/{skill-name}/` directory
- [ ] Add `SKILL.md` with required frontmatter
- [ ] Test skill available across projects
- [ ] Back up skill files

### For Plugin Distribution

- [ ] Create `.claude-plugin/plugin.json`
- [ ] Package skills in `skills/` directory
- [ ] Test plugin installation
- [ ] Submit to marketplace (if applicable)
- [ ] Document installation instructions

---

## 11. Real-World Examples

### Example 1: CodeRef Analyzer Skill

**File:** `.claude/skills/coderef-analyzer/SKILL.md`

```markdown
---
name: coderef-analyzer
description: Analyzes codebase using .coderef/index.json and .coderef/graph.json from dashboard's coderef-core integration. Reports on functions, classes, dependencies, and architecture patterns. NO CLI tools.
allowed-tools: Read, Grep, Glob
model: haiku
context: fork
---

# CodeRef Analyzer

Analyzes codebases using pre-generated coderef data.

## Workflow

1. **Read Index**
   ```bash
   Read: .coderef/index.json
   ```

2. **Parse Data**
   - Extract functions, classes, components
   - Build dependency graph from .coderef/graph.json

3. **Generate Report**
   - Total functions/classes/components
   - Most complex files
   - Dependency hotspots
   - Architecture patterns

## Constraints

- **NO CLI TOOLS** - Use dashboard's coderef-core only
- **Read-only** - No modifications to codebase
- **Fast** - Use haiku model for speed

[See examples](./EXAMPLES.md)
```

### Example 2: Git Commit Analyzer Skill

**File:** `.claude/skills/git-analyzer/SKILL.md`

```markdown
---
name: git-analyzer
description: Analyzes git commit history, generates release notes, identifies contributors, and creates commit summaries following conventional commit format.
allowed-tools: Bash(git:*), Read
---

# Git Commit Analyzer

Analyzes git repository history and generates reports.

## Features

- **Release Notes**: Generate notes between tags
- **Contributor Stats**: Top contributors by commits/LOC
- **Commit Format**: Validate conventional commit format

## Usage

Auto-triggers on: "analyze commits", "generate release notes", "show contributors"

## Commands

```bash
# Get commits between tags
git log v1.0.0..v2.0.0 --oneline

# Show contributor stats
git shortlog -sn
```

[See detailed guide](./REFERENCE.md)
```

---

## 12. Version Control Best Practices

### .gitignore

Skills should be **included** in version control:

```gitignore
# DON'T ignore skills
# .claude/

# DO ignore generated files
.claude/cache/
.claude/logs/
```

### Git Structure

```
.claude/
├── skills/
│   ├── skill-1/
│   │   ├── SKILL.md          # Commit this
│   │   └── REFERENCE.md      # Commit this
│   └── skill-2/
│       └── SKILL.md          # Commit this
├── commands/                  # Slash commands
│   └── custom.md
└── .gitignore                # Don't ignore .claude/skills/
```

---

## Official Resources

- **[Agent Skills - Claude Code Docs](https://code.claude.com/docs/en/skills)** - Complete skills documentation
- **[Using Agent Skills with the API - Claude Docs](https://platform.claude.com/docs/en/build-with-claude/skills-guide)** - API integration guide
- **[GitHub - anthropics/skills](https://github.com/anthropics/skills)** - Official skills repository with examples
- **[Introducing Agent Skills | Claude](https://claude.com/blog/skills)** - Skills announcement blog post
- **[Agent Skills - Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)** - Platform documentation

---

## Summary

**Quick Start:**
1. Create `.claude/skills/{skill-name}/SKILL.md`
2. Add frontmatter with `name` and `description`
3. Write instructions in Markdown
4. Skills load automatically

**Best Practice for Core Package:**
- Use project-local skills (`.claude/skills/`)
- Keep SKILL.md under 500 lines
- Write specific descriptions
- Restrict tools with `allowed-tools`
- Version control with project

**Recommendation:** Use **Option A (Project-Local Skills)** with `.claude/skills/` directory structure. This keeps skills version-controlled and distributable with your package while avoiding the complexity of API uploads or marketplace submission.

---

**Document ID:** `assistant-skills-guide-v2.0.0`
**Last Generated:** 2026-01-09
**Maintained by:** CodeRef Assistant (Orchestrator Persona)
