from main import app
from httpx import AsyncClient
from fastapi.testclient import TestClient
import pytest
import os
import pytest
import os
from sqlalchemy_utils import drop_database, database_exists, create_database
from db_models import Base
from sqlalchemy import create_engine
from utils.db_connection import get_sync_connection_string, get_connection_string
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import dependencies


@pytest.mark.anyio
async def test_auth(async_client):
    test_username = 'new_test_user'
    test_password = 'test_password'
    test_email = 'testemail@email.com'
    register_response = await async_client.post('/auth/register', json={'username': test_username,
                                                                        'password': test_password,
                                                                        'email': test_email})
    assert register_response.status_code == 201

    login_response = await async_client.post('/auth/token', data={'username': test_username, 'password': test_password})
    assert login_response.status_code == 200

    response_user_data = await async_client.get('/email', cookies=login_response.cookies)
    assert response_user_data.status_code == 200, response_user_data.text
    assert response_user_data.json() == test_email


