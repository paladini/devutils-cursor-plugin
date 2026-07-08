# DevUtils MCP — Cursor Plugin

Cursor plugin that bundles the [devutils-mcp-server](https://github.com/paladini/devutils-mcp-server) MCP server, giving your AI assistant **36 local developer utilities** with zero external API calls.

## What it does

When installed, this plugin registers an MCP server named `devutils` that runs via:

```bash
npx -y devutils-mcp-server
```

All tools execute locally on your machine. No API keys, no network requests.

## Available tools (36)

| Category | Tools |
| --- | --- |
| Hash (6) | `hash_md5`, `hash_sha1`, `hash_sha256`, `hash_sha512`, `hash_bcrypt`, `hash_bcrypt_verify` |
| Encoding (8) | `base64_encode`, `base64_decode`, `url_encode`, `url_decode`, `html_encode`, `html_decode`, `hex_encode`, `hex_decode` |
| Generators (4) | `generate_uuid`, `generate_nanoid`, `generate_password`, `generate_random_hex` |
| JWT (2) | `jwt_decode`, `jwt_validate` |
| Formatters (3) | `json_format`, `json_validate`, `json_path_query` |
| Converters (5) | `timestamp_to_date`, `date_to_timestamp`, `number_base_convert`, `color_convert`, `byte_convert` |
| Network (2) | `cidr_calculate`, `ip_validate` |
| Text (6) | `text_stats`, `lorem_ipsum`, `case_convert`, `slugify`, `regex_test`, `text_diff` |

See the [devutils-mcp-server README](https://github.com/paladini/devutils-mcp-server#readme) for full tool documentation.

## Installation

### Option 1 — Cursor Marketplace (recommended)

1. Open **Cursor Settings → Customize**.
2. Search for **DevUtils MCP**.
3. Click **Install**.

### Option 2 — Install from Git

1. Open **Cursor Settings → Customize**.
2. Add this repository as a plugin source (or import via team marketplace).
3. Install the **devutils-mcp** plugin.
4. Enable the **devutils** MCP server in Customize.

### Option 3 — Local development

Clone this repo and point Cursor to the local folder:

```bash
git clone https://github.com/paladini/devutils-cursor-plugin.git
```

Then install the plugin from the cloned directory via **Customize**.

## Requirements

- [Cursor](https://cursor.com) 3.9+ (plugin system with Customize page)
- [Node.js](https://nodejs.org/) 18+ (for `npx` to run the MCP server)

## Plugin structure

```text
devutils-cursor-plugin/
├── .cursor-plugin/
│   └── plugin.json        # Plugin manifest
├── mcp.json               # MCP server definition (auto-detected)
├── assets/
│   └── logo.svg
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Usage in Cursor

Once installed:

1. Open the Agent window or chat.
2. Ensure the **devutils** MCP server is enabled under **Customize → MCPs**.
3. Ask the agent to use DevUtils tools, for example:
   - "Generate a UUID v4"
   - "Decode this JWT"
   - "Calculate the CIDR range for 192.168.1.0/24"
   - "Hash this string with SHA-256"

Tools appear under **Available Tools** when the MCP server is connected.

## Related projects

- **MCP server package:** [paladini/devutils-mcp-server](https://github.com/paladini/devutils-mcp-server)
- **npm:** [devutils-mcp-server](https://www.npmjs.com/package/devutils-mcp-server)

## License

MIT — see [LICENSE](LICENSE).
