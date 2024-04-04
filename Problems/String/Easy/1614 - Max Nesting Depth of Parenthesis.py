from collections import deque


class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1

            ans = max(ans, count)

        return ans
