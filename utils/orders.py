from sqlalchemy import select
from models.orders import orders_table
from models.db import database
from schemas.orders import Order


async def get_order(order_id: int):
    query = (
        select(
            [
                orders_table.c.id,
                orders_table.c.car,
                orders_table.c.client,
                orders_table.c.data,
                orders_table.c.work_description,
                orders_table.c.status,
            ]
        )
        .where(orders_table.c.id == order_id)
    )
    return await database.fetch_one(query)


async def get_orders():
    query = (
        select(
            [
                orders_table.c.id,
                orders_table.c.car,
                orders_table.c.client,
                orders_table.c.data,
                orders_table.c.work_description,
                orders_table.c.status,
            ]
        )
    )
    return await database.fetch_all(query)


async def create_order(order: Order):
    query = (
        orders_table.insert()
        .values(
            id=order.id,
            car=order.car,
            client=order.client,
            data=order.data,
            work_description=order.work_description,
            status=order.status,
        )
        .returning(
            orders_table.c.id,
            orders_table.c.car,
            orders_table.c.client,
            orders_table.c.data,
            orders_table.c.work_description,
            orders_table.c.status,
        )
    )
    order = await database.fetch_one(query)
    order = dict(zip(order, order.values()))
    return order


async def update_order(order_id: int, order: Order):
    query = (
        orders_table.update()
        .where(orders_table.c.id == order_id)
        .values(
            id=order.id,
            car=order.car,
            client=order.client,
            data=order.data,
            work_description=order.work_description,
            status=order.status,
        )
    )
    return await database.execute(query)


async def delete_order(order_id: int):
    query = (
        orders_table.delete()
        .where(orders_table.c.id == order_id)
    )
    return await database.execute(query)
