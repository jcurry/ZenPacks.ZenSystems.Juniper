#!/bin/bash
#####################################################################
# Author:		Jane Curry
# Date			March 4th, 2011
# Updated:		Sept 4th, 2012
#                       Cater for SNMP V3 or v1/v2c
# Shellscript to count number of entries in IpSec VPN Phase 1 table
#
# Expects 	$1 = manageIp
#		$2 = zSnmpVer
#		$3 = zSnmpCommunity
#		$4 = zSnmpAuthType
#		$5 = zSnmpPrivType
#		$6 = zSnmpAuthPassword
#		$7 = zSnmpPrivPassword
#		$8 = zSnmpSecurityName
# Output is in "Nagios plugin" format - string | var=value
#
#####################################################################
#set -x
count=0
if [ $2 == "v3" ] 
then
  for i in `/usr/bin/snmpwalk -$2 -l authPriv -a $4 -x $5 -A $6 -X $7 -u $8 $1 .1.3.6.1.4.1.2636.3.52.1.1.2.1.6 | cut -f1 -d ' '`
  do
    count=$(($count+1))
  done
else
  for i in `/usr/bin/snmpwalk -$2 -c $3 $1 .1.3.6.1.4.1.2636.3.52.1.1.2.1.6 | cut -f1 -d ' '`
  do
    count=$(($count+1))
  done
fi

if [ $count -eq 0 ]
then
  echo "IPSec VPN Phase 1 table count failed - status WARNING "
  exitStatus=1
else
  echo "IPSec VPN Phase 1 table count - status OK | ipSecVPNP1Count=$count"
  exitStatus=0
fi
exit $exitStatus
 
