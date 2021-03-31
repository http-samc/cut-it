# https://pypi.org/project/richxerox/

# To Check OS Type
from sys import platform

# For Windows Clipboard
import klembord 

# For Mac Clipboard
#from richxerox import *

class clipboard():

    @staticmethod
    
    def add(text, html):
        """
        Injects both regular text (unformatted)
        and html ('rich' text) to clipboard
        """
        klembord.init()
        klembord.set_with_rich_text(text, html)
