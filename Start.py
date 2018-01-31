from uuid import getnode as get_mac
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from LED import LED
from Knop import Knop
from Buzzer import Buzzer
import RPi.GPIO as GPIO
import requests
from flask import json
import time

GPIO.setmode(GPIO.BCM)

hostename = "52.174.68.36"
mact = get_mac()
print("Mac: " + str(mact))
mac = 145851863414057
c = "/frame/" + str(mac)
# print(c)
mac = str(mac)
buzzer = Buzzer(23)
led = LED(25)

buttons = [21,20,16,12]

knop1 = Knop(buttons[0])
knop2 = Knop(buttons[1])
knop3 = Knop(buttons[2])
knop4 = Knop(buttons[3])

led.led_aan()

def on_connect(client, userdata, flags, rc):
    client.subscribe(c, 0)
    print("connected with result code " + str(rc))

def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))
    msg = str(msg.payload)
    print(msg)
    dictionaryToJson = json.dumps(msg.lower())
    print(dictionaryToJson)
    if(dictionaryToJson == '"frame_added"'):
        print("Knipperen LED")
        print("2x buzzer")
        buzzer.lawaai_buzzer_add_frame()
        led.led_knipperen()
        led.led_aan()
    if(dictionaryToJson == '"contact_added"'):
        print("Knipperen LED")
        print("3x buzzer")
        buzzer.lawaai_buzzer_add_contact()
        led.led_knipperen()
        led.led_aan()

def on_publish(msg):
    data = {
        "mac":mac,
        "text":msg
    }
    json_data = json.dumps(data)
    publish.single("message", json_data, hostname=hostename)

def loop():
    client.loop_start()
    knop1.event()
    knop2.event()
    knop3.event()
    knop4.event()
    client.loop_stop()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(hostename, 1883, 60)
client.loop_forever()


try:
    while True:
        print("niets")

except KeyboardInterrupt:
    GPIO.output(led, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)
    client.loop_stop()

GPIO.cleanup()


