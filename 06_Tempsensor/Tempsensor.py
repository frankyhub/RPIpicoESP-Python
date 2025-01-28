'''
Tempsensor.py

Liest den internen Temperatursensor aus
und gibt ihn in °C und °F aus
'''

from machine import ADC

# Interner Temperatursensor ist mit ADC-Kanal 4 verbunden
temp_sensor = ADC(4)

def read_internal_temperature():
    # Lesen des ADC-Werts
    adc_value = temp_sensor.read_u16()

    # ADC-Wert in Spannung umwandeln
    voltage = adc_value * (3.3 / 65535.0)

    # Temperaturberechnung auf Basis der Sensorcharakteristik
    temperature_celsius = 27 - (voltage - 0.706) / 0.001721

    return temperature_celsius

def celsius_to_fahrenheit(temp_celsius): 
    temp_fahrenheit = temp_celsius * (9/5) + 32 
    return temp_fahrenheit

# Ablesen und Drucken der Innentemperatur
temperature_c = read_internal_temperature()
temperature_f = celsius_to_fahrenheit(temperature_c)
print("InterneTemperatur:", temperature_c, "°C")
print("Interne Temperatur:", temperature_f, "°F")