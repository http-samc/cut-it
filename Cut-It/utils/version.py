import requests

class check:
    
    @staticmethod
    def support(version):

        data = {
            "version" : version,
        }

        r = requests.post("https://api.flare-software.live/otr/cut-it/version", data=data)
        r = r.status_code

        if r == 200:
            return True

        else:
            return False