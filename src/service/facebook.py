import os
import requests

from icecream import ic
from requests import Response
from typing import Dict
from dotenv import load_dotenv

class Facebook:
    def __init__(self) -> None:
        load_dotenv()

        self.api = os.getenv('API')+'/facebook/fb_id_finder'
        ...

    def main(self, profile: str) -> Dict[str, int]:

        self.param = {
            "url": "https://www.facebook.com/"+profile
        }

        response: Response = requests.get(self.api, params=self.param)
        ic(response)
        ic(response.json())
        ic(response.url)
        ...