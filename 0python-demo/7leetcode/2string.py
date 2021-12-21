from typing import List
from lutils import benchmark
from gmpy2 import mpz

class Solution:

    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s

    def reverse(self, x: int) -> int:
        l = list(str(x).replace("-", ""))
        l.reverse()
        x = -1 * int(''.join(l)) if x < 0 else int(''.join(l))
        if (x < -1*(2**31)) or (x >= (2**31 - 1)):
            x = 0
        return x

    @benchmark
    def firstUniqChar(self, s: str) -> int:
        for i, val in enumerate(s):
            c = s.count(val)
            if c == 1:
                return i
        return -1

    @benchmark
    def firstUniqCharFast(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        idx = {}
        for i, val in enumerate(letters):
            c = s.count(val)
            if c == 1:
                idx[s.index(val)] = val
        if len(idx) > 0:
            return min(idx.keys())
        return -1
    
    def __init__(self):
        self.letters = frozenset("1234567890")
        self.sin = frozenset("-+")

    @benchmark   
    def myAtoi(self, s: str) -> int:       
        sdig = 0
        start = True
        digInclude = False 
        sig = 1
        for c in s:
            if c in self.letters: 
                sdig = 10*sdig + int(c)
                start = False
                digInclude = True
                continue          
            if (c == " "): 
                if start: continue
                else:     break
            if (c == "."): 
                break
            if start:
                if (c in self.sin): 
                    if c =="-": sig = -1
                    start = False
                    continue          
            break             

        if digInclude: x = sig * sdig
        else: 
            return 0
        if (x < -2147483648):   return -2147483648
        if (x > 2147483647):    return 2147483647 
        return x 

sol = Solution()

print(sol.myAtoi("+123667868.1"))
