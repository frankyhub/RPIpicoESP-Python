'''
WEB-Server-json.py

in der Datei wifi_credentials.json
sind WLAN-Zugangsdaten gespechert


[
    {"ssid": "your_ssid_1", "password": "your_password_1"},
    {"ssid": "your_ssid_2", "password": "your_password_2"},
    {"ssid": "your_ssid_3", "password": "your_password_3"}
]

HTML:
Raspberry Pi Pico Web Server
Hello, Maker!

'''

import network
import socket
import time
import json

# HTML-Vorlage für die Webseite
webpage = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pico Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Raspberry Pi Pico Web Server</h1>
            <p>Hello, Maker!</p>
        </body>
        </html>
        """

def init_wifi_from_file(file_path='wifi_credentials.json'):
    try:
        with open(file_path, 'r') as file:
            credentials = json.load(file)
    except OSError:
        print(f"Fehler: {file_path} kann nicht gelesen werden. Stelle sicher, dass die Datei vorhanden und ordnungsgemäß formatiert ist.")
        return False

    for cred in credentials:
        ssid = cred.get('ssid')
        password = cred.get('password')
        if ssid and password:
            if init_wifi(ssid, password):
                return True

    print("Es kann keine Verbindung zu einem Wi-Fi-Netzwerk hergestellt werden.")
    return False

# Init Wi-Fi
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()

    print(f"Versuche eine Verbindung zum Wi-Fi-Netzwerk mit der SSID herzustellen: {ssid}")

    wlan.connect(ssid, password)

    # Warte auf Wi-Fi
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.isconnected():
            print('Verbindung erfolgreich!')
            network_info = wlan.ifconfig()
            print('IP Addresse:', network_info[0])
            return True

        connection_timeout -= 1
        print('Warten auf Wi-Fi-Verbindung...')
        time.sleep(1)

    print(f"Fehler beim Verbinden mit dem Wi-Fi-Netzwerk mit der SSID: {ssid}")
    return False

# Set up Wi-Fi
if not init_wifi_from_file():
    print("Programm beenden.")
else:
    try:
        # Set up socket and start listening
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(addr)
        s.listen()
        print('Abhören auf', addr)

        # Hauptschleife zum Abhören von Verbindungen
        while True:
            try:
                conn, addr = s.accept()
                print('Habe eine Verbindung von', addr)

                # Empfangen und Analysieren der Anforderung
                request = conn.recv(1024)
                request_str = request.decode('utf-8')
                print('Inhalte anfordern:')
                
                # Kopfzeilen und Text
                headers, body = request_str.split('\r\n\r\n', 1)
                print('Headers:\n', headers)
                print('Body:\n', body)

                # HTML-Antwort generieren
                response = webpage

                # Sende die HTTP-Antwort, und schließe die Verbindung.
                conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                conn.send(response)
                conn.close()

            except OSError as e:
                conn.close()
                print('Verbindung geschlossen')

    except KeyboardInterrupt:
        print('Server vom Benutzer gestoppt.')