from collections import defaultdict
from typing import List

#### MY SOLN #########################################################################
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = defaultdict(list)
        dp[len(nums)-1] = [nums[-1], nums[-1]]
        maxno = nums[-1]

        if len(nums) < 2:
            return nums[0]

        for i in range(len(nums) - 2, -1, -1):
            dp[i].append(max(nums[i], nums[i] * dp[i + 1][0], nums[i] * dp[i + 1][1]))
            dp[i].append(min(nums[i], nums[i] * dp[i + 1][0], nums[i] * dp[i + 1][1]))
            maxno = max(maxno, dp[i][0])

        return maxno
######################################################################################
    
### OPTIMISED SOLN ###################################################################
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n, tmp, n * curMin)
            curMin = min(n, tmp, n * curMin)
            res = max(res, curMax)
        
        return res
######################################################################################
    
s = Solution()
nums = [-2,3,-4]
print(s.maxProduct(nums))
        