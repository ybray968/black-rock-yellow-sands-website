# PowerShell script to permanently add gettext tools to system PATH
# Run this script as Administrator to add gettext tools to your system PATH permanently

$gettextPath = "C:\Users\Al Muaddib\construction_materials_site\gettext-tools\bin"

# Get current PATH
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")

# Check if gettext path is already in PATH
if ($currentPath -notlike "*$gettextPath*") {
    # Add gettext path to user PATH
    $newPath = $currentPath + ";" + $gettextPath
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    Write-Host "Gettext tools added to PATH successfully!" -ForegroundColor Green
    Write-Host "Please restart PowerShell/Command Prompt to use the new PATH." -ForegroundColor Yellow
} else {
    Write-Host "Gettext tools are already in PATH." -ForegroundColor Yellow
}

# Test if msgfmt is accessible
try {
    $result = & msgfmt --version 2>$null
    if ($result) {
        Write-Host "✓ msgfmt is working correctly!" -ForegroundColor Green
    }
} catch {
    Write-Host "⚠ msgfmt not found. You may need to restart your terminal." -ForegroundColor Orange
}
