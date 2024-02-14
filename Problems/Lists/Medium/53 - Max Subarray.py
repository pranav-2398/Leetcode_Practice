from collections import defaultdict
from typing import List

### MY ORIGINAL SOLN #####################################

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = defaultdict(int)

#         if len(nums) == 1:
#             return nums[0]

#         res[len(nums)-1] = nums[len(nums)-1]

#         for i in range(len(nums) - 2, -1, -1):
#             res[i] = max(nums[i], nums[i] + res[i + 1])
        
#         return max(res.values())
##########################################################

###### MY IMPROVED SOLN ##################################
 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxno = nums[0]
        temp = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], temp + nums[i])
            maxno = max(maxno, temp)
        
        return maxno
##########################################################

s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))
