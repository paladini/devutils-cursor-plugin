# DevUtils MCP

Multi-platform plugin for [devutils-mcp-server](https://github.com/paladini/devutils-mcp-server) — 36 local developer utilities (hash, encoding, UUID, JWT, JSON, network, text) with zero external API calls.

Works with **Cursor** and **Claude Code**. Shares a single `mcp.json` that runs `npx -y devutils-mcp-server`.

## Install

### Cursor

1. Open **Cursor Settings → Customize**
2. Search for **DevUtils MCP**
3. Click **Install**
4. Enable the **devutils** MCP server under **Customize → MCPs**

### Claude Code

```text
/plugin marketplace add paladini/devutils-cursor-plugin
/plugin install devutils-mcp@devutils-cursor-plugin
```

To publish or update in the Claude plugin directory, submit this repo at https://platform.claude.com/plugins/submit

### Official MCP Registry

- **Registry name:** `io.github.paladini/devutils-mcp-server`
- **Install:** `npx -y devutils-mcp-server`
- **Search:** https://registry.modelcontextprotocol.io

## Requirements

- [Cursor](https://cursor.com) or [Claude Code](https://claude.com/product/claude-code) with MCP/plugin support
- [Node.js](https://nodejs.org/) 18+

## Usage

Ask the agent to use DevUtils tools, for example:

- "Generate a UUID v4"
- "Decode this JWT"
- "Hash this string with SHA-256"

See the [devutils-mcp-server docs](https://github.com/paladini/devutils-mcp-server#readme) for the full list of 36 tools.

## Related

- MCP server: [paladini/devutils-mcp-server](https://github.com/paladini/devutils-mcp-server)
- npm: [devutils-mcp-server](https://www.npmjs.com/package/devutils-mcp-server)

## License

MIT — see [LICENSE](LICENSE).
