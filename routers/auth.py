from fastapi import APIRouter, Request, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from dependencies import get_async_session

auth_router = APIRouter()


@auth_router.post('/login')
async def login(request: Request,
                response: Response,
                credentials: OAuth2PasswordRequestForm = Depends(),
                async_session=Depends(get_async_session)
                ):
    """
    Returns JWT token in http_only cookie
    :param async_session:
    :param request:
    :param response:
    :param credentials:
    :return:
    """
    pass


@auth_router.post('/logout')
async def logout(request: Request,
                 response: Response,
                 async_session=Depends(get_async_session)
                 ):
    """
    Removes JWT token from http_only cookie
    :param async_session:
    :param request:
    :param response:
    :return:
    """
    pass


@auth_router.post('/register')
async def register(async_session=Depends(get_async_session)):
    """
    Registers a user
    :param async_session:
    :return:
    """
    pass
