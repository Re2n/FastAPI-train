from fastapi import APIRouter
from utils import orders as order_utils
from schemas.orders import Order

router = APIRouter()


@router.get('/get_orders')
async def get_orders():
    orders = await order_utils.get_orders()
    return orders


@router.post('/create_order')
async def create_order(order: Order):
    new_order = await order_utils.create_order(order)
    return new_order


@router.put('/update_order')
async def update_order(order_id: int, order: Order):
    await order_utils.update_order(order_id, order)
    return await order_utils.get_order(order_id)


@router.delete('/delete_order')
async def delete_order(order_id: int):
    await order_utils.delete_order(order_id)
    return {'response': 200}
