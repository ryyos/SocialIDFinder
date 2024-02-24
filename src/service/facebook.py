import os
import requests

from icecream import ic
from requests import Response
from typing import Dict
from dekimashita import Dekimashita

from ..component.facebookComponent import FacebookComponent
from ..component import API

class Facebook(FacebookComponent):
    def __init__(self) -> None:
        super().__init__()
        ...


    def build_response(self, response: Response) -> Dict[str, any]:

        raw_id: str = response.text.split('userID')[1].split(',')[0]

        return {
            "id": int(Dekimashita.vnum(raw_id))
        }
        ...

    def main(self, profile: str) -> Dict[str, int]:
        profile: str = profile if self.base_url not in profile else profile.replace(self.base_url, '')

        response: Response = requests.get(self.base_url+profile, cookies=self.cookies, headers=self.headers)

        if response.status_code == 200:
            return self.build_response(response)
        else:
            return response.status_code
        ...