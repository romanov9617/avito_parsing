from datetime import datetime
from sqlalchemy import insert, select
from sqlalchemy.orm import selectinload


from app.db.db_base import engine, async_session_factory
from app.db.db_schemas import PairsORM, CountsORM
from app.models.models import SearchRequest, StatistcickRequest
from app.config import settings


async def push_pair_to_db(request: SearchRequest):
    async with engine.begin() as conn:
        query = insert(PairsORM).values(
            q=request.query,
            region=request.region
        )
        query_id = await conn.execute(query)
        return query_id.inserted_primary_key[0]


async def get_all_queries():
    async with async_session_factory() as session:
        query = select(PairsORM).options(
            selectinload(PairsORM.counters)
        )
        result = await session.execute(query)
        return result.scalars().all()


async def push_counts_to_db(counters: list[tuple[int, int]]):
    async with async_session_factory() as session:
        queries = []
        for counter in counters:
            pair_id, quantity = counter
            res = CountsORM(pair_id=pair_id, quantity=quantity)
            queries.append(res)
        session.add_all(queries)
        await session.commit()


async def get_stat(id: int, start_datetime: datetime, end_datetime: datetime):
    async with async_session_factory() as session:
        query = select(CountsORM).where(
            CountsORM.pair_id == id,
            CountsORM.created_at >= start_datetime,
            CountsORM.created_at <= end_datetime
        )
        result = await session.execute(query)
        return result.scalars().all()
