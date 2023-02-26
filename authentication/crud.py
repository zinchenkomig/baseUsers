from sqlalchemy import select
from db_models import User


async def get_user(async_session, username):
    user_query_exec = await async_session.execute(select(User).filter_by(username=username))
    user = user_query_exec.scalars().one_or_none()
    return user
