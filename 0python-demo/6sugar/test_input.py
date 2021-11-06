from functools import reduce
mul=reduce(lambda x, y: x*y, map(int, input().strip().split()))
print(f' {mul}') 