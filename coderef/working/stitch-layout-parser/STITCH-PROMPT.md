# Prompt for Stitch Agent

When you generate a layout that I like, I need you to analyze it and create a JSON file that captures the design details.

## What to Extract

Analyze the generated layout and identify:

### 1. Spacing & Layout
- What spacing values are used? (padding, margins, gaps)
- What's the base unit? (8px, 16px, etc.)
- Grid or flexbox layout?
- Container widths and constraints

### 2. Colors
- What colors are used?
- Background colors
- Text colors
- Border colors
- Extract the hex codes

### 3. Typography
- Font sizes used
- Font weights (regular, bold, etc.)
- Line heights
- Text alignment

### 4. Components
- List each major component (header, card, sidebar, etc.)
- For each component note:
  - Its size (width/height)
  - Its spacing (padding/margin)
  - Its visual style (background, border, shadow)

### 5. What NOT to Copy
Identify things that would cause problems if copied:
- Absolute positioning
- Hardcoded pixel widths
- Magic numbers
- Inline styles
- Any weird CSS hacks

## Output Format

Create a JSON file named `layout-[date].json` with this structure:

```json
{
  "name": "dashboard-header",
  "created": "2026-01-01",

  "spacing": {
    "base_unit": "8px",
    "values_used": ["8px", "16px", "24px", "32px"]
  },

  "colors": {
    "background": "#ffffff",
    "text": "#1f2937",
    "border": "#e5e7eb",
    "accent": "#3b82f6"
  },

  "typography": {
    "sizes": ["14px", "16px", "20px", "24px"],
    "weights": ["400", "600", "700"]
  },

  "layout": {
    "type": "flexbox",
    "container_width": "1200px",
    "gap": "16px"
  },

  "components": [
    {
      "name": "header",
      "width": "100%",
      "height": "64px",
      "padding": "16px 24px",
      "background": "#ffffff",
      "border": "1px solid #e5e7eb"
    }
  ],

  "safe_to_reuse": {
    "spacing_system": "8px base with consistent scale",
    "color_palette": "neutral grays + blue accent",
    "layout_structure": "flexbox horizontal"
  },

  "do_not_copy": [
    "absolute positioning on sidebar",
    "hardcoded 1847px width on main container",
    "inline z-index styles"
  ]
}
```

## Example Request

When I say: **"Parse this layout"**

You should:
1. Look at the current layout code
2. Extract the values listed above
3. Create the JSON file
4. Tell me what you found and what to avoid copying

## Why This Helps

When I copy layouts between projects, unwanted CSS leaks through (weird positioning, hardcoded sizes, magic numbers). This JSON gives me a clean reference of ONLY the good patterns I want to reuse.
