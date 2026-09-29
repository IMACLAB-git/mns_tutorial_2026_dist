# workspace를 시연 시작 상태(papers\seed_papers.csv 하나)로 되돌린다.
$ws = Join-Path $PSScriptRoot 'workspace'
$seed = Join-Path $ws 'papers\seed_papers.csv'
if (-not (Test-Path $seed)) { Write-Error "seed_papers.csv가 없습니다: $seed"; exit 1 }

Get-ChildItem -LiteralPath $ws -Force | Where-Object { $_.Name -ne 'papers' } |
    Remove-Item -Recurse -Force -Confirm:$false
Get-ChildItem -LiteralPath (Join-Path $ws 'papers') -Force | Where-Object { $_.Name -ne 'seed_papers.csv' } |
    Remove-Item -Recurse -Force -Confirm:$false

Get-ChildItem -LiteralPath $ws -Recurse -Force | Select-Object -ExpandProperty FullName
