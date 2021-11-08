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
    @benchmark    
    def moveZeroes(self, nums: List[int]) -> None:
        zcount = 0
        l = len(nums)
        i = 0 
        while True: 
            if i >= l: break 
            if nums[i] == 0: 
                nums.insert(l, nums.pop(i))
                zcount = zcount + 1
                if i + zcount >= l: break
            else:              
                i = i + 1   
        return nums

x = Solution()
print(x.moveZeroes([0,0,0,3,12,0,0,12]))