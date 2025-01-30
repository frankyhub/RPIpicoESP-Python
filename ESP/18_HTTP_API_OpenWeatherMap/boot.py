'''
boot.py

ESP32 /ESP8266

'''

import time

try:
  import urequests as requests
except:
  import requests
  
try:
  import ujson as json
except:
  import json

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Deine_SSID'
password = 'Dein_PASSWORT'

city = 'Tegernsee'
country_code = 'DE'


open_weather_map_api_key = '6ff2d5fd94ed44197773c0dc2c5d32ec'
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Verbindung erfolgreich')
print(station.ifconfig())

#Lege eine eindeutige OpenWeatherMap.org-URL fest
open_weather_map_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country_code + '&APPID=' + open_weather_map_api_key

weather_data = requests.get(open_weather_map_url)
print(weather_data.json())

# Standort (Stadt- und Ländercode)
location = 'Location: ' + weather_data.json().get('name') + ' - ' + weather_data.json().get('sys').get('country')
print(location)

# Wetter Beschreibung
description = 'Description: ' + weather_data.json().get('weather')[0].get('main')
print(description)

# Temperatur
raw_temperature = weather_data.json().get('main').get('temp')-273.15

# Temperatur in Celsius
temperature = 'Temperature: ' + str(raw_temperature) + '*C'
#uncomment for temperature in Fahrenheit
#temperature = 'Temperature: ' + str(raw_temperature*(9/5.0)+32) + '*F'
print(temperature)

# Luftdruck
pressure = 'Pressure: ' + str(weather_data.json().get('main').get('pressure')) + 'hPa'
print(pressure)

# Luftfeuchte
humidity = 'Humidity: ' + str(weather_data.json().get('main').get('humidity')) + '%'
print(humidity)

# Wind
wind = 'Wind: ' + str(weather_data.json().get('wind').get('speed')) + 'mps ' + str(weather_data.json().get('wind').get('deg')) + '*'
print(wind)