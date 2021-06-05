"""
    - Function to allow resources to be accessed when the project is compiled
"""

import sys
import os

class PATH:

    @staticmethod
    def get(relative_path):

        """
        returns path for included files
        (used when packaged into a binary)
        """

        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)