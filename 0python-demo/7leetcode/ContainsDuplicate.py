from typing import List
from inputdat import nums
import time
from functools import reduce
import operator

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

    def singleNumber(self, nums: List[int]) -> int:
        setn = set()
        once = set()
        for item in nums:
            if not (item in setn): 
                once.add(item)
            else: 
                once.remove(item)
            setn.add(item)
        return once.pop()

    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = (set(nums1) & set(nums2))
        ret = list()
        for i in c: 
            ret = ret + [i] * min(nums1.count(i),nums2.count(i))
        return ret

    def robot(self,prices, days):
        profit = 0
        for i in range(1, days):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        profit = self.robot(prices, len(prices))
        return profit,prices
            
x = Solution()
print(x.maxProfit([7,6,4,3,1]))