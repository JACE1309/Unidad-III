'''
Jahir Artemio Casas Espínola
Scrip del Laboratorio 2.8 Parte 1
'''

import ncclient
from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="10.10.20.48",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
)

netconf_reply = m.get_config(source="running")
print(netconf_reply)

