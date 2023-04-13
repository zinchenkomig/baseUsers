from backend.main import app
from httpx import AsyncClient
import pytest


@pytest.mark.anyio
async def test_auth():
    async with AsyncClient(app=app, base_url='http://testenv') as client:
        response = await client.post("/auth/token", data={'username': 'new_user', 'password': '123456'})
        assert response.status_code == 200
        response_user_data = await client.get('/email', cookies=response.cookies)
        assert response_user_data.status_code == 200, response_user_data.text
        assert response_user_data.json() == 'mmm@mail.com'


