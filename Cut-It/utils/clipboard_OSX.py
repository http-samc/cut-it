"""
    Utility to inject rich text into the clipboard (MacOS only)
"""

from richxerox import *

class clipboard():

    @staticmethod
    def add(text, html):
        
        """
        Injects both regular text (unformatted)
        and html ('rich' text) to clipboard
        """

        pasteboard.set_contents(text=text, html=html)