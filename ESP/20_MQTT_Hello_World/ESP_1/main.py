'''
main.py
MQTT

ESP32 

'''

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP hat eine Hallo-Nachricht erhalten')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Verbindung mit %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
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
    if (time.time() - last_message) > message_interval:
      msg = b'Hello #%d' % counter
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()
