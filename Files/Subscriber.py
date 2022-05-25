import paho.mqtt.client as mqtt
from random import randrange, uniform
import time 

topic = "Public Chat"
def on_message(client, userdata, message):
    print(f"Received Message: {str(message.payload.decode('utf-8'))} ")

mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client("Receiver")
client.connect(mqttBroker)

client.loop_start()
client.subscribe(topic)
client.on_message = on_message
time.sleep(300)
client.loop_end
