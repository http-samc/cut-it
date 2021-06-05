"""
    - Checks to see if more recent version (update) is available
"""

import requests
from utils.distro import version, tag

class check:
    
    @staticmethod
    def support(version):

        data = {
            "tag" : tag(),
            "version" : version(),
        }

        r = requests.post("TODO: update backend support", data=data)
        r = r.status_code

        if r == 200:
            return True

        else:
            return False