from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.conf.secrets import db_address, db_user, db_password, db_name


def get_connection_string(address, user, password, db_name) -> str:
    return f'postgresql+asyncpg://{user}:{password}@{address}/{db_name}'


def get_sync_connection_string(address, user, password, db_name) -> str:
    return f'postgresql://{user}:{password}@{address}/{db_name}'


async_engine = create_async_engine(get_connection_string(db_address, db_user, db_password, db_name))
AsyncMainSession = async_sessionmaker(async_engine)

# In case of sync testing
sync_engine = create_engine(get_sync_connection_string(db_address, db_user, db_password, db_name))
SyncMainSession = sessionmaker(sync_engine)
