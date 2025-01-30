'''
PIR-LED2.py

Nach erkannter Bewegung geht die LED an und mit  5s Zeiverzögerung aus

LED GPIO20
PIR GPIO21

RLED=220Ω


'''


from machine import Pin, Timer
import time

# PIR sensor pin
pir_pin = 21
# LED pin 
led_pin = 20

# LED- und PIR-Sensor einrichten
led = Pin(led_pin, Pin.OUT)
pir = Pin(pir_pin, Pin.IN)

# Timer erstellen
motion_timer = Timer()

# Timer erstellen
motion = False
motion_printed = False

def handle_motion(pin):
    global motion
    motion = True
    motion_timer.init(mode=Timer.ONE_SHOT, period=5000, callback=turn_off_led)

def turn_off_led(timer):
    global motion, motion_printed
    led.on()  # Schalte die LED ein
    print('Keine Bewegung!')
    motion = False
    motion_printed = False

# Interrupt für den PIR-Bewegungsmelder
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_motion)

while True:
    if motion and not motion_printed:
        print('Bewegung erkannt!')
        led.off()  # Schalte die LED aus
        motion_printed = True
    elif not motion:
        time.sleep(0.1)
        # Weitere Aktionen?