param([string]$prompt)
#$outcome = @{"AX" = 4;}


$global:working = @()
$tree = @{"/" = 0}

function Get-Path {
    $path = "/"
    $path += $($working -join "/")
    return $path
}

function Move-Path ($target) {
    Switch ($target) {
        "/" { 
            $global:working = @()
         }
        ".." {
            if ($working.Length -eq 1) {
                $global:working = @()
            } else {
                $global:working = $working[0..$($working.Length - 2)]
            }
        }
        Default {
            $global:working += $target
        }
    }

    # Ensure directory is initialized
    if ($null -eq $tree[$working]){
        $tree[$(Get-Path)] = 0
    }
}

function Use-File ($size) {
    $tree["/"] += [int]$size
    $path = ""
    for ($i = 0; $i -lt $working.Length; $i++){
        $path += "/"
        $path += $working[$i]
        $tree[$path] += [int]$size
    }
}

foreach($line in Get-Content $prompt){
    $parts = $line.Split()

    # Move about
    if ($parts[0] -eq "$" -and $parts[1] -eq "cd") {
        Move-Path $parts[2]

    # Listing a directory
    } elseif ($parts[0] -eq "$" -and $parts[1] -eq "ls") {
        # you don't really need anything in ls for part 1
        # Anticipating something will happen for part 2 though

    # Reading a directory
    } else {
        # Using a global path as key, you don't actually need to keep track of child folders
        if ($parts[0] -ne "dir") { 
            Use-File $parts[0]
         } 
    }
}


Write-Host $tree

$sum = 0
$tree.Keys | ForEach-Object {
    if ($tree[$_][0] -le 100000) { 
        Write-Host $_ "--" $tree[$_]
        $sum += $tree[$_][0]
     }
}
Write-Host $sum
