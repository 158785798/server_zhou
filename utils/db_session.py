# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
#
# engine = create_async_engine(settings.DATABASE['URL'], pool_recycle=1500, echo=False)
# Session = sessionmaker(engine, class_=AsyncSession)
import aioredis
import peewee_async

from settings import DATABASE


class Redis():
    def __init__(self):
        self.pool = aioredis.ConnectionPool.from_url(
            "redis://localhost", encoding="utf-8", decode_responses=True
        )
        self.redis = aioredis.Redis(connection_pool=self.pool)

    async def set(self, key, value, ex=300):
        return await self.redis.set(key, value, ex)

    async def get(self, key):
        return await self.redis.get(key)

    async def close(self):
        await self.pool.disconnect()





db = peewee_async.PooledMySQLDatabase(
    host=DATABASE['HOST'],
    user=DATABASE['USER'],
    password=DATABASE['PASSWD'],
    database=DATABASE['NAME'],
    charset=DATABASE['CHARSET']
)

redis = Redis()
objects = peewee_async.Manager(db)
'$2b$12$3xM4QJKjQPObnRyVz29CxuezYyNbNRpbPbBFjXgEcoXAQm3TrVd8C'
