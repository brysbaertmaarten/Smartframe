import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
# import RPi.GPIO as GPIO
from uuid import getnode as get_mac
import time
from LED import LED
from Buzzer import Buzzer

# GPIO.setmode(GPIO.BCM)

hostename = "broker.hivemq.com"
# mac = get_mac()
mac = 123456789012345
c = "/frame/" + str(mac)
print(c)
buzzer = Buzzer(23)
led = LED(24)

def on_connect(client, userdata, flags, rc):
    client.subscribe(c, 0)
    print("connected with result code " + str(rc))

def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))
    msg = str(msg.payload)[2:-1]
    # print(msg)
    dictionaryToJson = json.dumps(msg.lower())
    print(dictionaryToJson)
    if(dictionaryToJson == "frame_added"):
        buzzer.lawaai_buzzer_add_frame()
        led.led_knipperen()
    if(dictionaryToJson == "contact_added"):
        buzzer.lawaai_buzzer_add_contact()
        led.led_knipperen()

def on_publish(msg):
    data = {
        "mac":mac,
        "text":msg
    }
    json_data = json.dumps(data)
    publish.single("message", json_data, hostname=hostename)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# print(mac)

client.connect(hostename, 1883, 60)
client.loop_forever()

# GPIO.cleanup()
