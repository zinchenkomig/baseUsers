from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from routers.authentication.crud import get_user
from routers.authentication.dependencies import get_current_user
from routers.authentication.router import auth_router
from routers.superuser.router import superuser_router

from dependencies import AsyncSessionDep

app = FastAPI(title='BaseUsers', version='0.1.1')


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
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


@app.get('/email')
async def get_email(user=Depends(get_current_user)):
    return user.email


@app.get('/check/username')
async def check_username(username: str, async_session: AsyncSessionDep):
    user = await get_user(async_session, username=username)
    return user is not None
