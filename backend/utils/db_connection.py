from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from backend.conf.secrets import db_address, db_user, db_password, db_name


def get_connection_string(address, user, password, db_name):
    return f'postgresql+asyncpg://{user}:{password}@{address}/{db_name}'


async_engine = create_async_engine(get_connection_string(db_address, db_user, db_password, db_name))
AsyncMainSession = async_sessionmaker(async_engine)
