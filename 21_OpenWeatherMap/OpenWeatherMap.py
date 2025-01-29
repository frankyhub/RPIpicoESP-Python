'''
OpenWeatherMap.py

Ergebis:

MPY: soft reboot
Verbindung erfolgreich
IP Addresse: 192.168.1.109
Antwortcode:  200
Weather JSON:  {'timezone': 3600, 'sys': {'sunrise': 1738133019, 'country': 'DE', 'sunset': 1738166905}, 'base': 'stations', 'main': {'pressure': 1012, 'feels_like': 279.22, 'temp_max': 279.22, 'temp': 279.22, 'temp_min': 279.22, 'humidity': 75, 'sea_level': 1012, 'grnd_level': 902}, 'visibility': 10000, 'id': 2823679, 'clouds': {'all': 37}, 'coord': {'lon': 11.7527, 'lat': 47.7097}, 'name': 'Tegernsee', 'cod': 200, 'weather': [{'id': 802, 'icon': '03d', 'main': 'Clouds', 'description': 'scattered clouds'}], 'dt': 1738157932, 'wind': {'gust': 1.08, 'speed': 0.74, 'deg': 324}}
Current weather:  scattered clouds
Temperatur in Kelvin: 279.22
Temperatur in Celsius: 6.07
Temperatur in Fahrenheit: 42.93
Windgeschwindigkeit in m/s: 0.74

'''


import network
import time
import requests

# Wi-Fi Zugangsdaten
ssid = 'R2-D2'
password = 'xxx'

api_key = '6ff2d5fd94ed44197773c0dc2c5d32ec'
city = 'Tegernsee'
country_code ='DE'

# URL anfordern
url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}'

# Init Wi-Fi Interface
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # WiFI Verbindung
    wlan.connect(ssid, password)
    # Warte auf WiFi Verbindung
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Warte auf WiFi Verbindung...')
        time.sleep(1)
    # Überprüfe, ob die Verbindung erfolgreich ist
    if wlan.status() != 3:
        return False
    else:
        print('Verbindung erfolgreich')
        network_info = wlan.ifconfig()
        print('IP Addresse:', network_info[0])
        return True

if init_wifi(ssid, password):
    try:
        # Anfrage stellen
        response = requests.get(url)
        #Drucken des Antwortcodes
        print('Antwortcode: ', response.status_code)
        
        # Abrufen von Antwortinhalten
        weather = response.json()
        # Anfrage schließen
        response.close()
        
        # Drucken aller Wetterdaten
        print('Weather JSON: ', weather)
        
        # Holen der spezifischen Wetterdaten
        weather_description = weather['weather'][0]['description']
        print('Current weather: ', weather_description)
        
        # Temperatur
        temperature_k = weather['main']['temp']  # Gibt die Temperatur in Kelvin zurück
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k - 273.15) * 9/5 + 32
        print(f'Temperatur in Kelvin: {temperature_k:.2f}')
        print(f'Temperatur in Celsius: {temperature_c:.2f}')
        print(f'Temperatur in Fahrenheit: {temperature_f:.2f}')              
        
        # Wind
        wind_speed = weather['wind']['speed']
        print('Windgeschwindigkeit in m/s:', wind_speed)

    except Exception as e:
        print('Fehler während der Anforderung:', e)
