# Install DevUtils MCP locally in Cursor

This script registers the DevUtils MCP server in your user-level Cursor MCP config (`~/.cursor/mcp.json`).

It does not replace the full plugin install flow in **Customize**, but it makes all 36 DevUtils tools available to the agent immediately after a Cursor reload.

## Usage

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-local.ps1
```

Then reload Cursor (`Developer: Reload Window`) or restart the IDE.

## What it changes

- Adds or updates the `devutils` entry under `mcpServers` in `%USERPROFILE%\.cursor\mcp.json`
- Uses `npx -y devutils-mcp-server` (same as the plugin's `mcp.json`)

## Uninstall

Remove the `devutils` block from `%USERPROFILE%\.cursor\mcp.json` and reload Cursor.
