from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxright = [0] * len(nums)
        i = len(nums) - 1
        prevmax = 0

        for n in reversed(nums):
            maxright[i] = max(n, prevmax)
            prevmax= maxright[i]
            i -= 1
        
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > maxright[r]:
                l += 1
            res = max(res, r - l)
        return res