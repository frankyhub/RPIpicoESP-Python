'''
WEB-Server4.py

WEB-Server mit externer webpage.html

Liefert BME280 Daten
Die int. LED blinkt
Die LED GPIO19 lässt sich über den WEB-Server e/a schalten
R = 220

BME280
Vin -> 3,3V
GND -> GND
SCA -> GPIO4
SCL -> GPIO5

WiFi Zugangsdaten von config.py
#config.py
wifi_ssid = 'R2-D2'
wifi_password =  'xxx'

'''

# Importieren notwendiger Module
import network
import asyncio
from config import wifi_ssid, wifi_password
import socket
import time
from machine import Pin, I2C
import BME280

# Konstante Variable zum Speichern des HTML-Dateipfads
HTML_FILE_PATH = "webpage.html"

# Erstellen der LEDs
led_blink = Pin(20, Pin.OUT)
led_control = Pin(19, Pin.OUT)
onboard_led = Pin('LED', Pin.OUT)

# Initialisieren des LED-Zustands
state = 'OFF'

# Initialisieren der I2C-Kommunikation
i2c = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=10000)
bme = BME280.BME280(i2c=i2c, addr=0x76)

# Funktion zum Auslesen von HTML-Inhalten aus der Datei
def read_html_file():
    with open(HTML_FILE_PATH, "r") as file:
        return file.read()

# Abrufen von Sensormesswerte
def get_readings():
    temp = bme.temperature[:-1]
    hum = bme.humidity[:-1]
    pres = bme.pressure[:-3]
    return temp, hum, pres

# HTML-Vorlage für die Webseite
def webpage(state):
    temperature, humidity, pressure = get_readings()
    html_content = read_html_file()
    html = html_content.format(state=state, temperature=temperature, humidity=humidity, pressure=pressure)
    print(webpage)
    return html

# Init Wi-Fi-Schnittstelle
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Verbinde mit dem Netzwerk
    wlan.connect(ssid, password)
    # Warte auf Wi-Fi-Verbindung
    connection_timeout = 10
    while connection_timeout > 0:
        print(wlan.status())
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Warte auf Wi-Fi-Verbindung...')
        time.sleep(1)
    # Überprüfe, ob die Verbindung erfolgreich ist
    if wlan.status() != 3:
        print('Verbindung zum WLAN fehlgeschlagen')
        return False
    else:
        print('Verbindung erfolgreich!')
        network_info = wlan.ifconfig()
        print('IP Addresse:', network_info[0])
        return True

# Asynchrone Funktion zur Verarbeitung von Client-Anfragen
async def handle_client(reader, writer):
    global state
    
    print("Client verbunden")
    request_line = await reader.readline()
    print('Request:', request_line)
    
    # Überspringen von HTTP-Anforderungsheadern
    while await reader.readline() != b"\r\n":
        pass
    
    request = str(request_line, 'utf-8').split()[1]
    print('Request:', request)
    
    # Verarbeiten der Anforderungs- und Aktualisierungsvariablen
    if request == '/lighton?':
        print('LED ein')
        led_control.value(1)
        state = 'ON'
    elif request == '/lightoff?':
        print('LED aus')
        led_control.value(0)
        state = 'OFF'
    
    # HTML-Antwort generieren
    response = webpage(state)  

    # Sende die HTTP-Antwort, und schließe die Verbindung.
    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(response)
    await writer.drain()
    await writer.wait_closed()
    print('Client getrennt')
    
async def blink_led():
    while True:
        led_blink.toggle()  # Toggle LED state
        await asyncio.sleep(0.5)  # Blink interval

async def main():    
    if not init_wifi(wifi_ssid, wifi_password):
        print('Programm beenden.')
        return
    
    # Starte den Server, und führe die Ereignisschleife aus.
    print('Server einrichten')
    server = asyncio.start_server(handle_client, "0.0.0.0", 80)
    asyncio.create_task(server)
    asyncio.create_task(blink_led())
    
    while True:
        print('Schleife')
        # Füge  weitere Aufgaben hinzu, die du  möglicherweise in der Schleife ausführen müssen
        await asyncio.sleep(5)
        onboard_led.toggle()
        
# Erstellen einer Ereignisschleife
loop = asyncio.get_event_loop()
# Erstellen einer Aufgabe zum Ausführen der Hauptfunktion
loop.create_task(main())

try:
    # Führe die Ereignisschleife unbegrenzt aus
    loop.run_forever()
except Exception as e:
    print('Fehler aufgetreten: ', e)
except KeyboardInterrupt:
    print('Programm vom Benutzer unterbrochen')
