param([string]$prompt)

$script_location = (Get-Location).Path

Remove-Item ./opt -Recurse
New-Item -Path ./opt -ItemType directory

foreach($line in Get-Content $prompt){
    $parts = $line.Split()
    if ($parts[0] -eq "$"){
        switch ($parts[1]){
            "cd" {
                switch ($parts[2]){
                    "/" {
                        cd $script_location/opt
                    }
                    ".." {
                        cd ..
                    }
                    Default {
                        cd $parts[2]
                    }
                }
            }
            "ls" {}
        }
    } else {
        switch ($parts[0]){
            "dir" {
                mkdir $parts[1]
            }
            Default {
                echo $parts[0] > $parts[1]
            }
        }
    }
}


