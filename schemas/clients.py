from pydantic import BaseModel
from fastapi import Query


class Client(BaseModel):
    id: int
    name: str
    surname: str
    address: str
    phone: str = Query(min_length=12, max_length=12)
