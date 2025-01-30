'''
ESP32_main.py

ESP32 

'''
def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Hello, World!</h1></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Habe eine Verbindung mit	 %s' % str(addr))
  request = conn.recv(1024)
  print('Inhalt = %s' % str(request))
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Inhaltstyp: text/html\n')
  conn.send('Verbindung: close\n\n')
  conn.sendall(response)
  conn.close()
