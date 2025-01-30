'''
Taster-LED.py

TASTER (21) - LED (20)
Wenn Taster -> 0 = LED on
R=220Ω
'''


from machine import Pin
from time import sleep
led = Pin(20, Pin.OUT)
button = Pin(21, Pin.IN, Pin.PULL_DOWN)
while True:
    led.value(button.value())
    sleep(0.1)
    print(button.value())
