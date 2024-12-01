param([string]$prompt)

$path = @{}
$hx,$hy,$tx,$ty=0,0,0,0

foreach ($line in $(Get-Content $prompt)) {
    #$i = $([int]$line[2] - 48) 
    # nope, there's two digit moves in the input

    $i = [int]$line.Split(" ")[1]
    for (; $i -gt 0; $i--) {
        switch ($line[0]) {
            "R" { $hx++ }
            "L" { $hx-- }
            "U" { $hy++ }
            "D" { $hy-- }
        }
        
        # find if close enough
        if ([Math]::Abs($($hx - $tx)) -gt 1 -or [Math]::Abs($($hy - $ty)) -gt 1) {
            if ($hx -gt $tx) { $tx++ }
            if ($hx -lt $tx) { $tx-- }
            if ($hy -gt $ty) { $ty++ }
            if ($hy -lt $ty) { $ty-- }
        }
        #Write-Host "($hx,$hy) -- ($tx,$ty)"
        $path["($tx,$ty)"] = $true
    }
}
Write-Host $path.Keys.Count
#3151 is too low