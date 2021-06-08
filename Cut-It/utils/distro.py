"""
    - Contains set details that will change between verisons
"""

VERSION = "1.0"
TAGS = ["Enterprise", "Release", "Beta"]
TAG = TAGS[1]

def version():
    """
        Returns current software version
    """

    return VERSION

def tag():
    """
        Returns current software tag
    """

    return TAG