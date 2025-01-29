'''
StepperP.py

Library: stepper.py

Ansteuerung über ULN2003

Externes Netzteil 12V oder 4x1,5VAAA

GND -> GND (38)
IN1 -> GPIO28
IN2 -> GPIO27
IN3 -> GPIO26
IN4 -> GPIO22

'''

import stepper
from time import sleep

# Definiere die Schrittmotor-Pins
IN1 = 28
IN2 = 27
IN3 = 26
IN4 = 22

# Initialisieren des Schrittmotors
stepper_motor = stepper.HalfStepMotor.frompins(IN1, IN2, IN3, IN4)

# Setze die aktuelle Position auf Position 0
stepper_motor.reset()

try:
    while True:
        #Bewegen den Motor 500 Schritte im Uhrzeigersinn
        stepper_motor.step(500)
        sleep(0.5) # Warte
        
        # Bewegen den Motor 500 Schritte im Uhrzeigersinn
        stepper_motor.step(-500)
        sleep(0.5) # Warte
        
        # Wechsle zu einer bestimmten Position (in Schritten)
        stepper_motor.step_until(2000)
        sleep(0.5) # Warte
        
        # Erzwinge Richtung mit dem Parameter dir
        stepper_motor.step_until(2000, dir=-1)
        sleep(0.5) # Warte     
        
        # Gehe zu einer bestimmten Position (Winkel, Maximum ist 359, sonst dreht es sich unendlich)
        stepper_motor.step_until_angle(359)
        sleep(0.5) # Warte
    
except KeyboardInterrupt:
    print('Keyboard interrupt')