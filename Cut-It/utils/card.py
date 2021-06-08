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
    TEXT: str
    HTML: str

    def isCard(self) -> bool:
        """
            Returns (bool) if the card actually has data
        """

        if ((self.TAG.replace(' ','').replace('\n','').replace('\t','') != "") or 
            (self.CITE.replace(' ','').replace('\n','').replace('\t','') != "") or 
            (self.CREDS.replace(' ','').replace('\n','').replace('\t','') != "") or 
            (self.URL.replace(' ','').replace('\n','').replace('\t','') != "") or
            (self.TEXT.replace(' ','').replace('\n','').replace('\t','') != "")):
            return True
            
        else:
            return False

    def getDict(self) -> dict:
        """
            Returns (dict) representation of the object
        """

        return asdict(self)