from collections import Counter
from typing import List


### 2 Pointer Soln ####################################
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = -1

        while l < r and nums[l] < 0 and nums[r] > 0 :
            if abs(nums[l]) == abs(nums[r]):
                res = abs(nums[l])
                break
            elif abs(nums[l]) < abs(nums[r]):
                r -= 1
            else:
                l += 1
        
        return res

#### Hash Map Soln ##########################################
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        count = Counter(nums)
        elements = [key for key in count.keys() if key < 0]
        res = -1
        for ele in elements:
            if abs(ele) in count:
                res = max(res, abs(ele))
        
        return res
#############################################################

s = Solution()
nums = [-1,2,-3,3]
print(s.findMaxK(nums))