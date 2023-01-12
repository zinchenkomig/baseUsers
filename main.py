from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers.auth import auth_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # ToDo: Change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=auth_router,
                   prefix='/auth',
                   tags=['auth']
                   )
