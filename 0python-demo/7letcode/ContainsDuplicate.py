from typing import List
from inputdat import nums
import time
# nums = [1,2,3]

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

x = Solution()
print(x.containsDuplicate(nums))