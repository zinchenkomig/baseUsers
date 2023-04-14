from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyCookie
from jose import jwt, JWTError

from conf.consts import ALGORITHM
from conf.secrets import PASSWORD_ENCODING_SECRET
from dependencies import get_async_session
from .crud import get_user

apikey_cookie_getter = APIKeyCookie(name='login_token')


async def get_current_user(token=Depends(apikey_cookie_getter), async_session=Depends(get_async_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, PASSWORD_ENCODING_SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(async_session, username=username)
    if user is None:
        raise credentials_exception
    return user
