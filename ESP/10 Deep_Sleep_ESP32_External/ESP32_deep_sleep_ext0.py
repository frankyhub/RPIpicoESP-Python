'''
ESP32_deep_sleep_ext0.py

ESP32 

'''

import machine
import esp32
from machine import Pin
from time import sleep

wake1 = Pin(14, mode = Pin.IN)

#Der Pegelparameter kann sein: ESP32. WAKEUP_ANY_HIGH oder ESP32. WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)

#Dein Hauptcode wird hier abgelegt, um eine Aufgabe auszuführen

print('Ich bin wach. In 10 Sekunden gehe ich schlafen')
sleep(10)
print('Gehe jetzt schlafen')
machine.deepsleep()
