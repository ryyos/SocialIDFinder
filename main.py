import uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.controller import controller

app: FastAPI = FastAPI(title='Social-ID-Finder', version='v0.0.1', description='Find User ID from Sosail Media', docs_url='/')

app.include_router(router=controller.router, prefix='/finder', tags=['Search User ID'])

if __name__ == '__main__':
    uvicorn.run(app, port=7373)
