from collections import Counter
from typing import List


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         nums2.sort()

#         i, j = 0, 0 
#         res = []
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 if not res or res[-1] != nums1[i]:
#                     res.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 i += 1
#         return res

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        res = []

        for k in count1.keys():
            if k in count2:
                res.append(k)

        return res