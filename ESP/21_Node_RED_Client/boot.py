'''
boot.py
Node red

ESP32 

'''

import time
import onewire
import ds18x20
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'Deine_SSID'
password = 'Dein_PASSWORT'
mqtt_server = 'Deine_MQTT_BROKER_IP'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'output'
topic_pub = b'temp'

last_sensor_reading = 0
readings_interval = 5

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Verbindung erfolgreich')
print(station.ifconfig())

ds_pin = machine.Pin(14)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

led = machine.Pin(2, machine.Pin.OUT, value=0)
