from sqlalchemy import select
from backend.db_models import User
from typing import Optional


async def get_user(async_session, username) -> Optional[User]:
    user_query_exec = await async_session.execute(select(User).filter_by(username=username).limit(1))
    user = user_query_exec.scalars().one_or_none()
    return user


async def check_is_user_exists(async_session, user_create):
    user_query_exec = await async_session.execute(select(User)
                                                  .filter((User.username == user_create.username)
                                                          | (User.email == user_create.email)).limit(1))
    user = user_query_exec.scalars().first()
    return user is not None
