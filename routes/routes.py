from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import RedirectResponse

from models.models import SearchRequest, StatistcickRequest, StaticResponce
from db.db_endpoints import push_pair_to_db, get_stat
from parsing.handlers import push_all_responses


router = APIRouter(
    prefix="/main",
    tags=["main"],
)

@router.get('/')
async def index():
    return RedirectResponse('/docs')

@router.post("/add")
async def add(request: SearchRequest, background_tasks: BackgroundTasks):
    id = await push_pair_to_db(request)
    if request.start_parsing:
        background_tasks.add_task(push_all_responses)
    return {
        'id': id
    }

@router.get('/stat')
async def get(request: StatistcickRequest):
    rows = await get_stat(request.id, request.start_datetime, request.end_datetime)
    stats = [StaticResponce(quantity=row.quantity, timestamp=row.created_at) for row in rows]
    return {"id": request.id,
            "stat": stats
        }