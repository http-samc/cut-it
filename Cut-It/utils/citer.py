import requests
import json

"""
    - Utility to generate citations based off QuickCite (Chitgopekar '21)
"""

class cite:

    def __init__(self, URL):
        """
            :param: URL (str) - the URL for your citation
            :desc: creates citation
        """

        self.data = {"url" : str(URL)}
        self.BASE = "https://formatically.com/api/website"
        self.response = None

        self.cite()

    def cite(self):
        """
            gets raw citation data from API
        """
        r = requests.post(url = self.BASE, data = self.data)
        self.response = dict(json.loads(r.text))
        self.format()

    def format(self):
        """
            formats raw citation date
        """

        self.firstName = self.response["creators"][0]["firstName"]
        self.lastName = self.response["creators"][0]["lastName"]
        self.title = self.response["title"]
        self.date = self.response["date"]

        if self.date is not None:
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

        else:
            self.date = ""
            self.year = ""
            self.accessed = ""

        self.publication = self.response["websiteTitle"]
        self.url = self.response["url"]

    def getMissingAttrs(self) -> list:
        """
            Returns a list of missing attributes (key) or None (if all present)
        """

        excludedData = ['abstractNote', 'websiteTitle', 'websiteType', 'shortTitle', 'language', 'rights', 'extra', 'tags', 'collections']
        retList = []

        for key in list(self.response.keys()):

            if key in excludedData:
                continue

            element = self.response[key]

            if isinstance(element, list) and len(element) == 0:
                retList.append(key)

            elif (element is None) or (element == ''):
                retList.append(key)

        if len(retList) == 0:
            return None

        return retList

    def debate(self):
        """
            Returns a simplified debate-ready citation
        """

        data = [self.lastName, self.year, self.publication, self.url]
        return data

    def mla(self):
        """
            Returns an MLA 8 citation
        """

        return f'{self.lastName}, {self.firstName}. "{self.title}" {self.publication}, {self.date}, {self.url}. Accessed {self.accessed}.'