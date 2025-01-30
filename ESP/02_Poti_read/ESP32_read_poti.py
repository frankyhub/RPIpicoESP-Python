'''
read_poti.py

ESP32

'''

from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       # 3.3v

while True:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.1)
