from sqlalchemy import select
from models.cars import cars_table
from models.db import database
from schemas.cars import Car


async def get_car(car_id: int):
    query = (
        select(
            [
                cars_table.c.id,
                cars_table.c.brand,
                cars_table.c.model,
                cars_table.c.year,
                cars_table.c.vin,
            ]
        )
        .where(cars_table.c.id == car_id)
    )
    return await database.fetch_one(query)


async def get_cars():
    query = (
        select(
            [
                cars_table.c.id,
                cars_table.c.brand,
                cars_table.c.model,
                cars_table.c.year,
                cars_table.c.vin,
            ]
        )
    )
    return await database.fetch_all(query)


async def create_car(car: Car):
    query = (
        cars_table.insert()
        .values(
            id=car.id,
            brand=car.brand,
            model=car.model,
            year=car.year,
            vin=car.vin,
        )
        .returning(
            cars_table.c.id,
            cars_table.c.brand,
            cars_table.c.model,
            cars_table.c.year,
            cars_table.c.vin,
        )
    )
    car = await database.fetch_one(query)
    car = dict(zip(car, car.values()))
    return car


async def update_car(car_id: int, car: Car):
    query = (
        cars_table.update()
        .where(cars_table.c.id == car_id)
        .values(
            id=car.id,
            brand=car.brand,
            model=car.model,
            year=car.year,
            vin=car.vin,
        )
    )
    return await database.execute(query)


async def delete_car(car_id: int):
    query = (
        cars_table.delete()
        .where(cars_table.c.id == car_id)
    )
    return await database.execute(query)
