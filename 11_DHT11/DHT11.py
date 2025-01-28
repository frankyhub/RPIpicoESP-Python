'''
DHT11.py

Liest den Temperatursensor DHT11 aus
und gibtdie Temperatur und die Luftfeuchte aus

DHT11:
1 -> 3,3V (36)
2 -> GPIO22 und 10k gegen  3,3V
3 -> NC
4 -> GND

'''

from machine import Pin
from time import sleep
import dht 

# Erstellen eines DHT11-Sensorobjekts auf GPIO-Pin 22
sensor = dht.DHT11(Pin(22))
# Alternativ für den DHT22 :
# sensor = dht.DHT22(Pin(22))

def celsius_to_fahrenheit(temp_celsius): 
    # Konvertiere die Temperatur von Celsius in Fahrenheit
    temp_fahrenheit = temp_celsius * (9/5) + 32 
    return temp_fahrenheit

while True:
    try:
        sleep(2)
        
        # Temperatur und Luftfeuchtigkeit messen
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # Temperatur in Fahrenheit umrechnen
        temp_f = celsius_to_fahrenheit(temp)
        
        # Drucken der Sensormesswerte
        print('DHT Werte: ')
        print('Temperatur: %3.1f ºC' % temp)
        print('Temperatur: %3.1f ºF' % temp_f)
        print('Luftfeuchte: %3.1f %%' % hum)
    
    except OSError as e:
        # Behandeln von Sensormessfehlern
        print('Sensor konnte nicht gelesen werden.')