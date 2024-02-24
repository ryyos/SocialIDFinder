import os
import requests

from icecream import ic
from requests import Response
from typing import Dict
from ..component import API


class Youtube:
    def __init__(self) -> None:

        self.api: str = API+'/youtube/web/account/search?channel_name='
        ...

    def build_chanel(self, chanel: str) -> str:
        return chanel if 'https://www.youtube.com/' not in chanel else chanel.replace('https://www.youtube.com/', '')
        ...

    def build_response(self, data: dict) -> Dict[str, any]:
        data: dict = data["data"][0]

        return {
            "id": data["channelId"],
            "chanel": data["title"]["simpleText"]
        }
        ...
    def main(self, chanel: str) -> Dict[str, any]:
        response: Response = requests.get(self.api+self.build_chanel(chanel))

        if response.status_code == 200:
            return self.build_response(response.json())
        else:
            return response.status_code
        ...

    