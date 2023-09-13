from aiohttp import ClientSession
from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete


from database.models import User, Favorite
from database.connection import async_session

class UserService:
    async def create_user(name: str):
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()

    async def delete_user(user_id: int):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id==user_id))
            await session.commit()

    async def list_user():
        async with async_session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()

    async def get_by_id(user_id: int):
            async with async_session() as session:
                result = await session.execute(select(User).where(User.id==user_id))
                return result.scalar()

class FavoriteService:
    async def add_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            session.add(Favorite(user_id=user_id, symbol=symbol))
            await session.commit()

    async def remove_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            await session.execute(delete(Favorite).where(Favorite.user_id==user_id, Favorite.symbol==symbol))
            await session.commit()

class AssetService:
    async def day_summary(symbol: str):
        async with ClientSession() as session:

            url = f'https://api.mercadobitcoin.net/api/v4/{symbol}/fees'
            response = await session.get(url=url)
            data = await response.json()
            print(data['deposit_minimum'])
            
            return {
                'symbol': symbol,
                'deposit_minimum': data['deposit_minimum'],
                'withdraw_minimum': data['withdraw_minimum'],
                'withdrawal_fee': data['withdrawal_fee']
            }