'''
2-LEDs_Interrupt.py

2 LED blinken mit unterschiedlicher Frequenz

LED 1 GPIO19
LED 2 GPIO20

RLED1=220Ω
RLED2=220Ω

'''
# 4.6.2 Unterschiedliche Blinkfrequenz
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/

from machine import Pin, Timer
from time import sleep

# LEDs
green_led_pin = 19
green_led = Pin(green_led_pin, Pin.OUT)
blue_led_pin = 20
blue_led = Pin(blue_led_pin, Pin.OUT)

# Callback-Funktion für den 1. Timer
def toggle_green_led(timer):
    green_led.toggle()  # Schalte den LED-Status um (EIN/AUS)
    print('LED 1 ist: ', green_led.value())

# Callback-Funktion für den 2. Timer
def toggle_blue_led(timer):
    blue_led.toggle()  # Schalte den LED-Status um (EIN/AUS)
    print('LED 2 ist: ', blue_led.value())

# Erstelle periodische Timer
green_timer = Timer()
blue_timer = Timer()

# Starte die Timer
green_timer.init(mode=Timer.PERIODIC, period=500, callback=toggle_green_led)  # Der Timer wiederholt sich alle 0,5 Sekunden
blue_timer.init(mode=Timer.PERIODIC, period=2000, callback=toggle_blue_led)  # Der Timer wiederholt sich alle 2 Sekunden

# Main loop (optional)
while True:
    print('Main Loop läuft')
    sleep(2)