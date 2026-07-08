$ErrorActionPreference = "Stop"

$repoRoot = Split-Path $PSScriptRoot -Parent
$targetRoot = Join-Path $env:USERPROFILE ".cursor\plugins\local\devutils-mcp"

$exclude = @(".git")

if (-not (Test-Path $targetRoot)) {
  New-Item -ItemType Directory -Path $targetRoot -Force | Out-Null
}

Get-ChildItem -Path $repoRoot -Force | Where-Object {
  $exclude -notcontains $_.Name
} | ForEach-Object {
  $destination = Join-Path $targetRoot $_.Name
  if ($_.PSIsContainer) {
    if (Test-Path $destination) {
      Remove-Item -Path $destination -Recurse -Force
    }
    Copy-Item -Path $_.FullName -Destination $destination -Recurse -Force
  } else {
    Copy-Item -Path $_.FullName -Destination $destination -Force
  }
}

Write-Host "Installed plugin to $targetRoot"
Write-Host "Reload Cursor (Developer: Reload Window), then verify devutils under Customize -> MCPs."
