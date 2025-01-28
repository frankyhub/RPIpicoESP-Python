'''
LED-Poti-dimm.py

Poti GPIO26 dimmt LED GPIO 20 hell-dunkel

RLED=220Ω

'''

from machine import Pin, PWM, ADC
from time import sleep

# PWM-Pin einrichten
led_pwm = PWM(Pin(20))

# Potentiometer einrichten
pot = ADC(Pin(26))

#PWM-Frequenz einstellen
frequency = 5000
led_pwm.freq (frequency)

try:
    while True:
        # Potentiometerwert ablesen und dem PWM-Bereich zuordnen
        pot_value = pot.read_u16()
        
        # Schalte die LED bei kleinen Wert aus
        if pot_value <= 420:
            led_pwm.duty_u16(0)
        else:            
            # Update der LED-Helligkeit
            led_pwm.duty_u16(pot_value)

        # Füge eine kleine Verzögerung hinzu, um schnelle Änderungen zu vermeiden
        sleep(0.1)
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    led_pwm.duty_u16(0)
    print(led_pwm)
    led_pwm.deinit()