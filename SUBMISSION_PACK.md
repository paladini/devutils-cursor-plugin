# Submission Pack — copy/paste values

Use these pre-filled values for remaining directory submissions.

---

## 1. Claude Code Plugin

**URL:** https://platform.claude.com/plugins/submit  
**Requires:** Login to Claude Console (individual authors)

**Before submit (optional):**
```bash
claude plugin validate C:\Users\Fernando Paladini\devutils-cursor-plugin
```

**Repository URL:**
```
https://github.com/paladini/devutils-cursor-plugin
```

**Privacy Policy URL:**
```
https://github.com/paladini/devutils-cursor-plugin/blob/master/PRIVACY.md
```

**Contact information:**
```
Name: Fernando Paladini
Email: fnpaladini@gmail.com
Support: https://github.com/paladini/devutils-cursor-plugin/issues
```

**Description:**
```
DevUtils MCP bundles devutils-mcp-server — 36 local developer utilities for AI agents: hashing, encoding, UUID/password generation, JWT decode, JSON formatting, timestamps, CIDR/IP tools, and text utilities. Runs via npx with zero API keys or external calls. MIT licensed.
```

**Example use cases (copy for submission form):**

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

**Short prompts users can try after install:**

```
- "Decode this JWT and tell me if it's expired"
- "Generate 5 UUID v4 values"
- "Hash this string with SHA-256"
- "Pretty-print this JSON and validate it"
- "What hosts are in 10.0.0.0/24?"
- "Convert user_profile_id to PascalCase"
- "Diff these two .env snippets"
```

**After approval, users install:**
```
/plugin marketplace add paladini/devutils-cursor-plugin
/plugin install devutils-mcp@devutils-cursor-plugin
```

---

## 2. mcpservers.org

**URL:** https://mcpservers.org/submit

| Field | Value |
| --- | --- |
| Server Name | DevUtils MCP Server |
| Short Description | 36 local developer utilities for AI agents — hash, encoding, UUID, JWT, JSON, network, text. Zero API keys. |
| Link | https://github.com/paladini/devutils-mcp-server |
| Category | Developer Tools |
| Contact Email | fnpaladini@gmail.com |

---

## 3. MCP Find

**URL:** https://www.mcpfind.org/submit

| Field | Value |
| --- | --- |
| Server Name | DevUtils MCP Server |
| GitHub Repository URL | https://github.com/paladini/devutils-mcp-server |
| Package Name | devutils-mcp-server |
| Short Description | 36 local developer utilities for AI agents. Hashing, encoding, UUID generation, JWT decoding, JSON formatting, network tools, and text utilities. Runs locally via npx with no external APIs. |
| Package Type | npm |
| Category | Developer Tools |

Click **Open GitHub Editor** to open the prefilled PR.

---

## 4. awesome-mcp-servers (GitHub PR)

**Repo:** https://github.com/punkpeye/awesome-mcp-servers

Add an entry under **Developer Tools** in README:

```markdown
- [devutils-mcp-server](https://github.com/paladini/devutils-mcp-server) - 36 local developer utilities (hash, encoding, UUID, JWT, JSON, network, text) for any MCP client. Zero API keys.
```

---

## 5. GitHub topics (optional, 1 minute)

On https://github.com/paladini/devutils-mcp-server → Settings → Topics, add:

```
mcp-server
mcp
developer-tools
model-context-protocol
```

---

## Already done (no action needed)

- Official MCP Registry: `io.github.paladini/devutils-mcp-server` v1.1.0 **active**
- npm: `devutils-mcp-server@1.1.0`
- Glama: https://glama.ai/mcp/servers/paladini/devutils-mcp-server
- Smithery: https://smithery.ai/server/devutils-mcp-server
- Cursor Marketplace: submitted (awaiting review)
- cursor.directory: submitted (awaiting listing)
