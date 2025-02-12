'''
OLED-BME280.py

Liest den BME280 aus
und gibt ihn in auf dem OLED aus

OLED
https://www.ebay.de/itm/404313020839
0.96" I2C IIC Serial 128X64 OLED LCD White LED Display Module For Arduino
Lmu-Arduino
SDA-> GPOI4
SCL -> GPIO5
GND -> GND
Vcc -> 3,3V

BME280
SDA-> GPOI8
SCL -> GPIO9
GND -> GND
Vcc -> 3,3V

'''

from machine import Pin, SoftI2C
import ssd1306
#import lib_oled96 
import BME280
from time import sleep

# Initialisieren der I2C-Verbindungen für OLED und BME280
i2c_oled = SoftI2C(scl=Pin(5), sda=Pin(4))
i2c_bme280 = SoftI2C(scl=Pin(9), sda=Pin(8))

# Einrichten von OLED-Anzeigeparametern
oled_width = 128
oled_height = 64

# Initialisieren des OLED-Displays
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c_oled, addr=0x3c)

while True:
    try:
        # BME280-Sensor initialisieren
        bme = BME280.BME280(i2c=i2c_bme280, addr=0x76)

        # Lösche das OLED-Display
        oled.fill(0)
        oled.show()

        # Lesen von Sensordaten vom BME280
        tempC = bme.temperature
        hum = bme.humidity
        pres = bme.pressure

        # Print Sensor Daten
        print('    ')
        print('          BME280')
        print('Temperatur: ', tempC)
        #print('Temperatur: ', temp_f)
        print('Luftfeuchte ', hum)
        print('Luftdruck: ', pres)
        
        
        # Temperatur in Fahrenheit umrechnen
        tempF = (bme.read_temperature() / 100) * (9 / 5) + 32
        tempF = str(round(tempF, 2)) + 'F'

        # Vorbereiten von Nachrichten für die Anzeige auf OLED
        tempC_oled = "Temp: " + tempC
        tempF_oled = "Temp: " + tempF
        hum_oled = "LFeuchte: " + hum
        pres_oled = "LDruck:" + pres

        # Anzeige von Sensordaten auf dem OLED
        oled.text("BME280" , 30, 0)
        oled.text(tempC_oled, 0, 15)
        oled.text(hum_oled, 0, 30)
        oled.text(pres_oled, 0, 45)

        # Aktualisiere das OLED-Display, um die Daten anzuzeigen
        oled.show()

    except Exception as e:
        # Error während des Auslesens des Sensors
        print('An error occurred:', e)

    # Warte 30 Sekunden
    sleep(30)
