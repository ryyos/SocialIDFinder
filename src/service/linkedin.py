import re
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

    def build_name(self, username: str):
    
        pattern = r'/in/([\w-]+)(?:-\w+)/?$'
    
        match = re.search(pattern, username)
        
        if match:
            return match.group(1)
        
        else:
            return username
        ...

    def main(self, name: str) -> Dict[str, any]:
        ic(self.build_name(name))
        response: Response = requests.get(self.api+self.build_name(name))
        if response.status_code == 200:
            return self.build_response(response.json())
        else:
            return response.status_code
        ...

    