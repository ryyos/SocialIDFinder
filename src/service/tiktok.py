import os
import requests

from icecream import ic
from requests import Response
from typing import Dict
from ..component import API
class Tiktok:
    def __init__(self) -> None:

        self.api = API+'/tiktok/api/account/search?fullname='
        ...

    def build_response(self, data: dict) -> Dict[str, any]:
        data: dict = data["data"][0]["user_info"]

        return {
            "username": data.get("unique_id", None),
            "uid": data.get("uid", None)
        }
        ...

    def main(self, username: str) -> Dict[str, any]:
        username: str = username if 'https://www.tiktok.com/' not in username else username.replace('https://www.tiktok.com/', '')
        response: Response = requests.get(self.api+username)

        if response.status_code == 200:
            return self.build_response(response.json())
        else:
            return response.status_code
        ...