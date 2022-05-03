from random import random
from sqlalchemy import create_engine, Column, MetaData, literal
from clickhouse_sqlalchemy import Table, make_session, get_declarative_base, types, engines

import lutils
import random
import json
from datetime import datetime
import time
from lutils import benchmark

Measurements_count = 800000

uri = 'clickhouse+native://default:@localhost/default'
engine = create_engine(uri)
session = make_session(engine)
engine.supports_statement_cache = False
metadata = MetaData(bind=engine)
Base = get_declarative_base(metadata=metadata)

class Sensor(Base):
    uuid = Column(types.Int32, primary_key=True)
    name = Column(types.String)
    __table_args__ = (
        engines.Memory(),
    )

class Measurements(Base):
    id = Column(types.Int32, primary_key=True)
    uuid = Column(types.Int32, nullable=False)
    dt = Column(types.DateTime)
    val = Column(types.Float)
    __table_args__ = (
        engines.Memory(),
    )

@benchmark
def create_db():
    print(f'Создаем новую стуктуру базы {uri}')
    Base.metadata.create_all()
    session.commit()

@benchmark
def generate_measurement():
    print(f'Заполняем запрос {Measurements_count} значений')
    for i in range(0,Measurements_count ):
        f = 3.14 * random.random()
        mes = Measurements(id=i, uuid=281479271, dt=datetime.now(), val=f)
        session.add(mes)

@benchmark
def do_commit(): 
    print(f'Выполняем запрос {Measurements_count} значений')
    session.commit()

if __name__=="__main__":
    create_db()
    generate_measurement()
    do_commit()