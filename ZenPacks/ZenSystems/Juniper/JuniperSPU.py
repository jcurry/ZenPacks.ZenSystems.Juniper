##########################################################################
# Author:               Jane Curry,  jane.curry@skills-1st.co.uk
# Date:                 September 23rd, 2012
# Revised:
#
# JuniperSPU object class
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""JuniperSPU

JuniperSPU is a component of a JuniperDevice Device

$Id: $"""

__version__ = "$Revision: $"[11:-2]

from Globals import DTMLFile
from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity


import logging
log = logging.getLogger('JuniperSPU')

class JuniperSPU(DeviceComponent, ManagedEntity):
    """Juniper SPU object"""

    portal_type = meta_type = 'JuniperSPU'
    
    #**************Custom data Variables here from modeling************************
    
    containerIndex = 1
    containerDescr = ''
    containerParentIndex = 1
    containerParentDescr = ''
    SPUDescr = ''
    SPUCPU = 0
    SPUMemory = 0
    
    #**************END CUSTOM VARIABLES *****************************
    
    
    #*************  Those should match this list below *******************
    _properties = (
        {'id':'containerIndex', 'type':'int', 'mode':''},
        {'id':'containerDescr', 'type':'string', 'mode':''},
        {'id':'containerParentIndex', 'type':'int', 'mode':''},
        {'id':'containerParentDescr', 'type':'string', 'mode':''},
        {'id':'SPUDescr', 'type':'string', 'mode':''},
        {'id':'SPUCPU', 'type':'int', 'mode':''},
        {'id':'SPUMemory', 'type':'int', 'mode':''},
        )
    #****************
    
    _relations = (
        ("JuniperDevSP", ToOne(ToManyCont,
            "ZenPacks.ZenSystems.Juniper.JuniperDevice", "JuniperSP")),
        )

    factory_type_information = ( 
        { 
            'id'             : 'JuniperSPU',
            'meta_type'      : 'JuniperSPU',
            'description'    : """Juniper SPU info""",
            'product'        : 'Juniper',
            'immediate_view' : 'viewJuniperSPU',
            'actions'        :
            ( 
                { 'id'            : 'status'
                , 'name'          : 'Juniper SPU Graphs'
                , 'action'        : 'viewJuniperSPU'
                , 'permissions'   : (ZEN_VIEW, )
                },
                { 'id'            : 'perfConf'
                , 'name'          : 'Juniper SPU Template'
                , 'action'        : 'objTemplates'
                , 'permissions'   : (ZEN_CHANGE_SETTINGS, )
                },                
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW, )
                },
            )
          },
        ) 


    def viewName(self):
        """Pretty version human readable version of this object"""
        return self.id


    # use viewName as titleOrId because that method is used to display a human
    # readable version of the object in the breadcrumbs
    titleOrId = name = viewName


    def device(self):
        return self.JuniperDevSP()
    
InitializeClass(JuniperSPU)
