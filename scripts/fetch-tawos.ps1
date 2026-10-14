param([string]$OutputDirectory = 'data/source')
$ErrorActionPreference = 'Stop'

# Pinned to the version linked by the upstream TAWOS v1.1 repository.
$metadata = Invoke-RestMethod -Uri 'https://api.figshare.com/v2/articles/21308124'
$file = $metadata.files | Where-Object { $_.id -eq 37806375 }
if (-not $file) { throw 'Pinned TAWOS archive not found in Figshare metadata.' }
New-Item -ItemType Directory -Force -Path $OutputDirectory | Out-Null
$archive = Join-Path (Resolve-Path -LiteralPath $OutputDirectory) 'TAWOS.sql.zip'
if (Test-Path -LiteralPath $archive) { throw "Archive already exists: $archive" }
$partial = "$archive.partial"
if (Test-Path -LiteralPath $partial) { throw "Partial archive exists; move it aside before retrying: $partial" }
Write-Host "Downloading TAWOS ($($file.size) bytes) to $partial"
Invoke-WebRequest -Uri $file.download_url -OutFile $partial
if ((Get-Item -LiteralPath $partial).Length -ne $file.size) { throw 'Download size mismatch; partial file retained.' }
$md5 = (Get-FileHash -LiteralPath $partial -Algorithm MD5).Hash.ToLowerInvariant()
if ($md5 -ne $file.computed_md5) { throw 'Download checksum mismatch; partial file retained.' }
Move-Item -LiteralPath $partial -Destination $archive
Write-Host "Verified archive: $archive"
Write-Host 'Extract the archive and restore the SQL dump into MySQL 8 before running nabu extract.'
