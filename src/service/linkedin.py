import re
import os
import requests

from icecream import ic
from requests import Response
from typing import Dict
from ..component import API

class Linkedin:
    def __init__(self) -> None:
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
        response: Response = requests.get(API+self.build_name(name))
        if response.status_code == 200:
            return self.build_response(response.json())
        else:
            return response.status_code
        ...

    