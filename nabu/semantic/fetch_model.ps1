param([Parameter(Mandatory=$true)][string]$ModelDirectory)
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
. (Join-Path $PSScriptRoot 'download_file.ps1')
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$repository = 'Qdrant/bge-small-en-v1.5-onnx-Q'
$revision = 'aa8f8b060edb00e03bfdd08813a2949946c8ba55'
$assets = @('config.json','model_optimized.onnx','ort_config.json','special_tokens_map.json','tokenizer.json','tokenizer_config.json','vocab.txt')
$metadata = Invoke-RestMethod -Uri "https://huggingface.co/api/models/$repository/revision/${revision}?blobs=true"
if ($metadata.sha -ne $revision) { throw 'Unexpected model revision' }
New-Item -ItemType Directory -Force -Path $ModelDirectory | Out-Null
$resolvedDirectory = (Resolve-Path -LiteralPath $ModelDirectory).Path
$hashes = [ordered]@{}
foreach ($filename in $assets) {
    $entry = $metadata.siblings | Where-Object { $_.rfilename -eq $filename }
    $target = Join-Path $resolvedDirectory $filename
    if ($entry.lfs) {
        Get-VerifiedFile -Url "https://huggingface.co/$repository/resolve/$revision/${filename}?download=true" -Target $target -Size $entry.size -Sha256 $entry.lfs.sha256
    } elseif (-not (Test-Path -LiteralPath $target)) {
        $partial = "$target.partial"
        Invoke-WebRequest -UseBasicParsing -Uri "https://huggingface.co/$repository/resolve/$revision/$filename" -OutFile $partial
        if ((Get-Item -LiteralPath $partial).Length -ne $entry.size) { throw "Download size mismatch: $filename" }
        Move-Item -LiteralPath $partial -Destination $target
    }
    if ((Get-Item -LiteralPath $target).Length -ne $entry.size) { throw "Asset size mismatch: $filename" }
    if ($entry.lfs) {
        $actual = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($actual -ne $entry.lfs.sha256) { throw "Checksum mismatch: $filename" }
    } else {
        $hash = [System.Security.Cryptography.IncrementalHash]::CreateHash([System.Security.Cryptography.HashAlgorithmName]::SHA1)
        try {
            $prefix = [System.Text.Encoding]::UTF8.GetBytes("blob $($entry.size)`0")
            $hash.AppendData($prefix)
            $hash.AppendData([System.IO.File]::ReadAllBytes($target))
            $actual = [BitConverter]::ToString($hash.GetHashAndReset()).Replace('-','').ToLowerInvariant()
        } finally { $hash.Dispose() }
        if ($actual -ne $entry.blobId) { throw "Checksum mismatch: $filename" }
    }
    $hashes[$filename] = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()
}
$manifest = [ordered]@{model='BAAI/bge-small-en-v1.5';repository=$repository;revision=$revision;assets=$hashes}
[System.IO.File]::WriteAllText((Join-Path $resolvedDirectory 'nabu-model.json'), ($manifest | ConvertTo-Json -Depth 5), [System.Text.UTF8Encoding]::new($false))
@{model=$manifest.model;revision=$revision;model_dir=$resolvedDirectory;verified_assets=$hashes.Count} | ConvertTo-Json
