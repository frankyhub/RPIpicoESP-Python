'''
WLAN_list.py

Listet verfügbare SSIDs

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
Verfügbare WLAN-Netzwerke:
(b'Vodafone Homespot', b'B+P\xea\xa3<', 1, -83, 0, 1)
(b'Vodafone-E9FF', b'@+P\xea\xa3<', 1, -86, 5, 2)
(b'FRITZ!Box 7490', b'\xf0\xb0\x14\xdc\x1d\x82', 6, -92, 5, 2)


'''



import network
# Init Wi-Fi-Schnittstelle
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# Nach verfügbaren WLAN-Netzwerken suchen
networks = wlan.scan()
# Drucken von Wi-Fi-Netzwerken
print("Verfügbare WLAN-Netzwerke:")
for network_info in networks:
    print(network_info)
