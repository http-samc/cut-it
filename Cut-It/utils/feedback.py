"""
    - Sends feedback from the Misc. box in the Settings page to a server (private)
"""

import json
from datetime import datetime

import requests
from PyQt5.QtCore import QThread

from utils.distro import version

class Feedback(QThread):
    def __init__(self, message, parent=None):
        QThread.__init__(self, parent)
        self.message = message

    def run(self):
        """
            Posts message to server
        """

        try:
            BASE = "https://api.jsonbin.io/b/60eca531c68da8710308199c/latest"

            ip = requests.get("https://api4.my-ip.io/ip").text

            r = requests.get(BASE)
            data = json.loads(r.text)
            data["messages"].append({"lastActive":str(datetime.now()),"ip":ip,"version":version(),"message":self.message})
            headers = { 'Content-Type': 'application/json' }
            r = requests.put(BASE.replace('latest', ''), json=data, headers=headers)

        except Exception:
            return