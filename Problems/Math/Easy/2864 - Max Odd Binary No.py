from typing import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = s.count('1')
        ones = '1' * (n - 1) if n >= 2 else ""
        return ones + '0' * (len(s) - n) + '1'

s = Solution()
print(s.maximumOddBinaryNumber("010"))