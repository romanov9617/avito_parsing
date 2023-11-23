from fastapi import FastAPI, BackgroundTasks
import asyncio

from app.db.db_initiate import init_db
from app.models.models import SearchRequest, StatistcickRequest, StaticResponce
from app.db.db_endpoints import push_pair_to_db, get_stat
from app.parsing.handlers import push_all_responses

app = FastAPI(
    title="AvitoParsingAPI",
)

loop = asyncio.get_event_loop()
loop.create_task(init_db())


flag = False

@app.post("/add")
async def add(request: SearchRequest):
    global flag
    id = await push_pair_to_db(request)
    print(flag)
    if not flag:
        loop.create_task(push_all_responses())
        print('Задача создана')
        flag = True
    return {
        'id': id
    }


@app.get('/stat')
async def get(request: StatistcickRequest):
    rows = await get_stat(request.id, request.start_datetime, request.end_datetime)
    stats = [StaticResponce(quantity=row.quantity, timestamp=row.created_at) for row in rows]
    return {"id": request.id,
            "stat": stats
        }