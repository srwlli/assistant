/**
 * Shared TypeScript Types for CodeRef Explorer
 *
 * Core data structures used across local and API modes
 * Place in: packages/dashboard/src/lib/coderef/types.ts
 *
 * Extracted from: C:\Users\willh\Desktop\assistant\web
 */

// ============================================================================
// Project Management
// ============================================================================

/**
 * Project metadata
 *
 * Stored in:
 * - Server: projects.json (via /api/projects endpoints)
 * - Client: IndexedDB (directory handles) + API registration
 *
 * Usage:
 *   const project: Project = {
 *     id: 'assistant-web',
 *     name: 'Assistant Web',
 *     path: 'C:\\Users\\willh\\Desktop\\assistant\\web'
 *   };
 */
export interface Project {
  /** Unique identifier (kebab-case, used as key) */
  id: string;

  /** Display name shown in UI */
  name: string;

  /**
   * File system path
   * - Typed paths: "C:\\Users\\..." or "/home/user/..."
   * - Browsed folders: "[Directory: folder-name]"
   */
  path: string;
}

/**
 * Extended project with access mode metadata
 * Used internally to track whether project uses local or API access
 */
export interface ProjectWithAccessMode extends Project {
  /** Access mode: local (File System API) or api (server endpoints) */
  accessMode: 'local' | 'api';

  /** Whether directory handle exists in IndexedDB */
  hasLocalHandle?: boolean;

  /** Last access timestamp */
  lastAccessed?: number;
}

// ============================================================================
// File System Tree
// ============================================================================

/**
 * Tree node representing a file or folder
 *
 * Used for:
 * - Server-mode: Full tree returned by /api/tree
 * - Local-mode: Built recursively from FileSystemDirectoryHandle
 *
 * Usage:
 *   const tree: TreeNode = {
 *     name: 'coderef',
 *     type: 'folder',
 *     path: 'C:\\project\\coderef',
 *     children: [
 *       { name: 'context.json', type: 'file', path: 'C:\\project\\coderef\\context.json' }
 *     ]
 *   };
 */
export interface TreeNode {
  /** File or folder name */
  name: string;

  /** Node type */
  type: 'file' | 'folder';

  /** Full path to file/folder */
  path: string;

  /** Child nodes (only for folders) */
  children?: TreeNode[];

  /** Whether this is a special coderef folder (for styling) */
  isCoderefFolder?: boolean;
}

// ============================================================================
// File Content
// ============================================================================

/**
 * File metadata and content
 *
 * Returned by:
 * - Server: /api/file?path=...
 * - Local: fileHandle.getFile() + file.text()
 *
 * Usage:
 *   const fileInfo: FileInfo = {
 *     name: 'context.json',
 *     content: '{ "feature": "..." }',
 *     path: 'C:\\project\\coderef\\context.json',
 *     size: 1024,
 *     modified: Date.now()
 *   };
 */
export interface FileInfo {
  /** File name (without path) */
  name: string;

  /** File content as text */
  content: string;

  /** Full path to file */
  path: string;

  /** File size in bytes */
  size: number;

  /** Last modified timestamp (milliseconds since epoch) */
  modified: number;
}

// ============================================================================
// IndexedDB Schema
// ============================================================================

/**
 * Directory handle record stored in IndexedDB
 *
 * Schema:
 * - Database: "CodeRefExplorer"
 * - Store: "directoryHandles"
 * - Key: projectId (string)
 *
 * Usage:
 *   const record: DirectoryHandleRecord = {
 *     projectId: 'assistant-web',
 *     handle: dirHandle
 *   };
 */
export interface DirectoryHandleRecord {
  /** Project ID (matches Project.id) */
  projectId: string;

  /** File System Access API directory handle */
  handle: FileSystemDirectoryHandle;
}

// ============================================================================
// Hybrid Mode Types
// ============================================================================

/**
 * Access attempt result
 * Used by hybrid router to track success/failure
 */
export interface AccessAttemptResult<T> {
  success: boolean;
  data?: T;
  error?: Error;
  mode: 'local' | 'api';
}

/**
 * Hybrid router configuration
 */
export interface HybridRouterConfig {
  /** Try local mode first? */
  preferLocal: boolean;

  /** Fallback to API if local fails? */
  fallbackToAPI: boolean;

  /** Cache results? */
  enableCache: boolean;

  /** Cache TTL in milliseconds */
  cacheTTL?: number;
}

// ============================================================================
// UI State Types
// ============================================================================

/**
 * Current file viewer state
 */
export interface FileViewerState {
  /** Currently selected file path */
  currentFilePath: string | null;

  /** File content */
  currentFileContent: string | null;

  /** File metadata */
  currentFileInfo: FileInfo | null;

  /** Loading state */
  isLoading: boolean;

  /** Error message if load failed */
  error: string | null;
}

/**
 * Tree expansion state
 * Tracks which folders are expanded in the UI
 */
export interface TreeExpansionState {
  /** Map of folder paths to expansion state */
  expandedFolders: Map<string, boolean>;
}

/**
 * Project selector state
 */
export interface ProjectSelectorState {
  /** All available projects */
  projects: Project[];

  /** Currently selected project */
  currentProject: Project | null;

  /** Loading state */
  isLoading: boolean;

  /** Error message if load failed */
  error: string | null;
}

// ============================================================================
// API Response Types
// ============================================================================

/**
 * Standard API response wrapper
 */
export interface APIResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

/**
 * Projects API responses
 */
export interface GetProjectsResponse extends APIResponse<Project[]> {}
export interface SaveProjectResponse extends APIResponse<{ id: string }> {}
export interface DeleteProjectResponse extends APIResponse<{ id: string }> {}

/**
 * Tree API response
 */
export interface GetTreeResponse extends APIResponse<TreeNode> {}

/**
 * File API response
 */
export interface GetFileResponse extends APIResponse<FileInfo> {}

// ============================================================================
// Constants
// ============================================================================

/**
 * IndexedDB configuration
 */
export const INDEXEDDB_CONFIG = {
  DB_NAME: 'CodeRefExplorer',
  DB_VERSION: 1,
  STORE_NAME: 'directoryHandles',
} as const;

/**
 * API endpoints
 */
export const API_ENDPOINTS = {
  PROJECTS: '/api/coderef/projects',
  PROJECT_BY_ID: (id: string) => `/api/coderef/projects/${id}`,
  TREE: '/api/coderef/tree',
  FILE: '/api/coderef/file',
} as const;

/**
 * File types for syntax highlighting
 */
export const FILE_TYPES = {
  JSON: ['.json'],
  MARKDOWN: ['.md', '.markdown'],
  TEXT: ['.txt', '.log'],
  CODE: ['.ts', '.tsx', '.js', '.jsx', '.py', '.java', '.c', '.cpp', '.go', '.rs'],
} as const;

// ============================================================================
// Type Guards
// ============================================================================

/**
 * Check if a node is a folder
 */
export function isFolder(node: TreeNode): boolean {
  return node.type === 'folder';
}

/**
 * Check if a node is a file
 */
export function isFile(node: TreeNode): boolean {
  return node.type === 'file';
}

/**
 * Check if File System Access API is supported
 */
export function isFileSystemAccessSupported(): boolean {
  return typeof window !== 'undefined' && 'showDirectoryPicker' in window;
}

/**
 * Check if a project uses browsed directory (vs typed path)
 */
export function isBrowsedDirectory(project: Project): boolean {
  return project.path.startsWith('[Directory:');
}

/**
 * Extract directory name from browsed path
 * "[Directory: folder-name]" → "folder-name"
 */
export function extractDirectoryName(path: string): string | null {
  const match = path.match(/^\[Directory:\s*(.+)\]$/);
  return match ? match[1] : null;
}

// ============================================================================
// Utility Functions
// ============================================================================

/**
 * Generate project ID from name
 * "My Project" → "my-project"
 */
export function generateProjectId(name: string): string {
  return name.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
}

/**
 * Format file size for display
 * 1024 → "1.00 KB"
 */
export function formatFileSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(2)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
}

/**
 * Format date for display
 * timestamp → "Jan 15, 2024"
 */
export function formatDate(timestamp: number): string {
  return new Date(timestamp).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
}

/**
 * Get file extension
 * "context.json" → ".json"
 */
export function getFileExtension(filename: string): string {
  const lastDot = filename.lastIndexOf('.');
  return lastDot === -1 ? '' : filename.substring(lastDot);
}

/**
 * Determine file type for syntax highlighting
 */
export function getFileType(filename: string): 'json' | 'markdown' | 'code' | 'text' {
  const ext = getFileExtension(filename);

  if (FILE_TYPES.JSON.includes(ext)) return 'json';
  if (FILE_TYPES.MARKDOWN.includes(ext)) return 'markdown';
  if (FILE_TYPES.CODE.includes(ext)) return 'code';
  return 'text';
}
