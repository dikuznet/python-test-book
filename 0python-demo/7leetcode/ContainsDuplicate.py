from typing import List
from inputdat import nums
import time
from functools import reduce

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        return_value = func(*args, **kwargs)
        end = time.monotonic()
        print(f'Время выполнения: {end-start} секунд.')
        return return_value
    return wrapper

class Solution:
    @benchmark
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1): 
            if digits[i] + 1 > 9: digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                break   
        if digits[0]==0: digits.insert(0, 1)  
        return digits 

x = Solution()
print(x.plusOne([8,9,9,9]))