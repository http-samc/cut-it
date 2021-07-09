"""
    - Checks to see if more recent version (update) is available
"""

import requests
from utils.distro import version

def check() -> str:

    try:
        r = requests.get(f"https://api.flare-software.live/otr/cut-it/version%{version()}")
        return r.text

    except Exception:
        return "Error. Please see update.cutit.cards."