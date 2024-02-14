from collections import defaultdict
from typing import List

###### MY SOLN #########################################

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = defaultdict(int)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        
        return dp[0]
########################################################
    
### OPTIMISED SOLN (SPACE) #############################
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0

        for i in range(len(nums) - 1, -1, -1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
#########################################################