import os
import requests

from icecream import ic
from requests import Response
from typing import Dict
from dotenv import load_dotenv


class Linkedin:
    def __init__(self) -> None:
        load_dotenv()

        self.api: str = os.getenv('API')+'/linkedin/search/account?limit=1&name='
        ...

    def build_response(self, data: dict) -> Dict[str, any]:
        data: dict = data["data"][0]

        return {
            "name": data["name"],
            "uid": data["urn_id"]
        }
        ...

    def build_name(self, name: str) -> str:
        name: str = name if 'https://www.linkedin.com/in/' not in name else name.replace('https://www.linkedin.com/in/', '')
        
        return '-'.join(name.split('-')[:-1])
        ...

    def main(self, name: str) -> Dict[str, any]:
        response: Response = requests.get(self.api+self.build_name(name))
        return self.build_response(response.json())
        ...

    