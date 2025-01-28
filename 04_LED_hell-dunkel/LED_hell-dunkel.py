'''
LED_hell-dunkel.py

LED (20) dimmt hell-dunkel

'''


from machine import Pin, PWM
from time import sleep

# PWM-Pin einrichten
led = machine.Pin(20)
led_pwm = PWM(led)
duty_step = 100  # Schrittweite zum ändern des Arbeitszyklus

#PWM Frequenz
frequency = 5000
led_pwm.freq (frequency)

try:
    while True:
        # Erhöhe das Tastverhältnis allmählich
        for duty_cycle in range(0, 65536, duty_step):
            led_pwm.duty_u16(duty_cycle)
            sleep(0.005)
          
        # Verringere das Arbeitszyklus allmählich
        for duty_cycle in range(65536, 0, -duty_step):
            led_pwm.duty_u16(duty_cycle)
            sleep(0.005)
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    led_pwm.duty_u16(0)
    print(led_pwm)
    led_pwm.deinit()