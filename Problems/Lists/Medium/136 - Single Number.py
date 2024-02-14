from typing import List

##### MY SOLN #################################################

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
        
#         nums.sort()

#         prev = None

#         for i in range(len(nums)):
#             if i == len(nums - 1):
#                 if prev != nums[i]:
#                     return nums[i]
#             elif nums[i] == prev or nums[i] == nums[i + 1]:
#                 prev = nums[i]
#             else:
#                 return nums[i]

#################################################################

##### ANOTHER SOLN ##############################################

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res

#################################################################
s = Solution()
nums = [4,1,2,1,2]
print(s.singleNumber(nums))
