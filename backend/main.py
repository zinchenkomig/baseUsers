import os

from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from components.authentication.crud import get_user
from components.authentication.dependencies import CurrentUserDep
from components.authentication.router import auth_router
from components.superuser.router import superuser_router
from components.user.router import user_router

from dependencies import AsyncSessionDep

app = FastAPI(title='BaseUsers', version='0.1.1')


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get('BASE_USERS_FRONTEND_URL')],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=auth_router,
                   prefix='/auth',
                   tags=['auth']
                   )

app.include_router(router=superuser_router,
                   prefix='/superuser',
                   tags=['superuser'])

app.include_router(router=user_router,
                   prefix='/user',
                   tags=['user'])


@app.get('/email')
async def get_email(user: CurrentUserDep):
    return user.email


@app.get('/check/username')
async def check_username(username: str, async_session: AsyncSessionDep):
    user = await get_user(async_session, username=username)
    return user is not None
