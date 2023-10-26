from pydantic import BaseModel


class Order(BaseModel):
    id: int
    car: int
    client: int
    data: str
    work_description: str
    status: str
