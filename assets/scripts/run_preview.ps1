<#
.SYNOPSIS
    Windows PowerShell preview launcher for citycraft.

.DESCRIPTION
    Substitutes __KEY__ placeholders in the template, serves the filled HTML
    on localhost, opens the default browser, waits for POST /submit, and
    prints the result JSON to stdout.

    Requires: PowerShell 5.1+ (Windows built-in) or PowerShell 7+.
    No external dependencies — uses System.Net.HttpListener from .NET.

.PARAMETER Template
    Path to the HTML template file.

.PARAMETER Output
    Path to write the filled HTML.

.PARAMETER Port
    HTTP port to listen on (default: 17432).

.PARAMETER Result
    Path to write the submitted JSON (default: %TEMP%\citycraft_result.json).

.PARAMETER Timeout
    Seconds to wait for submission (default: 300).

.PARAMETER Sub
    One or more KEY=VALUE substitution pairs. Replaces __KEY__ in the template.
    Repeat the flag for multiple pairs:  -Sub "K1=V1" -Sub "K2=V2"

.EXAMPLE
    .\run_preview.ps1 `
        -Template "$env:USERPROFILE\.agents\skills\citycraft\assets\style-preview-template.html" `
        -Output   .\style-preview.html `
        -Port     17433 `
        -Timeout  300 `
        -Sub "PRODUCT_NAME=My Product" `
        -Sub "PRODUCT_HEADLINE=Build faster" `
        -Sub "RECEIVER_PORT=17433"
#>
param(
    [Parameter(Mandatory)][string]   $Template,
    [Parameter(Mandatory)][string]   $Output,
    [int]      $Port    = 17432,
    [string]   $Result  = (Join-Path $env:TEMP "citycraft_result.json"),
    [int]      $Timeout = 300,
    [string[]] $Sub     = @()
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# ── 1. Template substitution ──────────────────────────────────────────────────
$templateFull = (Resolve-Path $Template).Path
$content = [System.IO.File]::ReadAllText($templateFull, [System.Text.Encoding]::UTF8)

foreach ($pair in $Sub) {
    $idx = $pair.IndexOf("=")
    if ($idx -lt 1) { continue }
    $key   = "__$($pair.Substring(0, $idx).Trim())__"
    $value = $pair.Substring($idx + 1)
    $content = $content.Replace($key, $value)
}

$outputFull = Join-Path (Get-Location) $Output
[System.IO.File]::WriteAllText($outputFull, $content, [System.Text.Encoding]::UTF8)

# ── 2. Start HTTP listener ────────────────────────────────────────────────────
$listener = [System.Net.HttpListener]::new()
$listener.Prefixes.Add("http://localhost:$Port/")
$listener.Start()

# ── 3. Open browser ───────────────────────────────────────────────────────────
Start-Process "http://localhost:$Port"

# ── 4. Request loop ───────────────────────────────────────────────────────────
$startTime  = [DateTime]::UtcNow
$submitted  = $false
$htmlBytes  = $null   # lazy-load on first GET

try {
    while ($listener.IsListening) {
        $elapsed = ([DateTime]::UtcNow - $startTime).TotalSeconds
        if ($elapsed -ge $Timeout) { break }

        # Non-blocking wait: up to 1 s per iteration
        $async = $listener.BeginGetContext($null, $null)
        if (-not $async.AsyncWaitHandle.WaitOne(1000)) { continue }

        $ctx  = $listener.EndGetContext($async)
        $req  = $ctx.Request
        $resp = $ctx.Response

        $resp.Headers.Add("Access-Control-Allow-Origin",  "*")
        $resp.Headers.Add("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        $resp.Headers.Add("Access-Control-Allow-Headers", "Content-Type")

        $route = "$($req.HttpMethod) $($req.Url.LocalPath)"

        switch ($route) {
            "OPTIONS /" {
                $resp.StatusCode = 204
            }
            "GET /" {
                if ($null -eq $htmlBytes) {
                    $htmlBytes = [System.IO.File]::ReadAllBytes($outputFull)
                }
                $resp.ContentType     = "text/html; charset=utf-8"
                $resp.ContentLength64 = $htmlBytes.Length
                $resp.OutputStream.Write($htmlBytes, 0, $htmlBytes.Length)
            }
            "POST /submit" {
                $reader = [System.IO.StreamReader]::new(
                    $req.InputStream, [System.Text.Encoding]::UTF8)
                $body = $reader.ReadToEnd()
                [System.IO.File]::WriteAllText(
                    $Result, $body, [System.Text.Encoding]::UTF8)
                $ok = [System.Text.Encoding]::UTF8.GetBytes('{"ok":true}')
                $resp.ContentType     = "application/json; charset=utf-8"
                $resp.ContentLength64 = $ok.Length
                $resp.OutputStream.Write($ok, 0, $ok.Length)
                $submitted = $true
            }
            default {
                $resp.StatusCode = 404
            }
        }

        $resp.Close()
        if ($submitted) { break }
    }
} finally {
    $listener.Stop()
}

# ── 5. Output ─────────────────────────────────────────────────────────────────
if ($submitted) {
    $data = [System.IO.File]::ReadAllText($Result, [System.Text.Encoding]::UTF8)
    Remove-Item $Result -ErrorAction SilentlyContinue
    Write-Output $data
} else {
    Write-Error "No submission in ${Timeout}s. Ask the user to type their choice manually."
    exit 1
}
