from collections import defaultdict
from typing import List

#### MY SOLN ##################################################
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i-1, -1, -1):
                dp[i][j] = (i - j) * min(height[j], height[i])
                res = max(res, dp[i][j])

        return res
################################################################
    
### OPTIMISED SOLN #############################################
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
#################################################################

height = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(height))




