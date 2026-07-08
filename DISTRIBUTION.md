# Distribution

DevUtils is distributed across multiple channels. Each targets a different install path.

| Channel | Repo | Status | Install |
| --- | --- | --- | --- |
| Cursor Marketplace | [devutils-cursor-plugin](https://github.com/paladini/devutils-cursor-plugin) | Submitted | Customize → DevUtils MCP |
| cursor.directory | devutils-cursor-plugin | Submitted | Directory listing |
| Claude Code | devutils-cursor-plugin | Submit manually | See below |
| Official MCP Registry | [devutils-mcp-server](https://github.com/paladini/devutils-mcp-server) | Ready to publish | See [REGISTRY_PUBLISH.md](https://github.com/paladini/devutils-mcp-server/blob/main/REGISTRY_PUBLISH.md) |
| npm | devutils-mcp-server | `1.0.0` live; `1.1.0` pending publish | `npx -y devutils-mcp-server` |

## Claude Code — submit

1. Open https://platform.claude.com/plugins/submit
2. Repository: `https://github.com/paladini/devutils-cursor-plugin`
3. Plugin includes `.claude-plugin/plugin.json` + shared `mcp.json`

**Install (after listed):**

```text
/plugin marketplace add paladini/devutils-cursor-plugin
/plugin install devutils-mcp@devutils-cursor-plugin
```

## Official MCP Registry — your steps

The server repo has everything configured. You still need to:

1. `npm login` && `npm publish` in `devutils-mcp-server` (publishes `1.1.0` with `mcpName`)
2. `mcp-publisher login github` (device code at https://github.com/login/device)
3. `mcp-publisher publish`

Full guide: https://github.com/paladini/devutils-mcp-server/blob/main/REGISTRY_PUBLISH.md
