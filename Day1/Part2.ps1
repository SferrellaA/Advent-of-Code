$calories = @()
$x = 0
Get-Content "input.txt" | ForEach-Object {
    if ($_ -eq "") {
        $calories += $x
        $x=0
    } else {
        $x += $_
    }
}
$calories += $x #If the last line isn't blank
$topthree =0
$($calories | Sort-Object)[-3..-1] | ForEach-Object {
    $topthree += $_
}
Write-Host $topthree