import requests

BASE = "http://api.flare-software.live/otr/cut-it/feedback"

def send_feedback(email, message):

    data = {
        "email" : email,
        "msg" : message
    }
    r = requests.post(BASE, data=data)