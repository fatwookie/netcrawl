#!/usr/bin/env python3
#

"""
This script contacts a network device via SNMP and tries to download
the contents of the MAC address table. This should normally be available
at the OID 1.3.6.1.2.1.17.4.3.1 from the BRIDGE-MIB, using object
dot1dTpFdbEntry.

See also: http://www.cisco.com/en/US/tech/tk648/tk362/technologies_tech_note09186a0080094a9b.shtml


SNMP MIB-2 SYSTEM 

system  => 1.3.6.1.2.1.1
ifDescr => 1.3.6.1.2.1.2.2.1.2
ifName  => 1.3.6.1.2.1.31.1.1.1.1
dot1dTpFdbEntry => 1.3.6.1.2.1.17.4.3.1


g = getCmd(SnmpEngine(),CommunityData('public'),UdpTransportTarget(('demo.snmplabs.com', 161)),ContextData(),ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
g = getCmd(SnmpEngine(),CommunityData('public'),UdpTransportTarget(('demo.snmplabs.com', 161)),ContextData(),ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
"""

import argparse
import re

from ncrawl import *

oid = "1.3.6.1.2.1.17.4.3.1"

def main():
    parser = argparse.ArgumentParser(description='Scan the switch TCAM')  
    parser.add_argument('ip_range', help='IP range to scan')
    args = parser.parse_args()
    det_snmp_up(args.ip_range, community)

if __name__ == "__main__":
    main()

exit
