# Project Manager - Component Structure

**CSS Location:** `src/css/main.css`
**Color Scheme:** Industrial Dark (Dark Mode default, Light Mode support)
**Font Stack:** Chakra Petch (display), JetBrains Mono (code)
**Design System:** Tailwind CSS + Custom Industrial Components

---

## Design Token System

### Colors

```
Dark Mode (default):
--color-ind-bg: #0c0c0e (Main background)
--color-ind-panel: #141416 (Panel/card background)
--color-ind-border: #3f3f46 (Borders)
--color-ind-accent: #ff6b00 (Orange - primary action)
--color-ind-accent-hover: #e65100 (Orange hover)
--color-ind-text: #f4f4f5 (Main text)
--color-ind-text-muted: #71717a (Secondary text)

Light Mode:
All colors inverted for light backgrounds
```

### Spacing (4px base unit)
```
--spacing-xs: 4px
--spacing-sm: 8px
--spacing-md: 12px
--spacing-lg: 16px
--spacing-xl: 24px
--spacing-2xl: 32px
```

### Border Radius
```
--radius-sm: 4px
--radius-md: 8px
--radius-lg: 12px
```

### Z-Index
```
--z-dropdown: 100
--z-modal: 1000
--z-toast: 1100
```

---

## Core Components

### 1. **Panel / Card**
```html
<div class="industrial-panel">
  Content goes here
</div>
```
**Properties:**
- Background: ind-panel
- Border: 1px solid ind-border
- Padding: var(--spacing-lg)
- Border radius: var(--radius-md)

### 2. **Buttons**

#### Primary Button
```html
<button class="industrial-button">Action</button>
```
**States:** Default, Hover, Active

#### Secondary Button
```html
<button class="industrial-button-secondary">Action</button>
```

#### Small Button
```html
<button class="industrial-button industrial-button-small">Action</button>
```

### 3. **Inputs**

#### Text Input
```html
<input type="text" class="industrial-input" placeholder="Enter text">
```

#### Form Group
```html
<div class="form-group">
  <label>Label</label>
  <input type="text" class="industrial-input">
  <small>Helper text</small>
</div>
```

### 4. **Tables**
```html
<table>
  <thead>
    <tr>
      <th>Header</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cell</td>
    </tr>
  </tbody>
</table>
```

### 5. **Icons**
```html
<span class="material-symbols-outlined">home</span>
<span class="material-symbols-outlined sm">home</span>
<span class="material-symbols-outlined lg">home</span>
<span class="material-symbols-outlined fill-1">home</span>
```

### 6. **Alerts**
```html
<div class="alert success">Success message</div>
<div class="alert error">Error message</div>
<div class="alert warning">Warning message</div>
<div class="alert info">Info message</div>
```

### 7. **Layout Utilities**

#### Flexbox
```html
<div class="flex gap-lg">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<div class="flex flex-col gap-md">
  <div>Row 1</div>
  <div>Row 2</div>
</div>

<div class="flex flex-center">Centered content</div>

<div class="flex flex-between">
  <span>Left</span>
  <span>Right</span>
</div>
```

#### Spacing Classes
```
Padding: p-xs, p-sm, p-md, p-lg, p-xl
Margin: m-xs, m-sm, m-md, m-lg, m-xl
Gap: gap-xs, gap-sm, gap-md, gap-lg, gap-xl
```

#### Sizing
```
w-full: width 100%
h-full: height 100%
```

#### Visibility
```
.hidden: display none
.block: display block
.inline: display inline
.inline-block: display inline-block
```

### 8. **Text Utilities**
```html
<p class="text-center">Centered text</p>
<p class="text-muted">Muted text (secondary)</p>
<p class="text-accent">Accent colored text</p>
```

### 9. **Animations**
```html
<div class="animate-float">Floats up/down</div>
<div class="animate-fadeIn">Fades in</div>
<div class="animate-slideIn">Slides in from top</div>
```

---

## Recommended Component Hierarchy

```
Layout Structure:
├── Header
│   ├── Logo
│   ├── Navigation
│   └── Theme Toggle
├── Sidebar
│   ├── Nav Links
│   ├── Project List
│   └── User Menu
├── Main Content
│   ├── Page Header
│   │   ├── Title
│   │   └── Actions
│   ├── Content Grid
│   │   └── Cards / Panels
│   └── Footer
└── Modals/Overlays
    ├── Dialog
    └── Toast Notifications
```

---

## Building New Components

### Template
```html
<!-- Component Name -->
<div class="component-name industrial-panel p-lg">
  <!-- Header -->
  <div class="flex flex-between mb-lg">
    <h3>Component Title</h3>
    <button class="industrial-button-secondary industrial-button-small">
      <span class="material-symbols-outlined sm">close</span>
    </button>
  </div>

  <!-- Content -->
  <div class="content">
    <!-- Your content here -->
  </div>

  <!-- Footer/Actions -->
  <div class="flex gap-lg mt-lg">
    <button class="industrial-button">Primary</button>
    <button class="industrial-button-secondary">Secondary</button>
  </div>
</div>
```

---

## Color Classes

```css
.text-muted /* Secondary text color */
.text-accent /* Orange accent color */
.industrial-border /* Border element */
.industrial-panel /* Panel container */
.bg-hazard /* Hazard stripe pattern */
```

---

## Responsive Design

Mobile-first approach:
- **Desktop:** Full layout
- **Tablet:** Reduced padding, adjusted grid
- **Mobile:** Single column, stacked elements

```css
@media (max-width: 768px) {
  /* Mobile adjustments */
}
```

---

## Migration Path to Dashboard

1. **Build in `/src/components/`** - Create all components as standalone HTML modules
2. **Use shared CSS** - Import `main.css` in all pages
3. **Test styling** - Verify dark/light mode switching works
4. **Document patterns** - Add component examples
5. **Migrate to Dashboard** - Convert components to React/Next.js equivalents

The CSS is ready to copy to coderef-dashboard's Tailwind config for seamless integration.

---

## File Organization

```
web/
├── src/
│   ├── css/
│   │   └── main.css (Master stylesheet)
│   ├── components/
│   │   ├── Header.html
│   │   ├── Sidebar.html
│   │   ├── ProjectCard.html
│   │   ├── Modal.html
│   │   └── ...more components
│   ├── js/
│   │   ├── theme.js (Dark/light mode)
│   │   ├── modal.js (Modal logic)
│   │   └── utils.js (Helpers)
│   └── pages/
│       ├── index.html (Dashboard)
│       ├── projects.html (Project list)
│       ├── settings.html
│       └── ...more pages
├── COMPONENT-STRUCTURE.md (This file)
└── index.html (Entry point)
```

