from fastapi import APIRouter
from utils import clients as client_utils
from schemas.clients import Client

router = APIRouter()


@router.get('/get_clients')
async def get_clients():
    clients = await client_utils.get_clients()
    return clients


@router.post('/create_client')
async def create_client(client: Client):
    new_client = await client_utils.create_client(client)
    return new_client


@router.put('/update_client')
async def update_client(client_id: int, client: Client):
    await client_utils.update_client(client_id, client)
    return await client_utils.get_client(client_id)


@router.delete('/delete_client')
async def delete_client(client_id: int):
    await client_utils.delete_client(client_id)
    return {'response': 200}


@router.get('/clients_car')
async def get_clients_cars(client_id: int):
    return await client_utils.get_client_cars(client_id)


@router.get('/clients_order')
async def get_clients_orders(client_id: int):
    return await client_utils.get_client_orders(client_id)
