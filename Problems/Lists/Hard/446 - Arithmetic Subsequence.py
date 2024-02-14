from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, n = 0, len(nums)

        dp = [defaultdict(int) for _ in range(n)]
        #dp[i][diff] -> No of subseq ending at i with diff

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += 1 + dp[j][diff]
        
        return res - (n * (n-1) // 2)
    
nums = [2,4,6,8,10]
s = Solution()
print(s.numberOfArithmeticSlices(nums))
