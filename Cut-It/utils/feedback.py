"""
    - Sends feedback from the Misc. box in the Settings page to a server (private)
"""

from utils.distro import version
import requests

BASE = "https://api.flare-software.live/otr/cut-it/feedback"

def send_feedback(message):

    data = {
        "version" : float(version()),
        "response" : message
    }

    try:
        r = requests.post(BASE, data=data)
        
    except Exception:
        pass