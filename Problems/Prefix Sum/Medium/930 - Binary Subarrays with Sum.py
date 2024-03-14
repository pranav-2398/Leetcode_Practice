from typing import List

#### MY SOLN (TLE) ###################################################
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0

        for i in range(len(nums)):
            sumval = 0
            for j in range(i, len(nums)):
                sumval += nums[j]
                if sumval == goal:
                    res += 1
        
        return res
#######################################################################

### OPTIMISED SOLN ####################################################
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        cursum = 0
        prefixsums = {0: 1}

        for n in nums:
            cursum += n
            diff = cursum - goal

            res += prefixsums.get(diff, 0)
            prefixsums[cursum] = 1 + prefixsums.get(cursum, 0)   
        return res
########################################################################


s = Solution()
nums = [1,0,1,0,1]
print(s.numSubarraysWithSum(nums, 2))