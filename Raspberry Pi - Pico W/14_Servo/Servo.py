'''
Servo.py

GND -> GND (38)
VCC -> VBUS (40)
Signal -> GPIO 

'''

from machine import Pin, PWM
from time import sleep

# PWM-Pin für Servosteuerung einrichten
servo_pin = machine.Pin(0)
servo = PWM(servo_pin)

# Stelle das Tastverhältnis für verschiedene Winkel 
max_duty = 7864
min_duty = 1802
half_duty = int(max_duty/2)

#PWM Frequenz
frequency = 50
servo.freq (frequency)

try:
    while True:
        #Servo bei 0 Grad
        servo.duty_u16(min_duty)
        sleep(2)
        #Servo bei 90 Grad
        servo.duty_u16(half_duty)
        sleep(2)
        #Servo bei 180 Grad
        servo.duty_u16(max_duty)
        sleep(2)    
      
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Deaktiviere PWM
    servo.deinit()