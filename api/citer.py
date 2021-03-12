import requests
import json

class cite:
    """
    create MLA citations with ease!
    """

    def __init__(self, URL):
        """
        @PARAM: URL (str) - the URL for your citation
        @Description: creates citation
        """

        self.data = {"url" : str(URL)}
        self.BASE = "https://formatically.com/api/website"
        self.response = None

        self.cite()

    def cite(self):
        """
        @Description: gets raw citation data from API
        """
        r = requests.post(url = self.BASE, data = self.data)
        self.response = dict(json.loads(r.text))
        self.format()

    def format(self):
        """
        @Description: formats raw citation date
        """

        self.firstName = self.response["creators"][0]["firstName"]
        self.lastName = self.response["creators"][0]["lastName"]
        self.title = self.response["title"]
        self.date = self.response["date"]
        self.date = self.date.replace('-', '/')
        self.date = self.date.split('/')
        self.date = self.date[1] + "/" + self.date[2] + "/" + self.date[0]

        #Getting last 2 digits of publication year
        self.split_date = self.date.split('/')
        self.year = None
        for _ in self.split_date:
            if len(_) == 4:
                self.year = _[2:4]
        if self.year == None:
            self.year = self.split_date[2]

        self.accessed = self.response["accessDate"]
        self.accessed = self.accessed.split('/')
        self.accessed = self.accessed[1] + "/" + self.accessed[0] + "/" + self.accessed[2]
        self.publication = self.response["websiteTitle"]
        self.url = self.response["url"]

    def debate(self):
        """
        @Description: Returns a simplified debate-ready citation
        """

        data = [self.lastName, self.year, self.publication, self.url]
        return data
    
    def mla(self):
        """
        @Description: Returns an MLA 8 citation
        """

        return f'{self.lastName}, {self.firstName}. "{self.title}" {self.publication}, {self.date}, {self.url}. Accessed {self.accessed}.'