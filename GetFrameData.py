import requests
from flask import json
from uuid import getnode as get_mac

class GetFrameData:

    def SendToCloud(self, url):
        url = url
        data = requests.get(url).content
        data = json.loads(data)
        return data

    def GetMac(self):
        # mac = get_mac()
        mac = 145851863414057
        return mac

    def GetFrame(self, mac):
        url = "https://smartframe.azurewebsites.net/api/GetFrameByMac/" + str(mac)
        return self.SendToCloud(url)

    def GetAccount(self, frame):
        accountId = frame["accountid"]
        url = "https://smartframe.azurewebsites.net/api/GetAccountNameByAccountId/" + accountId
        return self.SendToCloud(url)

    def GetMessages(self, frame):
        frameId = frame["frameid"]
        url = "https://smartframe.azurewebsites.net/api/GetMessages/" + frameId
        return self.SendToCloud(url)

    def GetContacts(self, frame):
        frameId = frame["frameid"]
        url = "https://smartframe.azurewebsites.net/api/GetContacts/" + frameId
        return self.SendToCloud(url)

GetFrameData = GetFrameData()
# mac = str(get_mac())
mac = 145851863414057
mac = str(mac)
frame = GetFrameData.GetFrame(mac)
account = GetFrameData.GetAccount(frame)
messages = GetFrameData.GetMessages(frame)
contacts = GetFrameData.GetContacts(frame)

print(frame)
print(account)
print(messages)
print(contacts)
