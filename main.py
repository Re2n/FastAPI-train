from fastapi import FastAPI

app = FastAPI(
    title='Car Service'
)

cars = [
    {'brand': 'Mercedes', 'model': 'CLS', 'year': 2023, 'VIN': 'XTA210990Y2766389'},
    {'brand': 'BMW', 'model': 'M5', 'year': 2023, 'VIN': 'LSJA16E3XCG067514'}
]

clients = [
    {'name': 'Bob', 'surname': 'Kawalski', 'address': ''}
]