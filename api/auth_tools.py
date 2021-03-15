import requests

class tools:

    @staticmethod
    def sign_up(email, password):

        data = {
            "email" : email,
            "pass" : password,
        }

        r = requests.post('http://api.flare-software.live/otr/cut-it/create', data=data)

        if r.status_code == 201:
            return True
        
        # TODO add different responses for email already registered vs bad password

        else:
            return False 

    @staticmethod
    def log_in(email, password):
        
        data = {
            "email" : email,
            "pass" : password,
        }

        r = requests.post('http://api.flare-software.live/otr/cut-it/auth', data=data)

        if r.status_code == 202:
            r = requests.get(f'http://api.flare-software.live/otr/cut-it/status%{email}%{password}')

            if r.status_code == 202:
                data = {
                    "email" : email,
                    "pass" : password,
                    "active" : True,
                }

                r = requests.post('http://api.flare-software.live/otr/cut-it/status', data=data)

                if r.status_code == 200:
                    return True

                else:
                    return False

            else:
                return False
    
        else:
            return False 

    @staticmethod
    def log_out(email, password):
        
        data = {
            "email" : email,
            "pass" : password,
        }

        r = requests.post('http://api.flare-software.live/otr/cut-it/auth', data=data)

        if r.status_code == 202:
            r = requests.get(f'http://api.flare-software.live/otr/cut-it/status%{email}%{password}')

            if r.status_code == 201:
                data = {
                    "email" : email,
                    "pass" : password,
                    "active" : False,
                }

                r = requests.post('http://api.flare-software.live/otr/cut-it/status', data=data)

                if r.status_code == 200:
                    return True

                else:
                    return False

            else:
                return False
    
        else:
            return False 