import json
from datetime import datetime
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mestype import Measurements

import connector
cursor = connector.connect('default').cursor()
cursor.execute('SELECT * FROM test LIMIT 10')
print(cursor.fetchone())

# Register SQLAlchemy dialect
from sqlalchemy.dialects import registry
registry.register("clickhouse", "base", "dialect")

# Test engine and table 
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *

engine = create_engine('clickhouse://default:@localhost:8123/default')
logs = Table('test', MetaData(bind=engine), autoload=True)
print(select([func.count('*')], from_obj=logs).scalar())


# engine = create_engine('clickhouse+native://delaulf:@localhost:9000/default[?options…]clickhouse://default:@localhost:{port}/{database}', echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()

# with open('configs8.json', 'rb') as f:
#     cfg = json.load(f)

# s8 = cfg['s8']

# ser = serial.Serial('/dev/ttyUSB1', 115200)

# cnt = 0
# while (True):
#     try:
#         data = ser.readline()
#         if str(data).find("CO2PPM") > 0:
#             print(data)
#             f = float(str(data)[9:-4:].strip("\'").strip("\\"))
#             # print(datetime.now(), f)
#             if f > 100:
#                 status = 0
#                 mes = Measurements(uuid=281479271743489, dt=datetime.now(), val=f, status=status)
#                 s8['regs'] = [0]*10
#                 s8['regs'][2] = f
#                 s8['regs'][1] = status
#                 s8['dt'] = str(datetime.now())
#                 res0 = client.set(hex(mes.uuid), s8)
#                 session.add(mes)
#                 cnt += 1
#                 if cnt >= 12:
#                     cnt = 0
#                     session.commit()
#     except KeyboardInterrupt:
#         exit()
#     except BaseException as err:
#         print(err, data)
#     time.sleep(10)
