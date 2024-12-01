function Get-Priority($letter) {
    $score = [byte][char]$letter
    if ($score -ge 97 -and $score -le 122) {$score -= 96} # Lowercase
    elseif ($score -ge 65 -and $score -le 90) {$score -= 38} # Uppercase
    return $score
}

$total = 0
$lines = Get-Content "input.txt"
for($i=0; $i -lt $lines.Length; $i+=3){
    foreach ($c in [char[]]$lines[$i]) {
        if($lines[$i+1].Contains($c) -and $lines[$i+2].Contains($c)) {
            $total += Get-Priority $c
            break
        }
    }
}
$total