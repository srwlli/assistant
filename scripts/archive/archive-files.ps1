# Archive Files Script
# Usage: .\archive-files.ps1 "path1" "path2" "path3" ...
# Automatically moves files to assistant/coderef/archived/{project-name}/

param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$FilePaths
)

$AssistantRoot = "C:\Users\willh\Desktop\assistant"
$ArchiveBase = Join-Path $AssistantRoot "coderef\archived"

if ($FilePaths.Count -eq 0) {
    Write-Host "Usage: .\archive-files.ps1 <file1> <file2> ..." -ForegroundColor Yellow
    Write-Host "Example: .\archive-files.ps1 'C:\Users\willh\Desktop\coderef-dashboard\doc.md'" -ForegroundColor Cyan
    exit 1
}

foreach ($FilePath in $FilePaths) {
    if (-not (Test-Path $FilePath)) {
        Write-Host "[ERROR] File not found: $FilePath" -ForegroundColor Red
        continue
    }

    # Extract project name from path
    # Assumes path format: C:\Users\willh\Desktop\{project-name}\...
    $PathParts = $FilePath -split '\\'
    $DesktopIndex = [array]::IndexOf($PathParts, 'Desktop')

    if ($DesktopIndex -eq -1 -or $DesktopIndex + 1 -ge $PathParts.Count) {
        Write-Host "[ERROR] Cannot determine project from path: $FilePath" -ForegroundColor Red
        continue
    }

    $ProjectName = $PathParts[$DesktopIndex + 1]

    # Skip if file is already in assistant project
    if ($ProjectName -eq 'assistant') {
        Write-Host "[SKIP] File already in assistant project: $FilePath" -ForegroundColor Yellow
        continue
    }

    # Create archive directory for this project
    $ArchiveDir = Join-Path $ArchiveBase $ProjectName
    if (-not (Test-Path $ArchiveDir)) {
        New-Item -ItemType Directory -Path $ArchiveDir -Force | Out-Null
        Write-Host "[NEW] Created archive directory: $ProjectName" -ForegroundColor Green
    }

    # Move the file
    $FileName = Split-Path $FilePath -Leaf
    $Destination = Join-Path $ArchiveDir $FileName

    try {
        Move-Item -Path $FilePath -Destination $Destination -Force
        Write-Host "Archived: $FileName -> coderef/archived/$ProjectName/" -ForegroundColor Green
    } catch {
        Write-Host "[ERROR] Failed to move $FileName : $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Archive complete!" -ForegroundColor Cyan
