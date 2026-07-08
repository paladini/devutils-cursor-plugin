# Marketplace Submission Checklist

Use this checklist before submitting the plugin to the Cursor Marketplace.

**Publisher type:** Individual open-source developer (MCP-only plugin).

## Repository

- [x] Single-plugin layout with content at repository root
- [x] Valid `.cursor-plugin/plugin.json` manifest
- [x] Plugin `name` is lowercase kebab-case: `devutils-mcp`
- [x] `displayName`, `description`, `version`, `author`, `license` present
- [x] `author.email` set for marketplace contact
- [x] Manifest and README text in English
- [x] `homepage` and `repository` URLs set
- [x] `keywords` array for discovery
- [x] `logo` uses relative path: `assets/logo.svg`
- [x] Logo committed to repository

## MCP

- [x] `mcp.json` at plugin root (auto-detected)
- [x] Server entry uses `mcpServers.devutils` with `npx -y devutils-mcp-server`
- [x] No secrets or environment variables required

## Documentation

- [x] `README.md` with description, install paths, and local plugin testing
- [x] `CHANGELOG.md` with v1.0.1 entry
- [x] `LICENSE` (MIT)

## Validation

- [x] MCP server starts via `npx -y devutils-mcp-server` (stdio)
- [x] `tools/list` returns 36 tools including `generate_uuid`
- [x] JSON manifests parse without errors
- [x] `scripts/install-plugin-local.ps1` installs to `~/.cursor/plugins/local/devutils-mcp`
- [ ] Reload Cursor and confirm `devutils` appears under Customize → MCPs (manual IDE step)
- [ ] Confirm tools appear under Available Tools in Agent window (manual IDE step)

## Publish

- [x] Push repository to GitHub: `https://github.com/paladini/devutils-cursor-plugin`
- [ ] Submit at https://cursor.com/marketplace/publish (individual account)
- [ ] Wait for manual review before Marketplace listing

## Marketplace form values

| Field | Value |
| --- | --- |
| Organization name | Fernando Paladini (or `fnpaladini`) |
| Organization handle | `fnpaladini` |
| Contact email | `fnpaladini@gmail.com` |
| Logotype URL | `https://raw.githubusercontent.com/paladini/devutils-cursor-plugin/master/assets/logo.svg` |
| GitHub repository | `https://github.com/paladini/devutils-cursor-plugin` |
| Website URL | `https://github.com/paladini` |

## Notes

- This plugin is a thin wrapper; the MCP server logic lives in [devutils-mcp-server](https://github.com/paladini/devutils-mcp-server).
- Requires Node.js 18+ on the user's machine for `npx`.
- No rules, skills, agents, commands, or hooks are required for an MCP-only plugin.
