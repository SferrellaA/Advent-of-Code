param([string]$prompt)
#$outcome = @{"AX" = 4;}


$global = @()
$working = "/"
$tree = @{}

foreach($line in Get-Content $prompt){
    $parts = $line.Split()
    if ($parts[0] -eq "$" -and $parts[1] -eq "cd") {
        $working = $parts[2]
        #Write-Host $parts
        if ($working -eq "..") {
            $global = $global[0..$($global.Length - 2)]
            #Write-Host $global
            continue
        } else {
            #Write-Host $global
            $global = $global + $working
        }

        # if you are in a directory, make sure it's initialized
        if ($null -eq $tree[$working]){
            $tree[$working] = @(0)
        }
    } elseif ($parts[0] -eq "$" -and $parts[1] -eq "ls") {
        # you don't really need anything in ls for part 1
        # Anticipating something will happen for part 2 though

    } else {
        if ($parts[0] -eq "dir") {
            $tree[$working] = $tree[$working] + $parts[1]
        } else {
            $tree[$working][0] += [int]$parts[0]

            # also add it to each step up too
            if ($global.Length -gt 1) {
            for($i = $global.Length - 2; $i -ge 0; $i--){
                $tree[$global[$i]][0] += [int]$parts[0]
            }}
        }
    }
}

$sum = 0
$tree.Keys | ForEach-Object {
    if ($tree[$_][0] -le 100000) { 
        Write-Host $_ "--" $tree[$_]
        $sum += $tree[$_][0]
     }
}

Write-Host $sum
