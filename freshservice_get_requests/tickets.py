import os
import requests
from pprint import pprint


class FreshSerive:
    """
    This class handles all freshservice get requests. FreshService api doucmentation can be found here,
    https://api.freshservice.com/v2/#introduction

    """

    def __init__(self, url):
        self.url = url

    base_url = os.environ["FRESH_SERVICE_URL"]
    key = os.environ["FRESH_SERVICE_KEY"]
    password = os.environ["FRESH_SERVICE_PASSWORD"]

    def get_data(self):
        return requests.get(url=f'{self.base_url}{self.url}', auth=(self.key, self.password), headers={'Accept': 'application/json'})


def all_tickets() -> dict:
    """Get all tickets.

    :return: Dict that contains a list of all the tickets.
    """

    url = "/tickets"
    tickets = FreshSerive(url).get_data().json()

    return tickets





