from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s

    def reverse(self, x: int) -> int:
        l = list(str(x).replace("-",""))
        l.reverse()
        x = -1 * int(''.join(l)) if x <0 else int(''.join(l))
        if (x < -1*(2**31)) or (x >= (2**31 - 1)): x = 0 
        return x

sol = Solution()
s = ["h","e","l","l","o"]
print(sol.reverse(-2147483648))
print(-1*(2**31))
