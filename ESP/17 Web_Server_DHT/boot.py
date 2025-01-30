'''
boot.py

ESP32 

'''

try:
  import usocket as socket
except:
  import socket

import network
from machine import Pin
import dht

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Deine_SSID'
password = 'Dein_PASSWORD'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Verbindung erfolgreich')
print(station.ifconfig())

'sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(14))
