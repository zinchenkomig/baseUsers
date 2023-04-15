from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from authentication.crud import get_user
from authentication.dependencies import get_current_user
from authentication.router import auth_router
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


@app.get('/email')
async def get_email(user=Depends(get_current_user)):
    return user.email


@app.get('/check/username')
async def check_username(username: str, async_session: AsyncSessionDep):
    user = await get_user(async_session, username=username)
    return user is not None
