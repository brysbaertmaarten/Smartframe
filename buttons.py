import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import RPi.GPIO as GPIO
from uuid import getnode as get_mac
import time

GPIO.setmode(GPIO.BCM)

hostename = "broker.hivemq.com"
mac = get_mac()
buttons = [21, 16, 12, 25]
messages = ["smiley", "angry", "heart", "happy"]

def actie(pin):
    index = buttons.index(pin)
    print("Ingedrukt: " + str(index + 1))
    on_publish(messages[index])

for button in buttons:
    GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.add_event_detect(button, GPIO.RISING, actie, 400)

def on_connect(client, userdata, flags, rc):
    client.subscribe("maarten", 0)
    print("connected with result code " + str(rc))

def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))
    msg = str(msg.payload)
    print(msg)
    dictionaryToJson = json.dumps(msg.lower())
    print(dictionaryToJson)

def on_publish(msg):
    data = {
        "mac":mac,
        "msg":msg
    }
    json_data = json.dumps(data)
    publish.single("message", json_data, hostname=hostename)
#
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(hostename, 1883, 60)
client.loop_forever()

GPIO.cleanup()
