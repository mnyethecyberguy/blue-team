#
# This script finds the built-in Administrator account in AD
#

Get-ADUser -Identity “$(((Get-ADDomain).domainsid).ToString())-500”