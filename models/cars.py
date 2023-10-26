import sqlalchemy

metadata = sqlalchemy.MetaData()

cars_table = sqlalchemy.Table(
    'cars',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('brand', sqlalchemy.String),
    sqlalchemy.Column('model', sqlalchemy.String),
    sqlalchemy.Column('year', sqlalchemy.Integer),
    sqlalchemy.Column('vin', sqlalchemy.String),
)
