from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn_str = 'clickhouse+native://default:@localhost/test'
engine = create_engine(conn_str)
session = sessionmaker(bind=engine)()