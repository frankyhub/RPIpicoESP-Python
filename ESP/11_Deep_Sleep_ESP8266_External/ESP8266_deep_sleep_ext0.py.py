'''
ESP8266_deep_sleep_ext0.py

ESP8266

'''
import machine
from machine import Pin
from time import sleep

led = Pin (2, Pin.OUT)
  
#blink LED
led.value(0)
sleep(1)
led.value(1)
sleep(1)

# Warte  5 Sekunden, damit der ESP wach bleibt, um später eine serielle Kommunikation herzustellen
# Diese Sleep-Zeile im endgültigen Skript entfernen
sleep(5)
print("Ich bin wach, aber ich gehe schlafen')
sleep(1)

#Schlafen auf unbestimmte Zeit
machine.deepsleep()