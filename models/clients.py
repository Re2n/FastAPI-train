import sqlalchemy

metadata = sqlalchemy.MetaData()

clients_table = sqlalchemy.Table(
    'clients',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('surname', sqlalchemy.String),
    sqlalchemy.Column('address', sqlalchemy.String),
    sqlalchemy.Column('phone', sqlalchemy.String),
)
