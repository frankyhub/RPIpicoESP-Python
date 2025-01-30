'''
boot.py

ESP32 / ESP8266

'''
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Deine_SSID'
password = 'Dein_PASSWORT'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Verbindung erfolgreich')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
