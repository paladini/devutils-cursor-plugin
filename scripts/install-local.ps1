$ErrorActionPreference = "Stop"

$mcpPath = Join-Path $env:USERPROFILE ".cursor\mcp.json"
$devutilsEntry = @{
  command = "npx"
  args = @("-y", "devutils-mcp-server")
}

if (-not (Test-Path (Split-Path $mcpPath -Parent))) {
  New-Item -ItemType Directory -Path (Split-Path $mcpPath -Parent) | Out-Null
}

if (Test-Path $mcpPath) {
  $config = Get-Content $mcpPath -Raw | ConvertFrom-Json
} else {
  $config = [pscustomobject]@{ mcpServers = [pscustomobject]@{} }
}

if (-not $config.mcpServers) {
  $config | Add-Member -NotePropertyName mcpServers -NotePropertyValue ([pscustomobject]@{})
}

$config.mcpServers | Add-Member -NotePropertyName devutils -NotePropertyValue $devutilsEntry -Force

$config | ConvertTo-Json -Depth 10 | Set-Content -Path $mcpPath -Encoding UTF8

Write-Host "Installed devutils MCP server in $mcpPath"
Write-Host "Reload Cursor (Developer: Reload Window) to connect."
