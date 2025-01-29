'''
Temperatur-Datalog.py

Liest den internen Temperatursensor aus
und gibt ihn in °C und °F aus

Alle 10 sek wird der C° Wert in der Datei temperatur_log.txt protokolliert
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


from time import sleep
from machine import Timer

def log_temperature(timer):
    # Lese den Wert des internen Temperatursensors ein
    temperature_c = read_internal_temperature()

    # Formatieren der Temperatur in eine Zeichenfolge mit zwei Dezimalstellen
    temperature_string = "{:.2f} °C\n".format(temperature_c)

    # Schreibe in die Datei
    file_path = 'temperatur_log.txt'
    try:
        print("InterneTemperatur:", temperature_c, "°C")
        print("Interne Temperatur:", temperature_f, "°F")
        file = open(file_path, 'a')
        file.write(temperature_string)
        print("Temperatur erfolgreich protokolliert.")
        file.close()
    except OSError as e:
        print("Error: ", e)

# Erfasse die Temperatur, wenn das Programm zum ersten Mal ausgeführt wird
#log_temperature(0)

# Erstellen eines Timers, der log_temperature jede Minute (60.000 Millisekunden) aufruft
log_timer = Timer(period=10000, mode=Timer.PERIODIC, callback=log_temperature)

# Programm starten
try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    # stoppe den Timer bei Tastaturunterbrechung
    log_timer.deinit()
    print("Keyboard Interrupt")
