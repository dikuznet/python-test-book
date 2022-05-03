from clickhouse_driver import Client
client = Client('127.0.0.1') #логин пароль порт по умолчанию, дефолтная БД тоже по умолчанию
result = client.execute("SHOW DATABASES")
print(result)