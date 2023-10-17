from datetime import datetime
from typing import List

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(
    title='Car Service'
)

cars = [
    {'id': 1, 'brand': 'Mercedes', 'model': 'CLS', 'year': 2023, 'vin': 'XTA210990Y2766389'},
    {'id': 2, 'brand': 'BMW', 'model': 'M5', 'year': 2023, 'vin': 'LSJA16E3XCG067514'}
]

clients = [
    {'id': 1, 'name': 'Bob', 'surname': 'Kawalski', 'address': '61 HELENA AVE YONKERS NY 10710-3024 USA',
     'phone': '+19292884560'},
    {'id': 2, 'name': 'Jhon', 'surname': 'Kawalski', 'address': '61 HELENA AVE YONKERS NY 10710-3024 USA',
     'phone': '+19292887839'}
]

orders = [
    {'id': 1, 'car': [cars[0]], 'client': [clients[0]], 'data': '2023-10-16T14:20:13', 'work_description': 'Repair',
     'status': 'Complete'},
    {'id': 2, 'car': [cars[1]], 'client': [clients[1]], 'data': '2023-10-16T16:20:13', 'work_description': 'Repair',
     'status': 'Awaiting repair'}
]


class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    vin: str = Query(min_length=17, max_length=17)


class Client(BaseModel):
    id: int
    name: str
    surname: str
    address: str
    phone: str = Query(min_length=12, max_length=12)


class Order(BaseModel):
    id: int
    car: List[Car]
    client: List[Client]
    data: datetime
    work_description: str
    status: str


@app.get('/clients', response_model=List[Client])
def get_clients():
    return clients


@app.post('/clients/new_client')
def add_new_client(client: List[Client]):
    clients.extend(client)
    return {'status': 200, 'data': clients}


@app.post('/clients/update_client')
def update_client(client_id: int, new_name: str | None = None, new_surname: str | None = None,
                  new_address: str | None = None, new_phone: str | None = None):
    current_client = list(filter(lambda client: client.get('id') == client_id, clients))[0]
    if new_name: current_client['name'] = new_name
    if new_surname: current_client['surname'] = new_surname
    if new_address: current_client['address'] = new_address
    if new_phone and len(new_phone) == 12: current_client['phone'] = new_phone
    if new_phone and (len(new_phone) < 12 or len(new_phone) > 12): return {'Incorrect phone number length'}
    return {'status': 200, 'data': current_client}


@app.post('/clients/delete_client')
def delete_client(client_id: int):
    current_client = list(filter(lambda client: client.get('id') == client_id, clients))[0]
    clients.remove(current_client)
    return clients


@app.get('/cars', response_model=List[Car])
def get_cars():
    return cars


@app.post('/cars/new_car')
def add_new_car(car: List[Car]):
    cars.extend(car)
    return {'status': 200, 'data': cars}


@app.post('/cars/update_car')
def update_car(car_id: int, new_brand: str | None = None, new_model: str | None = None,
               new_year: int | None = None, new_vin: str | None = None):
    current_car = list(filter(lambda car: car.get('id') == car_id, cars))[0]
    if new_brand: current_car['brand'] = new_brand
    if new_model: current_car['model'] = new_model
    if new_year: current_car['year'] = new_year
    if new_vin and len(new_vin) == 17: current_car['vin'] = new_vin
    if new_vin and (len(new_vin) < 17 or len(new_vin) > 17): return {'Incorrect VIN length'}
    return {'status': 200, 'data': current_car}


@app.post('/cars/delete_car')
def delete_car(car_id: int):
    current_car = list(filter(lambda car: car.get('id') == car_id, cars))[0]
    cars.remove(current_car)
    return cars


@app.get('/orders', response_model=List[Order])
def get_orders():
    return orders


@app.post('/orders/new_order')
def add_new_order(order: List[Order]):
    orders.extend(order)
    return {'status': 200, 'data': orders}


@app.post('/orders/update_order')
def update_order(order_id: int, new_data: datetime | None = None, new_work_description: str | None = None,
                 new_status: str | None = None, new_car: List[Car] | None = None, new_client: List[Client] | None = None):
    current_order = list(filter(lambda order: order.get('id') == order_id, orders))[0]
    if new_data: current_order['data'] = new_data
    if new_work_description: current_order['work_description'] = new_work_description
    if new_status: current_order['status'] = new_status
    if new_car: current_order['car'] = new_car
    if new_client: current_order['client'] = new_client
    return {'status': 200, 'data': current_order}


@app.post('/cars/order_car')
def delete_order(order_id: int):
    current_order = list(filter(lambda order: order.get('id') == order_id, orders))[0]
    orders.remove(current_order)
    return orders


@app.get('/clients/cars')
def get_cars_of_client(client_id: int):
    cars_of_client = []
    for order in orders:
        if order['client'][0]['id'] == client_id:
            cars_of_client.append(order['car'][0])
    return {'status': 200, 'data': cars_of_client}


@app.get('/clients/orders')
def get_orders_of_client(client_id: int):
    orders_of_client = []
    for order in orders:
        if order['client'][0]['id'] == client_id:
            orders_of_client.append(order)
    return {'status': 200, 'data': orders_of_client}