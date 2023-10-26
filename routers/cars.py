from fastapi import APIRouter
from utils import cars as car_utils
from schemas.cars import Car

router = APIRouter()


@router.get('/get_cars')
async def get_cars():
    cars = await car_utils.get_cars()
    return cars


@router.post('/create_car')
async def create_car(car: Car):
    new_car = await car_utils.create_car(car)
    return new_car


@router.put('/update_car')
async def update_car(car_id: int, car: Car):
    await car_utils.update_car(car_id, car)
    return await car_utils.get_car(car_id)


@router.delete('/delete_car')
async def delete_car(car_id: int):
    await car_utils.delete_car(car_id)
    return {'response': 200}
