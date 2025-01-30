'''
BME280-Prgramm.py

BME280 ->Adresse 0x76

VIN -> 3,3V
GND -> GND
SCL -> GPIO5
SDA -> GPIO4
'''

from machine import Pin, I2C
from time import sleep
import BME280

# Initialisieren der I2C-Kommunikation
i2c = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=10000)

while True:
    try:
        # BME280-Sensor initialisieren
        bme = BME280.BME280(i2c=i2c, addr=0x76)
        
        # Lese Sensor Daten
        temp_c = bme.temperature
        hum = bme.humidity
        pres = bme.pressure
        
        # Temperatur in Fahrenheit umrechnen
        temp_f = (bme.read_temperature()/100) * (9/5) + 32
        temp_f = str(round(temp_f, 2)) + 'F'
        
        # Print Sensor Daten
        print('Temperatur: ', temp_c)
        print('Temperatur: ', temp_f)
        print('Luftfeuchte ', hum)
        print('Luftdruck: ', pres)
        
    except Exception as e:
        # Handle any exceptions during sensor reading
        print('An error occurred:', e)

    sleep(5)
