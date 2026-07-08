# DevUtils — Distribution Map

Last updated: 2026-07-08

## Published and live

| Store | Type | URL | Version | Notes |
| --- | --- | --- | --- | --- |
| **Official MCP Registry** | Canonical | https://registry.modelcontextprotocol.io | 1.1.0 | `io.github.paladini/devutils-mcp-server` — status **active** |
| **npm** | Package | https://www.npmjs.com/package/devutils-mcp-server | 1.1.0 | `npx -y devutils-mcp-server` |
| **Glama** | MCP directory | https://glama.ai/mcp/servers/paladini/devutils-mcp-server | indexed | Auto-crawled from GitHub |
| **Smithery** | MCP directory | https://smithery.ai/server/devutils-mcp-server | indexed | `smithery.yaml` in server repo |
| **awesome-ai-rabbit-holes** | Curated catalog | https://github.com/gabrielmoreira/awesome-ai-rabbit-holes | listed | `catalog/items/github/paladini/devutils-mcp-server.yml` |

## Submitted — awaiting review

| Store | Type | Repo submitted | Status |
| --- | --- | --- | --- |
| **Cursor Marketplace** | Plugin | `paladini/devutils-cursor-plugin` | Submitted by you — manual review |
| **cursor.directory** | Plugin/MCP | `paladini/devutils-cursor-plugin` | Submitted by you — check listing |

## Ready to submit (copy-paste in SUBMISSION_PACK.md)

| Store | Submit URL | Repo to use |
| --- | --- | --- |
| **Claude Code plugin** | https://platform.claude.com/plugins/submit | `devutils-cursor-plugin` |
| **mcpservers.org** | https://mcpservers.org/submit | `devutils-mcp-server` |
| **MCP Find** | https://www.mcpfind.org/submit | `devutils-mcp-server` |
| **awesome-mcp-servers** | PR to `punkpeye/awesome-mcp-servers` | `devutils-mcp-server` |

## Plugin vs server

| Artifact | Repository | Used by |
| --- | --- | --- |
| MCP server (36 tools) | `devutils-mcp-server` | Registry, npm, Glama, Smithery, manual `mcp.json` |
| Cursor + Claude plugin wrapper | `devutils-cursor-plugin` | Cursor Marketplace, cursor.directory, Claude plugin directory |

## Install paths by client

| Client | How users install |
| --- | --- |
| **Any MCP client** | `npx -y devutils-mcp-server` or Official MCP Registry |
| **Cursor** | Customize → DevUtils MCP plugin |
| **Claude Code** | `/plugin install devutils-mcp@devutils-cursor-plugin` (after approval) |
| **Claude Desktop** | `mcp.json` block in config (see server README) |
| **VS Code / Windsurf** | `mcp.json` (see server README) |

## Optional improvements

- Add GitHub topic `mcp-server` on `devutils-mcp-server` (helps Glama/directory crawlers)
- Submit to `punkpeye/awesome-mcp-servers` (high-traffic list)
- Claim/manage Glama listing if you want to update metadata manually
