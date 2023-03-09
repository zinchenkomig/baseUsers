from sqlalchemy import select
from backend.db_models import User


async def get_user(async_session, username):
    user_query_exec = await async_session.execute(select(User).filter_by(username=username))
    user = user_query_exec.scalars().one_or_none()
    return user


async def check_is_user_exists(async_session, user_create):
    user_query_exec = await async_session.execute(select(User)
                                                  .filter((User.username == user_create.username)
                                                          | (User.email == user_create.email)))
    user = user_query_exec.scalars().first()
    return user is not None
