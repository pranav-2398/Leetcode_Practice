from collections import defaultdict
from typing import List

### MY ORIGINAL SOLN #############################
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums) - 1

#         def helper(pos):
#             res = False
#             if pos == n:
#                 return True
            
#             if pos > n:
#                 return False
            
#             for i in range(nums[pos], 0, -1):
#                 res = helper(pos + i)
#                 if res:
#                     return res
                
#             return res
    
#         return helper(0)
######################################################

### MY ORIGINAL SOLN V2 ##############################
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         dp = defaultdict(bool)
#         n = len(nums) - 1

#         def helper(pos):
#             if pos == n:
#                 dp[pos] = True
#                 return 
            
#             if pos > n:
#                 dp[pos] = False
#                 return
            
#             if pos in dp:
#                 return
            
#             for i in range(nums[pos], 0, -1):
#                 helper(pos + i)
#                 dp[pos] = dp[pos] or dp[pos + i] 
#                 break
                
#             return dp[pos]
        
#         helper(0)
    
#         return dp[0]
######################################################

#### GREEDY SOLN #####################################
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= end:
                end = i

        return True if end == 0 else False
########################################################

s = Solution()
nums = [0]
print(s.canJump(nums))
# print(False and True)
