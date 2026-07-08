# Privacy Policy — DevUtils MCP Plugin

**Last updated:** July 8, 2026  
**Publisher:** Fernando Paladini (individual open-source developer)  
**Contact:** fnpaladini@gmail.com

## Summary

DevUtils MCP is a local developer utilities plugin. It does **not** collect, store, or transmit personal data to the plugin author or any third-party service operated by the author.

## What this plugin does

When enabled, the plugin runs the open-source MCP server `devutils-mcp-server` locally on your machine via `npx`. All tool operations (hashing, encoding, UUID generation, JWT decoding, JSON formatting, etc.) execute **locally**. No API keys are required.

## Data handling

- **No account** is required to use this plugin.
- **No telemetry** is sent to the plugin author.
- **No cloud service** is operated by the author for this plugin.
- Input you pass to DevUtils tools (strings, JWTs, JSON, etc.) is processed **only on your device** by the local MCP server process.

## Third-party services

The plugin may download the `devutils-mcp-server` package from **npm** when first run (`npx -y devutils-mcp-server`). That download is subject to [npm's policies](https://www.npmjs.com/policies/privacy). The plugin author does not receive data from that process.

## Open source

- Plugin: https://github.com/paladini/devutils-cursor-plugin  
- MCP server: https://github.com/paladini/devutils-mcp-server  

## Contact

Questions or privacy concerns:

- **Email:** fnpaladini@gmail.com  
- **GitHub Issues:** https://github.com/paladini/devutils-cursor-plugin/issues

## Changes

This policy may be updated in the plugin repository. The latest version is always available at this file in the GitHub repo.
