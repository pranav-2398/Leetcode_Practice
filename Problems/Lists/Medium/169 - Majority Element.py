from typing import List

############# EASY SOLN ###############################

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}
#         res = maxcount = 0

#         for num in nums:
#             count[num] = 1 + count.get(num, 0)
#             res = num if count[num] > maxcount else res
#             maxcount = max(count[num], maxcount)
#         return res

#########################################################        

########### OPTIMISED SOLN ##############################

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += 1 if res == n else -1
        
        return res
    
############################################################