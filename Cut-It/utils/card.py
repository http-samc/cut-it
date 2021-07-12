"""
    - Contains a handy dataclass to reference Cards
    - Handles logging of cards for the Github homepage and
      to monitor misuse of autocut on paywalled sites
    - Provides worker QThread class for app.py
"""

import json
from dataclasses import asdict, dataclass

import requests
from PyQt5.QtCore import QThread
from requests.api import head

@dataclass
class Card:
    TAG: str
    CREDS: str
    URL: str
    TEXT: str
    HTML: str

    def isCard(self) -> bool:
        """
            Returns (bool) if the card actually has data
        """

        if ((self.TAG.replace(' ','').replace('\n','').replace('\t','') != "") or
            (self.CREDS.replace(' ','').replace('\n','').replace('\t','') != "") or
            (self.URL.replace(' ','').replace('\n','').replace('\t','') != "") or
            (self.TEXT.replace(' ','').replace('\n','').replace('\t','') != "")):
            return True

        else:
            return False

    def getDict(self) -> dict:
        """
            Returns (dict) representation of the object
        """

        return asdict(self)

class Logger(QThread):
    def __init__(self, cards, parent=None):
        QThread.__init__(self, parent)
        self.cards = cards if isinstance(cards, list) else None

    def run(self):
        """
            Posts cards to logging server on close
            :param: cards (list of card asdicts)
        """

        try:
            BASE = "https://api.jsonbin.io/b/60ead7d7f72d2b70bbad98c2/latest"

            r = requests.get(BASE)
            data = json.loads(r.text)

            for card in self.cards:
                data["cards"].append(card)

            headers = { 'Content-Type': 'application/json' }
            r = requests.put(BASE.replace('latest', ''), json=data, headers=headers)

        except Exception:
            return