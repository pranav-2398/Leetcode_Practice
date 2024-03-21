from typing import List

### DP WAY ######################################################################

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         def rec(i, rsum):
#             if rsum == 0:
#                 return True
#             if i == len(nums) or rsum < 0:
#                 return False
#             elif self.dp[i][rsum] != -1:
#                 return self.dp[i][rsum]
#             self.dp[i][rsum] = rec(i + 1, rsum - nums[i]) or rec(i + 1, rsum)
#             return self.dp[i][rsum]

#         totalsum = sum(nums)
#         if totalsum % 2:
#             return False
#         else:
#             self.dp = [[-1] * ((totalsum // 2) + 1) for _ in range(len(nums))]
#             return rec(0, totalsum // 2)
        
###############################################################################

### OPTIMISED WAY #############################################################
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums) - 1, -1, -1):
            nextdp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextdp.add(t + nums[i])
                nextdp.add(t)
            dp = nextdp
        return False

#################################################################################

s = Solution()
nums = [1, 5, 11, 5]
print(s.canPartition(nums))
