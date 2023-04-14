from utils.db_connection import AsyncMainSession, SyncMainSession


async def get_async_session():
    async_session = AsyncMainSession()
    try:
        yield async_session
    finally:
        await async_session.close()


# In case of sync testing
def get_sync_session():
    session = SyncMainSession()
    try:
        yield session
    finally:
        session.close()
