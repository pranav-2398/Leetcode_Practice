from typing import List

########### MY SOLN ##############################################

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         for i in range(len(nums)-1):
#             if nums[i] == 0:
#                 for j in range(i+1, len(nums)):
#                     if nums[j] != 0:
#                         nums[i], nums[j] = nums[j], nums[i]
#                         break

####################################################################

############### OPTIMISED SOLN #####################################

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0

        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

######################################################################


s = Solution()
nums = [0, 1, 0, 3, 12]

s.moveZeroes(nums)
print(nums)

        