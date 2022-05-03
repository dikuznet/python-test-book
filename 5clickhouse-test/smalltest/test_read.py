from mclickhouse import * 

@benchmark
def read_measurements():
    rd = session.query(Measurements).all() #\
    print(f'прочитано {len(rd)}')

if __name__=="__main__":
    print("Тестирование чтения")
    read_measurements()