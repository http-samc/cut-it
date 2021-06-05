"""
    - Contains a handy dataclass to reference Cards
"""

from dataclasses import dataclass, asdict

@dataclass
class Card:
    TAG: str
    CITE: str
    CREDS: str
    URL: str
    HTML: str
    TEXT: str

    def isCard(self) -> bool:
        """
            Returns (bool) if the card actually has data
        """

        if ((self.TAG.replace(' ','') != "") or 
            (self.CITE.replace(' ','') != "") or 
            (self.CREDS.replace(' ','') != "") or 
            (self.URL.replace(' ','') != "") or
            (self.TEXT.replace(' ','') != "")):
            return True
        else:
            return False

    def getDict(self) -> dict:
        """
            Returns (dict) representation of the object
        """

        return asdict(self)