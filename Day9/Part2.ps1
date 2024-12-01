param([string]$prompt)

$path = @{}
$x = @(0,0,0,0,0,0,0,0,0,0)
$y = @(0,0,0,0,0,0,0,0,0,0)
# the H is 0

foreach ($line in $(Get-Content $prompt)) {
    
    $i = [int]$line.Split(" ")[1]
    for (; $i -gt 0; $i--) {
        # Handle the had as is
        switch ($line[0]) {
            "R" { $x[0]++ }
            "L" { $x[0]-- }
            "U" { $y[0]++ }
            "D" { $y[0]-- }
        }
        
        # Handle each of the knots
        for ($j = 1; $j -le 9; $j++) {

            # find if close enough
            if ([Math]::Abs($($x[$j-1] - $x[$j])) -gt 1 -or [Math]::Abs($($y[$j-1] - $y[$j])) -gt 1) {
                if ($x[$j-1] -gt $x[$j]) { $x[$j]++ }
                if ($x[$j-1] -lt $x[$j]) { $x[$j]-- }
                if ($y[$j-1] -gt $y[$j]) { $y[$j]++ }
                if ($y[$j-1] -lt $y[$j]) { $y[$j]-- }
            }
        }
        $path["($($x[9]),$($y[9]))"] = $true
    }
}
Write-Host $path.Keys.Count
