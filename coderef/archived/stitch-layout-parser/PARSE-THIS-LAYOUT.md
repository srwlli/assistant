# Layout Analysis Guide

Use this guide to manually extract UI/UX patterns from the CodeRef Scanner layout.

---

## 1. SPACING ANALYSIS

### Base Unit
Look for the smallest repeating spacing value. Common patterns:
- **4px** = ultra-tight (icon padding)
- **8px** = tight (button padding) ← LIKELY BASE
- **16px** = standard (card padding)
- **24px** = comfortable (section margins)

**From the code:**
```
p-1.5 = 6px (1.5 × 4px)
p-2 = 8px ← BASE UNIT
p-3 = 12px
p-4 = 16px
px-3 py-1.5 = 12px horizontal, 6px vertical
px-6 py-4 = 24px horizontal, 16px vertical
```

**Your turn:** What's the base spacing unit? ___8px___

**Scale identified:**
- [ ] 4px
- [ ] 6px (1.5rem)
- [ ] 8px
- [ ] 12px
- [ ] 16px
- [ ] 24px
- [ ] 32px

---

## 2. COLOR PALETTE

### Extract hex codes from Tailwind config:

**Primary Colors:**
```javascript
primary: "#FF6B00" // Vivid orange
primary-hover: "#E65100" // Darker orange
```

**Background Colors:**
```javascript
background-light: "#F3F4F6" // Light gray
background-dark: "#0A0A0A" // Very dark (almost black)
```

**Surface Colors:**
```javascript
surface-light: "#FFFFFF" // White
surface-dark: "#171717" // Dark gray
```

**Border Colors:**
```javascript
border-light: "#E5E7EB" // Light gray border
border-dark: "#333333" // Dark gray border
```

**Text Colors (from classes):**
- `text-gray-900` = #111827 (primary text)
- `text-gray-500` = #6B7280 (secondary text)
- `text-gray-400` = #9CA3AF (muted text)
- `text-green-400` = #4ADE80 (console text)
- `text-blue-400` = #60A5FA (console highlight)

**Your turn - Fill in the palette:**
```json
{
  "primary": "#FF6B00",
  "primary_hover": "#E65100",
  "background": {
    "light": "#F3F4F6",
    "dark": "#0A0A0A"
  },
  "surface": {
    "light": "#FFFFFF",
    "dark": "#171717"
  },
  "border": {
    "light": "#E5E7EB",
    "dark": "#333333"
  },
  "text": {
    "primary": "#111827",
    "secondary": "#6B7280",
    "muted": "#9CA3AF"
  },
  "accent": {
    "green": "#4ADE80",
    "blue": "#60A5FA"
  }
}
```

---

## 3. TYPOGRAPHY

### Font Families:
```javascript
display: ["Inter", "sans-serif"]
mono: ["JetBrains Mono", "monospace"]
```

### Font Sizes (from classes):
- `text-xs` = 12px
- `text-sm` = 14px
- `text-base` = 16px (default)
- `text-lg` = 18px
- `text-xl` = 20px
- `text-2xl` = 24px

### Font Weights:
- `font-normal` = 400
- `font-medium` = 500
- `font-semibold` = 600
- `font-bold` = 700

**Your turn - List all sizes used:**
- [ ] 12px (text-xs)
- [ ] 14px (text-sm)
- [ ] 16px (text-base)
- [ ] 18px (text-lg)
- [ ] 20px (text-xl)

---

## 4. LAYOUT STRUCTURE

### Container:
- Max width: `max-w-7xl` = 1280px
- Grid: `grid-cols-1 lg:grid-cols-12` = 12-column grid
- Gap: `gap-6` = 24px

### Main sections:
1. **Left Panel** = `lg:col-span-8` (8 columns)
2. **Right Sidebar** = `lg:col-span-4` (4 columns)
3. **Bottom Action Bar** = `lg:col-span-12` (full width)

**Layout type:** Grid (12-column responsive)

---

## 5. COMPONENT BREAKDOWN

### Header Component:
```
Height: py-4 = 32px padding (total height ~64px)
Background: bg-surface-light dark:bg-surface-dark
Border: border-b
Position: sticky top-0 z-50
```

### Project List Card:
```
Background: bg-surface-light dark:bg-surface-dark
Border: border border-border-light dark:border-border-dark
Border radius: rounded-xl = 12px
Height: h-[500px] (fixed)
Shadow: shadow-sm
```

### Console/Sidebar Panel:
```
Background: bg-gray-900 (terminal area)
Border radius: rounded-xl = 12px
Height: h-[500px] (fixed)
Text: font-mono text-xs
```

### Primary Action Button:
```
Background: bg-primary hover:bg-primary-hover
Padding: py-4 md:px-12 = 16px vertical, 48px horizontal
Border radius: rounded-lg = 8px
Shadow: shadow-lg shadow-primary/20
Transform: hover:-translate-y-0.5 (lift effect)
```

**Your turn - Extract these properties:**

**Card Component:**
- Background: _______________
- Border: _______________
- Border radius: _______________
- Padding: _______________
- Shadow: _______________

---

## 6. SAFE TO REUSE

Check off the patterns that are **reusable across projects:**

- [ ] **8px spacing rhythm** (4px, 8px, 12px, 16px, 24px)
- [ ] **Orange primary color** (#FF6B00)
- [ ] **Neutral gray palette** (#F3F4F6, #E5E7EB, #6B7280)
- [ ] **12px border radius** (rounded-xl on cards)
- [ ] **Inter font family** for UI text
- [ ] **JetBrains Mono** for code/console
- [ ] **12-column grid layout** (max-width: 1280px)
- [ ] **24px gap** between sections
- [ ] **Sticky header** with shadow
- [ ] **Card shadow pattern** (shadow-sm on cards, shadow-lg on buttons)

---

## 7. DO NOT COPY

Mark the patterns that cause **unwanted characteristic leakage:**

- [ ] **Fixed heights** (`h-[500px]` on cards) - breaks responsive flow
- [ ] **Hardcoded z-index** (`z-50` on header) - can conflict with modals
- [ ] **Tailwind CDN config** in `<script>` tag - should be in tailwind.config.js
- [ ] **Inline JavaScript** for tab switching - should be in separate .js file
- [ ] **Dark mode toggle inline** - should be in state management
- [ ] **Absolute color values** in classes - should use CSS variables

---

## 8. RESPONSIVE BREAKPOINTS

From Tailwind classes:

- **Mobile (default):** No prefix
- **Medium (md):** 768px+ → `md:flex`, `md:w-auto`, `md:px-12`
- **Large (lg):** 1024px+ → `lg:col-span-8`, `lg:grid-cols-12`

**Mobile behavior:**
- Grid collapses to 1 column
- Sidebar stacks below main content
- Button becomes full width

---

## 9. OUTPUT JSON

Now fill in this JSON with your findings:

```json
{
  "name": "coderef-scanner-interface",
  "created": "2026-01-01",

  "spacing": {
    "base_unit": "___px",
    "scale": ["___", "___", "___", "___", "___"]
  },

  "colors": {
    "primary": "___",
    "background_light": "___",
    "background_dark": "___",
    "surface_light": "___",
    "surface_dark": "___",
    "border_light": "___",
    "border_dark": "___"
  },

  "typography": {
    "display_font": "___",
    "mono_font": "___",
    "sizes": ["___", "___", "___"],
    "weights": ["___", "___", "___"]
  },

  "layout": {
    "type": "___",
    "max_width": "___",
    "columns": "___",
    "gap": "___"
  },

  "components": [
    {
      "name": "header",
      "height": "___",
      "padding": "___",
      "background": "___",
      "position": "___"
    },
    {
      "name": "card",
      "border_radius": "___",
      "shadow": "___",
      "border": "___"
    },
    {
      "name": "primary_button",
      "background": "___",
      "padding": "___",
      "shadow": "___",
      "hover_effect": "___"
    }
  ],

  "safe_to_reuse": [
    "___",
    "___",
    "___"
  ],

  "do_not_copy": [
    "___",
    "___",
    "___"
  ]
}
```

---

## QUICK REFERENCE

**Where to look:**
- Spacing → `p-*`, `px-*`, `py-*`, `gap-*` classes
- Colors → `tailwind.config` object + `bg-*`, `text-*` classes
- Typography → `font-*`, `text-*` classes
- Layout → `grid-cols-*`, `max-w-*`, `gap-*` classes
- Border radius → `rounded-*` classes
- Shadows → `shadow-*` classes

**Save the completed JSON as:** `layout-coderef-scanner-2026-01-01.json`
