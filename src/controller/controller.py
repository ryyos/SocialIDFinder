from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus

from ..model import BodyResponse
from ..enums import Sosmed
from ..service import *
from ..component import codes

class Controller:
    def __init__(self) -> None:
        self.router = APIRouter()

        self.router.get('/search')(self.__search)
        ...

    def __search(self, sosmed: Sosmed, username: str) -> JSONResponse:
        
        match sosmed:
            case Sosmed.INSTAGRAM:
                medsos = Instagram()
                ...

            case Sosmed.TWITTER:
                medsos = Twiter()
                ...

            case Sosmed.TIKTOK:
                medsos = Tiktok()
                ...

            case Sosmed.YOUTUBE:
                medsos = Youtube()
                ...

            case Sosmed.FACEBOOK:
                medsos = Facebook()
                ...

            case Sosmed.LINKEDIN:
                medsos = Linkedin()

        try:
            response: dict | int = medsos.main(username)

            if isinstance(response, int):
                return JSONResponse(content=BodyResponse(response, codes.get(str(response)), None).__dict__, status_code=response)

            return JSONResponse(content=BodyResponse(HTTPStatus.OK, 'id found', response).__dict__, status_code=HTTPStatus.OK)

        except Exception as err:
            return JSONResponse(content=BodyResponse(HTTPStatus.INTERNAL_SERVER_ERROR, str(err), None).__dict__, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
        ...