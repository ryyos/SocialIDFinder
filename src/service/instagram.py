import requests

from typing import Dict
from fake_useragent import FakeUserAgent
from icecream import ic

from ..utils import Header

class Instagram:
    def __init__(self) -> None:

        self.api = 'https://www.instagram.com/web/search/topsearch/?query='
        ...

    def main(self, username: str) -> Dict[str, int]:
        ic(Header.ex())
        response = requests.get(self.api+username, headers=Header.ex())
        ic(response)
        ...