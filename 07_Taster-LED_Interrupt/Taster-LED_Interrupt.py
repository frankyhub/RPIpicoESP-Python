'''
Taster-LED_Interrupt.py

Taster GPIO21 schaltet LED GPIO 20 über Interrupt 
und zählt die Taster-Betätigungen

RLED=220Ω

'''


from machine import Pin
from time import sleep

led = Pin(20, Pin.OUT)
button = Pin(21, Pin.IN, Pin.PULL_DOWN)
counter = 0   # Initialisieren der Anzahl der Tastenbetätigung

def button_pressed(pin):
    global counter # Variable als global deklarieren
    counter +=1
    print("Button Pressed! Count: ", counter)
    sleep(0.5)
    
    # Schalte die LED bei jedem Tastendruck um
    led.value(not led.value())

# Aktiviert den Interrupt an der steigenden Flanke des Buttons
button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)
sleep(1)
