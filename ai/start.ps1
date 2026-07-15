# NoLoop AI engine — Windows / PowerShell launcher (:8000)
# Usage:  ./start.ps1
$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

# Create venv + install deps on first run
if (-not (Test-Path ".venv")) {
    python -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
}

# Run the API (uses the venv's uvicorn without needing to "activate")
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
