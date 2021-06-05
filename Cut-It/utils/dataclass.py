"""
    - Manages User Preferences and Card History
"""

from utils.resource import PATH
import json


P_PATH = PATH.get('resources/data.json') # Preferences Storage Path
C_PATH = PATH.get('resources/cards.json') # Card History Storage Path

def init():
    """
        Initializes both Card and Preferences storage
    """

    # Preferences
    try:
        with open(P_PATH, 'r') as f:
            data = json.loads(f.read())

    except Exception:
        with open(P_PATH, 'w') as f:
            data = {
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
            }
            json.dump(data, f)

    # Card History
    try:
        with open(C_PATH, 'r') as f:
            json.loads(f.read())['cards']
    
    except Exception:
        with open(C_PATH, 'w') as f:
            json.dump({"cards":[]}, f)
