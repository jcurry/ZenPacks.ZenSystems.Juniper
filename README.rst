==========================
ZenPacks.ZenSystems.Juniper
==========================


Description
===========

Provides support for various Juniper devices (firewalls, routers and switches).  Many components are modeled and 
displayed and performance graphs are available for devices and components.

This ZenPack is Zenoss 3 compliant.

Components
==========

The ZenPack has the following new Device Classes of object class JuniperDevice

    * /Devices/Network/Router/Juniper
    * /Devices/Network/Router/Firewall/Juniper
    * /Devices/Network/Switch/Juniper

     
A large number of components are defined as object classes and modeled. Not all components are relevant to all 
devices (this is controlled by the modeler plugins selected):
        * JuniperComponents and JuniperBaseComp which have container relationship information
        * JuniperContents  which has details for:
            * Parent container, description, serial number, chassis information, CPU, memory, up time 
        * JuniperFan
        * JuniperPowerSupply
        * JuniperFPC (Flexible PIC Concentrator)  which has details for:
            * Parent container, description, serial number, chassis information, CPU, memory, up time 
        * JuniperSPU (Service Processing Unit)  which has details for:
            * Parent container, description, serial number, chassis information, CPU, memory, up time 
        * JuniperPIC (Physical Interface Card) and JuniperMIC (Modular Interface Card) which have details for:
            * Parent container, description, serial number, chassis information, CPU, memory, up time
            * The relationship between FPC and their contained MICs and PICs can be seen 
        * JuniperRoutingEngine
        * JuniperVlan  which has details for:
            * VLAN name, type, tag, port group and interface information
        * JuniperBGP  which has details for:
            * BGP local address, remote address, remote ASN and BGP state information
        * JuniperIpSecVPN and JuniperIpSecPolicy  which have details for:
            * VPN phase 1 and phase 2 IDs, gateways and state

     
Note that not all components or details of components are displayed. Check Juniper.js in the resources 
subdirectory for elements that are commented out:

     
A large number of modeler plugins populate the fields of the devices and their components. These correspond 
directly with the different components detailed above
     
    * Device template JuniperMemoryUsedPercent provides device-level performance information
    * Device templates ipSecPolicyCount, ipSecVPNPhase1Count and ipSecVPNPhase1Count are available to provide performance information  relating to VPNs
    * Device template ipSecNATCount provides device-level performance information on NAT translation tables
    * There are component templates providing performance information for each of the components listed above.
    * A separate Juniper Information menu delivers tabular and graphical  information for the overall device


Requirements & Dependencies
===========================

    * Zenoss Versions Supported: 3.x and 4.x
    * External Dependencies: The relevant Juniper MIBs need to be available on target devices
    * ZenPack Dependencies:
    * Installation Notes: zenhub and zopectl restart after installing this ZenPack.
    * Configuration: 

Download
========
Download the appropriate package for your Zenoss version from the list
below.

* Zenoss 3.0+ `Latest Package for Python 2.6`_
* Zenoss 4.0+ `Older Package for Python 2.7`_
* Zenoss 4.2+ `Latest Package for Python 2.7`_

Installation
============
Normal Installation (packaged egg)
----------------------------------
Copy the downloaded .egg to your Zenoss server and run the following commands as the zenoss
user::

   zenpack --install <package.egg>
   zenhub restart
   zopectl restart

Developer Installation (link mode)
----------------------------------
If you wish to further develop and possibly contribute back to this 
ZenPack you should clone the git repository, then install the ZenPack in
developer mode::

   zenpack --link --install <package>
   zenhub restart
   zopectl restart

Configuration
=============

This ZenPack was tested with Zenoss 3.1 against:

    * MX80, MX240 Juniper routers
    * SRX100, SRX210 Juniper firewalls
    * EX220, EX4200 Juniper switches

Change History
==============
* 1.0
   * Initial Release
* 1.1
   * Some updates for extra debug
* 1.2
   * Transferred to new github methods
* 2.0
   * Tested for Zenoss Core 4.2
   * Scripts for command templates in lib directory support SNMP v3
* 2.2
   * Added support for Service Processing Unit (SPU) components
   * Moved shellscripts for ipSec templates from lib to libexec to preserve permission bits

Screenshots
===========
|JuniperInfo_firewall|
|Juniper_router_bgp|
|Juniper_router_fpc|
|Juniper_switch_vlan|


.. External References Below. Nothing Below This Line Should Be Rendered

.. _Latest Package for Python 2.6: https://github.com/downloads/jcurry/ZenPacks.ZenSystems.Juniper/ZenPacks.ZenSystems.Juniper-1.2-py2.6.egg

.. _Older Package for Python 2.7: https://github.com/downloads/jcurry/ZenPacks.ZenSystems.Juniper/ZenPacks.ZenSystems.Juniper-2.0-py2.7.egg
.. _Latest Package for Python 2.7: https://github.com/jcurry/ZenPacks.ZenSystems.Juniper/blob/4.2/dist/ZenPacks.ZenSystems.Juniper-2.2-py2.7.egg


.. |JuniperInfo_firewall| image:: http://github.com/jcurry/ZenPacks.ZenSystems.Juniper/raw/master/screenshots/JuniperInfo_firewall.jpg
.. |Juniper_router_bgp| image:: http://github.com/jcurry/ZenPacks.ZenSystems.Juniper/raw/master/screenshots/Juniper_router_bgp.jpg
.. |Juniper_router_fpc| image:: http://github.com/jcurry/ZenPacks.ZenSystems.Juniper/raw/master/screenshots/Juniper_router_fpc.jpg
.. |Juniper_switch_vlan| image:: http://github.com/jcurry/ZenPacks.ZenSystems.Juniper/raw/master/screenshots/Juniper_switch_vlan.jpg

                                                                        

