'''
WEB-Server1.py

Raspberry Pi Pico Web Server
Hello, Maker!

MPY: soft reboot
Verbindung erfolgreich!
IP address: 192.168.1.109
Abhören auf ('0.0.0.0', 80)


'''


# Importieren notwendiger Module
import network
import socket
import time


# Wi-Fi-Anmeldeinformationen
ssid = 'R2-D2'
password = 'xxx'

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

# Init Wi-Fi
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Verbinde mit WiFi
    wlan.connect(ssid, password)
    # Warte auf WiFi
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Warten auf Wi-Fi-Verbindung...')
        time.sleep(1)
    # Check if connection is successful
    if wlan.status() != 3:
        return False
    else:
        print('Verbindung erfolgreich!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        return True

if init_wifi(ssid, password):
    # Set up socket and start listening
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen()
    print('Abhören auf', addr)

# Main loop to listen for connections
while True:
    try:
        conn, addr = s.accept()
        print('Habe eine Verbindung von', addr)

        # Receive and parse the request
        request = conn.recv(1024)
        request_str = request.decode('utf-8')
        print('Inhalt anfordern:')
        
        # Split headers and body
        headers, body = request_str.split('\r\n\r\n', 1)
        print('Headers:\n', headers)
        print('Body:\n', body)

        # Generate HTML response
        response = webpage

        # Send the HTTP response and close the connection
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()

    except OSError as e:
        conn.close()
        print('Verbindung geschlossen')
