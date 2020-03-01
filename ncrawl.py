import pyasn1

try:
    from config import *
except:
    print("Import error: config.py. Make sure to view README")
    exit(2)

try:
    import ipaddress
except:
    print("Import error: ipaddress. Make sure to run pip3 install -r requirements.txt")
    exit(2)

try:
    from pysnmp.hlapi import *
except:
    print("Import error: pysnmp. Make sure to run pip3 install -r requirements.txt")
    exit(2)

def det_scan_targets(ip_range):
    targets = []
    scan_target_net = ipaddress.ip_network(ip_range)
    for scan_target_ip in scan_target_net.hosts():
        targets.append(str(scan_target_ip))
    return targets

def det_snmp_up(ip_range, community):
    for target in det_scan_targets(ip_range):

        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                CommunityData(community),
                UdpTransportTarget((target, 161)),
                ContextData(),ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
        )
        
        if errorIndication:
            print("No response from: {}".format(str(target)))
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))