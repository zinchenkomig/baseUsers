from datetime import timedelta
from typing import Union

from fastapi import APIRouter, Response, Depends, HTTPException, status
# Used here just for swagger integrated login
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from backend.db_models import User
from backend.dependencies import get_async_session
from backend.json_schemes import UserCreate, UserRead

from .crud import get_user, check_is_user_exists
from .security import verify_password, get_password_hash, create_access_token
from conf.consts import ACCESS_TOKEN_EXPIRE_MINUTES, IS_SECURE_COOKIE


auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def authenticate_user(async_session, username: str, password: str) -> Union[User, bool]:
    user = await get_user(async_session, username)
    if user is None:
        return False
    if not verify_password(password, user.password):
        return False
    return user


@auth_router.post("/token", response_model=UserRead)
async def login_for_access_token(response: Response,
                                 async_session=Depends(get_async_session),
                                 form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(async_session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response.set_cookie(key='login_token', value=access_token,
                        samesite='none',
                        secure=IS_SECURE_COOKIE,
                        httponly=True
                        )

    return user


@auth_router.post('/logout')
async def logout(response: Response,
                 ):
    """
    Removes JWT token from http_only cookie
    :param response:
    :return:
    """
    response.set_cookie('login_token', value='', httponly=True, samesite='lax', secure=True)


@auth_router.post('/register')
async def register(user_create: UserCreate, response: Response,
                   async_session=Depends(get_async_session)):
    """
    Registers a user
    :param response:
    :param user_create:
    :param async_session:
    :return:
    """
    if await check_is_user_exists(async_session, user_create):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    else:
        hashed_pass = get_password_hash(user_create.password)
        user = User(username=user_create.username,
                    email=user_create.email,
                    password=hashed_pass,
                    is_active=True)
        async_session.add(user)
        await async_session.commit()
        response.status_code = status.HTTP_201_CREATED

