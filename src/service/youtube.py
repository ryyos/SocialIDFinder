import os
import requests

from icecream import ic
from requests import Response
from typing import Dict
from dotenv import load_dotenv


class Youtube:
    def __init__(self) -> None:
        load_dotenv()

        self.api: str = os.getenv('API')+'/youtube/web/account/search?channel_name='
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

        return self.build_response(response.json())
        ...

    