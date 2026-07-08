# Marketplace Submission Checklist

Use this checklist before submitting the plugin to the Cursor Marketplace.

## Repository

- [x] Single-plugin layout with content at repository root
- [x] Valid `.cursor-plugin/plugin.json` manifest
- [x] Plugin `name` is lowercase kebab-case: `devutils-mcp`
- [x] `displayName`, `description`, `version`, `author`, `license` present
- [x] `homepage` and `repository` URLs set
- [x] `keywords` array for discovery
- [x] `logo` uses relative path: `assets/logo.svg`
- [x] Logo committed to repository

## MCP

- [x] `mcp.json` at plugin root (auto-detected)
- [x] Server entry uses `npx -y devutils-mcp-server`
- [x] No secrets or environment variables required

## Documentation

- [x] `README.md` with description and installation steps
- [x] `CHANGELOG.md` with v1.0.0 entry
- [x] `LICENSE` (MIT)

## Validation

- [x] MCP server starts via `npx -y devutils-mcp-server` (stdio)
- [x] `tools/list` returns 36 tools including `generate_uuid`
- [x] JSON manifests parse without errors
- [ ] Install plugin locally via Cursor Customize (manual step in IDE)
- [ ] Confirm tools appear under Available Tools in Agent window

## Publish

- [ ] Push repository to GitHub: `https://github.com/paladini/devutils-cursor-plugin`
- [ ] Submit repository link to Cursor team (Slack or `kniparko@anysphere.com`)
- [ ] Wait for manual review before Marketplace listing

## Notes

- This plugin is a thin wrapper; the MCP server logic lives in [devutils-mcp-server](https://github.com/paladini/devutils-mcp-server).
- Requires Cursor 3.9+ and Node.js 18+ on the user's machine.
