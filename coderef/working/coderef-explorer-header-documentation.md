# CodeRef Explorer - Header Documentation

**File:** `web/src/pages/coderef-explorer.html`
**Lines:** 245-261
**Component:** Page Header

---

## Structure

```html
<header class="flex flex-between items-center">
    <div class="flex items-center gap-lg" style="flex: 1; min-width: 0;">
        <!-- Left: Branding -->
    </div>
    <div class="flex gap-lg items-center">
        <!-- Right: Action Buttons -->
    </div>
</header>
```

---

## Layout

| Section | Content | Alignment |
|---------|---------|-----------|
| **Left** | Logo + Title | Flex-start |
| **Right** | Theme Toggle + User Button | Flex-end |

**CSS Classes:**
- `flex` - Flexbox container
- `flex-between` - `justify-content: space-between`
- `items-center` - `align-items: center`

---

## Left Section: Branding

### Icon
- **Type:** Material Symbols Outlined
- **Name:** `folder_open`
- **Size:** 28px
- **Style:** `vertical-align: middle`

### Title
- **Text:** "CodeRef Explorer"
- **Element:** `<h1>`
- **Font Size:** 20px
- **Margin:** 0

### Container
- **Flex:** 1 (takes available space)
- **Min-width:** 0 (allows text truncation)
- **Gap:** Large (`var(--spacing-lg)`)

---

## Right Section: Action Buttons

### 1. Theme Toggle Button
**Icon:** `dark_mode` (Material Symbols)
**Function:** `toggleTheme()`
**Purpose:** Switch between dark/light mode
**Classes:**
- `industrial-button-secondary`
- `industrial-button-small`

**Behavior:**
- Toggles `<html>` class between `dark` and `light`
- Saves preference to `localStorage.theme`
- Updates icon dynamically

### 2. User/Profile Button
**Icon:** `person` (Material Symbols)
**Function:** None (placeholder)
**Purpose:** Future user account/settings
**Classes:**
- `industrial-button-secondary`
- `industrial-button-small`

**Status:** Not yet implemented

---

## Styling System

### Industrial Design
- **Button Secondary:** Outlined style with border
- **Button Small:** Compact size for toolbar
- **Icon Size:** `sm` class (small Material Symbols)

### Color Variables
- `--color-ind-bg` - Background color
- `--color-ind-text` - Text color
- `--color-ind-border` - Border color
- `--spacing-lg` - Large spacing (gap between elements)

---

## Responsive Behavior

**Mobile (< 768px):**
- Header collapses to single column
- Buttons stack vertically
- Title may truncate

**Desktop:**
- Full width with space-between
- Fixed 60px height
- Horizontal layout

---

## Grid Position

**CSS Grid:**
```css
grid-row: 1;
grid-column: 1 / -1; /* Spans full width */
height: 60px;
```

The header spans the entire top row across both sidebar and main content areas.

---

## Dependencies

### External Libraries
- **Material Symbols:** Google Fonts (icons)
- **Industrial CSS:** `../css/main.css`

### JavaScript Functions
- `toggleTheme()` - Theme switcher (line ~582)
- `initTheme()` - Initialize theme from localStorage (line ~1059)

---

## Accessibility

- ✅ Semantic HTML (`<header>`, `<h1>`)
- ✅ Icon buttons have clear purpose
- ⚠️ Missing `aria-label` on icon-only buttons
- ⚠️ No keyboard shortcuts defined

---

## Future Enhancements

1. **User Button:** Implement account/settings menu
2. **Search:** Add global search bar
3. **Breadcrumb:** Show current project path
4. **Actions:** Add export, share, or settings options
5. **Notifications:** Badge for updates or alerts

---

## Related Components

- **Sidebar:** Project selector (lines 264-277)
- **Main Content:** File header with breadcrumb (lines 329-367)
- **Theme System:** Dark/light mode CSS variables

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| 2025-12-27 | Initial header implementation | Claude |
| 2025-12-27 | Added theme toggle button | Claude |
| 2025-12-27 | Documented structure | Claude |
