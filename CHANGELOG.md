# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-07-08

### Changed

- English marketplace manifest in `.cursor-plugin/plugin.json`.
- Added `author.email` for marketplace submission.
- README clarifies MCP-only plugin scope and official local plugin testing flow.
- Updated submission docs and added `install-plugin-local.ps1`.

## [1.0.0] - 2026-07-07

### Added

- Initial Cursor plugin release packaging `devutils-mcp-server` as an MCP server.
- Marketplace manifest at `.cursor-plugin/plugin.json`.
- MCP configuration at `mcp.json` using `npx -y devutils-mcp-server`.
- Plugin logo at `assets/logo.svg`.
- Documentation for installation via Cursor Customize and Git.
