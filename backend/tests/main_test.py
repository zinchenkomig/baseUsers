import pytest


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


