"""
    - Utility to inject rich text into the clipboard (Windows only)
"""

import klembord

class clipboard():

    @staticmethod
    def add(text, html):

        """
        Injects both regular text (unformatted)
        and html ('rich' text) to clipboard
        """

        klembord.init()
        klembord.set_with_rich_text(text, html)