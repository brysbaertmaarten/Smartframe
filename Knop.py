import RPi.GPIO as GPIO
import time
import requests
from Buzzer import Buzzer
from flask import json
from GetFrameData import GetFrameData

buttons = [21,20,16,12]

class Knop:

    def __init__(self, pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.RISING, Knop.actie, 5000)
        self.__pin = pin

    @staticmethod
    def knop_pressed(knop):
        mac = GetFrameData.GetMac()
        frame = GetFrameData.GetFrame(mac)

        name_sender = GetFrameData.GetAccount(frame)["name"]
        messages = GetFrameData.GetMessages(frame)
        contacts = GetFrameData.GetContacts(frame)

        for contact in contacts:
            chat_id = contact["number"]
            message = messages[knop]["text"]
            text = name_sender + " has send you a message: \n\n" + message

            jsondata = {"chat_id": chat_id, "text": text}

            url = "https://api.telegram.org/bot499139643:AAGagO20thq-Qownz6LeKPfGiRPS47UOF-g/sendMessage"
            requests.post(url, data=jsondata)

    @staticmethod
    def actie(pin):
        p = GPIO.PWM(23, 261)
        p.start(50)
        time.sleep(0.2)
        p.stop()
        time.sleep(0.2)
        index = buttons.index(pin)
        Knop.knop_pressed(index)
        return("Knop " + str(index + 1) + " is ingedrukt!")

    def knop_ingedrukt(self):
        knop_ingedrukt = 1
        knop = GPIO.input(self.__pin)
        if (knop == False):
            string = Knop.actie(self.__pin)
            print("Knop " + str(buttons.index(self.__pin) + 1) + " is ingedrukt")
            self.__p.start(50)
            time.sleep(0.2)
            self.__p.stop()
            time.sleep(0.2)
            knop_ingedrukt = 0
