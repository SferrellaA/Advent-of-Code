[System.Collections.ArrayList]$towers = @()

function Print-Towers {
    #Read-Host
    # Find max length
    $height = 0

    for($i=0; $i -lt $towers.Count; $i++){
        if ($towers[$i].Length -gt $height) {
            $height = $towers[$i].Length
        }
    }
    for($h=$height-1; $h -ge 0; $h--){
        $display = ""
        for($t=1; $t -lt $towers.Count; $t++){
            if ($towers[$t].Length -gt $h) {
                $display += "[" + $towers[$t][$h] + "]"
            } else {
                $display += "   "
            }
        }
        Write-Host $display
    }

    # Finish off nicely
    # This can be so much cleaner but I just want to finish this fast
    $secondlast
    $final = ""
    for($i=1; $i -lt $towers.Count; $i++){
        $final += "---"
        $secondlast += " " + $i + " "
    }

    Write-Host $secondlast
    Write-Host $final
}

function Setup-Crates([System.Int32]$t, [char[]]$boxes){
    if ($t -ge $towers.Count) {
        for ($x=$t; $x -gt $towers.Count; $x--){
            $towers.Add([char[]]@())
        }
        $towers.Add([char[]]$boxes)
    } else {
        $towers[$t] = $boxes + $towers[$t]
    }
}

function Move-Crates([int]$count, [int]$start, [int]$end){
    $set = @()
    while($count -gt 0){
        $set = @($towers[$start][-1]) + $set
        if ($towers[$start].Length -eq 1) {
            $towers[$start] = @()
        } else{
            $towers[$start] = $towers[$start][0..$($towers[$start].Length-2)]
        }
        $count--
    }
    #Read-Host $set
    $towers[$end] = $towers[$end] + $set
}

foreach($line in Get-Content "input.txt") {
    if ($line.Contains([char]'[')) {
        $copy = $line
        $t = 1
        while($copy.Length -gt 1) {
            $cl = $copy.Length 
            $spot = $copy[1]
            $copy = $copy[4..$cl]
            Setup-Crates -t $t -boxes @($spot)
            $t++
        }
    } 

    if ($line.Length -eq 0){
        for ($t=1; $t -le $towers.Count; $t++) {
            for ($i=0; $i -lt $towers[$t].Length; $i++) {
                if ([byte]$towers[$t][$i] -eq 32) {
                    $towers[$t] = $towers[$t][0..$($i-1)]
                    break
                }
            }
        }
    }

    if ($line.contains("move")) {
        Print-Towers
        $count,$start,$end = $line.Split(' ')[1, 3, 5]
        Move-Crates $count $start $end
    }
}

Print-Towers
$answer = ""
foreach($tower in $towers){
    $answer += $tower[-1]
}
Write-Host $answer