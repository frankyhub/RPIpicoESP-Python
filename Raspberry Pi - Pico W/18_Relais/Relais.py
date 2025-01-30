'''
Relais.py

'''

from machine import Pin
from time import sleep

relay = Pin(0, Pin.OUT)

while True:
    # RELAY aus
    relay.value(0)
    sleep(10)
    
    # RELAY an
    relay.value(1)
    sleep(10)