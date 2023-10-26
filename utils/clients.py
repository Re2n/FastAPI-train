from sqlalchemy import select
from models.clients import clients_table
from models.orders import orders_table
from models.db import database
from schemas.clients import Client


async def get_client(client_id: int):
    query = (
        select(
            [
                clients_table.c.id,
                clients_table.c.name,
                clients_table.c.surname,
                clients_table.c.address,
                clients_table.c.phone,
            ]
        )
        .where(clients_table.c.id == client_id)
    )
    return await database.fetch_one(query)


async def get_clients():
    query = (
        select(
            [
                clients_table.c.id,
                clients_table.c.name,
                clients_table.c.surname,
                clients_table.c.address,
                clients_table.c.phone,
            ]
        )
    )
    return await database.fetch_all(query)


async def create_client(client: Client):
    query = (
        clients_table.insert()
        .values(
            id=client.id,
            name=client.name,
            surname=client.surname,
            address=client.address,
            phone=client.phone
        )
        .returning(
            clients_table.c.id,
            clients_table.c.name,
            clients_table.c.surname,
            clients_table.c.address,
            clients_table.c.phone,
        )
    )
    client = await database.fetch_one(query)
    client = dict(zip(client, client.values()))
    return client


async def update_client(client_id: int, client: Client):
    query = (
        clients_table.update()
        .where(clients_table.c.id == client_id)
        .values(
            id=client.id,
            name=client.name,
            surname=client.surname,
            address=client.address,
            phone=client.phone
        )
    )
    return await database.execute(query)


async def delete_client(client_id: int):
    query = (
        clients_table.delete()
        .where(clients_table.c.id == client_id)
    )
    return await database.execute(query)


async def get_client_cars(client_id: int):
    query = (
        select(
            orders_table.c.car,
        )
        .where(orders_table.c.client == client_id)
    )
    return await database.fetch_all(query)


async def get_client_orders(client_id: int):
    query = (
        select(
            orders_table.c.id,
        )
        .where(orders_table.c.client == client_id)
    )
    return await database.fetch_all(query)
