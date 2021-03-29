# https://pypi.org/project/richxerox/

# To Check OS Type
from sys import platform

# For Windows Clipboard
import klembord 

# For Mac Clipboard
#from richxerox import *

class clipboard():

    def __init__(self):
        """
        Sets the User OS
        """

        self.OS = None

        if platform == "linux" or platform == "linux2":
            self.OS = "LINUX"

        elif platform == "darwin":
            self.OS = "OSX"

        elif platform == "win32":
            self.OS = "WIN"
    
    def add(self, text, html):
        """
        Injects both regular text (unformatted)
        and html ('rich' text) to clipboard
        """

        if self.OS == "WIN": # This is working

            klembord.init()
            klembord.set_with_rich_text(text, html)
        
        elif self.OS == "OSX":
            # pasteboard.set_contents(text=text, html=html)
                #  Ideally avoid RTF and stick with text & html