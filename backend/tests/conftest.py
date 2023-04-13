import pytest


# Is required for anyio to work properly
# https://anyio.readthedocs.io/en/stable/testing.html#specifying-the-backends-to-run-on
@pytest.fixture
def anyio_backend():
    return 'asyncio'
