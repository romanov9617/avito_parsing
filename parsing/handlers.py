from aiohttp import ClientResponse, ClientSession
import asyncio
import random

from parsing.parser import parse_responce
from db.db_endpoints import get_all_queries, push_counts_to_db
from config import settings


async def get_response(id: int, query: str, region: str):
    async with ClientSession() as session:
        await asyncio.sleep(random.randint(1, 10))
        url = f'https://api.scraperapi.com?api_key={settings.API_TOKEN}&autoparse=true&url=https://www.avito.ru/{region}?q={query}'
        async with session.get(url) as request:
            response = await request.text()
            return id, parse_responce(response)

async def push_all_responses():
    while True:
        queries = await get_all_queries()
        tasks = []
        for query in queries:
            tasks.append(asyncio.create_task(get_response(query.id, query.q, query.region)))
        result = await asyncio.gather(*tasks)
        await push_counts_to_db(result)
        await asyncio.sleep(3600)


