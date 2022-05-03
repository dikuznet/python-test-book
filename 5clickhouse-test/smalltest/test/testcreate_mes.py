import json
from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, MetaData, literal
from clickhouse_sqlalchemy import Table, make_session, get_declarative_base, types, engines

uri = 'clickhouse://default:@localhost/test'
engine = create_engine(uri)
session = make_session(engine)
metadata = MetaData(bind=engine)
Base = get_declarative_base(metadata=metadata)


class Sensor(Base):
    # __tablename__ = 'sensors'
    cache_ok = True
    uuid = Column(types.Int32, primary_key=True)

    __repr_attrs__ = ['dt', 'val']
    uuid = Column(Integer, primary_key=True)
    name = Column(String)


class Measurements(Base):
    # __tablename__ = 'measurements'
   
    # another_table = Table('another_rate', metadata,
    #     Column('day', types.Date, primary_key=True),
    #     Column('value', types.Int32, server_default=literal(1)),
    #     engines.Memory()
    # )

    # __repr_attrs__ = ['uuid', 'dt', 'val']
    # id = Column(Integer, primary_key=True)
    # uuid = Column(Integer, ForeignKey(Sensor.uuid), nullable=False)
    # dt = Column(DateTime)
    # val = Column(Float)
    # status = Column(Integer)

    # def __repr__(self):
    #     return f'{self.id} {hex(self.uuid)} {self.dt} {self.val} {self.status}'

    # def __str__(self) -> str:
    #     return str(self.to_dict())

    # def to_json(self):
    #     return json.dumps(self.to_dict())

    # def to_dict(self):
    #     return {'id': self.id, 'dt': str(self.dt), 'value': self.val, 'uuid': str(self.uuid)}


def CreateAll():
    try:
        Base.metadata.create_all()
        session.commit()
    except:
        pass


if __name__ == "__main__":
    CreateAll()
