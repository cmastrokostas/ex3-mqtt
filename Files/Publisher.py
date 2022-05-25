import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import requests
from datetime import datetime

def httpPost(username):
    pload = {
            'username': username, # Given Username
            'message':input("Message:"), # Type Message
            'datetime':datetime.now().strftime("%d/%m/%Y %H:%M:%S") #Current time with dd/mm/yyyy format
            } 
    r = requests.post('https://httpbin.org/post', data = pload)
    r_dictionary= r.json()
    return r_dictionary

username = input("Username:")
mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client(username)

client.connect(mqttBroker)
topic = "Public Chat"

while True:
    message = httpPost(username)
    client.publish(topic, f"{message['form']['datetime']} {message['form']['username']} says : {message['form']['message']}")
    print(f"{username} just published {message['form']['message']} to Topic {topic}.")