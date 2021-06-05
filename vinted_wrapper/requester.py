import json
import requests
from requests.exceptions import HTTPError


class Requester:
    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'sec-fetch-dest': 'none',
            'accept': '*/*',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'accept-language': 'en-US'
        }

        self.session = requests.Session()

    def get(self, url, params=None):
        """
        Perform a http get request.

        :param url: str
        :param params: dict, optional

        :return: dict
            Json format
        """
        response = self.session.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise HTTPError
        if not response.content:
            return None
        data = json.loads(response.content)
        return data

    def set_cookie(self, url):
        """
        Perform a http get request for setting up an initial cookie. Required for Vinted.

        :param url: str
        :return: None
        """
        self.session.get(url)


requester = Requester()
