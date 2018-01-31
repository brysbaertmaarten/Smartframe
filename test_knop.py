import requests
from flask import json
from python.GetFrameData import GetFrameData

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
        print(jsondata)
        requests.post(url, data=jsondata)
