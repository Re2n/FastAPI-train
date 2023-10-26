from pydantic import BaseModel
from fastapi import Query


class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    vin: str = Query(min_length=17, max_length=17)
