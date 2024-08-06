#
# This script emulates a simple network beacon
#

function Start-BasicBeacon {
    param (
        [string]$Destination = "google.com",
        [int]$Port = 80,
        [int]$Interval = 30
    )

    $count = 1

    Do {
        if(Test-Connection -TargetName $Destination -TcpPort $Port) {
            $time = Get-Date -Format T
            Write-Host "Connection to $Destination Successful at $time - Count of $count"
        } else {
            $time = Get-Date -Format T
            Write-Host "Connection to $Destination Failed at $time - Count of $count"
        }
        $count++
        Start-Sleep -Seconds $Interval
    } While (1 -eq 1)

}

