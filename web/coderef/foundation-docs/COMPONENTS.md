# UI Components

**Version:** 1.0.0
**Last Updated:** 2025-12-28

---

## Overview

CodeRef Explorer uses a custom "Industrial UI" design system built with vanilla CSS and JavaScript. The component library prioritizes:

- **Zero dependencies** - No UI framework required
- **Dark-first design** - Dark mode by default with light mode support
- **Accessible** - Semantic HTML with ARIA patterns
- **Responsive** - Mobile-friendly layouts

This document catalogs all reusable UI components, their variants, and usage patterns.

---

## Design Tokens

### Color System

```css
/* Dark Mode (Default) */
--color-ind-bg: #0c0c0e              /* Page background */
--color-ind-panel: #141416           /* Panel/card background */
--color-ind-border: #3f3f46          /* Borders and dividers */
--color-ind-accent: #ff6b00          /* Primary accent (orange) */
--color-ind-accent-hover: #e65100    /* Accent hover state */
--color-ind-text: #f4f4f5            /* Primary text */
--color-ind-text-muted: #71717a      /* Secondary text */
```

```css
/* Light Mode */
--color-ind-bg: #ffffff
--color-ind-panel: #f5f5f5
--color-ind-border: #e0e0e0
--color-ind-accent: #ff6b00
--color-ind-accent-hover: #e65100
--color-ind-text: #1a1a1a
--color-ind-text-muted: #666666
```

**Implementation:** `src/css/main.css:4-47`

---

### Typography

```css
--font-display: 'Chakra Petch', sans-serif
--font-mono: 'JetBrains Mono', monospace
```

**Font Loading:** Google Fonts (self-hosted recommended for production)
**Fallbacks:** System UI fonts if Google Fonts unavailable

**Type Scale:**
- H1: 32px, -0.5px tracking, 700 weight
- H2: 24px, -0.3px tracking, 700 weight
- H3: 20px, -0.2px tracking, 700 weight
- H4: 16px, normal tracking, 700 weight
- Body: 14px, 1.6 line-height, 400 weight
- Code: 12px, monospace

**Implementation:** `src/css/main.css:16-146`

---

### Spacing

```css
--spacing-xs: 4px
--spacing-sm: 8px
--spacing-md: 12px
--spacing-lg: 16px
--spacing-xl: 24px
--spacing-2xl: 32px
```

**Usage:**
```html
<div class="p-lg">Padding: 16px</div>
<div class="gap-md">Gap: 12px</div>
<div class="m-xl">Margin: 24px</div>
```

**Implementation:** `src/css/main.css:19-25`

---

### Border Radius

```css
--radius-sm: 4px
--radius-md: 8px
--radius-lg: 12px
```

**Implementation:** `src/css/main.css:27-30`

---

### Z-Index Layers

```css
--z-dropdown: 100
--z-modal: 1000
--z-toast: 1100
```

**Implementation:** `src/css/main.css:32-35`

---

## Core Components

### Panel / Card

**Class:** `.industrial-panel`
**Purpose:** Container for grouped content

```html
<div class="industrial-panel">
  <h3>Panel Title</h3>
  <p>Panel content goes here.</p>
</div>
```

**Styling:**
- Background: `var(--color-ind-panel)`
- Border: `1px solid var(--color-ind-border)`
- Border radius: `var(--radius-md)` (8px)
- Padding: `var(--spacing-lg)` (16px)

**Responsive:**
- Mobile: Padding reduces to `var(--spacing-md)` (12px)

**Implementation:** `src/css/main.css:179-184`

---

### Buttons

#### Primary Button

**Class:** `.industrial-button`

```html
<button class="industrial-button">
  <span class="material-symbols-outlined sm">add</span>
  Click Me
</button>
```

**States:**
- Default: Orange background (#ff6b00), black text
- Hover: Darker orange (#e65100), lifts 2px, shadow
- Active: Returns to original position
- Disabled: N/A (use `:disabled` pseudo-class)

**Modifiers:**
- `.industrial-button-small` - Reduced padding, 12px font size

**Implementation:** `src/css/main.css:191-216`

---

#### Secondary Button

**Class:** `.industrial-button-secondary`

```html
<button class="industrial-button-secondary industrial-button-small">
  Cancel
</button>
```

**States:**
- Default: Transparent background, gray text, gray border
- Hover: Border color intensifies, text brightens

**Modifiers:**
- `.industrial-button-small` - Compact variant

**Implementation:** `src/css/main.css:218-241`

---

### Inputs

#### Text Input

**Class:** `.industrial-input`

```html
<input
  type="text"
  class="industrial-input"
  placeholder="Enter project path..."
/>
```

**Styling:**
- Height: 48px
- Background: Panel color
- Border: 2px solid border color
- Font: Monospace (JetBrains Mono)
- Focus state: Orange border with subtle shadow

**Disabled State:**
- Opacity: 0.5
- Cursor: not-allowed

**Implementation:** `src/css/main.css:249-277`

---

#### Select Dropdown

**Class:** Inherits from global `select` styles

```html
<select id="project-select">
  <option value="1">Project One</option>
  <option value="2">Project Two</option>
</select>
```

**Styling:**
- Matches `.industrial-input` appearance
- Browser-native dropdown functionality
- Custom focus state

**Implementation:** `src/css/main.css:310-326`

---

### Form Group

**Class:** `.form-group`

```html
<div class="form-group">
  <label for="project-name">Project Name</label>
  <input type="text" id="project-name" class="industrial-input">
  <small>Enter a descriptive name</small>
</div>
```

**Structure:**
- Label: Uppercase, 14px, 600 weight, 0.5px tracking
- Input: Full width
- Helper text: Gray, 12px, appears below input

**Implementation:** `src/css/main.css:280-300`

---

### Table

**Class:** No wrapper class (applies to native `<table>`)

```html
<table>
  <thead>
    <tr>
      <th>Project Name</th>
      <th>Status</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CodeRef Explorer</td>
      <td><span class="badge">Active</span></td>
      <td><button class="industrial-button-secondary industrial-button-small">View</button></td>
    </tr>
  </tbody>
</table>
```

**Styling:**
- Full width, collapsed borders
- Header: Panel background, uppercase, bold
- Rows: Hover effect, bottom border
- 14px font size

**Implementation:** `src/css/main.css:329-359`

---

### Alerts

**Class:** `.alert` + variant class

```html
<div class="alert success">
  <strong>Success!</strong> Project saved.
</div>

<div class="alert error">
  <strong>Error!</strong> Failed to load project.
</div>

<div class="alert warning">
  <strong>Warning!</strong> Permission required.
</div>

<div class="alert info">
  <strong>Info:</strong> File System Access API enabled.
</div>
```

**Variants:**
- `.success` - Green (#22c55e)
- `.error` - Red (#ef4444)
- `.warning` - Orange (#fb923c)
- `.info` - Blue (#3b82f6)

**Styling:**
- 4px left border
- 10% opacity background
- 16px padding

**Implementation:** `src/css/main.css:362-391`

---

## Layout Components

### Header

**Element:** `<header>`
**Grid Position:** Row 1, full width

```html
<header class="flex flex-between items-center">
  <div class="flex items-center gap-lg">
    <h1>
      <span class="material-symbols-outlined">dashboard</span>
      Project Manager
    </h1>
  </div>
  <div class="flex gap-lg items-center">
    <button class="industrial-button-secondary industrial-button-small" onclick="toggleTheme()">
      <span class="material-symbols-outlined sm">dark_mode</span>
    </button>
  </div>
</header>
```

**Styling:**
- Fixed height: 60px
- Bottom border: 1px
- Horizontal padding: 16px

**Implementation:** `index.html:62-77`, `coderef-explorer.html:237-269`

---

### Sidebar

**Element:** `<aside>`
**Grid Position:** Column 1, row 2

```html
<aside class="p-lg no-scrollbar">
  <nav class="flex flex-col gap-md">
    <!-- Navigation items -->
  </nav>
</aside>
```

**Styling:**
- Fixed width: 250px
- Right border: 1px
- Overflow-y: auto
- Custom scrollbar hidden

**Responsive:**
- Mobile: Collapses to horizontal scroll

**Implementation:** `index.html:80-104`

---

### Main Content Area

**Element:** `<main>`
**Grid Position:** Column 2, row 2

```html
<main>
  <div class="flex flex-between items-center mb-xl">
    <h2>Page Title</h2>
    <button class="industrial-button">Action</button>
  </div>
  <!-- Content -->
</main>
```

**Styling:**
- Fills remaining space
- Padding: 24px
- Overflow-y: auto

**Implementation:** `index.html:107-218`

---

## CodeRef Explorer Components

### Project Selector

**Class:** `.project-selector-inline`

```html
<div class="project-selector-inline">
  <select id="project-select">
    <option value="proj-1">My Project</option>
  </select>
  <button class="industrial-button-secondary industrial-button-small" onclick="showAddProjectDialog()">
    <span class="material-symbols-outlined sm">add</span>
  </button>
  <button class="industrial-button-secondary industrial-button-small" onclick="removeCurrentProject()">
    <span class="material-symbols-outlined sm">delete</span>
  </button>
</div>
```

**Styling:**
- Flexbox layout
- Select expands to fill space
- Action buttons fixed width (36px)

**Implementation:** `src/pages/coderef-explorer.html:61-97`

---

### Tree View

**Classes:** `.tree-item`, `.tree-children`, `.chevron`

```html
<div class="tree-item folder active">
  <span class="material-symbols-outlined chevron expanded">chevron_right</span>
  <span class="material-symbols-outlined icon">folder</span>
  <span>src</span>
</div>

<div class="tree-children show">
  <div class="tree-item file">
    <span class="material-symbols-outlined icon">description</span>
    <span>main.js</span>
  </div>
</div>
```

**States:**
- `.active` - Orange background, left border accent
- `.coderef-folder` - Subtle orange tint for special folders
- `.expanded` - Chevron rotates 90deg

**Behavior:**
- Folders toggle on click
- Files highlight and load content on click
- Hover effect: 10% opacity orange

**Implementation:** `src/pages/coderef-explorer.html:99-137`

---

### Badge

**Class:** `.badge`

```html
<span class="badge">JSON</span>
```

**Styling:**
- Tiny font (9px)
- Orange background (20% opacity)
- Orange text
- 2px border radius

**Use Cases:**
- File type indicators
- Status labels
- Category tags

**Implementation:** `src/pages/coderef-explorer.html:139-146`

---

### Toast Notification

**Class:** `.toast` (defined inline in coderef-explorer.html)

```javascript
function showToast(message) {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
}
```

```html
<div id="toast" class="toast"></div>
```

**Styling:**
- Fixed position: bottom-right
- Z-index: 1100
- Slide-in animation
- Auto-dismiss after 3s

**Implementation:** `src/pages/coderef-explorer.html:1076-1094`

---

### Modal Dialog

**Class:** `.modal` (used for "Add Project" dialog)

```html
<div id="modal-add-project" class="modal hidden">
  <div class="modal-content">
    <div class="modal-header">
      <h3>Add New Project</h3>
      <button onclick="closeAddProjectModal()">×</button>
    </div>
    <div class="modal-body">
      <!-- Form fields -->
    </div>
    <div class="modal-footer">
      <button class="industrial-button-secondary" onclick="closeAddProjectModal()">Cancel</button>
      <button class="industrial-button" onclick="confirmAddProject()">Add Project</button>
    </div>
  </div>
</div>
```

**Behavior:**
- Full-screen overlay with dark backdrop
- Centered content panel
- Escape key to close
- Click outside to close

**Implementation:** `src/pages/coderef-explorer.html:271-434`

---

## Icon System

**Library:** Material Symbols Outlined (Google)

### Usage

```html
<!-- Standard size (24px) -->
<span class="material-symbols-outlined">folder</span>

<!-- Small (18px) -->
<span class="material-symbols-outlined sm">add</span>

<!-- Large (32px) -->
<span class="material-symbols-outlined lg">dashboard</span>

<!-- Filled variant -->
<span class="material-symbols-outlined fill-1">star</span>
```

**Common Icons:**
- `folder` - Directories
- `description` - Files
- `add` - Create actions
- `delete` - Remove actions
- `settings` - Configuration
- `dark_mode` / `light_mode` - Theme toggle
- `chevron_right` - Expandable items

**Implementation:** `src/css/main.css:148-174`

---

## Utility Classes

### Layout

```css
.flex              /* display: flex */
.flex-col          /* flex-direction: column */
.flex-center       /* align-items: center; justify-content: center */
.flex-between      /* justify-content: space-between */
.items-center      /* align-items: center */
```

### Spacing

```css
.gap-xs, .gap-sm, .gap-md, .gap-lg, .gap-xl   /* Flexbox gap */
.p-xs, .p-sm, .p-md, .p-lg, .p-xl            /* Padding */
.m-xs, .m-sm, .m-md, .m-lg, .m-xl            /* Margin */
.mb-lg, .mt-sm, etc.                          /* Directional spacing */
```

### Sizing

```css
.w-full            /* width: 100% */
.h-full            /* height: 100% */
```

### Display

```css
.hidden            /* display: none */
.block             /* display: block */
.inline            /* display: inline */
.inline-block      /* display: inline-block */
```

### Text

```css
.text-center, .text-left, .text-right
.text-muted        /* Muted text color */
.text-accent       /* Accent text color */
.text-sm           /* Small font size */
.uppercase         /* text-transform: uppercase */
.font-weight-700   /* font-weight: 700 */
```

### Opacity

```css
.opacity-50        /* opacity: 0.5 */
.opacity-75        /* opacity: 0.75 */
```

**Implementation:** `src/css/main.css:446-499`

---

## Animations

### Built-in Animations

```css
@keyframes float        /* Y-axis floating effect */
@keyframes fadeIn       /* Opacity fade-in */
@keyframes slideIn      /* Slide + fade from top */
```

**Usage:**
```html
<div class="animate-float">Floating element</div>
<div class="animate-fadeIn">Fades in</div>
<div class="animate-slideIn">Slides in from top</div>
```

**Implementation:** `src/css/main.css:394-433`

---

## Responsive Design

### Breakpoints

```css
@media (max-width: 768px) {
  /* Mobile styles */
}
```

**Mobile Adaptations:**
- Sidebar collapses to horizontal scroll
- Panel padding reduces
- Typography scales down
- Grid layouts simplify to single column

**Implementation:** `src/css/main.css:502-514`

---

## Accessibility

### Keyboard Navigation

- All interactive elements are keyboard accessible
- Focus states use `:focus` with orange accent
- Tab order follows visual hierarchy

### Screen Readers

- Semantic HTML5 elements (`<nav>`, `<main>`, `<header>`)
- Icon-only buttons include `aria-label` attributes
- Form inputs have associated `<label>` elements

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Implementation:** `src/css/main.css:517-523`

---

## Theme System

### Theme Toggle

**Function:** `toggleTheme()` (defined in each HTML file)

```javascript
function toggleTheme() {
  const html = document.documentElement;
  const isDark = html.classList.contains('dark');

  if (isDark) {
    html.classList.remove('dark');
    html.classList.add('light');
    localStorage.setItem('theme', 'light');
  } else {
    html.classList.remove('light');
    html.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  }
}
```

**Persistence:** LocalStorage (`theme` key)
**Initialization:** `initTheme()` loads saved preference on page load

**Implementation:**
- `index.html:221-244`
- `coderef-explorer.html:951-1111`

---

## Component Patterns

### Button with Icon

```html
<button class="industrial-button">
  <span class="material-symbols-outlined sm" style="margin-right: var(--spacing-sm);">add</span>
  New Project
</button>
```

### Card with Header Actions

```html
<div class="industrial-panel">
  <div class="flex flex-between items-center mb-lg">
    <h3>Card Title</h3>
    <button class="industrial-button-secondary industrial-button-small">Action</button>
  </div>
  <p>Card content...</p>
</div>
```

### Status Badge

```html
<span style="display: inline-block; padding: 4px 8px; background: rgba(34, 197, 94, 0.2); color: #22c55e; border-radius: 4px; font-size: 12px;">
  Active
</span>
```

---

## Component File References

**CSS Framework:** `src/css/main.css`
**Dashboard UI:** `index.html`
**Explorer UI:** `src/pages/coderef-explorer.html`
**Backup/Reference:** `src/pages/coderef-explorer.backup.html`

---

## AI Agent Notes

**For autonomous agents working with this UI:**

1. **Adding new components:**
   - Define styles in `src/css/main.css`
   - Follow BEM-like naming: `.component-name-variant`
   - Use CSS variables for colors/spacing
   - Ensure dark + light mode support

2. **Component consistency:**
   - All buttons use `.industrial-button` or `.industrial-button-secondary`
   - All inputs use `.industrial-input`
   - All panels use `.industrial-panel`
   - Follow established spacing scale (xs/sm/md/lg/xl)

3. **Accessibility requirements:**
   - Add `aria-label` for icon-only buttons
   - Include `:focus` states for keyboard navigation
   - Test with `@media (prefers-reduced-motion)`

4. **Testing themes:**
   - Toggle with `document.documentElement.classList.toggle('dark')`
   - Check all components in both modes
   - Verify contrast ratios (WCAG AA minimum)

---

_Generated with CodeRef foundation documentation system._
