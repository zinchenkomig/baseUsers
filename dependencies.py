from utils.db_connection import AsyncMainSession


async def get_async_session():
    async_session = AsyncMainSession()
    try:
        yield async_session
    finally:
        await async_session.close()
