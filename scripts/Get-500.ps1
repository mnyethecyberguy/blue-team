#
# This script finds the built-in Administrator account in AD
#

function Get-500 {

    Get-ADUser -Identity “$(((Get-ADDomain).domainsid).ToString())-500”
}

Get-500