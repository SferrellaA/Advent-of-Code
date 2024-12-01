function Get-Priority($letter) {
    $score = [byte][char]$letter
    if ($score -ge 97 -and $score -le 122) {$score -= 96} # Lowercase
    elseif ($score -ge 65 -and $score -le 90) {$score -= 38} # Uppercase
    return $score
}

$total = 0
Get-Content "input.txt" | ForEach-Object { # Why is ForEach like this? SOOOOO weird
    $C1 = $_[0..$($_.Length / 2 - 1)]
    $C2 = $_[$($_.Length / 2)..$_.Length]
    $already = $false # I do not like this workaround
    $C1 | ForEach-Object {
        if ($already) {return}
        if($C2 -ccontains $_) {
            $already = $true
            $total += $(Get-Priority $_)
        }
    }
}
Write-Host $total