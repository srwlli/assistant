# Windows Terminal Profiles & Quick Launch Configuration

> **Source:** `C:\Users\willh\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`
> **Last Updated:** 2025-12-24
> **Backup:** `settings.backup.json` (same directory)

---

## Overview

Windows Terminal profiles define quick launch tabs for projects. Each profile specifies:
- Starting directory
- Shell (pwsh.exe, cmd.exe, etc.)
- Tab color and icon
- Keybindings for quick access

**Note:** All project profiles use **PowerShell 7** (`pwsh.exe`) for modern, cross-platform shell support.

---

## Current Profiles (11 Active)

### Main Projects (1)

| # | Profile | Icon | Shortcut | Directory | Color | Status |
|---|---------|------|----------|-----------|-------|--------|
| 1 | **Assistant** | 🤖 | `Ctrl+Shift+1` | `Desktop/assistant` | #3B82F6 (Blue) | ✅ Active |

### Coderef (Nested folder in new tab menu - 10)

| # | Profile | Icon | Shortcut | Directory | Color | Status |
|---|---------|------|----------|-----------|-------|--------|
| 2 | **Coderef > Context** | 🔍 | (No binding) | `.mcp-servers/coderef-context` | #EAB308 (Yellow) | ✅ Active |
| 3 | **Coderef > Docs** | 📚 | (No binding) | `.mcp-servers/coderef-docs` | #EAB308 (Yellow) | ✅ Active |
| 4 | **Coderef > MCP** | 🔌 | (No binding) | `.mcp-servers` | #EAB308 (Yellow) | ✅ Active |
| 5 | **Coderef > Workflow** | 📋 | (No binding) | `.mcp-servers/coderef-workflow` | #EAB308 (Yellow) | ✅ Active |
| 6 | **Coderef > System** | 💻 | (No binding) | `Desktop/projects/coderef-system` | #EAB308 (Yellow) | ✅ Active |
| 7 | **Coderef > Dashboard** | 📊 | `Ctrl+Shift+D` | `Desktop/coderef-dashboard` | #8B5CF6 (Purple) | ✅ Active |
| 8 | **Coderef > Personas** | 🎭 | (No binding) | `.mcp-servers/coderef-personas` | #FBBF24 (Amber) | ✅ Active |
| 9 | **Coderef > Testing** | 🧪 | (No binding) | `.mcp-servers/coderef-testing` | #EAB308 (Yellow) | ✅ Active |
| 10 | **Coderef > Papertrail** | 📋 | (No binding) | `.mcp-servers/papertrail` | #EAB308 (Yellow) | ✅ Active |
| 11 | **Coderef > Packages** | 📦 | (No binding) | `Desktop/projects/coderef-system/packages` | #EAB308 (Yellow) | ✅ Active |

**Note:** The 10 Coderef-related tabs are nested in the "Coderef" folder in the new tab menu for organization.

---

## Quick Launch Actions

Actions defined in settings.json (lines 4-104):

```json
{
  "command": {
    "action": "newTab",
    "profile": "Assistant"
  },
  "id": "User.openAssistant"
}
```

**7 Quick Launch Actions:**
- User.openAssistant → Assistant
- User.openCoderefContext → Coderef-Context
- User.openCoderefWorkflow → Coderef-Workflow
- User.openCoderefMCP → Coderef-MCP
- User.openCoderefDocs → Coderef-Docs
- User.openCoderefDashboard → CodeRef Dashboard
- User.openCoderefPersonas → Coderef-Personas

---

## Keybindings

| Action | Shortcut | Profile |
|--------|----------|---------|
| **Assistant** | `Ctrl+Shift+1` | 🤖 |
| **CodeRef Dashboard** | `Ctrl+Shift+D` | 📊 |
| **Split Pane (duplicate)** | `Alt+Shift+D` | — |
| **Find** | `Ctrl+Shift+F` | — |
| **Copy** | `Ctrl+C` | — |
| **Paste** | `Ctrl+V` | — |

**Unbound Shortcuts Available:** `Ctrl+Shift+2`, `Ctrl+Shift+3`, `Ctrl+Shift+4`, `Ctrl+Shift+5`, `Ctrl+Shift+6`, `Ctrl+Shift+7`, `Ctrl+Shift+8`, `Ctrl+Shift+9`, `Ctrl+Shift+B`, `Ctrl+Shift+E`, `Ctrl+Shift+I`, `Ctrl+Shift+R`, `Ctrl+Shift+S`, `Ctrl+Shift+T`, `Ctrl+Shift+U`, `Ctrl+Shift+Y`, `Ctrl+Shift+N`

---

## Profile Structure (JSON)

Each profile in `settings.json` has this structure:

```json
{
  "commandline": "powershell.exe",
  "guid": "{11111111-1111-1111-1111-111111111101}",
  "hidden": false,
  "icon": "🤖",
  "name": "Assistant",
  "startingDirectory": "C:\\Users\\willh\\Desktop\\assistant",
  "tabColor": "#3B82F6",
  "tabTitle": "Assistant"
}
```

**Fields:**
- `commandline` - Shell to use (powershell.exe, cmd.exe, etc.)
- `guid` - Unique identifier (must be unique)
- `hidden` - Whether profile appears in menu
- `icon` - Emoji or icon
- `name` - Profile display name
- `startingDirectory` - Where shell opens
- `tabColor` - Hex color of tab
- `tabTitle` - Label shown in tab

---

## To Add a New Quick Launch Profile

### 1. Choose an Available Shortcut
From the unbound list above (e.g., `Ctrl+Shift+2`)

### 2. Create a New GUID
Use an online GUID generator or Windows PowerShell:
```powershell
[guid]::NewGuid()
```

### 3. Add Profile Entry
In `settings.json` → `profiles.list`, add:

```json
{
  "commandline": "powershell.exe",
  "guid": "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}",
  "hidden": false,
  "icon": "📁",
  "name": "MyProject",
  "startingDirectory": "C:\\path\\to\\project",
  "tabColor": "#HEXCOLOR",
  "tabTitle": "MyProject"
}
```

### 4. Add Action Entry
In `settings.json` → `actions`, add:

```json
{
  "command": {
    "action": "newTab",
    "profile": "MyProject"
  },
  "id": "User.openMyProject"
}
```

### 5. Add Keybinding (Optional)
In `settings.json` → `keybindings`, add:

```json
{
  "id": "User.openMyProject",
  "keys": "ctrl+shift+2"
}
```

### 6. Update newTabMenu (Optional)
Add to `newTabMenu` if you want it in the new tab dropdown menu

### 7. Save & Reload
Windows Terminal auto-reloads on file save. New profile appears immediately.

---

## File Location & Backup

**Main File:**
```
C:\Users\willh\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
```

**Backup:**
```
C:\Users\willh\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.backup.json
```

**To Edit:**
1. Close Windows Terminal (important!)
2. Edit settings.json directly in VS Code or text editor
3. Save file
4. Reopen Windows Terminal

---

## Color Reference

Common hex colors used:

| Color | Hex | Usage |
|-------|-----|-------|
| Blue | #3B82F6 | Assistant |
| Purple | #8B5CF6 | Scriptboard |
| Red | #EF4444 | Football Stats |
| Green | #22C55E | Gridiron |
| Orange | #F97316 | Noted, Scout |
| Yellow | #EAB308 | MCP Servers |
| Cyan | #06B6D4 | Selector |
| Slate | #64748B | CodeRef |
| Pink | #EC4899 | MultiTenant |
| Teal | #14B8A6 | Stats Backed |

---

## New Tab Menu Configuration

The `newTabMenu` section controls what appears in the "new tab" dropdown:

```json
"newTabMenu": [
  {
    "icon": null,
    "profile": "{11111111-1111-1111-1111-111111111101}",
    "type": "profile"
  },
  {
    "type": "remainingProfiles"
  },
  {
    "allowEmpty": false,
    "entries": [ /* list of profiles */ ],
    "icon": null,
    "inline": "never",
    "name": "Projects",
    "type": "folder"
  }
]
```

**Current structure:**
- First entry: Assistant (favorite)
- Second entry: All other profiles
- "Projects" folder: Groups remaining project profiles

---

## Notes

- **GUIDs must be unique** - Duplicates will cause conflicts
- **Hex colors are case-insensitive** - `#3B82F6` = `#3b82f6`
- **Tab Title** is separate from **Profile Name** - Use friendly names in settings
- **Icon Emojis** work great but any unicode character can be used
- **Keybindings** use Windows Terminal hotkey syntax (Ctrl, Alt, Shift combinations)
- **Auto-reload** - No Terminal restart needed after file save

---

## Related Stubs

- **STUB-020:** `terminal-settings-sync` - GUI to configure profiles from Scriptboard
- Consider creating a dashboard widget to manage terminal profiles programmatically
