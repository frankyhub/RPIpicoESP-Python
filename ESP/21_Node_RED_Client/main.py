'''
main.py

Node red

ESP32 

'''

def read_ds_sensor():
  roms = ds_sensor.scan()
  print('Gefundene DS-Geräte: ', roms)
  print('Temperatur: ')
  ds_sensor.convert_temp()
  time.sleep(1)
  for rom in roms:
    temp = ds_sensor.read_temp(rom)
    if isinstance(temp, float):
      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0
      msg = (b'{0:3.1f}'.format(temp))
      print(temp, end=' ')
      print('Gültige Temperatur')
      return msg
  return b'0.0'

def sub_cb(topic, msg):
  print((topic, msg))
  if msg == b'on':
    led.value(1)
  elif msg == b'off':
    led.value(0)

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Verbunden mit %s MQTT-Broker, abonniert %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Fehler beim Verbinden mit dem MQTT-Broker. Wiederherstellen...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_sensor_reading) > readings_interval:
      msg = read_ds_sensor()
      client.publish(topic_pub, msg)
      last_sensor_reading = time.time()
  except onewire.OneWireError:
    print('Fehler beim Lesen/Veröffentlichen von Sensormesswerten.')
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()
