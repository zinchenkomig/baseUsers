from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from backend.authentication.router import auth_router
from backend.authentication.dependencies import get_current_user
from authentication.crud import get_user
from dependencies import get_async_session
from json_schemes import UserRead


app = FastAPI()


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


@app.get('/current_user', response_model=UserRead)
async def get_user(user=Depends(get_current_user)):
    return user


@app.get('/check/username')
async def check_username(username: str, async_session=Depends(get_async_session)):
    user = await get_user(async_session, username=username)
    return user is not None
