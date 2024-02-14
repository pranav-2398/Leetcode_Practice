from typing import List

############ MY ORIGINAL SOLN ##############################
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}

        for num in nums:
            if num in cache:
                return True
            else:
                cache[num] = 1

        return False
##############################################################


############ MY SOLN 2 #######################################
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        prev = None

        for i in range(len(nums)):
            if prev == nums[i]:
                return True
            prev = nums[i]

        return False
    
###############################################################

