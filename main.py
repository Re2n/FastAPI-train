from models.db import database
from fastapi import FastAPI
from routers import clients, cars, orders

app = FastAPI(
    title='Car Service'
)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(clients.router)
app.include_router(cars.router)
app.include_router(orders.router)
