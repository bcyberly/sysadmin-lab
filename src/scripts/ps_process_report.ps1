param(
    [string]$Path = "process_report.csv"
)

$processes = Get-Process | Select-Object Name, Id, CPU, WorkingSet, StartTime
$processes | Export-Csv -Path $Path -NoTypeInformation

Write-Host "Total processes: $($processes.Count)"
Write-Host "Top 5 by CPU:"
$processes | Sort-Object Cpu -Descending | Select-Object -First 5 | Format-Table Name, CPU
Write-Host "Top 5 by memory (WorkingSet):"
$processes | Sort-Object WorkingSet -Descending | Select-Object -First 5 | Format-Table Name, WorkingSet