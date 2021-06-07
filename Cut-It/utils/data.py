"""
    - Manages User Preferences and Card History
"""

from typing import Dict
from schema import Schema, And, Use, Optional, SchemaError
from utils.resource import PATH
from utils.card import Card
import json

P_PATH = PATH.get('userData/data.json') # Preferences Storage Path
C_PATH = PATH.get('userData/cards.json') # Card History Storage Path

# Defining Schema for the preferences and shortcuts section of Preferences
PREFS_SCHEMA = Schema({
    "Font": And(str, len),
    "Primary Highlight Color": And(str, len),
    "Secondary Highlight Color": And(str, len),
    "Font Size of Normal Text": And(Use(int)),
    "Font Size of Minimized Text": And(Use(int)),
    "Primary Emphasis Settings": And(list),
    "Secondary Emphasis Settings": And(list),
    "Tertiary Emphasis Settings": And(list),
    "Theme": And(str)
})

SHORTCUTS_SCHEMA = Schema({
    "Primary Emphasis": And(str, len),
    "Secondary Emphasis": And(str, len),
    "Tertiary Emphasis": And(str, len),
    "Keep Selected Text" : And(str, len),
    "Minimize Text": And(str, len),
    "AutoPoll": And(str, len),
    "AutoCite": And(str, len),
    "AutoPoll + AutoCite": And(str, len),
    "Save As PDF": And(str, len),
    "Close Window": And(str, len)
})

# Data validator/fixer
def init():
    """
        Initializes both Card and Preferences storage
    """

    # Preferences
    try:
        with open(P_PATH, 'r') as f:
            data = json.loads(f.read())
            data["Card Index"]
            PREFS_SCHEMA.validate(data["preferences"])
            SHORTCUTS_SCHEMA.validate(data["shortcuts"])

    except Exception:

        with open(P_PATH, 'w') as f:
            """
                Em. Settings in the form:
                [
                    (bool) bold,
                    (bool) italicised,
                    (bool) underlined,
                    (str) highlight color || None,
                ]
            """

            data = {
                "preferences": {
                    "Font": "Times New Roman",
                    "Primary Highlight Color": "Cyan",
                    "Secondary Highlight Color": "Yellow",
                    "Font Size of Normal Text": 8,
                    "Font Size of Minimized Text": 2,
                    "Primary Emphasis Settings": [
                        True,
                        False,
                        True,
                        "Cyan",
                        12
                    ],
                    "Secondary Emphasis Settings": [
                        True,
                        False,
                        False,
                        None,
                        8
                    ],
                    "Tertiary Emphasis Settings": [
                        False,
                        False,
                        True,
                        None,
                        8
                    ],
                    "Theme" : "dark"
                },
                "shortcuts": {
                    "Primary Emphasis": "CTRL+S",
                    "Secondary Emphasis": "CTRL+SHIFT+S",
                    "Tertiary Emphasis": "CTRL+ALT+S",
                    "Keep Selected Text" : "Ctrl+K",
                    "Minimize Text": "ALT+M",
                    "AutoPoll": "CTRL+D",
                    "AutoCite": "CTRL+SHIFT+D",
                    "AutoPoll + AutoCite": "CTRL+ALT+D",
                    "Save As PDF": "CTRL+P",
                    "Close Window": "CTRL+W"
                },
                "Card Index": None
            }
            json.dump(data, f)

    # Card History
    try:
        with open(C_PATH, 'r') as f:
            json.loads(f.read())['cards']
            
    
    except Exception:
        with open(C_PATH, 'w') as f:
            json.dump({"cards":[]}, f)

def getIndex() -> int:
    """
        Returns (int) current card index
    """

    with open(P_PATH, 'r') as f:
        return json.loads(f.read())["Card Index"]

"""
    Preferences Methods
"""

# Getters and Setters

def getPrefData() -> dict:
    """
        Returns a dict of data.json
    """

    with open(P_PATH, 'r') as f:
        return json.loads(f.read())

def setPrefData(data) -> None:
    """
        Writes to data.json
    """

    with open(P_PATH, 'w') as f:
        json.dump(data, f)

# Functions

def getPref(key: str) -> any:
    """
        Returns the value of the inputted preference key
    """

    return getPrefData()["preferences"][key]

def setPref(key: str, val: any) -> None:
    """
        Sets the value of the inputted preference key to the
        inputted value
    """

    if isinstance(val, list) and val[3] == "None":
        val[3] = None

    data = getPrefData()
    data["preferences"][key] = val
    setPrefData(data)

def getShort(key: str) -> any:
    """
        Returns the value of the inputted shortcut key
    """

    return getPrefData()["shortcuts"][key]

def setShort(key: str, val: any) -> None:
    """
        Sets the value of the inputted shortcut key to the
        inputted value
    """

    data = getPrefData()
    data["shortcuts"][key] = val
    setPrefData(data)

"""
    Card Methods
"""

# Getters and Setters

def getCardData() -> dict:
    """
        Returns a dict of cards.json
    """

    with open(C_PATH, 'r') as f:
        return json.loads(f.read())

def setCardData(data) -> None:
    """
        Writes to cards.json
    """

    with open(C_PATH, 'w') as f:
        json.dump(data, f)

# Functions

def getCard(idx: int = 0) -> Card:
    """
        Returns card at start OR at supplied index
    """

    return Card(**getCardData()["cards"][idx])

def addCard(card: Card, idx: int = None) -> None:
    """
        Checks if a card contains information, if so adds it
        at the first pos of cards.json, or if an index is 
        supplied it will overwrite the card at that pos
    """

    data = getCardData()
    if idx:
        data["cards"][idx] = card.getDict()

    else:
        data["cards"].insert(0, card.getDict())

    setCardData(data)

def deleteCard(idx: int) -> None:
    """
        Deletes card at specified index
    """

    data = getCardData()
    del data["cards"][idx]

    setCardData(data)