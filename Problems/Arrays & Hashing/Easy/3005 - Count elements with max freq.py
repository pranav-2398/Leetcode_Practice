from collections import Counter
from typing import List

#### MY SOLN ###############################################
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxfreq = 0
        nums.sort()
        res = 0
        
        i = 0
        while i < len(nums):
            j = i + 1
            count = 1
            while j < len(nums):
                if nums[j] == nums[i]:
                    count += 1
                    j += 1
                else:
                    break
            if count == maxfreq:
                res += 1
            elif count > maxfreq:
                maxfreq = count
                res = 1
            i = j

        return res * maxfreq
#############################################################
    
### ANOTHER SOLN ############################################
# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         d = Counter(nums)

#         m = max(d.values())

#         count = 0        
#         for k,v in d.items():
#             if v == m:
#                 count += v
        
#         return count
##############################################################

s = Solution()
nums = [1, 2, 2, 3, 1, 4]
print(s.maxFrequencyElements(nums))

