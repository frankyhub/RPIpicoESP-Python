'''
I2C-Scanner.py

BME280 ->Adresse 0x76
OLED -> 0x3c

VIN -> 3,3V
GND -> GND
SCL -> GPIO5
SDA -> GPIO4
'''

# I2C Scanner MicroPython
from machine import Pin, I2C

# Du kannst eine beliebige andere Kombination von I2C-Pins auswählen (GPIO12/13,16/17...)
i2c = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=10000)

print('I2C SCANNER')
devices = i2c.scan()

if len(devices) == 0:
    print("Kein i2c-Gerät !")

else:
    print('I2C-Gerät gefunden:', len(devices))

    for device in devices:
        print("I2C hex Adresse: ", hex(device))