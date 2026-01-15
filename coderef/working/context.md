# Context: CodeRef Services Portfolio System

**Created:** 2025-12-28
**Project:** tracking (orchestrator)
**Target Platform:** coderef-dashboard (Next.js)

---

## Overview

Creating a docs-driven portfolio system to showcase business offerings and AI agent team capabilities. Uses markdown documentation as source of truth, with coderef-dashboard as the frontend UI. Route namespace: `/tracking` - reflecting actively tracked ideas, services, and team members.

---

## Core Concept

**Docs → UI Pipeline:**
```
assistant/tracking/services/IDEA-XXX.md (documentation)
  ↓ coderef-dashboard reads
  ↓ generates routes
/tracking/services/[slug] (live pages)
```

**Not for code projects** - this is for human-readable business offerings and service catalog.

---

## Architecture

### File Structure

```
assistant/
├── tracking/
│   ├── services/
│   │   ├── IDEA-001-ai-chatbot.md
│   │   ├── IDEA-002-inventory-system.md
│   │   └── portfolio.md (auto-generated index)
│   └── team/
│       └── (agent persona data)
└── coderef/working/
    ├── coderef-services-portfolio/
    ├── route-based-documentation-standards/
    ├── research-assistant-integration/
    └── agent-persona-team-page/

coderef-dashboard/src/app/tracking/
├── services/
│   ├── page.tsx (portfolio index)
│   └── [slug]/page.tsx (individual service pages)
└── team/
    └── page.tsx (agent persona staff page)
```

### ID Schema

**IDEA-XXX** - Business offerings (separate from STUB-XXX for code projects)
- IDEA-001, IDEA-002, etc.
- Format: `IDEA-XXX-kebab-case-name.md`

---

## Features (Stubs Created)

### 1. coderef-services-portfolio
**File:** `coderef/working/coderef-services-portfolio/stub.json`

**Purpose:** Universal `/log-idea` command to capture business offerings

**Details:**
- Entry point: `/log-idea "AI Customer Support Bot"`
- Creates: `assistant/tracking/services/IDEA-XXX-ai-customer-support-bot.md`
- Updates: `portfolio.md` (catalog index)
- Works from any project (universal command)

**Template:**
```markdown
# IDEA-XXX: [Name]
**Tagline:** [value prop]
**For:** [target customer]
**Value:** [key benefit]
```

### 2. route-based-documentation-standards
**File:** `coderef/working/route-based-documentation-standards/stub.json`

**Purpose:** Auto-generate route-specific documentation using coderef-context

**Details:**
- Analyzes route implementations with coderef-context
- Creates page-level standards (API patterns, component structure, data flow)
- Extracts existing code patterns per route
- Generates docs in coderef-docs

### 3. research-assistant-integration
**File:** `coderef/working/research-assistant-integration/stub.json`

**Purpose:** Track research assistant capabilities

**Details:**
- Delegate research tasks to specialized assistant
- Track research outputs
- Aggregate findings into project documentation

### 4. agent-persona-team-page
**File:** `coderef/working/agent-persona-team-page/stub.json`

**Purpose:** Team page showcasing agent personas as staff

**Details:**
- Route: `/team`
- Data source: `coderef-personas/personas/`
- Displays: CodeRef Assistant, Ava, Taylor, etc.
- Shows: role, expertise, specializations
- Demonstrates AI-powered team capabilities to clients

---

## coderef-dashboard Integration

### Platform
- **Framework:** Next.js (monorepo)
- **Approach:** Docs-driven UI
- **Source:** Markdown files in `assistant/services/`

### Routes

**Portfolio Routes (under /tracking):**
- `/tracking/services` → Portfolio index (grid of all offerings)
- `/tracking/services/ai-chatbot` → Individual service page (from IDEA-001-ai-chatbot.md)
- `/tracking/services/inventory-system` → Individual service page (from IDEA-002-inventory-system.md)

**Team Route:**
- `/tracking/team` → Agent persona staff page (from coderef-personas)

### Technical Implementation

**Dynamic Routes:**
```typescript
// app/tracking/services/[slug]/page.tsx
- Read markdown from assistant/tracking/services/IDEA-XXX-{slug}.md
- Parse frontmatter + content
- Render as service page
```

**Data Flow:**
```
/log-idea command
  ↓ creates IDEA-XXX.md
  ↓ dashboard detects new file
  ↓ new route appears: /tracking/services/{slug}
```

---

## Showcase Strategy

**Dual Showcase:**
1. **CodeRef System** (HOW) - Show the development system itself
2. **Service Offerings** (WHAT) - Show what we can build with it

**For Clients:**
- Portfolio at `/tracking/services` - "Here's what we can build for you"
- Team at `/tracking/team` - "Here's our AI-powered team"
- Live examples of coderef system in action
- `/tracking` namespace = actively tracked ideas, services, and capabilities

**Documentation Phase:**
- This IS the documentation phase for the project
- If logged → it's an offering (no decision point)
- Personal portfolio = client offering catalog

---

## Naming Convention

**Project:** `coderef-services`
- Complies with coderef standards
- "services" describes the project exactly

**Files:** `IDEA-XXX-kebab-case-name.md`
- Sequential numbering
- Descriptive slug for URL routing

---

## Workflow

### Log New Idea
```bash
/log-idea "AI Customer Support Chatbot"

# Creates:
assistant/tracking/services/IDEA-XXX-ai-customer-support-chatbot.md

# Result:
- New file in tracking/services/
- Auto-updates portfolio.md
- New route at /tracking/services/ai-customer-support-chatbot
```

### View Portfolio
```
Navigate to: coderef-dashboard/tracking/services
- See grid of all offerings
- Click card → /tracking/services/{slug}
- View full service details
```

### Export Portfolio
```
- PDF generation from portfolio.md
- Shareable link to /tracking/services
- Client presentation ready
```

---

## Integration Points

### MCP Servers
- **coderef-context:** Route analysis, pattern detection
- **coderef-docs:** Documentation generation, standards
- **coderef-personas:** Team page data source
- **coderef-workflow:** Potential workflow automation

### Projects
- **coderef-dashboard:** Frontend platform (Next.js)
- **assistant:** Documentation source of truth (tracking/services/, tracking/team/)

---

## Next Steps

1. Promote `coderef-services-portfolio` stub to workorder
2. Implement `/log-idea` slash command
3. Create `assistant/tracking/services/` directory
4. Build `/tracking/services` route in coderef-dashboard
5. Build `/tracking/team` route in coderef-dashboard
6. Test docs-driven UI pipeline

---

## Notes

- **Universal command:** `/log-idea` works from any project
- **Not code-focused:** For business offerings, not technical stubs
- **Human-readable:** Documentation for client consumption
- **Auto-scaling:** Add IDEA-XXX.md → new page appears
- **Monorepo ready:** coderef-dashboard can host multiple apps/routes
