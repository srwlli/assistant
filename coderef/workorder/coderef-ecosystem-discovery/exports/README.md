# Graph Exports

Dependency graphs from all CodeRef MCP servers (JSON format).

## Available Exports

- `graph-coderef-context.json` - coderef-context
- `graph-coderef-docs.json` - coderef-docs
- `graph-coderef-personas.json` - coderef-personas
- `graph-coderef-testing.json` - coderef-testing
- `graph-coderef-workflow.json` - coderef-workflow
- `graph-papertrail.json` - papertrail

## Missing Exports

- archived/coderef-mcp (graph.json not found)

## Usage

These JSON files can be imported into:
- Neo4j (graph database)
- GraphQL schema generators
- Custom analysis tools
- Dependency visualization tools