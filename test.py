from python.GetFrameData import GetFrameData
from uuid import getnode as get_mac
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from python.test_knop import knop_pressed
# from python.LED import LED
# from python.Knop import Knop
# from python.Buzzer import Buzzer
# import RPi.GPIO as GPIO
import requests
from flask import json
import time

aantal = 0

hostename = "52.174.68.36"
# mac = get_mac()
mac = 145851863414057
c = "/frame/" + str(mac)
str_mac = str(mac)
# print(c)
# buzzer = Buzzer(23)
# led = LED(24)
#
# buttons = [21,16,12,25]
#
# knop1 = Knop(buttons[0])
# knop2 = Knop(buttons[1])
# knop3 = Knop(buttons[2])
# knop4 = Knop(buttons[3])

def on_connect(client, userdata, flags, rc):
    client.subscribe(c, 0)
    print("connected with result code " + str(rc))

def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))
    msg = str(msg.payload)[2:-1]
    print(msg)
    dictionaryToJson = json.dumps(msg.lower())
    print(dictionaryToJson)
    if(dictionaryToJson == '"frame_added"'):
        print("Knipperen LED")
        print("2x buzzer")
        # buzzer.lawaai_buzzer_add_frame()
        # led.led_knipperen()
    if(dictionaryToJson == '"contact_added"'):
        print("Knipperen LED")
        print("3x buzzer")
        # buzzer.lawaai_buzzer_add_contact()
        # led.led_knipperen()

def on_publish(msg):
    data = {
        "mac":mac,
        "text":msg
    }
    json_data = json.dumps(data)
    publish.single("message", json_data, hostname=hostename)

def loop():
    client.loop_start()
    # knop_pressed(2)
    client.loop_stop()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(hostename, 1883, 60)
client.loop_forever()

# try:
#     while True:
#         time.sleep(60)
        # knop_pressed(1)
        # knop1.knop_ingedrukt()
        # knop2.knop_ingedrukt()
        # knop3.knop_ingedrukt()
        # knop4.knop_ingedrukt()

# except KeyboardInterrupt:
    # GPIO.output(led, GPIO.LOW)
    # GPIO.output(buzzer, GPIO.LOW)
    # client.loop_stop()