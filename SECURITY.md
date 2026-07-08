# Security Policy

## Supported versions

| Version | Supported |
| --- | --- |
| Latest release | Yes |

## Reporting a vulnerability

Email **fnpaladini@gmail.com** with:

- Description of the issue
- Steps to reproduce
- Affected version
- Impact assessment (if known)

Please do **not** open public issues for undisclosed security vulnerabilities.

## Scope

DevUtils runs **locally** via `npx -y devutils-mcp-server`. The plugin wrapper does not add network endpoints or collect user data.

Security-relevant areas:

- Input validation in MCP tool handlers ([devutils-mcp-server](https://github.com/paladini/devutils-mcp-server))
- Docker image hardening
- Dependency updates

## Response

Expect an initial reply within 7 days. Fixes are released via npm and GitHub tags.
