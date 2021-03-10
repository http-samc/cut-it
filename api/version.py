import requests

class check:
    
    @staticmethod
    def support(version):

        data = {
            "version" : version,
        }

        r = requests.post("https://api.flare-software.live/otr/cut-it/version", data=data)
        r = int(str(r).replace('<Response [', '').replace(']>', ''))

        if r == 200:
            return True

        else:
            return False