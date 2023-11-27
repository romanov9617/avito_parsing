import os, sys
import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

sys.path.insert(1, os.path.join(sys.path[0], 'app'))

from db.db_initiate import init_db
from routes.routes import router


app = FastAPI(
    title="AvitoParsingAPI",
)

app.include_router(router)

loop = asyncio.get_event_loop()
loop.create_task(init_db())


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
