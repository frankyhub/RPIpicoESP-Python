'''
blink.py

RPI flash
RP2
Raspberry Pi - Pico W / Pico WH

Blink interne LED (25)
'''


from machine import Pin
from time import sleep
led = Pin('LED', Pin.OUT)
while True:
    led.value(not led.value())
    sleep(0.5)
