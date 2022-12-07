'''
Jahir Artemio Casas Espínola
Scrip del Laboratorio 2.8 Parte 4
'''

import ncclient
from ncclient import manager
import xml.dom.minidom
import ncclient


m = manager.connect(
    host="10.10.20.48",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
)

netconf_data = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>NEWHOSTNAME</hostname>
  </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
