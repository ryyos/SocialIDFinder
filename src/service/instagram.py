import os
import requests

from dotenv import load_dotenv
from typing import Dict
from fake_useragent import FakeUserAgent
from icecream import ic

class Instagram:
    def __init__(self) -> None:
        load_dotenv()

        self.__COOKIES = os.getenv('COOKIES')
        self.__IG_CLAIM = os.getenv('IG_CLAIM')

        self.api = 'https://www.instagram.com/web/search/topsearch/?query='
        ...

    def __build_header(self, username: str) -> dict:

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': self.__COOKIES,
            'Dpr': '1',
            'Referer': f'https://www.instagram.com/{username}/',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Full-Version-List': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Google Chrome";v="120.0.6099.130"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Viewport-Width': '1920',
            'X-Asbd-Id': '129477',
            'X-Csrftoken': 'VqFUdHhunrwbNuPNn3UgjYlWYMPHrnwD',
            'X-Ig-App-Id': '936619743392459',
            'X-Ig-Www-Claim': self.__IG_CLAIM,
            'X-Requested-With': 'XMLHttpRequest'
        }

        return headers
        ...

    def build_response(self, data: dict) -> Dict[str, any]:
        data: dict = data['users'][0]

        return {
            "id": data['user']['pk_id'],
            "username": data["user"]["username"]
        }
        ...

    def build_username(username: str) -> str:
        return username if 'https://www.instagram.com/' not in username else \
            username.replace('https://www.instagram.com/', '').replace('/', '')
        ...

    def main(self, username: str) -> Dict[str, int]:
        username: str = self.build_username(username)
        response = requests.get(self.api+username, headers=self.__build_header(username))
        
        if response.status_code == 200:
            return self.build_response(response.json())
        else:
            return response.status_code
        ...