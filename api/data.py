from api.resource import PATH
from api.auth_tools import tools
import json

global path
path = PATH.get('resources/data.json')

class store:

    @staticmethod
    def init():
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
                            "Font": "MS Shell Dlg 2",
                            "Primary Highlight Color": "Cyan",
                            "Secondary Highlight Color": "Green",
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
                            "Minimize Text": "ALT+M",
                            "AutoPoll": "CTRL+D",
                            "AutoCite": "CTRL+SHIFT+D",
                            "AutoPoll + AutoCite": "CTRL+ALT+D",
                            "Save As PDF": "CTRL+P",
                            "Save Card In Progress": "CTRL+SHIFT+P",
                            "Open Shortcuts": "ALT+S",
                            "Open Preferences": "ALT+P",
                            "Close Window": "CTRL+W"
                        }
                    },
                    "fixed_win": False,
                    "stay_logged_in": False
                }

                json.dump(data, f)

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
    def add_prefs(prefs):
        data = store.getData()

        data["settings"]["preferences"] = prefs

        store.setData(data)

    # Depreciated
    @staticmethod
    def add_shorts(shorts):

        data = store.getData()

        data["settings"]["shortcuts"] = shorts

        store.setData(data)
    
    # Make everything after this its own class!
    @staticmethod
    def get_font():
        return store.getData()["settings"]["preferences"]["Font"]

    @staticmethod
    def phc():
        return store.getData()["settings"]["preferences"]["Primary Highlight Color"]

    @staticmethod
    def shc():
        return store.getData()["settings"]["preferences"]["Secondary Highlight Color"]

    @staticmethod
    def fspe():
        return store.getData()["settings"]["preferences"]["Font Size of Primary Emphasis"]

    @staticmethod
    def fsnt():
        return store.getData()["settings"]["preferences"]["Font Size of Normal Text"]

    @staticmethod
    def fsmt():
        return store.getData()["settings"]["preferences"]["Font Size of Minimized Text"]

    @staticmethod
    def pes():
        return store.getData()["settings"]["preferences"]["Primary Emphasis Settings"]

    @staticmethod
    def ses():
        return store.getData()["settings"]["preferences"]["Secondary Emphasis Settings"]

    @staticmethod
    def tes():
        return store.getData()["settings"]["preferences"]["Tertiary Emphasis Settings"]

store.init()