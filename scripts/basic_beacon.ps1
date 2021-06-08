#
# This script emulates a simple network beacon
#

$beacon_destination = "google.com"
$beacon_port = 80
$beacon_interval = 30

$count = 1

Do {
    if(Test-NetConnection -ComputerName $beacon_destination -Port $beacon_port) {
        $time = Get-Date -Format T
        Write-Host "Connection Successful at $time - Count of $count"
    } else {
        $time = Get-Date -Format T
        Write-Host "Connection Failed at $time - Count of $count"
    }
    $count++
    Start-Sleep -Seconds $beacon_interval
} While (1 -eq 1)