# Distribution Map

Where DevUtils is published, submitted, and how to install it.

Last updated: 2026-07-08

## Live

| Channel | Type | URL | Version |
| --- | --- | --- | --- |
| **Official MCP Registry** | Canonical | https://registry.modelcontextprotocol.io | 1.1.0 — `io.github.paladini/devutils-mcp-server` **active** |
| **npm** | Package | https://www.npmjs.com/package/devutils-mcp-server | 1.1.0 |
| **Glama** | MCP directory | https://glama.ai/mcp/servers/paladini/devutils-mcp-server | indexed |
| **Smithery** | MCP directory | https://smithery.ai/server/devutils-mcp-server | indexed |
| **awesome-ai-rabbit-holes** | Curated catalog | https://github.com/gabrielmoreira/awesome-ai-rabbit-holes | listed |

## Awaiting review

| Channel | Repo | Status |
| --- | --- | --- |
| **Cursor Marketplace** | `paladini/devutils-cursor-plugin` | Submitted |
| **cursor.directory** | `paladini/devutils-cursor-plugin` | Submitted |

## Ready to submit

### Claude Code Plugin

**URL:** https://platform.claude.com/plugins/submit

| Field | Value |
| --- | --- |
| Repository | `https://github.com/paladini/devutils-cursor-plugin` |
| Privacy Policy | `https://github.com/paladini/devutils-cursor-plugin/blob/master/PRIVACY.md` |
| Contact | Fernando Paladini — fnpaladini@gmail.com |
| Support | `https://github.com/paladini/devutils-cursor-plugin/issues` |

**Description:**
```
DevUtils MCP bundles devutils-mcp-server — 36 local developer utilities for AI agents: hashing, encoding, UUID/password generation, JWT decode, JSON formatting, timestamps, CIDR/IP tools, and text utilities. Runs via npx with zero API keys or external calls. MIT licensed.
```

**Example use cases:**
```
1. Debug auth flows — Decode a JWT from a failing API request, check expiration, and verify the payload without leaving the terminal.
2. Prepare test data — Generate UUIDs, secure passwords, and random hex strings while writing scripts, seeds, or API fixtures.
3. Inspect and fix JSON — Validate malformed config files, pretty-print API responses, and extract nested values with dot-notation paths.
4. Network troubleshooting — Calculate CIDR ranges for a subnet and validate whether an IP is private, loopback, or public.
5. Everyday encoding — Base64-encode/decode payloads, URL-encode query params, and convert strings between hex, HTML entities, and plain text.
6. Refactor naming — Convert variable names between camelCase, snake_case, kebab-case, and slugify titles for URLs or filenames.
7. Quick hashing — Hash passwords with bcrypt, verify hashes, or generate SHA-256/SHA-512 digests for checksums and comparisons.
8. Text and diff work — Compare two config snippets line-by-line, test regex patterns, and get word/line counts for docs or logs.
```

**After approval:**
```text
/plugin marketplace add paladini/devutils-cursor-plugin
/plugin install devutils-mcp@devutils-cursor-plugin
```

### mcpservers.org

**URL:** https://mcpservers.org/submit

| Field | Value |
| --- | --- |
| Server Name | DevUtils MCP Server |
| Short Description | 36 local developer utilities for AI agents — hash, encoding, UUID, JWT, JSON, network, text. Zero API keys. |
| Link | https://github.com/paladini/devutils-mcp-server |
| Category | Developer Tools |
| Contact Email | fnpaladini@gmail.com |

### MCP Find

**URL:** https://www.mcpfind.org/submit

| Field | Value |
| --- | --- |
| Server Name | DevUtils MCP Server |
| GitHub Repository URL | https://github.com/paladini/devutils-mcp-server |
| Package Name | devutils-mcp-server |
| Short Description | 36 local developer utilities for AI agents. Hashing, encoding, UUID generation, JWT decoding, JSON formatting, network tools, and text utilities. Runs locally via npx with no external APIs. |
| Package Type | npm |
| Category | Developer Tools |

### awesome-mcp-servers

**Repo:** https://github.com/punkpeye/awesome-mcp-servers

Add under **Developer Tools**:

```markdown
- [devutils-mcp-server](https://github.com/paladini/devutils-mcp-server) - 36 local developer utilities (hash, encoding, UUID, JWT, JSON, network, text) for any MCP client. Zero API keys.
```

## Plugin vs server

| Artifact | Repository | Used by |
| --- | --- | --- |
| MCP server (36 tools) | `devutils-mcp-server` | Registry, npm, Glama, Smithery, manual `mcp.json` |
| Cursor + Claude plugin | `devutils-cursor-plugin` | Cursor Marketplace, cursor.directory, Claude plugin directory |

## Install by client

| Client | How |
| --- | --- |
| **Cursor** | Customize → DevUtils MCP plugin |
| **Claude Code** | `/plugin install devutils-mcp@devutils-cursor-plugin` |
| **Any MCP client** | `npx -y devutils-mcp-server` |
| **Claude Desktop / VS Code / Windsurf** | `mcp.json` — see [server README](https://github.com/paladini/devutils-mcp-server#-client-setup) |
