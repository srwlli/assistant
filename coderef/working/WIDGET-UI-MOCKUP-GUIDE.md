# Prompting Workflow Widget - UI Mockup & CSS Guide

## Project Structure

```
packages/widgets/@coderef-dashboard/widget-prompting-workflow/
├── src/
│   ├── components/
│   │   ├── PromptingWorkflow.tsx              # Main container component
│   │   ├── PromptingWorkflow.module.css
│   │   ├── PromptSelector.tsx                 # Prompt selection UI
│   │   ├── PromptSelector.module.css
│   │   ├── AttachmentManager.tsx              # File list & controls
│   │   ├── AttachmentManager.module.css
│   │   ├── AttachmentDropZone.tsx             # Drag & drop zone
│   │   ├── AttachmentDropZone.module.css
│   │   ├── WorkflowMeta.tsx                   # Metadata display
│   │   ├── WorkflowMeta.module.css
│   │   ├── ExportMenu.tsx                     # Export buttons
│   │   ├── ExportMenu.module.css
│   │   ├── PasteTextModal.tsx                 # Text paste modal
│   │   ├── PasteTextModal.module.css
│   │   ├── PasteFinalResultModal.tsx          # Final result modal
│   │   └── PasteFinalResultModal.module.css
│   ├── hooks/
│   │   ├── useWorkflow.ts
│   │   ├── useClipboard.ts
│   │   └── useFileHandlers.ts
│   ├── utils/
│   │   ├── fileContentExtractor.ts
│   │   ├── languageMap.ts
│   │   ├── tokenEstimator.ts
│   │   ├── filenameGenerator.ts
│   │   ├── prompts.ts
│   │   └── exportFormatter.ts
│   ├── types/
│   │   └── index.ts
│   └── index.ts                              # Entry point
├── package.json
└── tsconfig.json
```

---

## Theme & Colors

```
Dark Theme:
- Background:      #0a0a0a (pure black)
- Card Background: #1a1a1a (dark grey)
- Element BG:      #242424 (darker grey)
- Borders:         #333333 (light grey)
- Text Primary:    #ffffff (white)
- Text Secondary:  #888888 (medium grey)
- Text Muted:      #aaaaaa (light grey)

Accent Colors:
- Primary:         #FF6B00 (orange)
- Primary Light:   #ff8a33 (lighter orange)
- Success:         #4caf50 (green)
- Error:           #ff6b6b (red)
- Warning:         #FF9933 (orange-yellow)
- Info:            #4a9eff (blue)

Font:
- System Font Stack: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif
- Monospace:        monospace (for code/previews)
```

---

## Component CSS Files

### 1. PromptingWorkflow.module.css

**Full Path:** `packages/widgets/@coderef-dashboard/widget-prompting-workflow/src/components/PromptingWorkflow.module.css`

**Purpose:** Main container and layout

```css
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
  background: #0a0a0a;
  color: #ffffff;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
    sans-serif;
}

.header {
  margin-bottom: 32px;
}

.title {
  font-size: 32px;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 8px 0;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 16px;
  color: #888888;
  margin: 0;
  line-height: 1.5;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.exportSection {
  padding: 24px;
  background: #1a1a1a;
  border-radius: 8px;
  border: 1px solid #333333;
}

.sectionTitle {
  font-size: 18px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 16px 0;
}

.warningText {
  margin-top: 16px;
  padding: 12px 16px;
  background: rgba(255, 153, 51, 0.1);
  border-left: 3px solid #FF9933;
  color: #FF9933;
  font-size: 14px;
  border-radius: 4px;
}

.pasteResultButton {
  margin-top: 16px;
  padding: 12px 20px;
  background: #333333;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.pasteResultButton:hover {
  background: #444444;
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .container {
    padding: 16px;
  }
  .title {
    font-size: 24px;
  }
  .subtitle {
    font-size: 14px;
  }
}
```

---

### 2. PromptSelector.module.css

**Full Path:** `packages/widgets/@coderef-dashboard/widget-prompting-workflow/src/components/PromptSelector.module.css`

**Purpose:** Prompt selection cards with token badges

```css
.container {
  padding: 24px;
  background: #1a1a1a;
  border-radius: 8px;
  margin-bottom: 24px;
}

.title {
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 8px 0;
}

.subtitle {
  font-size: 14px;
  color: #888888;
  margin: 0 0 20px 0;
}

.promptGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
  margin-bottom: 20px;
}

.promptCard {
  padding: 16px;
  background: #242424;
  border: 2px solid #333333;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: left;
  font-family: inherit;
}

.promptCard:hover {
  border-color: #FF6B00;
  background: #2a2a2a;
  transform: translateY(-2px);
}

.promptCard.selected {
  border-color: #FF6B00;
  background: #2a2a2a;
  box-shadow: 0 0 12px rgba(255, 107, 0, 0.3);
}

.promptHeader {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.promptName {
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  margin: 0;
  flex: 1;
}

.tokenBadge {
  background: #FF6B00;
  color: #ffffff;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
  margin-left: 8px;
}

.promptDescription {
  font-size: 13px;
  color: #aaaaaa;
  margin: 0 0 12px 0;
  line-height: 1.4;
}

.promptMeta {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: #666666;
}

.promptKey {
  font-weight: 500;
  color: #888888;
}

.tokenCount {
  color: #FF6B00;
  font-weight: 500;
}

.selectedInfo {
  padding: 12px 16px;
  background: rgba(255, 107, 0, 0.1);
  border-left: 3px solid #FF6B00;
  border-radius: 4px;
}

.selectedText {
  margin: 0;
  font-size: 14px;
  color: #ffffff;
}
```

---

### 3. AttachmentDropZone.module.css

**Full Path:** `packages/widgets/@coderef-dashboard/widget-prompting-workflow/src/components/AttachmentDropZone.module.css`

**Purpose:** Drag & drop zone with state indicators

```css
.dropZone {
  border: 2px dashed #333333;
  border-radius: 8px;
  padding: 48px 24px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
  background: #1a1a1a;
}

.dropZone:hover {
  border-color: #FF6B00;
  background: #242424;
}

.dropZone.drag {
  border-color: #FF6B00;
  background: rgba(255, 107, 0, 0.1);
  box-shadow: inset 0 0 12px rgba(255, 107, 0, 0.2);
}

.dropZone.loading {
  border-color: #4a9eff;
  background: rgba(74, 158, 255, 0.05);
  pointer-events: none;
}

.dropZone.success {
  border-color: #4caf50;
  background: rgba(76, 175, 80, 0.05);
}

.dropZone.error {
  border-color: #ff6b6b;
  background: rgba(255, 107, 107, 0.05);
}

.dropZone.disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

.content {
  display: block;
  cursor: pointer;
}

.icon {
  font-size: 48px;
  margin-bottom: 16px;
  display: inline-block;
}

.spinner {
  display: inline-block;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.message {
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 8px 0;
}

.hint {
  font-size: 13px;
  color: #888888;
  margin: 0;
}

.error {
  font-size: 13px;
  color: #ff6b6b;
  margin: 8px 0 0 0;
}
```

---

### 4. AttachmentManager.module.css

**Full Path:** `packages/widgets/@coderef-dashboard/widget-prompting-workflow/src/components/AttachmentManager.module.css`

**Purpose:** File list display and controls

```css
.container {
  padding: 24px;
  background: #1a1a1a;
  border-radius: 8px;
  margin-bottom: 24px;
}

.title {
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 20px 0;
}

.actions {
  display: flex;
  gap: 12px;
  margin-top: 16px;
  margin-bottom: 20px;
}

.pasteButton,
.clearButton {
  padding: 10px 16px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.pasteButton {
  background: #FF6B00;
  color: #ffffff;
}

.pasteButton:hover {
  background: #ff8a33;
  transform: translateY(-1px);
}

.clearButton {
  background: #333333;
  color: #ffffff;
}

.clearButton:hover {
  background: #444444;
}

.summary {
  display: flex;
  gap: 24px;
  padding: 12px 16px;
  background: #242424;
  border-radius: 6px;
  margin-bottom: 20px;
}

.summaryItem {
  display: flex;
  align-items: center;
  gap: 8px;
}

.summaryLabel {
  font-size: 13px;
  color: #888888;
  font-weight: 500;
}

.summaryValue {
  font-size: 14px;
  color: #FF6B00;
  font-weight: 600;
}

.attachmentList {
  margin-top: 20px;
}

.listTitle {
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 12px 0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.attachmentItem {
  background: #242424;
  border: 1px solid #333333;
  border-radius: 6px;
  margin-bottom: 12px;
  overflow: hidden;
  transition: border-color 0.2s;
}

.attachmentItem:hover {
  border-color: #FF6B00;
}

.attachmentHeader {
  display: flex;
  align-items: center;
  padding: 12px;
  gap: 12px;
}

.attachmentIcon {
  font-size: 24px;
  flex-shrink: 0;
}

.attachmentInfo {
  flex: 1;
  min-width: 0;
}

.attachmentName {
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 4px 0;
  word-break: break-word;
}

.attachmentMeta {
  font-size: 12px;
  color: #888888;
  margin: 0;
}

.removeButton {
  background: none;
  border: none;
  color: #888888;
  font-size: 18px;
  cursor: pointer;
  padding: 4px;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all 0.2s;
  flex-shrink: 0;
}

.removeButton:hover {
  background: #333333;
  color: #ff6b6b;
}

.attachmentPreview {
  padding: 12px;
  background: #1a1a1a;
  border-top: 1px solid #333333;
  font-size: 12px;
  color: #888888;
  font-family: monospace;
  max-height: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.attachmentPreview p {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
}
```

---

### 5. WorkflowMeta.module.css

**Full Path:** `packages/widgets/@coderef-dashboard/widget-prompting-workflow/src/components/WorkflowMeta.module.css`

**Purpose:** Metadata display (tokens, files, languages)

```css
.container {
  padding: 24px;
  background: #1a1a1a;
  border-radius: 8px;
  margin-bottom: 24px;
}

.title {
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 20px 0;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}

.card {
  background: #242424;
  border: 1px solid #333333;
  border-radius: 8px;
  padding: 16px;
}

.cardTitle {
  font-size: 12px;
  font-weight: 600;
  color: #FF6B00;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 12px 0;
}

.promptInfo {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.promptLabel {
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  margin: 0;
}

.promptTokens {
  font-size: 14px;
  color: #FF6B00;
  margin: 0;
}

.empty {
  font-size: 14px;
  color: #888888;
  margin: 0;
  font-style: italic;
}

.stats {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stat {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
}

.statLabel {
  color: #888888;
}

.statValue {
  color: #ffffff;
  font-weight: 600;
}

.tokenCount {
  font-size: 32px;
  font-weight: 700;
  color: #FF6B00;
  margin: 0;
  word-break: break-word;
}

.tokenCount.warning {
  color: #ff9d33;
}

.tokenBreakdown {
  font-size: 12px;
  color: #888888;
  margin: 8px 0 0 0;
}

.sectionTitle {
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 12px 0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.languages,
.fileTypes {
  margin-bottom: 20px;
}

.languageBadges,
.fileTypeBadges {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.languageBadge,
.fileTypeBadge {
  display: inline-block;
  padding: 6px 12px;
  background: #333333;
  color: #ffffff;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.languageBadge {
  background: rgba(255, 107, 0, 0.15);
  color: #FF6B00;
  border: 1px solid rgba(255, 107, 0, 0.3);
}

.fileTypeBadge {
  background: rgba(100, 200, 255, 0.15);
  color: #64c8ff;
  border: 1px solid rgba(100, 200, 255, 0.3);
}

.warningBox {
  padding: 16px;
  background: rgba(255, 153, 51, 0.1);
  border-left: 4px solid #FF9933;
  border-radius: 4px;
  margin-bottom: 20px;
}

.warningText {
  font-size: 14px;
  color: #FF9933;
  margin: 0 0 8px 0;
  font-weight: 600;
}

.warningHint {
  font-size: 12px;
  color: #FF9933;
  margin: 0;
  opacity: 0.8;
}

.emptyState {
  padding: 40px 20px;
  text-align: center;
}

.emptyText {
  font-size: 14px;
  color: #888888;
  margin: 0;
  font-style: italic;
}
```

---

### 6. ExportMenu.module.css

**Full Path:** `packages/widgets/@coderef-dashboard/widget-prompting-workflow/src/components/ExportMenu.module.css`

**Purpose:** Export buttons and dropdown menu

```css
.container {
  display: flex;
  gap: 12px;
  align-items: center;
  flex-wrap: wrap;
}

.button {
  padding: 12px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  white-space: nowrap;
}

.primary {
  background: #FF6B00;
  color: #ffffff;
}

.primary:hover:not(:disabled) {
  background: #ff8a33;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(255, 107, 0, 0.3);
}

.primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.secondary {
  background: #333333;
  color: #ffffff;
  position: relative;
}

.secondary:hover:not(:disabled) {
  background: #444444;
}

.secondary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.menuWrapper {
  position: relative;
}

.menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: #242424;
  border: 1px solid #333333;
  border-radius: 6px;
  margin-top: 4px;
  min-width: 180px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  z-index: 100;
}

.menuItem {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  padding: 12px 16px;
  background: none;
  border: none;
  color: #ffffff;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  text-align: left;
}

.menuItem:first-child {
  border-radius: 5px 5px 0 0;
}

.menuItem:last-child {
  border-radius: 0 0 5px 5px;
}

.menuItem:hover:not(:disabled) {
  background: #333333;
  padding-left: 20px;
}

.menuItem:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.icon {
  font-size: 16px;
  flex-shrink: 0;
}

.message {
  font-size: 13px;
  margin: 0;
  padding: 8px 12px;
  background: rgba(76, 175, 80, 0.1);
  color: #4caf50;
  border-radius: 4px;
  white-space: nowrap;
}
```

---

### 7. PasteTextModal.module.css

**Full Path:** `packages/widgets/@coderef-dashboard/widget-prompting-workflow/src/components/PasteTextModal.module.css`

**Purpose:** Text paste modal styling

```css
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: #242424;
  border: 1px solid #333333;
  border-radius: 12px;
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px;
  border-bottom: 1px solid #333333;
}

.title {
  font-size: 18px;
  font-weight: 600;
  color: #ffffff;
  margin: 0;
}

.closeButton {
  background: none;
  border: none;
  color: #888888;
  font-size: 24px;
  cursor: pointer;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s;
}

.closeButton:hover {
  color: #ffffff;
}

.body {
  padding: 24px;
  overflow-y: auto;
  flex: 1;
}

.formGroup {
  margin-bottom: 20px;
}

.label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 8px;
}

.input {
  width: 100%;
  padding: 10px 12px;
  background: #1a1a1a;
  border: 1px solid #333333;
  border-radius: 6px;
  color: #ffffff;
  font-size: 14px;
  font-family: inherit;
  box-sizing: border-box;
  transition: border-color 0.2s;
}

.input:focus {
  outline: none;
  border-color: #FF6B00;
  box-shadow: 0 0 8px rgba(255, 107, 0, 0.2);
}

.textarea {
  width: 100%;
  height: 200px;
  padding: 12px;
  background: #1a1a1a;
  border: 1px solid #333333;
  border-radius: 6px;
  color: #ffffff;
  font-size: 14px;
  font-family: monospace;
  resize: vertical;
  box-sizing: border-box;
  transition: border-color 0.2s;
}

.textarea:focus {
  outline: none;
  border-color: #FF6B00;
  box-shadow: 0 0 8px rgba(255, 107, 0, 0.2);
}

.textarea:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.hint {
  font-size: 12px;
  color: #888888;
  margin-top: 6px;
  margin-bottom: 0;
}

.footer {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  padding: 16px 24px;
  border-top: 1px solid #333333;
}

.cancelButton,
.submitButton {
  padding: 10px 20px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
  font-family: inherit;
}

.cancelButton {
  background: #333333;
  color: #ffffff;
}

.cancelButton:hover {
  background: #444444;
}

.submitButton {
  background: #FF6B00;
  color: #ffffff;
}

.submitButton:hover:not(:disabled) {
  background: #ff8a33;
  transform: translateY(-1px);
}

.submitButton:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

---

### 8. PasteFinalResultModal.module.css

**Full Path:** `packages/widgets/@coderef-dashboard/widget-prompting-workflow/src/components/PasteFinalResultModal.module.css`

**Purpose:** Final result paste & save modal (same as PasteTextModal with slight differences)

```css
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: #242424;
  border: 1px solid #333333;
  border-radius: 12px;
  width: 90%;
  max-width: 700px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px;
  border-bottom: 1px solid #333333;
}

.title {
  font-size: 18px;
  font-weight: 600;
  color: #ffffff;
  margin: 0;
}

.closeButton {
  background: none;
  border: none;
  color: #888888;
  font-size: 24px;
  cursor: pointer;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s;
}

.closeButton:hover {
  color: #ffffff;
}

.body {
  padding: 24px;
  overflow-y: auto;
  flex: 1;
}

.description {
  font-size: 14px;
  color: #aaaaaa;
  margin: 0 0 20px 0;
  line-height: 1.5;
}

.formGroup {
  margin-bottom: 20px;
}

.label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 8px;
}

.textarea {
  width: 100%;
  height: 300px;
  padding: 12px;
  background: #1a1a1a;
  border: 1px solid #333333;
  border-radius: 6px;
  color: #ffffff;
  font-size: 14px;
  font-family: monospace;
  resize: vertical;
  box-sizing: border-box;
  transition: border-color 0.2s;
}

.textarea:focus {
  outline: none;
  border-color: #FF6B00;
  box-shadow: 0 0 8px rgba(255, 107, 0, 0.2);
}

.textarea:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.hint {
  font-size: 12px;
  color: #888888;
  margin-top: 6px;
  margin-bottom: 0;
}

.footer {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  padding: 16px 24px;
  border-top: 1px solid #333333;
}

.cancelButton,
.saveButton {
  padding: 10px 20px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
  font-family: inherit;
}

.cancelButton {
  background: #333333;
  color: #ffffff;
}

.cancelButton:hover {
  background: #444444;
}

.saveButton {
  background: #FF6B00;
  color: #ffffff;
}

.saveButton:hover:not(:disabled) {
  background: #ff8a33;
  transform: translateY(-1px);
}

.saveButton:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

---

## Component Hierarchy & Layout Flow

```
PromptingWorkflow (Main Container)
│
├── Header Section
│   ├── Title: "LLM Prompting Workflow"
│   └── Subtitle: "Select a prompt, attach files, and export for LLM analysis"
│
├── PromptSelector
│   ├── Title: "1. Select a Prompt"
│   ├── Grid (3 columns, responsive)
│   │   ├── PromptCard (CODE_REVIEW)
│   │   │   ├── Name + Token Badge
│   │   │   ├── Description
│   │   │   └── Meta Info
│   │   ├── PromptCard (SYNTHESIZE)
│   │   └── PromptCard (CONSOLIDATE)
│   └── Selected Prompt Display Box
│
├── AttachmentManager
│   ├── Title: "2. Attach Files & Code"
│   ├── Action Buttons (Paste, Clear)
│   ├── Summary Stats (Files, Total Size, Tokens)
│   ├── AttachmentDropZone
│   │   ├── Icon (📁)
│   │   ├── Message: "Drag & drop files here"
│   │   ├── Hint: "or click to browse"
│   │   └── States: idle, drag, loading, success, error
│   └── Attachment List
│       └── AttachmentItem (repeating)
│           ├── Icon + Name + Meta
│           ├── Remove Button
│           └── Preview (first 200 chars)
│
├── PasteTextModal (Opens when "Paste" clicked)
│   ├── Header: "Paste Code or Text"
│   ├── Form
│   │   ├── Label: "Filename"
│   │   ├── Input: auto-clipboard detection
│   │   ├── Label: "Content"
│   │   ├── Textarea: large area for code
│   │   └── Hint: "Auto-incrementing filenames (clipboard_001.txt, etc)"
│   └── Footer: Cancel | Submit buttons
│
├── WorkflowMeta
│   ├── Title: "3. Workflow Metadata"
│   ├── Grid Layout
│   │   ├── Card: Selected Prompt (name, tokens)
│   │   └── Card: Token Count (large number, warning state)
│   ├── Stats Grid
│   │   ├── Files: 3
│   │   ├── Total Size: 12.4 KB
│   │   ├── Languages: TypeScript, Python
│   │   └── File Types: CODE, PASTED_TEXT
│   └── Languages & File Types (badge grid)
│
├── ExportMenu
│   ├── Primary Button: "Copy All to Clipboard"
│   └── Secondary Button: "Export"
│       ├── Menu Item: Export as JSON
│       └── Menu Item: Export as Markdown
│
└── PasteFinalResultModal (Opens when ready)
    ├── Header: "Paste LLM Result"
    ├── Form
    │   ├── Description
    │   ├── Label: "LLM Response"
    │   ├── Textarea: large area for response
    │   └── Character/Token count
    └── Footer: Cancel | Save buttons
```

---

## Responsive Breakpoints

```css
/* Desktop (1200px+) */
.promptGrid: 3 columns (280px min)
.grid: 4+ columns (200px min)

/* Tablet (768px - 1199px) */
@media (max-width: 1024px) {
  .promptGrid: 2 columns
  .grid: 2 columns
}

/* Mobile (< 768px) */
@media (max-width: 768px) {
  .container: padding 16px
  .title: 24px font
  .promptGrid: 1 column
  .grid: 1 column
  .actions: flex-direction column
  .summary: flex-direction column
}
```

---

## Interactive States

**Buttons:**
- Default: base color, no shadow
- Hover: lighter shade, -1px translateY, slight shadow
- Active: darker shade
- Disabled: 0.5 opacity, not-allowed cursor

**Cards:**
- Default: #333333 border, #242424 bg
- Hover: #FF6B00 border, #2a2a2a bg, -2px translateY
- Selected: #FF6B00 border, box-shadow glow

**Inputs:**
- Default: #333333 border, #1a1a1a bg
- Focus: #FF6B00 border, 0 0 8px rgba(255,107,0,0.2) shadow

**Drop Zone:**
- Idle: #333333 dashed border, #1a1a1a bg
- Hover: #FF6B00 border, #242424 bg
- Drag: #FF6B00 border, rgba(255,107,0,0.1) bg, inset shadow
- Loading: #4a9eff border, rgba(74,158,255,0.05) bg
- Success: #4caf50 border, rgba(76,175,80,0.05) bg
- Error: #ff6b6b border, rgba(255,107,107,0.05) bg

---

## Animation & Transitions

```css
/* All transitions are 0.2s ease */
transition: all 0.2s;

/* Spinner animation */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
animation: spin 1s linear infinite;

/* No animation on click, smooth on hover/focus */
```

---

## Usage for Mock UI

**For an agent to mock the UI:**

1. Use the component paths listed at the top
2. Follow the CSS exactly (colors, fonts, spacing)
3. Implement the component hierarchy
4. Use the interactive states for hover/focus
5. Follow the responsive breakpoints
6. Apply animations to spinners and transitions
7. Use semantic HTML with proper accessibility
8. Match the dark theme (#0a0a0a → #1a1a1a → #242424)
9. Accent color is always #FF6B00 (orange)
10. Border colors default to #333333, #FF6B00 on interactive

All CSS is in **CSS Modules** format (.module.css), so class names are scoped to components.
