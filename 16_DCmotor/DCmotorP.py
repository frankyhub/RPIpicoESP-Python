'''
DCmotorP.py

Library: dcmotor.py

Ansteuerung über L298N H-Bridge
Externes Netzteil 12V oder 4x1,5VAAA

GND -> GND (38)
ENA -> GPIO2
IN1 -> GPIO3
IN2 -> GPIO4

'''

from dcmotor import DCMotor
from machine import Pin, PWM
from time import sleep

frequency = 1000

pin1 = Pin(3, Pin.OUT)
pin2 = Pin(4, Pin.OUT)
enable = PWM(Pin(2), frequency)

dc_motor = DCMotor(pin1, pin2, enable)

# Stelle die minimale Einschaltdauer (15000) und die maximale Einschaltdauer (65535) ein
#dc_motor = DCMotor(Pin1, Pin2, aktivieren, 15000, 65535)

try:
    print('Forward with speed: 50%')
    dc_motor.forward(50)
    sleep(5)
    dc_motor.stop()
    sleep(5)
    print('Backwards with speed: 100%')
    dc_motor.backwards(100)
    sleep(5)
    print('Forward with speed: 5%')
    dc_motor.forward(5)
    sleep(5)
    dc_motor.stop()
    
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    dc_motor.stop()
