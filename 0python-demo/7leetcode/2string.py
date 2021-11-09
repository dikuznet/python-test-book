from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return s

sol = Solution()
s = ["h","e","l","l","o"]
print(sol.reverseString(s))
