"""
    Utility to store user preferences between sessions
    TODO: make a logical card access protocol
"""

from os import stat
from utils.resource import PATH
import json

global path, card_path
path = PATH.get('resources/data.json') # the path to the settings storage file
card_path = PATH.get('resources/cards.json') # the path to the card storage file

class store:
    """
        Class to access preferences data
    """

    @staticmethod
    def init():
        """
            Checks for existing preference file, creates one IFF DNE
        """

        try:
            with open(path, 'r') as f:
                pass

        except Exception:
            with open(path, 'w') as f:
                data = {
                    "login": {
                        "email": None,
                        "pass": None,
                        "exists": False
                    },
                    "settings": {
                        "preferences": {
                            "Font": "Times New Roman",
                            "Primary Highlight Color": "Cyan",
                            "Secondary Highlight Color": "Yellow",
                            "Font Size of Primary Emphasis": "12",
                            "Font Size of Normal Text": "8",
                            "Font Size of Minimized Text": "2",
                            "Primary Emphasis Settings": "Bold + Underline + Highlight (Primary)",
                            "Secondary Emphasis Settings": "Bold",
                            "Tertiary Emphasis Settings": "Underline"
                        },
                        "shortcuts": {
                            "Cut-It (Primary Emphasis)": "CTRL+S",
                            "Cut-It (Secondary Emphasis)": "CTRL+SHIFT+S",
                            "Cut-It (Tertiary Emphasis)": "CTRL+ALT+S",
                            "Keep Selected Text" : "Ctrl+K",
                            "Minimize Text": "ALT+M",
                            "AutoPoll": "CTRL+D",
                            "AutoCite": "CTRL+SHIFT+D",
                            "AutoPoll + AutoCite": "CTRL+ALT+D",
                            "Save As PDF": "CTRL+P",
                            "Open/Create Card": "CTRL+SHIFT+P",
                            "Open Settings": "ALT+S",
                            "Close Window": "CTRL+W"
                        }
                    },
                    "fixed_win": True,
                    "stay_logged_in": True,
                    "zoom": 0
                }

                json.dump(data, f)
        
        try:
            with open(card_path, 'r') as f:
                pass
        
        except Exception:
            with open(card_path, 'w') as f:
                data = {
                    "cards" : [{
                        "tag": "",
                        "cite": "",
                        "creds": "",
                        "link": "",
                        "html": "",
                        "text": ""
                    }],
                    "currentCard" : 0
                }

                json.dump(data, f)

    @staticmethod
    def getCardData():
        """
            Returns all the stored cards
        """

        with open(card_path, 'r') as f:
            data = json.loads(f.read())
        
        return data

    @staticmethod
    def getCard():

        return store.getCardData()["cards"][store.getCurrentCard()]

    @staticmethod
    def addCard(card):
        data =  store.getCardData()
        
        data["cards"].insert(0, card)

        with open(card_path, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def updateCard(card, index):
        data =  store.getCardData()
        
        data["cards"][index] = card

        with open(card_path, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def setCurrentCard(index):
        
        try:
            index = int(index)
        except Exception:
            index = None

        data = store.getCardData()
        data["currentCard"] = index

        with open(card_path, 'w') as f:
            json.dump(data, f)
    
    @staticmethod
    def getCurrentCard():
        return store.getCardData()["currentCard"]

    @staticmethod
    def getData():
        with open(path, 'r') as f:
            return json.loads(f.read())

    @staticmethod
    def setData(data):
        with open(path, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def check_login():
        data = store.getData()
        
        if (data["login"]["exists"]) and (data["stay_logged_in"] == True):
            return True
        
        elif (data["login"]["exists"]) and (data["stay_logged_in"] == False):
            store.log_out()
            return False

        else:
            return data["login"]["exists"]

    @staticmethod
    def log_out():
        data = store.getData()

        EMAIL = data["login"]["email"]
        PASS = data["login"]["pass"]

        tools.log_out(EMAIL, PASS)
        
        data["login"]["email"] =  None
        data["login"]["pass"] = None
        data["login"]["exists"] = False

        store.setData(data)

    @staticmethod
    def add_login(EMAIL, PASSWORD):
        data = store.getData()

        data["login"]["email"] = EMAIL
        data["login"]["pass"] = PASSWORD
        data["login"]["exists"] = True

        store.setData(data)
    
    @staticmethod
    def add_misc(fixed_win, stay_logged_in):
        data = store.getData()

        data["fixed_win"] = fixed_win
        data["stay_logged_in"] = stay_logged_in

        store.setData(data)

    @staticmethod  
    def setZoom(zoom):
        data = store.getData()

        data["zoom"] = zoom

        store.setData(data)

    @staticmethod
    def add_prefs(prefs):
        data = store.getData()

        data["settings"]["preferences"] = prefs

        store.setData(data)

store.init()