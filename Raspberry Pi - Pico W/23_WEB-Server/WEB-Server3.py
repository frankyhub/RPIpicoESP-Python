'''
WEB-Server3.py

WEB-Server mit externer webpage.html

Liefert BME280 Daten und schaltet die int. LED

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
from config import wifi_ssid, wifi_password
import socket
import time
from machine import Pin, I2C
import BME280

# Konstante Variable zum Speichern des HTML-Dateipfads
HTML_FILE_PATH = "webpage.html"

# Erstellen eines LED-Objekts auf dem Pin 'LED'
led = Pin('LED', Pin.OUT)

# Initialize LED state
state = 'OFF'

# Initialisierung der I2C-Kommunikation
i2c = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=10000)
bme = BME280.BME280(i2c=i2c, addr=0x76)

# Funktion zum Auslesen von HTML-Inhalten aus der Datei
def read_html_file():
    with open(HTML_FILE_PATH, "r") as file:
        return file.read()

# Abrufen der Sensormesswerte
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
    return html

# Init Wi-Fi-Schnittstelle
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Verbinde mich mit dem Netzwerk
    wlan.connect(ssid, password)
    # Warte auf die Wi-Fi-Verbindung
    connection_timeout = 10
    while connection_timeout > 0:
        print(wlan.status())
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Warten auf Wi-Fi-Verbindung...')
        time.sleep(1)
    #   Überprüfe, ob die Verbindung erfolgreich ist
    if wlan.status() != 3:
        print('Verbindung zum WLAN fehlgeschlagen')
        return False
    else:
        print('Verbindung erfolgreich!')
        network_info = wlan.ifconfig()
        print('IP Addresse:', network_info[0])
        return True

if not init_wifi(wifi_ssid, wifi_password):
    print("Beende das Program.")
else:
    try:
        # Socket einrichten und mit dem auslesem beginnen
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(addr)
        s.listen()
        print('Listening on', addr)

        # Hauptschleife zum Abhören 
        while True:
            try:
                conn, addr = s.accept()
                print('Habe eine Verbindung mit', addr)
                
                # Empfangen und Analysieren der Anforderung
                request = conn.recv(1024)
                request_str = request.decode('utf-8')
                print('Inhalte anfordern:')

                try:
                    request = request.split()[1]
                    print('Inhalte:', request)
                except IndexError:
                    pass
                
                # Verarbeiten der Anforderungs- und Aktualisierungsvariablen
                if request == b'/lighton?':
                    print('LED ein')
                    led.value(1)
                    state = 'ON'
                elif request == b'/lightoff?':
                    print('LED aus')
                    led.value(0)
                    state = 'OFF'
                    print(state)
                # HTML-Antwort generieren
                response = webpage(state)  

                # Beende die HTTP-Antwort und schließe die Verbindung
                conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                conn.send(response)
                conn.close()

            except OSError as e:
                conn.close()
                print('Verbindung geschlossen')
                
    except KeyboardInterrupt:
            print('Server vom Benutzer gestoppt.')