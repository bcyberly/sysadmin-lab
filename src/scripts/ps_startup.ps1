param([string]$Path = "startup_programs.csv")

$hklm = Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
$hkcu = Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

$startup = @()
$hklm.PSObject.Properties | Where-Object {$_.MemberType -eq 'NoteProperty'} | ForEach-Object{
    $startup += [PSCustomObject]@{
        Key = "HKLM:Run"
        Name = $_.Name
        Value = $_.Value
    }
}

$hkcu.PSObject.Properties | Where-Object {$_.MemberType -eq 'NoteProperty'} | ForEach-Object{
    $startup += [PSCustomObject]@{
        Key = "HKCU:Run"
        Name = $_.Name
        Value = $_.Value
    }
}

$startup | Export-Csv -Path $Path -NoTypeInformation
$startup | Format-Table -AutoSize