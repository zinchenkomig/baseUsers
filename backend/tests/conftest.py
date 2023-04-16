import pytest
import os

from httpx import AsyncClient
from sqlalchemy_utils import drop_database, database_exists, create_database

import dependencies
from db_models import Base
from sqlalchemy import create_engine

from main import app
from utils.db_connection import get_connection_string
from utils.db_connection_sync import get_sync_connection_string
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


# Is required for anyio to work properly
# https://anyio.readthedocs.io/en/stable/testing.html#specifying-the-backends-to-run-on
@pytest.fixture(scope='class')
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope='class')
async def async_client():
    db_address = 'localhost'
    db_user = os.getenv('TEST_DB_USER', 'testuser')
    db_password = os.getenv('TEST_DB_PASSWORD', '123')
    db_name = os.getenv('TEST_DB_NAME', 'test')
    async_engine = create_async_engine(get_connection_string(db_address, db_user, db_password, db_name))
    AsyncMainSession = async_sessionmaker(async_engine)

    async def _get_async_session():
        async_session = AsyncMainSession()
        try:
            yield async_session
        finally:
            await async_session.close()

    app.dependency_overrides[dependencies.get_async_session] = _get_async_session
    client = await AsyncClient(app=app, base_url='http://testenv').__aenter__()
    try:
        yield client
    finally:
        await client.__aexit__()


@pytest.fixture(scope='class')
def mocked_connection() -> str:
    db_address = 'localhost'
    db_user = os.getenv('TEST_DB_USER', 'testuser')
    db_password = os.getenv('TEST_DB_PASSWORD', '123')
    db_name = os.getenv('TEST_DB_NAME', 'test')
    db_connection_string = get_sync_connection_string(db_address, db_user, db_password, db_name)
    return db_connection_string


@pytest.fixture(autouse=True, scope='class')
def clear_db_before_usage(mocked_connection):
    db_connection_string = mocked_connection
    if database_exists(db_connection_string):
        drop_database(db_connection_string)
    create_database(db_connection_string)
    test_engine = create_engine(db_connection_string)
    Base.metadata.create_all(test_engine)
