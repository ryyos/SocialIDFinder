import os
import json
import requests

from icecream import ic
from requests import Response
from typing import Dict
from dotenv import load_dotenv

from src.component.twiterComponent import TwiterComponent

class Twiter(TwiterComponent):
    def __init__(self) -> None:
        super().__init__()
        ...

    def build_header(self, username: str) -> Dict[str, any]:
        self.headers.update({
            "referer": self.base_url+username
        })

        return self.headers
        ...
    
    def build_param(self, usernmae: str) -> Dict[str, any]:
        self.params.update({
            "variables": json.dumps({
                "screen_name": usernmae.lower(),
                "withSafetyModeUserFields": True
            })
        })

        return self.params
        ...

    def build_response(self, data: dict) -> Dict[str, any]:
        data: dict = data["data"]["user"]["result"]

        return {
            "id": data["rest_id"],
            "username": data["legacy"]["screen_name"]
        }
        ...

    def main(self, username: str) -> Dict[str, any]:
        username: str = username if self.base_url not in username else username.replace(self.base_url, '')
        response: Response = requests.get(
            url='https://twitter.com/i/api/graphql/k5XapwcSikNsEsILW5FvgA/UserByScreenName',
            headers=self.build_header(username),
            params=self.build_param(username),
            cookies=self.cookies
        )

        if response.status_code == 200:
            return self.build_response(response.json())
        else:
            return response.status_code
        ...

    