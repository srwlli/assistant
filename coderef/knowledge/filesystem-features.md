# Filesystem MCP Server - Features Reference

**Server:** @modelcontextprotocol/server-filesystem
**Type:** Node.js MCP Server
**Purpose:** Secure filesystem operations with directory-level access control
**Current Root:** C:\Users\willh (full home directory access)

---

## Read Operations (Read-Only)

### read_text_file
- Retrieve complete file contents as text
- Optional head/tail parameters for partial reads
- Cannot use head and tail simultaneously

### read_media_file
- Access image or audio files
- Returns base64-encoded data with MIME type
- Supports binary file formats

### read_multiple_files
- Process multiple files in a single operation
- Accepts array of file paths
- Tolerates individual read failures (continues on error)

### list_directory
- View directory contents with type prefixes
- Shows [FILE] or [DIR] markers
- Basic directory listing

### list_directory_with_sizes
- Directory listing with file size information
- Optional sorting by name or size
- Includes summary statistics (total files, total size)

### directory_tree
- Recursive JSON tree structure of directories
- Optional exclude patterns for filtering
- Returns hierarchical file/folder representation

### search_files
- Pattern-based file and directory search
- Supports glob-style pattern matching
- Configurable exclude patterns

### get_file_info
- Detailed file metadata retrieval
- Returns: size, creation time, modified time, access time, type, permissions
- Single file metadata query

### list_allowed_directories
- Display all accessible directories
- Shows current access control configuration
- No parameters required

---

## Write Operations

### create_directory
- Create new directories or verify existence
- Automatically creates parent directories (recursive)
- Idempotent (safe to retry)

### write_file
- Create new files or overwrite existing content
- Accepts file path and text content
- Destructive operation (overwrites without warning)

### edit_file
- Selective file modifications with advanced matching
- Supports line-based and multi-line edits
- Features: whitespace normalization, indentation preservation, dry-run preview mode
- Multiple simultaneous edits in single operation

### move_file
- Rename or relocate files and directories
- Fails if destination already exists (no overwrite)
- Works for both files and directories

---

## Security & Access Control

### Directory Access Control
- Command-line arguments for startup configuration
- MCP Roots for dynamic runtime updates (recommended)
- No server restart required when using Roots

### Read-Only Mode
- Add `--readonly` flag to restrict write operations
- Prevents all destructive operations
- Maintains read access to configured directories

### Tool Annotations
- All tools marked with MCP hints (read-only, idempotent, destructive)
- Write operations flagged as destructive
- Idempotent operations marked safe to retry

---

## Configuration Methods

### 1. Command-line Arguments
```bash
node index.js --root C:\Users\willh
```

### 2. Claude Code settings.local.json
```json
{
  "enabledMcpjsonServers": ["filesystem"]
}
```

### 3. MCP Server Configuration (.mcp-servers/filesystem.json)
```json
{
  "command": "node",
  "args": ["path/to/server", "--root", "C:\\Users\\willh"],
  "transport": "stdio"
}
```

### 4. Docker Deployment
- Mount directories to `/projects` container path
- Sandboxed environment for filesystem access

---

## Use Cases for Orchestrator

- Read workorder files from target projects (communication.json, plan.json)
- Create stub.json files in coderef/working/
- Update workorders.json and projects.md
- Generate handoff context files in target project directories
- Aggregate deliverables across multiple projects
- Validate file structures across coderef ecosystem

---

## Sources

- [Filesystem MCP Server - GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
- [Official README](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md)
- [@modelcontextprotocol/server-filesystem - npm](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem)
- [Model Context Protocol Examples](https://modelcontextprotocol.io/examples)

---

**Last Updated:** 2026-01-01
**Maintained by:** Assistant Orchestrator
