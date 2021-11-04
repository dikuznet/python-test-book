
def gen():
    mylist = range(5)
    for i in mylist:
        yield i*2

for i in gen():
    print(i)