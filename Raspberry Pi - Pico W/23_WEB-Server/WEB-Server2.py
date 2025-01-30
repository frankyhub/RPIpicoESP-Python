'''
WEB-Server2.py

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
from time import sleep
from machine import Pin, I2C
import BME280

# Erstelle ein LED-Objekt auf dem Pin 'LED'
led = Pin('LED', Pin.OUT)

# Initialisieren des LED-Zustands
state = 'OFF'

# Initialisieren der I2C-Kommunikation
i2c = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=10000)
bme = BME280.BME280(i2c=i2c, addr=0x76)

# Abrufen der Sensormesswerte
def get_readings():
    temp = bme.temperature[:-1]
    hum = bme.humidity[:-1]
    pres = bme.pressure[:-3]
    return temp, hum, pres

# HTML-Vorlage für die Webseite
def webpage(state):
    #Erhalte jedes Mal neue Sensormesswerte, wenn "Refresh"-Button betätigt wird
    temperature, humidity, pressure = get_readings()
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pico Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Raspberry Pi Pico Web Server</h1>
            <h2>Led Control</h2>
            <form action="./lighton">
                <input type="submit" value="LED an" />
            </form>
            <br>
            <form action="./lightoff">
                <input type="submit" value="LED aus" />
            </form>
            <p>LED Status: {state}</p>
            <h2>BME280 Sensor:</h1>
            <p>Temperatur: {temperature} &#176C</p>
            <p>Luftfeuchte: {humidity} %</p>
            <p>Luftdruck: {pressure} hPa</p>
            <form action="./">
                <input type="submit" value="Refresh" />
            </form>
        </body>
        </html>
        """
    return str(html)

# Init Wi-Fi 
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Verbinde mich mit dem Netzwerk
    wlan.connect(ssid, password)
    # Warte auf Wi-Fi-Verbindung
    connection_timeout = 10
    while connection_timeout > 0:
        print(wlan.status())
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Warten auf Wi-Fi-Verbindung...')
        sleep(1)
    # Überprüfe, ob die Verbindung erfolgreich ist
    if wlan.status() != 3:
        print('...')
        return False
    else:
        print('Verbindung erfolgreich!')
        network_info = wlan.ifconfig()
        print('IP Addresse:', network_info[0])
        return True

if not init_wifi(wifi_ssid, wifi_password):
    print("Programm beenden.")
else:
    try:
        # Socket einrichten und mit dem auslesen beginnen
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(addr)
        s.listen()
        print('Höre auf', addr)

        # Hauptschleife 
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
                    #print('Request:', request)
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

                # Sende die HTTP-Antwort und schließe die Verbindung.
                conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                conn.send(response)
                conn.close()

            except OSError as e:
                conn.close()
                print('Verbindung geschlossen')
                
    except KeyboardInterrupt:
            print('Server vom Benutzer gestoppt.')