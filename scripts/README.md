# Install scripts

Two scripts are provided for different use cases.

## `install-plugin-local.ps1` (recommended for plugin testing)

Installs the full plugin to the official Cursor local plugin path:

```text
%USERPROFILE%\.cursor\plugins\local\devutils-mcp\
```

This matches the [Cursor docs](https://cursor.com/docs/plugins) flow for testing a plugin before Marketplace submission.

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-plugin-local.ps1
```

Then run **Developer: Reload Window** and verify `devutils` under **Customize → MCPs**.

## `install-local.ps1` (MCP-only shortcut)

Writes the `devutils` MCP server directly to `%USERPROFILE%\.cursor\mcp.json`.

Use this when you only want the MCP tools without testing the plugin bundle itself.

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-local.ps1
```

Then reload Cursor.

## Which one should I use?

| Goal | Script |
| --- | --- |
| Test the plugin before Marketplace submit | `install-plugin-local.ps1` |
| Quickly enable DevUtils MCP tools | `install-local.ps1` |
