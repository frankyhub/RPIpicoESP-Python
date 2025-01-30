'''
ESP8266_deep_sleep.py

ESP8266

'''

import machine
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

def deep_sleep(msecs):
  # RTC konfigurieren. ALARM0, um das Gerät aufwecken zu können
  rtc = machine.RTC()
  rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

  # RTC einstellen. ALARM0 wird nach X Millisekunden ausgelöst (Aufwecken des Geräts)
  rtc.alarm(rtc.ALARM0, msecs)

  # Versetze das Gerät in den Ruhezustand
  machine.deepsleep()
  
#blink LED
led.value(1)
sleep(1)
led.value(0)
sleep(1)

# Warte 5 Sekunden, damit der ESP wach bleibt, um später eine serielle Kommunikation herzustellen
# Diese Sleep-Zeile im endgültigen Skript entfernen
sleep(5)

print('Im awake, but Im going to sleep')

#sleep für 10 seconds (10000 milliseconds)
deep_sleep(10000)
