'''
bitcoin.py

Ergebis:

MPY: soft reboot
Verbindung erfolgreich!
IP Addresse: 192.168.1.109
Antwort (200=ok):  200
Bitcoin Preis in (USD):  101832


'''

import network
import requests
from time import sleep

# Wi-Fi-Anmeldeinformationen
ssid = 'R2-D2'
password = 'xxx'

# URL anfordern
url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

# Init Wi-Fi Interface
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Verbinde mit dem Netzwerk
    wlan.connect(ssid, password)
    # Warten Sie auf Wi-Fi-Verbindung
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Warten auf Wi-Fi-Verbindung...')
        sleep(1)
    # Überprüfe, ob die Verbindung erfolgreich ist
    if wlan.status() != 3:
        return False
    else:
        print('Verbindung erfolgreich!')
        network_info = wlan.ifconfig()
        print('IP Addresse:', network_info[0])
        return True

if init_wifi(ssid, password):
    try:
        # Anfrage stellen
        response = requests.get(url)
        #Drucken des Antwortcodes
        print('Antwort (200=ok): ', response.status_code)
        
        # Abrufen des Inhalts
        bitcoin = response.json()
        # Schließen Sie die Anfrage
        response.close()
        
        # Bitcoin-Preis
        bitcoin_price = bitcoin['bitcoin']['usd']
        print('Bitcoin Preis in (USD): ', bitcoin_price)

    except Exception as e:
        print('Fehler während der Anforderung:', e)
