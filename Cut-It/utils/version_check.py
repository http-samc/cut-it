"""
    - Checks to see if more recent version (update) is available
"""

import json
import platform

import requests

from utils.distro import releases, tag, version

def pollReleases():
    """Searches GitHub Releases for new version of matching tag
    """

    TAG = tag()

    VERSION = int(version().replace('.', ''))

    r = requests.get(releases())
    data = json.loads(r.text)

    highestRelease = None

    for i, release in enumerate(data):
        if not TAG in release["tag_name"]: continue
        val = release["tag_name"].replace(TAG, '').replace('v', '').replace('.', '').replace('@', '')

        try: val = int(val)
        except Exception: continue

        if val > VERSION:
            highestRelease = i

    if highestRelease is None: return False

    release = data[highestRelease]

    targetDist = "dist-win" if platform.system() == "Windows" else "dist-mac"

    distURL = None

    for asset in release["assets"]:
        if targetDist in asset["name"]: distURL = asset["browser_download_url"]

    if not distURL: return None

    return {
        "name": release["tag_name"],
        "desc": release["body"],
        "date": release["published_at"],
        "required": True if "<req>" in release["body"] else False,
        "download": distURL
    }

def check() -> str:
    query = pollReleases()
    if not query: return "No updates available."
    else: return f"Restart to download {query['name']}"
