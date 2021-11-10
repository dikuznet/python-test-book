from typing import List
from lutils import benchmark


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


sol = Solution()

print(sol.firstUniqChar_fast("leetcode"))
