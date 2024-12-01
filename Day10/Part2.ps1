param($prompt) 

$row, $rows = "", @()
$tick, $X = 1, 1

foreach ($op in $(Get-Content $prompt).Split()){
    if ($row.Length -eq 40) {
        $rows = $rows + $row
        $row = ""
    }

    if ([math]::Abs($($row.Length - $X)) -le 1) { $row += "#" }
    else { $row += "." }

    # Oof, it's important the addition happens at the end
    if ($op -ne "noop" -and $op -ne "addx") {
        #Write-Host $tick $op
        $X += [int]$op
    }
    $tick++    
}
$rows = $rows + $row

foreach ($r in $rows) {
    Write-Host $r
}