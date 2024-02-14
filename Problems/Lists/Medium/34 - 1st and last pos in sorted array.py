from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.bs(nums, target, True), self.bs(nums, target, False)]

    def bs(self, nums, target, leftbias):
        l, r = 0, len(nums)-1

        i = -1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftbias:
                    r = m - 1
                else:
                    l = m + 1

        return i
