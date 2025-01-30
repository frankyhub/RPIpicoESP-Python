'''
ESP32_deep_sleep.py

ESP32 

'''

import machine
from machine import Pin
from time import sleep

led = Pin (2, Pin.OUT)

#blink LED
led.value(1)
sleep(1)
led.value(0)
sleep(1)

# Warte 5 Sekunden, damit Sie den ESP wach bleibt, um später eine serielle Kommunikation herzustellen
# Diese Sleep-Zeile im endgültigen Skript entfernen
sleep(5)

print('Im awake, but Im going to sleep')

#sleep für 10 seconds (10000 milliseconds)
machine.deepsleep(10000)
