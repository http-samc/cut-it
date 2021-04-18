# https://pypi.org/project/richxerox/
# 95% sure this works

from richxerox import *

class clipboard():

    @staticmethod
    def add(text, html):
        """
        Injects both regular text (unformatted)
        and html ('rich' text) to clipboard
        """
        pasteboard.set_contents(text=text, html=html)