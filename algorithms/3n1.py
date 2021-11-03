# Проверка теоремы 3n+1
import math
import time

def rec(n):
    if (x % 2 == 0): 
        y = n // 2 
    else: 
        y = 3 * n + 1
    return y

st = []
# print('Введите любое целое число:',end=' ')
# x = int(input())
# inter_count = 0
# stop, start4 = False, False

for i in range(1,50000000000):
    inter_count = 0
    stop, start4 = False, False
    x = i
    while not stop:
        x = rec(x)
        if ((x==4) or (start4)): 
            st.append(x)
            start4 = True
            if st == [4,2,1,4,2,1]: 
                stop = True
        
        if len(st)>6: st = []
        inter_count = inter_count + 1
    print(i,st, inter_count)

