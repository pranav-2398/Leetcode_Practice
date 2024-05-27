from typing import List


######## MY SOLN ####################################
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            count = 0
            for num in nums:
                if num >= i:
                    count += 1
            if count == i:
                return i
        
        return -1 

#### OPTIMISED SOLN ##################################
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)
        for n in nums:
            index = min(n, len(nums))
            count[index] += 1
        
        total_right = 0
        for i in reversed(range(len(nums) + 1)):
            total_right += count[i]
            if total_right == i:
                return i
            
        return -1
#######################################################