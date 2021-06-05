"""
    - Sends feedback from the Misc. box in the Settings page to a server (private)
    - TODO: Clean up the backend code
"""

import requests

BASE = "http://api.flare-software.live/otr/cut-it/feedback"

def send_feedback(email, message):

    data = {
        "email" : email,
        "msg" : message
    }

    try:
        r = requests.post(BASE, data=data)
    except Exception:
        pass