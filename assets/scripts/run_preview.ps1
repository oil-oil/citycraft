# Windows 包装入口；与 macOS/Linux 共用 Python 实现。
param(
    [Parameter(Mandatory)][string] $Template,
    [Parameter(Mandatory)][string] $Output,
    [int] $Port = 17432,
    [string] $Result = "",
    [int] $Timeout = 300,
    [string[]] $Sub = @()
)
$ErrorActionPreference = "Stop"
$invokeArgs = @((Join-Path $PSScriptRoot "run_preview.py"), "--template", $Template, "--output", $Output, "--port", "$Port", "--timeout", "$Timeout")
if ($Result) { $invokeArgs += @("--result", $Result) }
$invokeArgs += $Sub
if (Get-Command py -ErrorAction SilentlyContinue) { & py -3 @invokeArgs }
elseif (Get-Command python3 -ErrorAction SilentlyContinue) { & python3 @invokeArgs }
else { throw "请先安装 Python 3；也可直接在对话中提供风格选择。" }
exit $LASTEXITCODE
