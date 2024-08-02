from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        totalones = nums.count(1)
        l = 0
        windowones = maxwindowones = 0
        for r in range(2 * N):
            if nums[r % N]:
                windowones += 1
            if r - l + 1 > totalones:
                windowones -= nums[l % N]
                l += 1
            maxwindowones = max(maxwindowones, windowones)

        return totalones - maxwindowones