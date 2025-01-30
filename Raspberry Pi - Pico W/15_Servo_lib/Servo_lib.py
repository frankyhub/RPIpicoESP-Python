'''
Servo_lib.py

Library: servo.py

GND -> GND (38)
VCC -> VBUS (40)
Signal -> GPIO 

'''

from servo import Servo
from time import sleep

# Erstelle Servo-Objekt an Pin 0
servo = Servo(pin=0)

try:
    while True:
        #Servo bei 0 Grad
        servo.move(0)
        sleep(2)
        #Servo bei 90 Grad
        servo.move(90)
        sleep(2)
        #Servo bei 180 Grad
        servo.move(180)
        sleep(2)
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Deaktiviere PWM
    servo.stop()
