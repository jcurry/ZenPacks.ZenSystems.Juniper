##########################################################################
# Author:               Jane Curry,  jane.curry@skills-1st.co.uk
# Date:                 March 1st, 2011
# Revised:		
#
# JuniperRoutingEngine modeler plugin
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """JuniperSPUMap

Gather table information from Juniper Contents tables
"""

import re
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class JuniperSPUMap(SnmpPlugin):
    """Map Juniper SPU table to model."""
    maptype = "JuniperSPUMap"
    modname = "ZenPacks.ZenSystems.Juniper.JuniperSPU"
    relname = "JuniperSP"
    compname = ""

    snmpGetTableMaps = (
        GetTableMap('jnxContentsTable',
                    '.1.3.6.1.4.1.2636.3.1.8.1',
                    {
                        '.1': 'containerIndex',
                    }
        ),
        GetTableMap('jnxJsSPUMonitoringMib',
                    '.1.3.6.1.4.1.2636.3.39.1.12.1.1.1',
                    {
                        '.4': 'SPUCPU',
                        '.5': 'SPUMemory',
                        '.11': 'SPUDescr',
                    }
        ),
        GetTableMap('jnxContainersTable',
                    '.1.3.6.1.4.1.2636.3.1.6.1',
                    {
                        '.1': 'containerIndex',
                        '.3': 'containerLevel',
                        '.4': 'containerNextLevel',
                        '.5': 'containerType',
                        '.6': 'containerDescr',
                    }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        rm = self.relMap()
        contentsTable = tabledata.get('jnxContentsTable')
        SPUMonitoringTable = tabledata.get('jnxJsSPUMonitoringMib')
        containersTable = tabledata.get('jnxContainersTable')

# If no data supplied then simply return
        if not contentsTable:
            log.warn( 'No SNMP response from %s for the %s plugin for contents', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return
        if not SPUMonitoringTable:
            log.warn( 'No SNMP response from %s for the %s plugin for operating system', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return
        if not containersTable:
            log.warn( 'No SNMP response from %s for the %s plugin for containers', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return
 
        for oid, data in SPUMonitoringTable.items():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.split('.')[-1]
                log.info(' SPUDescr is %s  SPU CPU is %s SPU memory is %s SPU Monitoring index is %s' % (om.SPUDescr, om.SPUCPU, om.SPUMemory, om.snmpindex))
                om.id = self.prepId( om.SPUDescr.replace(' ','_') + '_' + str( om.snmpindex ) )

            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in %s modeler plugin %s' % ( self.name(), errorInfo))
                continue
            rm.append(om)
#            log.info('rm %s' % (rm) )

        return rm

