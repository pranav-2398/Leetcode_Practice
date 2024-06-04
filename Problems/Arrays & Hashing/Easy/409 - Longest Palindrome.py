from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        one_count = 0
        for val in count.values():
            if val % 2 == 1:
                res += val-1
                one_count += 1
            else:
                res += val
        return res if not one_count else res + 1