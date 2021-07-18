"""
    - Contains set details that will change between verisons
"""

VERSION = "1.0"
TAGS = ["ISD", "Enterprise for ISD®", "Release", "Beta"]
TAG_DISPLAY = TAGS[2] # 1 for ISD
TAG = TAGS[2] # 0 for ISD

URL = "https://api.github.com/repos/http-samc/cut-it/releases"

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

def tagDisplay():
    """
        Returns display name of tag
    """

    return TAG_DISPLAY

def releases():
    """
        Returns GitHub API Releases URL
    """

    return URL