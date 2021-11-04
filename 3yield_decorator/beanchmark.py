import time
import requests

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения: {end-start} секунд.')
        return return_value
    return wrapper

@benchmark
def fetch_webpage(url):
    webpage = requests.get(url)
    return webpage.text

url = 'http://ya.ru'
webpage = fetch_webpage(url)
print(webpage)