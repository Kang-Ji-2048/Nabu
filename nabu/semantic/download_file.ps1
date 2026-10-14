function Get-VerifiedFile {
    param([string]$Url,[string]$Target,[long]$Size,[string]$Sha256)
    $ErrorActionPreference = 'Stop'
    if (Test-Path -LiteralPath $Target) {
        if ((Get-Item -LiteralPath $Target).Length -eq $Size -and (Get-FileHash -LiteralPath $Target -Algorithm SHA256).Hash.ToLowerInvariant() -eq $Sha256) { return }
        throw "Existing file does not match expected hash: $Target"
    }
    $chunkSize = 1MB
    $parts = [int][Math]::Ceiling($Size / $chunkSize)
    $partial = "$Target.partial"
    # Reuse complete prefix chunks left by an interrupted sequential download.
    if (Test-Path -LiteralPath $partial) {
        $prefix = [System.IO.File]::OpenRead($partial)
        try {
            $buffer = [byte[]]::new($chunkSize)
            for ($index = 0; $index -lt [Math]::Floor($prefix.Length / $chunkSize); $index++) {
                $count = $prefix.Read($buffer,0,$buffer.Length)
                [System.IO.File]::WriteAllBytes("$Target.part.$index",$buffer)
            }
        } finally { $prefix.Dispose() }
    }
    0..($parts-1) | ForEach-Object -Parallel {
        $index = $_
        $start = [long]$index * $using:chunkSize
        $end = [Math]::Min($start + $using:chunkSize - 1,$using:Size - 1)
        $part = "$using:Target.part.$index"
        if ((Test-Path -LiteralPath $part) -and (Get-Item -LiteralPath $part).Length -eq ($end-$start+1)) { return }
        $separator = if (($using:Url).Contains('?')) { '&' } else { '?' }
        $partUrl = "$using:Url${separator}nabu_part=$index"
        & curl.exe --fail --location --silent --show-error --range "$start-$end" --connect-timeout 15 --max-time 180 --retry 2 --output $part $partUrl
        if ($LASTEXITCODE -ne 0 -or (Get-Item -LiteralPath $part).Length -ne ($end-$start+1)) { throw "Incomplete download part $index" }
    } -ThrottleLimit 16
    $stream = [System.IO.File]::Open($partial,[System.IO.FileMode]::Create,[System.IO.FileAccess]::Write)
    try {
        for ($index = 0; $index -lt $parts; $index++) {
            $inputStream = [System.IO.File]::OpenRead("$Target.part.$index")
            try { $inputStream.CopyTo($stream) } finally { $inputStream.Dispose() }
        }
    } finally { $stream.Dispose() }
    if ((Get-Item -LiteralPath $partial).Length -ne $Size -or (Get-FileHash -LiteralPath $partial -Algorithm SHA256).Hash.ToLowerInvariant() -ne $Sha256) { throw 'Assembled download checksum mismatch' }
    Move-Item -LiteralPath $partial -Destination $Target
}
