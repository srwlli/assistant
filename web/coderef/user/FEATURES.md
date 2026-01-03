# CodeRef Explorer - Features

Comprehensive overview of all features and capabilities.

---

## Core Features

### 1. Multi-Project Management

**What it does:** Manage unlimited projects from a single interface

**Capabilities:**
- Add projects via File System Access API or manual path entry
- Store project metadata in persistent JSON file
- Quick project switcher with dropdown selector
- Remove projects without deleting files

**Use Cases:**
- Developers managing multiple codebases
- Documentation writers working across projects
- Team leads reviewing different repositories
- Students organizing course projects

**Benefits:**
- No need to navigate file system repeatedly
- All projects accessible in one place
- Fast context switching (<2 seconds)
- Persistent across app restarts

---

### 2. Dual Access Modes

**What it does:** Two methods to access project files

#### Mode A: File System Access API (Browser)

**How it works:**
- Browser asks for directory permission via native picker
- Direct access to files (no server uploads)
- Permissions persist in IndexedDB

**Advantages:**
- Faster file access (no HTTP overhead)
- Offline-capable
- Lower resource usage

**Requirements:**
- Chromium-based browser (Chrome, Edge, Brave)
- User permission grant

---

#### Mode B: HTTP API (Server)

**How it works:**
- Python server reads files from disk
- Serves content via HTTP endpoints
- No browser permissions needed

**Advantages:**
- Works in any browser
- No permission prompts
- Server can add validation/preprocessing

**Requirements:**
- Python 3.6+ installed
- Server running on port 8080

---

**Comparison:**

| Feature | File System API | HTTP API |
|---------|----------------|----------|
| Speed | Faster | Slightly slower |
| Permissions | Required once | None |
| Browser Support | Chrome, Edge only | All browsers |
| Offline | Yes | Requires server |
| Best For | Daily use | One-time access |

---

### 3. File Explorer

**What it does:** Browse project folders with intuitive tree view

**Features:**
- Recursive folder expansion
- Files sorted alphabetically
- Folders before files
- Visual hierarchy with indentation
- Icon indicators (folders vs files)
- Active state highlighting

**Interactions:**
- Click folder → Expand/collapse
- Click file → View content
- Hover → Orange highlight
- Chevron icon rotates on expand

**Performance:**
- Async rendering (no UI blocking)
- Handles large projects (1000+ files)
- Lazy loading ready (future optimization)

**Use Cases:**
- Finding documentation quickly
- Exploring unfamiliar codebases
- Navigating deep folder structures
- Locating specific file types

---

### 4. File Content Viewer

**What it does:** Display file content with smart rendering

#### Supported Formats

**JSON Files (.json)**
- Syntax highlighting with color
- Indented formatting
- Key/value color coding
- Copy button for full content

**Markdown Files (.md)**
- Rendered HTML (via marked.js)
- Headers, lists, code blocks
- Links clickable
- Preview + raw toggle (future)

**Code Files (.js, .py, .css, .html, etc.)**
- Monospace font (JetBrains Mono)
- Syntax highlighting (basic)
- Line numbers (future)
- Copy button

**Text Files (.txt)**
- Plain text display
- Monospace font
- No formatting

**Binary Files (.png, .pdf, etc.)**
- Not currently supported
- Shows "Unsupported format" message
- Roadmap: v2.0 will add preview

---

#### File Metadata

Each file shows:
- **Name** - Full filename with extension
- **Size** - Human-readable (e.g., "1.2 KB")
- **Modified** - Last modification timestamp
- **Path** - Absolute file system path

#### File Actions

**Copy Path**
- Copies absolute path to clipboard
- Useful for CLI commands
- Example: `/Users/name/project/src/index.js`

**Copy Code**
- Copies file content to clipboard
- Preserves formatting
- Useful for sharing snippets

**Share Link** (Future)
- Generates shareable URL
- Opens file directly
- Browser mode only

---

### 5. Industrial UI Design

**What it does:** Custom design system with dark-first approach

#### Theme System

**Dark Mode (Default)**
- Background: #0c0c0e (near-black)
- Panels: #141416 (dark gray)
- Text: #f4f4f5 (off-white)
- Accent: #ff6b00 (orange)

**Light Mode**
- Background: #ffffff (white)
- Panels: #f5f5f5 (light gray)
- Text: #1a1a1a (near-black)
- Accent: #ff6b00 (orange)

**Toggle:**
- Click moon icon in header
- Instant switch
- Persists in LocalStorage

---

#### Typography

**Display Font:** Chakra Petch (sans-serif)
- Headers, buttons, labels
- Bold, uppercase for emphasis
- Industrial aesthetic

**Monospace Font:** JetBrains Mono
- Code blocks
- File paths
- JSON content

---

#### Components

**Buttons**
- Primary: Orange fill, black text
- Secondary: Transparent, gray border
- Hover effects: Lift, shadow, color change

**Inputs**
- 2px border
- Focus state: Orange glow
- Monospace font

**Panels**
- Subtle border
- Rounded corners (8px)
- Shadow on hover

**Alerts**
- Color-coded by type
- Left border accent
- Auto-dismiss (toasts)

---

#### Accessibility

**Keyboard Navigation**
- Tab through interactive elements
- Focus visible with orange outline
- Logical tab order

**Reduced Motion**
- Respects `prefers-reduced-motion`
- Disables animations
- Instant transitions

**Screen Readers**
- Semantic HTML5 elements
- ARIA labels on icon buttons
- Proper heading hierarchy

---

### 6. Offline-First Architecture

**What it does:** Works without internet connection

**Storage:**
- **IndexedDB** - Directory handles persist
- **LocalStorage** - Theme preference
- **File System** - projects.json on disk

**Capabilities:**
- Add projects (File System API mode)
- Browse files
- View content
- Switch projects
- Toggle theme

**Limitations:**
- Initial install requires download
- External resources (fonts, icons) cache on first load
- HTTP API mode requires local server

**Benefits:**
- Privacy (no external requests)
- Speed (no network latency)
- Reliability (no server downtime)
- Portability (works anywhere)

---

### 7. Cross-Platform Desktop App

**What it does:** Native desktop experience via Electron

#### Windows Support

**Features:**
- Start Menu integration
- Desktop shortcut
- System tray icon (future)
- File associations (future)

**Installation:**
- NSIS installer (.exe)
- Auto-update support (future)

---

#### macOS Support

**Features:**
- Applications folder
- Dock integration
- Native notifications (future)
- Touch Bar support (future)

**Installation:**
- DMG disk image
- Code signed (required for distribution)

---

#### Linux Support

**Features:**
- AppImage (portable)
- .deb package (Ubuntu/Debian)
- .rpm package (Fedora/RedHat)

**Installation:**
- No admin required (AppImage)
- Package managers (deb/rpm)

---

**Benefits by Platform:**

| Platform | Benefits |
|----------|----------|
| Windows | Native window controls, Start Menu search |
| macOS | Spotlight search, native file picker |
| Linux | Open-source, package manager integration |

---

## Feature Comparison

### CodeRef Explorer vs. Alternatives

| Feature | CodeRef Explorer | VS Code | File Explorer | GitHub |
|---------|-----------------|---------|---------------|--------|
| Multi-project | ✅ Unlimited | ✅ Workspaces | ❌ Single folder | ✅ Per-repo |
| Offline | ✅ Full support | ✅ Yes | ✅ Yes | ❌ Requires internet |
| File preview | ✅ JSON, MD | ✅ All formats | ❌ Limited | ✅ Web only |
| Dark mode | ✅ Default | ✅ Configurable | ⚠️ OS-dependent | ✅ Yes |
| Speed | ✅ Fast | ⚠️ Heavy | ✅ Native | ⚠️ Network-dependent |
| Learning curve | ✅ Low | ⚠️ Moderate | ✅ None | ⚠️ Moderate |
| Resource usage | ✅ Low (~200MB) | ⚠️ High (~500MB) | ✅ Minimal | N/A |

---

## Features by User Type

### For Developers

**Most Valuable:**
- Multi-project management (switch between codebases)
- Fast file access (no IDE startup time)
- JSON syntax highlighting (config files)
- Monospace fonts (code readability)

**Use Cases:**
- Quick config file checks
- Documentation browsing
- Project structure exploration
- Cross-project file comparison (future)

---

### For Documentation Writers

**Most Valuable:**
- Markdown rendering (preview docs)
- Project switching (multiple doc sets)
- Dark mode (long writing sessions)
- Offline access (work anywhere)

**Use Cases:**
- Previewing markdown files
- Organizing documentation sets
- Cross-referencing docs
- Reviewing contributor submissions

---

### For Team Leads

**Most Valuable:**
- Multi-project view (oversee all repos)
- Fast navigation (quick code reviews)
- Lightweight (low resource usage)
- Shareable projects.json (team sync)

**Use Cases:**
- Code review prep
- Architecture audits
- Onboarding new team members
- Quick file lookups during meetings

---

### For Students

**Most Valuable:**
- Free and open-source
- Low learning curve
- Offline-capable (study anywhere)
- Multiple course projects

**Use Cases:**
- Organizing course assignments
- Reviewing example code
- Preparing for exams (quick reference)
- Exploring open-source projects

---

## Roadmap

### Version 1.1 (Planned)

**Features:**
- [ ] Keyboard shortcuts (Ctrl+P file finder)
- [ ] Search within files (Ctrl+F)
- [ ] File type filters (show only .md)
- [ ] Recent files list
- [ ] Breadcrumb navigation

**Timeline:** Q2 2025

---

### Version 1.5 (Planned)

**Features:**
- [ ] Multiple file tabs
- [ ] Split view (side-by-side files)
- [ ] File editing (basic text editor)
- [ ] Git integration (show modified files)
- [ ] Favorites/bookmarks

**Timeline:** Q3 2025

---

### Version 2.0 (Planned)

**Features:**
- [ ] Code editor (Monaco or CodeMirror)
- [ ] Terminal integration
- [ ] Extension/plugin system
- [ ] Team collaboration features
- [ ] Cloud sync (optional)

**Timeline:** Q4 2025

---

## Feature Requests

**Submit ideas:** https://github.com/yourusername/coderef-explorer/issues

**Most Requested (Community):**
1. Global search across all projects
2. File comparison (diff viewer)
3. Image file preview
4. PDF viewer
5. Custom themes/color schemes

---

## Technical Specifications

### Performance Metrics

| Operation | Time | Conditions |
|-----------|------|------------|
| Add project | <2s | File System API |
| Switch project | <1s | Cached handles |
| Load folder tree | <3s | 1000 files |
| View file | <0.5s | <1MB file |
| Theme toggle | Instant | CSS variables |

### Resource Usage

| Metric | Value | Platform |
|--------|-------|----------|
| RAM (idle) | ~150MB | Windows 10 |
| RAM (active) | ~250MB | With 5 projects |
| Disk space | ~180MB | Installed |
| CPU (idle) | <1% | Background |
| Network | 0 | Offline mode |

### Scalability Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Projects | Unlimited | Limited by disk space |
| Files per project | 10,000+ | Performance degrades >50k |
| File size | 10MB | Larger files may be slow |
| IndexedDB storage | ~50% disk | Browser-dependent |

---

## Security Features

### Current Implementation

**Local-only Server:**
- Binds to `localhost` (127.0.0.1)
- Not accessible from network
- No external connections

**Electron Security:**
- Context isolation enabled
- Node integration disabled
- No remote code execution

**Data Privacy:**
- No analytics or tracking
- No external API calls
- All data stored locally

### Recommendations for Production

If deploying to team/organization:

1. **Add authentication** to HTTP API
2. **Enable HTTPS** for server
3. **Implement CORS whitelist**
4. **Code sign** executables
5. **Regular security audits**

---

## Limitations

### Known Limitations

**Browser Support:**
- Firefox not supported (no File System Access API)
- Safari not supported (no File System Access API)
- Internet Explorer not supported (obsolete)

**File Types:**
- Binary files not previewed (images, PDFs, videos)
- Large files (>10MB) may be slow
- Encrypted files cannot be read

**Features:**
- No file editing (view-only)
- No version control (Git integration planned)
- No collaborative editing
- No cloud sync

**Platform:**
- Windows 7 not supported (Electron 28 requirement)
- macOS 10.12 and older not supported
- Linux kernel 3.x not supported

---

## Accessibility Features

**Current Support:**

- Keyboard navigation (Tab, Enter, Escape)
- Focus indicators (orange outline)
- Semantic HTML (screen reader friendly)
- Color contrast (WCAG AA compliant)
- Reduced motion support

**Future Enhancements:**

- Keyboard shortcuts (v1.1)
- Screen reader announcements (v1.5)
- High contrast themes (v2.0)
- Font size customization (v2.0)

---

_Version: 1.0.0 | Last Updated: 2025-12-28_
