from datetime import datetime

from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str
    region: str
    start_parsing: bool = False

class StatistcickRequest(BaseModel):
    id: int
    start_datetime: datetime
    end_datetime: datetime

class StaticResponce(BaseModel):
    quantity: int
    timestamp: datetime
