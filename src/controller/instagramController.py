
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus

from model import BodyResponse
from service import Instagram
class InstagramController:
    def __init__(self) -> None:
        self.router = APIRouter()

        self.router.get('/search')()
        ...

    def search(self, username: str) -> JSONResponse[BodyResponse]:
        instagram = Instagram()
        try:
            response: dict | int = instagram.main(username)

            if isinstance(response, int):
                return JSONResponse(content=BodyResponse(response, ))

        except Exception as err:
            return JSONResponse(content=BodyResponse(HTTPStatus.INTERNAL_SERVER_ERROR, str(err), None).__dict__, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
        ...