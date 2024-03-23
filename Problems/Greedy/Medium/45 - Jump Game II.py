from typing import List

### MY SOLN (DP) #######################################
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] > 1 else 0
        
        dp = [float("inf")] * len(nums)
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i] = min(dp[i], 1 + dp[i + j])
        
        return dp[0]
#########################################################
    
### OPTIMISED SOLN (GREEDY) #############################
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        
        return res
##########################################################

s = Solution()
nums = [2,3,0,1,4]
print(s.jump(nums))