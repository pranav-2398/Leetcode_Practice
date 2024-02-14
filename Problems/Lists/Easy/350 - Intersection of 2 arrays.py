from typing import List

#### MY ORIGINAL SOLN #####################################################

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        if len(nums1) < len(nums2):
            small, large = nums1, nums2
        else:
            small, large = nums2, nums1
        
        i = j = 0
        res = []
        cache = {}

        for num in small:
            cache[num] = cache.get(num, 0) + 1

        for num in large:
            if cache.get(num, 0):
                cache[num] -= 1
                res.append(num)

        return res
    
############################################################################
    
############## ANOTHER SOLN ################################################
    
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        
        return res
    
##############################################################################
    
s = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(s.intersect(nums1, nums2))

