import sqlalchemy
from .cars import cars_table
from .clients import clients_table

metadata = sqlalchemy.MetaData()

orders_table = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('car', sqlalchemy.ForeignKey(cars_table.c.id)),
    sqlalchemy.Column('client', sqlalchemy.ForeignKey(clients_table.c.id)),
    sqlalchemy.Column('data', sqlalchemy.String),
    sqlalchemy.Column('work_description', sqlalchemy.String),
    sqlalchemy.Column('status', sqlalchemy.String),
)
