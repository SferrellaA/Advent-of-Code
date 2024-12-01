param($prompt) 

$tick, $X = 1, 1
$checkpoints = @(20, 60, 100, 140, 180, 220)
$signal = 0
foreach ($op in $(Get-Content $prompt).Split()){
    #if ($tick -gt 180) {
    if ($tick -in $checkpoints) {
        #Write-Host "$tick $X $($tick * $X)"
        $signal += $($tick * $X)
    }
    
    # Oof, it's important the addition happens at the end
    if ($op -ne "noop" -and $op -ne "addx") {
        #Write-Host $tick $op
        $X += [int]$op
    }

    # This is just setup for the next step
    $tick++
    
    # To save a bit of time
    if ($tick -gt $checkpoints[-1]) {
        break
    }
}
Write-Host $signal