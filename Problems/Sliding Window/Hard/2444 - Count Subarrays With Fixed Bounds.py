from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_idx = i

            if num == minK:
                left_idx = i
            
            if num == maxK:
                right_idx = i

            print(left_idx, right_idx, bad_idx, max(0, min(left_idx, right_idx) - bad_idx))

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res
        
s = Solution()
# nums = [1,3,5,2,7,5]
# minK = 1
# maxK = 5
nums = [1, 1, 1, 1]
minK = 1
maxK = 1
print(s.countSubarrays(nums, minK, maxK))