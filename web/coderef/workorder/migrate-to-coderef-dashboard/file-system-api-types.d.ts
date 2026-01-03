/**
 * File System Access API TypeScript Definitions
 *
 * Complete type definitions for File System Access API (WICG standard)
 * Used by CodeRef Explorer for local directory browsing
 *
 * Source: https://wicg.github.io/file-system-access/
 * Extracted from: C:\Users\willh\Desktop\assistant\web\src\pages\coderef-explorer.html
 */

// ============================================================================
// Core File System Access API Types
// ============================================================================

/**
 * Permission state for file system access
 */
type PermissionState = 'granted' | 'denied' | 'prompt';

/**
 * Mode for file system access
 */
interface FileSystemHandlePermissionDescriptor {
  mode?: 'read' | 'readwrite';
}

/**
 * Options for directory picker
 */
interface DirectoryPickerOptions {
  mode?: 'read' | 'readwrite';
  startIn?: 'desktop' | 'documents' | 'downloads' | 'music' | 'pictures' | 'videos';
}

/**
 * Base interface for all file system handles
 */
interface FileSystemHandle {
  kind: 'file' | 'directory';
  name: string;

  /**
   * Check current permission state
   */
  queryPermission(descriptor?: FileSystemHandlePermissionDescriptor): Promise<PermissionState>;

  /**
   * Request permission from user
   */
  requestPermission(descriptor?: FileSystemHandlePermissionDescriptor): Promise<PermissionState>;

  /**
   * Check if two handles refer to the same entry
   */
  isSameEntry(other: FileSystemHandle): Promise<boolean>;
}

/**
 * Handle to a file in the file system
 */
interface FileSystemFileHandle extends FileSystemHandle {
  kind: 'file';

  /**
   * Get File object for reading
   */
  getFile(): Promise<File>;

  /**
   * Create writable stream (requires 'readwrite' permission)
   */
  createWritable(): Promise<FileSystemWritableFileStream>;
}

/**
 * Handle to a directory in the file system
 */
interface FileSystemDirectoryHandle extends FileSystemHandle {
  kind: 'directory';

  /**
   * Async iteration over directory entries
   * Usage: for await (const entry of dirHandle.values()) { ... }
   */
  values(): AsyncIterableIterator<FileSystemFileHandle | FileSystemDirectoryHandle>;

  /**
   * Async iteration over directory entries with keys
   */
  entries(): AsyncIterableIterator<[string, FileSystemFileHandle | FileSystemDirectoryHandle]>;

  /**
   * Async iteration over entry names
   */
  keys(): AsyncIterableIterator<string>;

  /**
   * Get a file handle by name
   */
  getFileHandle(name: string, options?: { create?: boolean }): Promise<FileSystemFileHandle>;

  /**
   * Get a directory handle by name
   */
  getDirectoryHandle(name: string, options?: { create?: boolean }): Promise<FileSystemDirectoryHandle>;

  /**
   * Remove a file or directory
   */
  removeEntry(name: string, options?: { recursive?: boolean }): Promise<void>;

  /**
   * Resolve path from this directory to a descendant
   */
  resolve(possibleDescendant: FileSystemHandle): Promise<string[] | null>;
}

/**
 * Writable stream for file operations (requires 'readwrite' permission)
 */
interface FileSystemWritableFileStream extends WritableStream {
  write(data: BufferSource | Blob | string | WriteParams): Promise<void>;
  seek(position: number): Promise<void>;
  truncate(size: number): Promise<void>;
}

interface WriteParams {
  type: 'write' | 'seek' | 'truncate';
  data?: BufferSource | Blob | string;
  position?: number;
  size?: number;
}

// ============================================================================
// Window API Extensions
// ============================================================================

interface Window {
  /**
   * Show directory picker dialog
   * Returns a handle to the selected directory
   *
   * Usage:
   *   const dirHandle = await window.showDirectoryPicker({ mode: 'read' });
   *   for await (const entry of dirHandle.values()) {
   *     console.log(entry.name, entry.kind);
   *   }
   */
  showDirectoryPicker(options?: DirectoryPickerOptions): Promise<FileSystemDirectoryHandle>;

  /**
   * Show file picker dialog (single file)
   */
  showOpenFilePicker(options?: OpenFilePickerOptions): Promise<FileSystemFileHandle[]>;

  /**
   * Show save file picker dialog
   */
  showSaveFilePicker(options?: SaveFilePickerOptions): Promise<FileSystemFileHandle>;
}

interface OpenFilePickerOptions {
  multiple?: boolean;
  excludeAcceptAllOption?: boolean;
  types?: FilePickerAcceptType[];
}

interface SaveFilePickerOptions {
  excludeAcceptAllOption?: boolean;
  suggestedName?: string;
  types?: FilePickerAcceptType[];
}

interface FilePickerAcceptType {
  description?: string;
  accept: Record<string, string[]>;
}

// ============================================================================
// IndexedDB Types for Storing Directory Handles
// ============================================================================

/**
 * IndexedDB database schema for CodeRef Explorer
 * Stores directory handles for persistent access
 */
interface CodeRefExplorerDB extends IDBDatabase {
  name: 'CodeRefExplorer';
  version: 1;
  objectStoreNames: DOMStringList & {
    contains(name: 'directoryHandles'): boolean;
  };
}

/**
 * Record stored in IndexedDB
 * Maps project IDs to directory handles
 */
interface DirectoryHandleRecord {
  projectId: string;
  handle: FileSystemDirectoryHandle;
}

/**
 * IndexedDB operations helper types
 */
interface IndexedDBOperations {
  /**
   * Open or create database
   */
  openDB(): Promise<IDBDatabase>;

  /**
   * Save directory handle to IndexedDB
   */
  saveDirectoryHandle(projectId: string, dirHandle: FileSystemDirectoryHandle): Promise<void>;

  /**
   * Retrieve directory handle from IndexedDB
   */
  getDirectoryHandle(projectId: string): Promise<FileSystemDirectoryHandle | undefined>;

  /**
   * Delete directory handle from IndexedDB
   */
  deleteDirectoryHandle(projectId: string): Promise<void>;
}

// ============================================================================
// CodeRef Explorer Data Models
// ============================================================================

/**
 * Project metadata
 * Stored in projects.json on server
 */
interface Project {
  id: string;           // kebab-case identifier
  name: string;         // Display name
  path: string;         // File system path OR "[Directory: name]" for browsed folders
}

/**
 * Tree node for file/folder hierarchy
 * Used for server-mode rendering
 */
interface TreeNode {
  name: string;
  type: 'file' | 'folder';
  path: string;
  children?: TreeNode[];
}

/**
 * File metadata and content
 * Returned by /api/file endpoint
 */
interface FileInfo {
  name: string;
  content: string;
  size: number;         // bytes
  modified: number;     // timestamp
  path: string;
}

// ============================================================================
// Usage Examples
// ============================================================================

/**
 * Example: Browse folder and build tree
 *
 * async function browseFolderAndBuildTree() {
 *   // 1. Show directory picker
 *   const dirHandle = await window.showDirectoryPicker({ mode: 'read' });
 *
 *   // 2. Save to IndexedDB for persistence
 *   await saveDirectoryHandle('my-project', dirHandle);
 *
 *   // 3. Check/request permissions
 *   const permission = await dirHandle.queryPermission({ mode: 'read' });
 *   if (permission !== 'granted') {
 *     await dirHandle.requestPermission({ mode: 'read' });
 *   }
 *
 *   // 4. Build tree recursively
 *   async function buildTree(handle: FileSystemDirectoryHandle): Promise<TreeNode[]> {
 *     const nodes: TreeNode[] = [];
 *     for await (const entry of handle.values()) {
 *       if (entry.kind === 'directory') {
 *         nodes.push({
 *           name: entry.name,
 *           type: 'folder',
 *           path: entry.name,
 *           children: await buildTree(entry)
 *         });
 *       } else {
 *         nodes.push({
 *           name: entry.name,
 *           type: 'file',
 *           path: entry.name
 *         });
 *       }
 *     }
 *     return nodes;
 *   }
 *
 *   return await buildTree(dirHandle);
 * }
 *
 * Example: Read file content
 *
 * async function readFileContent(fileHandle: FileSystemFileHandle): Promise<string> {
 *   const file = await fileHandle.getFile();
 *   return await file.text();
 * }
 */

// ============================================================================
// Browser Compatibility
// ============================================================================

/**
 * Browser Support (as of 2024):
 * - Chrome/Edge: Full support (v86+)
 * - Firefox: No support (under consideration)
 * - Safari: No support
 *
 * Recommended: Electron with Chromium (100% compatible)
 * Next.js: Use in client components only ('use client')
 *
 * Feature Detection:
 *   if ('showDirectoryPicker' in window) {
 *     // File System Access API supported
 *   } else {
 *     // Fallback to server-mode API
 *   }
 */

export {};
