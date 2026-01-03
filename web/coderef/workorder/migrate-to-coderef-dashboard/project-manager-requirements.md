# ProjectManager Component Requirements

> **Purpose:** Document UI requirements for ProjectManager component in React/Next.js
>
> **Source:** `C:\Users\willh\Desktop\assistant\web\src\pages\coderef-explorer.html` (lines 366-457)
>
> **Target:** `packages/dashboard/src/components/coderef/ProjectManager.tsx`

---

## Overview

The **ProjectManager** component is the top-level UI for CodeRef Explorer. It handles:
1. Project selector dropdown (switch between projects)
2. "Add Project" button (with modal dialog)
3. "Remove Project" button
4. Integration with both local (File System API) and API modes

---

## Next.js Requirements

### Must Use 'use client' Directive

```typescript
'use client';

import { useState, useEffect } from 'react';
import { showDirectoryPicker } from '@/lib/coderef/local-access';
```

**Why?**
- File System Access API (`window.showDirectoryPicker`) only works in **browser environment**
- Next.js App Router defaults to **Server Components**
- 'use client' marks component for client-side rendering

**Error if not used:**
```
ReferenceError: window is not defined
```

---

## Source HTML Structure (Current App)

### Project Selector (Lines 366-376)

```html
<div class="project-selector-inline">
    <select id="project-select" onchange="changeProject(this.value)">
        <!-- Projects loaded dynamically -->
    </select>
    <button class="industrial-button-secondary industrial-button-small"
            onclick="showAddProjectDialog()"
            title="Add new project">
        <span class="material-symbols-outlined sm">add</span>
    </button>
    <button class="industrial-button-secondary industrial-button-small"
            onclick="removeCurrentProject()"
            title="Remove current project">
        <span class="material-symbols-outlined sm">delete</span>
    </button>
</div>
```

### Add Project Modal (Lines 427-457)

```html
<div id="addProjectModal" class="modal" style="display: none;">
    <div class="modal-content">
        <div class="modal-header">
            <h3>Add New Project</h3>
            <button class="modal-close" onclick="closeAddProjectModal()">&times;</button>
        </div>
        <div class="modal-body">
            <div class="form-group">
                <label for="projectName">Project Name</label>
                <input type="text" id="projectName" placeholder="Enter project name..." class="industrial-input">
            </div>
            <div class="form-group">
                <label for="projectPath">Project Folder Path</label>
                <div style="display: flex; gap: var(--spacing-sm);">
                    <input type="text" id="projectPath" placeholder="e.g., C:\Users\willh\Desktop\assistant\coderef" class="industrial-input" style="flex: 1;">
                    <button class="industrial-button-secondary" onclick="browseFolderForPath()" title="Browse for folder">
                        <span class="material-symbols-outlined sm">folder_open</span>
                        Browse
                    </button>
                </div>
                <p class="text-muted text-sm" style="margin-top: var(--spacing-sm);">
                    Type the path or click Browse to select a folder
                </p>
            </div>
        </div>
        <div class="modal-footer">
            <button class="industrial-button-secondary" onclick="closeAddProjectModal()">Cancel</button>
            <button id="addProjectBtn" class="industrial-button-primary" onclick="confirmAddProject()" disabled>Add Project</button>
        </div>
    </div>
</div>
```

---

## React Component Structure

### File: `packages/dashboard/src/components/coderef/ProjectManager.tsx`

```typescript
'use client';

import { useState, useEffect } from 'react';
import { Project } from '@/lib/coderef/types';
import { showDirectoryPicker } from '@/lib/coderef/local-access';
import { saveDirectoryHandle } from '@/lib/coderef/indexeddb';
import { Plus, Trash2, FolderOpen } from 'lucide-react';

interface ProjectManagerProps {
  onProjectChange: (project: Project | null) => void;
  className?: string;
}

export function ProjectManager({ onProjectChange, className }: ProjectManagerProps) {
  const [projects, setProjects] = useState<Project[]>([]);
  const [currentProject, setCurrentProject] = useState<Project | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [projectName, setProjectName] = useState('');
  const [projectPath, setProjectPath] = useState('');
  const [pendingDirHandle, setPendingDirHandle] = useState<FileSystemDirectoryHandle | null>(null);

  // Component implementation...
}
```

---

## Key Features

### 1. Load Projects on Mount

```typescript
useEffect(() => {
  loadProjects();
}, []);

async function loadProjects() {
  try {
    const response = await fetch('/api/coderef/projects');
    const data = await response.json();

    if (data.success) {
      setProjects(data.data);

      // Auto-select first project
      if (data.data.length > 0 && !currentProject) {
        handleProjectChange(data.data[0]);
      }
    }
  } catch (error) {
    console.error('Failed to load projects:', error);
  }
}
```

---

### 2. Project Selector Dropdown

```tsx
<select
  value={currentProject?.id || ''}
  onChange={(e) => {
    const project = projects.find(p => p.id === e.target.value);
    handleProjectChange(project || null);
  }}
  className="flex-1 px-3 py-2 bg-zinc-900 border-2 border-zinc-700 rounded-md"
>
  {projects.length === 0 ? (
    <option disabled>No projects</option>
  ) : (
    projects.map(project => (
      <option key={project.id} value={project.id}>
        {project.name}
      </option>
    ))
  )}
</select>
```

---

### 3. Add Project Button (with Modal)

```tsx
<button
  onClick={() => setIsModalOpen(true)}
  className="p-2 bg-zinc-800 hover:bg-zinc-700 border-2 border-zinc-700 rounded-md"
  title="Add new project"
>
  <Plus className="w-4 h-4" />
</button>
```

---

### 4. Browse Folder Flow (CRITICAL - Hybrid Mode)

```typescript
async function handleBrowseFolder() {
  try {
    // Show directory picker
    const dirHandle = await showDirectoryPicker();

    if (!dirHandle) {
      // User cancelled
      return;
    }

    // Store handle for later
    setPendingDirHandle(dirHandle);

    // Auto-populate form fields
    setProjectPath(`[Directory: ${dirHandle.name}]`);

    if (!projectName) {
      setProjectName(dirHandle.name);
    }
  } catch (error) {
    console.error('Browse folder failed:', error);
    toast.error('File System Access API not supported');
  }
}
```

**Key Points:**
- Store `dirHandle` in component state (`pendingDirHandle`)
- Set path to `[Directory: name]` format (indicates browsed folder)
- Auto-populate name field if empty

---

### 5. Confirm Add Project (Hybrid Storage)

```typescript
async function handleConfirmAddProject() {
  if (!projectName || !projectPath) {
    toast.error('Please fill in all fields');
    return;
  }

  const id = projectName.toLowerCase().replace(/\s+/g, '-');

  try {
    // 1. If user browsed folder, save directory handle to IndexedDB
    if (pendingDirHandle) {
      await saveDirectoryHandle(id, pendingDirHandle);
    }

    // 2. Always save project metadata to API
    const response = await fetch('/api/coderef/projects', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        id,
        name: projectName,
        path: projectPath,
      }),
    });

    const data = await response.json();

    if (data.success) {
      // 3. Reload projects and select new one
      await loadProjects();
      const newProject = projects.find(p => p.id === id);
      if (newProject) {
        handleProjectChange(newProject);
      }

      // 4. Close modal and reset form
      setIsModalOpen(false);
      setProjectName('');
      setProjectPath('');
      setPendingDirHandle(null);

      toast.success('Project added successfully!');
    } else {
      toast.error('Failed to add project');
    }
  } catch (error) {
    console.error('Add project failed:', error);
    toast.error('Failed to add project');
  }
}
```

**Critical - Hybrid Storage Pattern:**
1. **IndexedDB:** Save directory handle (if browsed)
2. **API:** Always save project metadata
3. **Result:** Project works in both local and API modes

---

### 6. Remove Project

```typescript
async function handleRemoveProject() {
  if (!currentProject) return;

  if (!confirm(`Remove project "${currentProject.name}"?`)) {
    return;
  }

  try {
    // 1. Delete from API
    const response = await fetch(`/api/coderef/projects/${currentProject.id}`, {
      method: 'DELETE',
    });

    const data = await response.json();

    if (data.success) {
      // 2. Delete directory handle from IndexedDB
      await deleteDirectoryHandle(currentProject.id);

      // 3. Reload projects
      await loadProjects();
      setCurrentProject(null);
      onProjectChange(null);

      toast.success('Project removed');
    } else {
      toast.error('Failed to remove project');
    }
  } catch (error) {
    console.error('Remove project failed:', error);
    toast.error('Failed to remove project');
  }
}
```

---

## Modal Dialog Requirements

### Using Radix UI Dialog (Dashboard Standard)

```tsx
import * as Dialog from '@radix-ui/react-dialog';

<Dialog.Root open={isModalOpen} onOpenChange={setIsModalOpen}>
  <Dialog.Portal>
    <Dialog.Overlay className="fixed inset-0 bg-black/70 z-50" />
    <Dialog.Content className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-zinc-900 border border-zinc-700 rounded-lg w-full max-w-md max-h-[90vh] overflow-y-auto z-50">
      <Dialog.Title className="px-6 py-4 border-b border-zinc-700 text-lg font-semibold">
        Add New Project
      </Dialog.Title>

      <div className="p-6 space-y-4">
        {/* Form fields */}
      </div>

      <div className="px-6 py-4 border-t border-zinc-700 flex justify-end gap-3">
        <button onClick={() => setIsModalOpen(false)}>Cancel</button>
        <button onClick={handleConfirmAddProject}>Add Project</button>
      </div>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

---

## Form Validation

### Enable/Disable "Add Project" Button

```typescript
const isFormValid = projectName.trim().length > 0 && projectPath.trim().length > 0;

<button
  onClick={handleConfirmAddProject}
  disabled={!isFormValid}
  className={cn(
    'px-4 py-2 rounded-md',
    isFormValid
      ? 'bg-orange-600 hover:bg-orange-700 text-white'
      : 'bg-zinc-700 text-zinc-400 cursor-not-allowed'
  )}
>
  Add Project
</button>
```

---

## State Management

### Component State

```typescript
const [projects, setProjects] = useState<Project[]>([]);           // All projects
const [currentProject, setCurrentProject] = useState<Project | null>(null); // Selected project
const [isModalOpen, setIsModalOpen] = useState(false);             // Modal visibility
const [projectName, setProjectName] = useState('');                // Form: name
const [projectPath, setProjectPath] = useState('');                // Form: path
const [pendingDirHandle, setPendingDirHandle] = useState<FileSystemDirectoryHandle | null>(null); // Browsed folder handle
```

### Props (Parent Communication)

```typescript
interface ProjectManagerProps {
  /** Callback when project selection changes */
  onProjectChange: (project: Project | null) => void;

  /** Optional CSS classes */
  className?: string;
}
```

**Usage in Parent Widget:**
```typescript
<ProjectManager
  onProjectChange={(project) => {
    if (project) {
      loadProjectTree(project.id);
    } else {
      setProjectTree(null);
    }
  }}
/>
```

---

## Styling Requirements

### Match Dashboard Design System

```tsx
// Container
<div className="flex items-center gap-2 pb-4 border-b border-zinc-700">

// Dropdown
<select className="flex-1 px-3 py-2 bg-zinc-900 border-2 border-zinc-700 rounded-md text-white font-mono text-sm focus:outline-none focus:border-orange-600">

// Buttons
<button className="p-2 bg-zinc-800 hover:bg-zinc-700 border-2 border-zinc-700 rounded-md transition-colors">

// Modal
<div className="bg-zinc-900 border border-zinc-700 rounded-lg">

// Input
<input className="w-full px-3 py-2 bg-zinc-950 border-2 border-zinc-700 rounded-md text-white font-mono text-sm focus:outline-none focus:border-orange-600" />
```

**Color Palette (from dashboard):**
- Background: `bg-zinc-950` (darkest), `bg-zinc-900` (panels)
- Borders: `border-zinc-700`
- Hover: `hover:bg-zinc-700`
- Accent: `bg-orange-600`, `focus:border-orange-600`
- Text: `text-white`, `text-zinc-400` (muted)

---

## Error Handling

### 1. API Failures

```typescript
try {
  const response = await fetch('/api/coderef/projects');
  const data = await response.json();

  if (!data.success) {
    throw new Error(data.error || 'Failed to load projects');
  }
} catch (error) {
  console.error('API error:', error);
  toast.error('Failed to load projects');
}
```

### 2. File System API Not Supported

```typescript
async function handleBrowseFolder() {
  try {
    const dirHandle = await showDirectoryPicker();
    // ...
  } catch (error) {
    if (error instanceof Error && error.message.includes('not supported')) {
      toast.error('File System Access API not supported. Please type the full path instead.');
    } else {
      console.error('Browse folder failed:', error);
      toast.error('Failed to browse folder');
    }
  }
}
```

### 3. Permission Denied

Handled by `checkAndRequestPermission` in `local-access.ts`. ProjectManager just calls `onProjectChange` and lets parent handle tree loading.

---

## Testing Checklist

### Manual Testing

- [ ] **Load Projects:** Open component, projects load from API
- [ ] **Select Project:** Choose project from dropdown, `onProjectChange` fires
- [ ] **Add Project (Typed Path):** Type path manually, save → shows in dropdown
- [ ] **Add Project (Browsed Folder):** Click "Browse Folder", select directory → auto-populates name/path
- [ ] **Remove Project:** Delete project → removed from dropdown, IndexedDB cleaned up
- [ ] **Form Validation:** "Add Project" button disabled until both fields filled
- [ ] **Modal Close:** Click "Cancel" or X → modal closes, form resets
- [ ] **No Projects State:** Delete all projects → dropdown shows "No projects"

### Unit Tests

```typescript
// packages/dashboard/src/components/coderef/__tests__/ProjectManager.test.tsx

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { ProjectManager } from '../ProjectManager';

test('loads projects on mount', async () => {
  render(<ProjectManager onProjectChange={jest.fn()} />);
  await waitFor(() => {
    expect(screen.getByRole('option', { name: 'Assistant Web' })).toBeInTheDocument();
  });
});

test('calls onProjectChange when selection changes', () => {
  const handleChange = jest.fn();
  render(<ProjectManager onProjectChange={handleChange} />);

  fireEvent.change(screen.getByRole('combobox'), { target: { value: 'assistant-web' } });

  expect(handleChange).toHaveBeenCalledWith(expect.objectContaining({ id: 'assistant-web' }));
});
```

---

## Summary: Implementation Checklist

### Files to Create

- [ ] `packages/dashboard/src/components/coderef/ProjectManager.tsx`
- [ ] `packages/dashboard/src/components/coderef/__tests__/ProjectManager.test.tsx`

### Dependencies

- [ ] `@radix-ui/react-dialog` (modal)
- [ ] `lucide-react` (icons)
- [ ] `react-hot-toast` or `sonner` (toast notifications)

### Integration Points

- [ ] Imports from `lib/coderef/types.ts`
- [ ] Imports from `lib/coderef/local-access.ts`
- [ ] Imports from `lib/coderef/indexeddb.ts`
- [ ] Calls to `/api/coderef/projects` endpoints

### Key Features

- [ ] 'use client' directive
- [ ] Project selector dropdown
- [ ] Add project modal with "Browse Folder" button
- [ ] Remove project button
- [ ] Hybrid storage (IndexedDB + API)
- [ ] Auto-populate form from directory handle
- [ ] Form validation
- [ ] Error handling
- [ ] Toast notifications

---

**Next:** See `permission-checking-patterns.md` for detailed permission flow documentation (LOCAL-003).
