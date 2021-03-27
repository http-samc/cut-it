"""
returns type-appropriate values for each settings (shortcuts & preferences) in data.json
"""

from api.data import store

class Settings:
    def __init__(self) -> None:
        self.data = store.getData()
    
    """
    Preferences Getters
    """

    def font(self):
        """
        Returns Font
        """
        return self.data["settings"]["preferences"]["Font"]

    def PHC(self):
        """
        Returns primary highlight color
        """
        return self.data["settings"]["preferences"]["Primary Highlight Color"]
    
    def SHC(self):
        """
        Returns secondary highlight color
        """
        return self.data["settings"]["preferences"]["Secondary Highlight Color"]

    def FSPE(self):
        """
        Returns font size of primary emphasis
        """
        return int(self.data["settings"]["preferences"]["Font Size of Primary Emphasis"])

    def FSNT(self):
        """
        Returns font size of normal text
        """
        return int(self.data["settings"]["preferences"]["Font Size of Normal Text"])

    def FSMT(self):
        """
        Returns font size of minimized text
        """
        return int(self.data["settings"]["preferences"]["Font Size of Minimized Text"])

    def PES(self):
        """
        Returns Primary Emphasis Settings [Italic, Bold, Underline, Highlight] (bools)
        """
        settings =  self.data["settings"]["preferences"]["Primary Emphasis Settings"]
        
        i = True if "Italicized" in settings else False
        b = True if "Bold" in settings else False
        u =  True if "Underline" in settings else False
        h = True if "Highlight" in settings else False

        return [i, b, u, h]

    def SES(self):
        """
        Returns Secondary Emphasis Settings [Italic, Bold, Underline, Highlight] (bools)
        """

        settings =  self.data["settings"]["preferences"]["Secondary Emphasis Settings"]
        
        i = True if "Italicized" in settings else False
        b = True if "Bold" in settings else False
        u =  True if "Underline" in settings else False
        h = True if "Highlight" in settings else False

        return [i, b, u, h]

    def TES(self):
        """
        Returns Tertiary Emphasis Settings [Italic, Bold, Underline, Highlight] (bools)
        """

        settings =  self.data["settings"]["preferences"]["Tertiary Emphasis Settings"]
        
        i = True if "Italicized" in settings else False
        b = True if "Bold" in settings else False
        u =  True if "Underline" in settings else False
        h = True if "Highlight" in settings else False

        return [i, b, u, h]

    """
    Shortcuts getters
    """

    def PE(self):
        """
        Shortcut for Primary Emphasis
        """

        return self.data["settings"]["shortcuts"]["Cut-It (Primary Emphasis)"]

    def SE(self):
        """
        Shortcut for Secondary Emphasis
        """

        return self.data["settings"]["shortcuts"]["Cut-It (Secondary Emphasis)"]

    def TE(self):
        """
        Shortcut for Tertiary Emphasis
        """

        return self.data["settings"]["shortcuts"]["Cut-It (Tertiary Emphasis)"]

    def MT(self):
        """
        Shortcut for Minimizing Text
        """

        return self.data["settings"]["shortcuts"]["Minimize Text"]

    def AP(self):
        """
        Shortcut for AutoPoll
        """

        return self.data["settings"]["shortcuts"]["AutoPoll"]

    def AC(self):
        """
        Shortcut for AutoCite
        """

        return self.data["settings"]["shortcuts"]["AutoCite"]

    def AP_AC(self):
        """
        Shortcut for AutoPoll + AutoCite
        """

        return self.data["settings"]["shortcuts"]["AutoPoll + AutoCite"]

    def PDF(self):
        """
        Shortcut for Saving as PDF
        """

        return self.data["settings"]["shortcuts"]["Save As PDF"]

    def IP(self):
        """
        Shortcut for Saving Card In Progress
        """

        return self.data["settings"]["shortcuts"]["Save Card In Progress"]

    def OS(self):
        """
        Shortcut for Opening Settings
        """

        return self.data["settings"]["shortcuts"]["Open Settings"]

    def CW(self):
        """
        Shortcut for Closing Window
        """

        return self.data["settings"]["shortcuts"]["Close Window"]

    """
    Misc getters
    """

    def WS(self):
        """
        Returns (bool) fixed win size
        """
        return self.data["fixed_win"]
    
    def LI(self):
        """
        Returns (bool) stay logged in
        """
        return self.data["stay_logged_in"]