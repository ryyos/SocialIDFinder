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


    def build_reponse(self, data: dict) -> Dict[str, any]:
        return {
            "id": data["data"]["fb_id"]
        }
        ...

    def main(self, profile: str) -> Dict[str, int]:
        profile: str = profile if 'https://www.facebook.com/' not in profile else profile.replace('https://www.facebook.com/', '')
        
        self.param = {
            "url": "https://www.facebook.com/"+profile
        }

        response: Response = requests.get(self.api, params=self.param)
        if response.status_code == 200:
            return self.build_response(response.json())
        else:
            return response.status_code
        ...