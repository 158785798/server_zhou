from sqlalchemy import create_engine
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'mysql+aiomysql://root:mysql@localhost/zhou?charset=utf8mb4'



async_engine = create_async_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=1500)

async_session = sessionmaker(async_engine, class_=AsyncSession)
async def a():
    async with async_session() as session:
        res = await session.execute('select * from users')
        print(res.fetchall())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(a())