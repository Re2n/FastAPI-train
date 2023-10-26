from pydantic import BaseModel
from datetime import datetime


class Order(BaseModel):
    id: int
    car: int
    client: int
    data: str
    work_description: str
    status: str
